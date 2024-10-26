import datetime
import time
from pathlib import Path
from report_data import ReportData
from plots.strategy import DispersionPlot
from typing import Dict, Any
from plots.appearance import (
    AppearanceComposite,
    EnumeratePoints,
    LegendPosition,
    FacetGridAxisLabels,
)
from jinja2 import FileSystemLoader, Environment
from weasyprint import HTML
filepath = Path("./results/common_voice_12000.csv")
data: ReportData = ReportData(filepath.__str__())

params = data.df[["provider_name", "params"]].drop_duplicates().to_dict(
    orient="records",
)
new_cfg: Dict[str, Dict[str, Any]] = {}

for config in params:
    params_ = eval(config["params"])
    params_.pop("name")
    name = config["provider_name"]
    new_cfg[name] = params_

provider_group = data.group_by_mean("provider_name").round(3)

mean_stats = provider_group.to_dict(orient="index")

data.df = provider_group
data.df["provider_name"] = [
    f"{n + 1} {name}" for n, name in enumerate(data.df.index.tolist())
]

strategy = DispersionPlot(
    x="accuracy",
    y="rtf",
    hue="provider_name",
)

plot = strategy.plot(data.df)

appearance_kit: AppearanceComposite = AppearanceComposite()
appearance_kit.add(EnumeratePoints(data.df, "accuracy", "rtf"))
appearance_kit.add(LegendPosition(plot))
appearance_kit.add(
    FacetGridAxisLabels(
        plot=plot,
        xlabel="Accuracy (%)",
        ylabel="RTF",
        font_size=11.0,
    )
)
plot_path = "./results/plots/test_flow.png"
appearance_kit.customize()
plot.savefig(plot_path)

jinja_env = Environment(loader=FileSystemLoader("./wavbench/report/templates"))
template = jinja_env.get_template("index.html")
html = HTML(
    string=template.render(
        mean_stats=mean_stats,
        dispersion=plot_path,
        model_configs=new_cfg,
        created_at=datetime.datetime.now(datetime.UTC),
        file=filepath.name,
    ),
    base_url="./"
).write_pdf("./results/reports/asrbench-demo-report.pdf")

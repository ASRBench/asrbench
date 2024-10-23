from report_data import ReportData
from plots.strategy import DispersionPlot
from plots.axis_labels import FacetGridAxisLabels
from plots.appearance import (
    AppearanceComposite,
    EnumeratePoints,
    LegendPosition,
    AxisLabels,
)

data: ReportData = ReportData("../../results/common_voice_12000.csv")
provider_group = data.group_by_mean("provider_name")
print(provider_group)

data.df = provider_group
data.df["provider_name"] = [
    f"{n + 1} {name}" for n, name in enumerate(data.df.index.tolist())
]
# data.enumerate_index()

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
    AxisLabels(
        FacetGridAxisLabels(
            plot=plot,
            xlabel="Accuracy (%)",
            ylabel="RTF",
            font_size=11.0,
        )
    )
)

appearance_kit.customize()
plot.savefig("../../results/plots/test_flow.png")

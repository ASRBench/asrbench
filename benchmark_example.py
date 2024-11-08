import logging
import warnings
from wavbench.configfile import Configfile
from wavbench.transcribers.factory import DefaultTranscriberFactory
from wavbench.report.report_template import DefaultReport
from wavbench.report.input_ import CsvInput

warnings.filterwarnings(action="ignore", category=FutureWarning)

logging.basicConfig(
    level=logging.ERROR,
    format=(
        "%(asctime)s : %(levelname)s :  %(message)s -  %(name)s:%(lineno)d"
    ),
    filename="wavbench.log",
    filemode="a",
)

cfg = Configfile(
    filepath_="configfile_example.yml",
    factory=DefaultTranscriberFactory(),
)

benchmark = cfg.set_up_benchmark()
output_filepath: str = benchmark.run()

report = DefaultReport(CsvInput(output_filepath))
report.generate_report()

import logging
import warnings
from asrbench.configfile import Configfile
from asrbench.transcribers.factory import DefaultTranscriberFactory
from asrbench.report.report_template import DefaultReport
from asrbench.report.input_ import CsvInput

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

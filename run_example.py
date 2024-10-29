import logging
import warnings
from wavbench.configfile import Configfile
from wavbench.providers.factory import DefaultProviderFactory

warnings.filterwarnings(action="ignore", category=FutureWarning)

logging.basicConfig(
    level=logging.ERROR,
    format=(
        "%(asctime)s : %(levelname)s :  %(message)s -  %(name)s:%(lineno)d"
    ),
    filename="wavbench.log",
    filemode="a",
)

benchmark = Configfile(
    filepath_="configfile_example.yml",
    factory=DefaultProviderFactory(),
).set_up_benchmark()
benchmark.run()

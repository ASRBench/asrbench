import logging
import warnings
from wavbench.configfile import Configfile

warnings.filterwarnings(action="ignore", category=FutureWarning)

logging.basicConfig(
    level=logging.ERROR,
    format=(
        "%(asctime)s : %(levelname)s :  %(message)s -  %(name)s:%(lineno)d"
    ),
    filename="wavbench.log",
    filemode="a",
)

benchmark = Configfile("dataset_benchmark_exemple.yml").set_up_benchmark()
benchmark.run()

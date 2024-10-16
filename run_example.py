import logging
from wavbench.configfile import Configfile

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

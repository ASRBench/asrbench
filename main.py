import logging
from wavbench.config_loader import BenchmarkFactory

logging.basicConfig(
    level=logging.ERROR,
    format=(
        "%(asctime)s : %(levelname)s :  %(message)s -  %(name)s:%(lineno)d"
    ),
    filename="wavbench.log",
    filemode="a",
)

benchmark = BenchmarkFactory.from_config("dataset_benchmark_exemple.yml")
benchmark.run()

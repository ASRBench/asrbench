from benchmark.config_loader import BenchmarkFactory

benchmark = BenchmarkFactory.from_config("dataset_benchmark_exemple.yml")
benchmark.run()

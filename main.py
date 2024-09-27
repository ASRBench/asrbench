from benchmark.config_loader import BenchmarkFactory

benchmark = BenchmarkFactory.from_config("benchmark_exemple.yml")
benchmark.run()

With the configuration file ready, just create a Python script to read the file and set up the benchmark environment.
See an example below:

```python
from asrbench.config_loader import ConfigLoader

loader = ConfigLoader("path/to/configfile.yml")
benchmark = loader.set_up_benchmark()
benchmark.run()
```

If you also want to generate a PDF report from the data generated in the benchmark, just add the following
code snippet:

```python
from asrbench.report.report_template import DefaultReport
from asrbench.report.input_ import CsvInput
...

output_path = benchmark.run()
report = DefaultReport(CsvInput(output_filepath))
report.generate_report()

```

If you prefer a more direct and simplified solution, you can check out 
[asrbench-cli](https://github.com/ASRBench/asrbench-cli).

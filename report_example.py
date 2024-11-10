from pathlib import Path
from asrbench.report.report_template import DefaultReport
from asrbench.report.input_ import CsvInput

path = Path()

report = DefaultReport(
    CsvInput("./results/common_voice_12000.csv"),
)

report.generate_report()

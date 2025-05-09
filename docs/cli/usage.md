The ASRBench CLI offers two commands for running and analyzing benchmarks: run and resume.
Use the run command to run a benchmark based on a configuration file:

```sh
asrbench-cli run path/to/config.yml
```

The CLI reads the configuration file, configures the benchmark and runs it automatically. The progress, including the percentage completed and a time estimate for each stage of the transcription process, is displayed in the terminal.
Summarize Results

Use the resume command to view the performance averages for each transcriber from a results file (CSV or JSON):

```sh
asrbench-cli resume path/to/results.csv
```

The CLI calculates the averages and displays a formatted table in the terminal with the results.

| transcriber_name | audio_duration | runtime | rtf   | wer   | wil   | wip   | cer   | mer   | accuracy |
|------------------|----------------|---------|-------|-------|-------|-------|-------|-------|----------|
| faster_whisper   | 3.161          | 6.224   | 2.087 | 0.022 | 0.042 | 0.958 | 0.008 | 0.022 | 97.8     |
| wav2vec          | 3.161          | 1.147   | 0.35  | 0.57  | 0.672 | 0.328 | 0.25  | 0.55  | 43.0     |


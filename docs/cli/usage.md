With the configuration file in hand you can now **run** your benchmark:

```sh
asrbench-cli run path/to/configfile.yml
```

The CLI will read the configuration file, set up the benchmark and run it automatically. All progress and steps 
will be displayed directly in the terminal, including the percentage of completion and a time estimate for the 
completion of each stage of the transcription process.

Another command available in the cli is the **resume** command, which is very useful for quickly viewing the averages of
each transcriber, after providing a file of the benchmark results (csv/json) it will calculate the averages and create a
table in the terminal.

```sh
asrbench-cli resume path/to/resultfile.csv
```
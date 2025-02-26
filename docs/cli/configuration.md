ASRBench Cli allows you to configure and run the benchmark using a YAML configuration file. This approach facilitates the
benchmark environment by allowing the user to define datasets, transcribers and output parameters in a simple and declarative way.
parameters in a simple and declarative way. 

## Example

Below is an example of the configuration file structure:

```yaml
# data output configuration
output:
  type: "csv"
  dir: "./results"
  filename: "example_filename"

# configuration of datasets
datasets:
  dataset1:
    audio_dir: "resources/common_voice_05/wav"
    reference_dir: "resources/common_voice_05/txt"

# transcription system configuration
transcribers:
  faster_whisper_medium_int8:
    asr: "faster_whisper"
    model: "medium"
    compute_type: "int8"
    device: "cpu"
    beam_size: 5
    language: "en"  
```

The configuration file is divided into three main sections: output, datasets and transcribers. Below are details of each
section of the YAML file.

## Output
??? info "Optional Section"
    This section is optional. If not provided, the framework will use default values: the type will be csv, the filename 
    will be asrbench, and the directory will be the current directory.

In this section, we configure [OutputCtx](./references/output.md), where we define:

- type: Type of output file, such as csv or json.
- dir: Directory where the file will be saved.
- filename: Base name of the file, which will be combined with a timestamp.

## Datasets

In this section, we define the datasets that will be used in the benchmark. For each [Dataset](./references/dataset.md), 
we provide:

- identifier: A unique name for the dataset.
- audio_dir: Directory where the audio files for transcription are located.
- reference_dir: Directory with the reference files for each audio.

!!! warning "Dataset Files"
    For the system to correctly identify audio and transcript pairs, the files must have the same name, differing only 
    by extension. Audio files can have any extension, while transcription files must have the extension .txt.

## Transcribers

In this section, we configure the transcription systems (ASR), with parameters that vary according to the system chosen. 
For each [Transcriber](./references/transcribers/transcriber.md), we provide:

- identifier: A unique name for the transcriber.
- asr: name of the ASR system registered in the framework.
- other configuration parameters, such as model, compute_type, device, beam_size, language, etc., depending on the 
specifics of the transcriber.

```yaml
transcribers:
  identifier:
    asr: "asr_name"
    model: "medium"
    compute_type: "float16"
```

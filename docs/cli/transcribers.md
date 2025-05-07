# Transcribers

This section presents the speech recognition systems (ASR) implemented by the ASRBench CLI. Each
transcriber is described with a brief introduction, followed by its configuration in YAML format. More
complex parameters are explained in detail in the section.

## Wav2Vec

Wav2Vec 2.0, by Meta AI, is a self-supervised learning model that generates speech representations from raw audio, using a Transformer architecture. It is efficient with little labeled data, achieving low error rates in benchmarks.

```yaml
wav2vec:
  asr: "wav2vec"
  model: "facebook/wav2vec2-large-xlsr-53-portuguese"
  compute_type: "float32" # Set the precision of the calculations 
  device: "cpu"
```

??? info "Available models"
    The facebook/wav2vec2-large-xlsr-53-portuguese template is optimized for Portuguese. Other
    pre-trained templates can be used, according to the 
    [Wav2Vec](https://huggingface.co/docs/transformers/model_doc/wav2vec2) documentation.

## Whisper

Whisper, from OpenAI, is a speech recognition system trained on a large scale with 680,000 hours of audio
in several languages. Its generalization capability allows it to perform competitively in a variety of
scenarios without specific tuning.

```yaml
whisper:
  asr: "whisper"
  model: "medium"
  device: "cpu"
  language: "en"
  fp16: false # Enable 16-bit floating point
```

## Faster Whisper

Faster Whisper is an optimized version of Whisper, implemented with the CTranslate2 library. It offers
greater efficiency and lower memory consumption, while maintaining the accuracy of the original model.

```yaml
faster_whisper:
  asr: "faster_whisper"
  model: "medium"
  compute_type: "int8" # Defines the precision of the calculations 
  device: "cpu"
  beam_size: 5 # Controls sequence search 
  language: "en"
```

## Vosk

Vosk is an offline speech recognition toolkit, compatible with 20 languages. Its architecture combines
deep neural networks, hidden Markov models and finite state transducers, making it ideal for embedded
systems.

```yaml
vosk:
  asr: "vosk"
  model: "medium"
  language: "en"
```

!!! warning "Vosk templates"
    Vosk models must be downloaded separately and configured correctly. See the
    documentation for details.

## Common parameters

Some parameters are shared between transcribers and influence performance and accuracy.
Below, we explain the most relevant ones:

### Compute Type

Defines the numerical precision used in the model's calculations. The options are:

- int8: 8-bit integer, optimized for speed, but with a possible loss of precision.
- float16: 16-bit floating point, balances performance and accuracy.
- float32: 32-bit floating point, offers greater precision but is slower.

The choice depends on the hardware and the balance between speed and quality.

### FP16

Enables (true) or disables (false) the use of 16-bit floating point. When enabled, it reduces memory
consumption and speeds up processing, but can have an impact on precision.

### Beam Size

Controls the width of the search in the Beam Search algorithm, used to generate text sequences. Larger
values (e.g. 5 or 10) increase accuracy, but consume more time and memory. Smaller values (e.g. 1 or 3)
are faster but less accurate.

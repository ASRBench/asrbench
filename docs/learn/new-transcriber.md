## Creating a New Transcriber Implementation

To add a new transcriber to ASRBench, you must create a class that inherits from the 
Transcriber abstract class and implements its methods.  In addition, you must use the register_transcriber 
decorator so that the transcriber is recognized and instantiated automatically during execution.

## Steps

We suggest creating a package for your transcribers. In the ASRBench configuration file, you will indicate the path
of this directory to load the transcribers.

Create a new class that inherits from Transcriber [Transcriber](../references/transcribers/transcriber.md) and use the
[@register_transcriber](../references/transcribers/registry.md) decorator.

```python
from asrbench.transcribers.abc_transcriber import Transcriber
from asrbench.transcribers.registry import register_transcriber

@register_transcriber
class MyTranscriber(Transcriber):
    @classmethod
    def from_config(cls, name: str, config: Dict[str, Any]):
        # Initializes the transcriber based on name and configuration
        pass

    @property
    def params(self) -> Dict[str, Any]:
        # Returns the configuration parameters
        pass

    @property
    def name(self) -> str:
        # Returns the name of the transcriber
        pass

    def transcribe(self, audio_path: str) -> str:
        # Transcribe the audio from the provided path
        pass

    def load(self) -> None:
        # Loads the required model and resources
        pass

    def unload(self) -> None:
        # Releases the model's resources
        pass
```

Implement Each method of the Transcriber abstract class:

- **from_config**: Creates an instance of the transcriber from the name and configuration.
- **params**: Returns the parameters used in the configuration.
- **name**: Returns the name of the transcriber in the configuration file.
- **transcribe**: Processes an audio file and returns the transcription.
- **load**: Loads the model and resources into memory.
- **unload**: Releases the resources from memory.

See the Transcriber class documentation for details of each method. Examples of implementations are
available at [cli repository](https://github.com/ASRBench/asrbench-cli/tree/main/asrbench_cli/transcribers).

## Questions
If you need help implementing the methods or integrating the transcriber, consult the or open an 
[issue](https://github.com/ASRBench/asrbench-cli/issues/new).
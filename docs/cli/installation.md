To install ASRBench cli, all you need is [Python 3.12+](https://www.python.org/downloads/) and pip. Use the
command below to install the latest version:

```sh
pip install asrbench-cli
``` 

??? warning "Torch cuda"
    There is a certain problem with the version of nvidia cuda you use,
    currently the framework and cli deal with torch+cu12, which would be
    compatible with cuda 12, if you use a different version you would have to
    upgrade or downgrade to cuda 12. I honestly don't know how to solve this
    kind of problem since the cuda version of torch is installed as an indirect
    dependency. If you know how to solve it, or have an idea of how to solve it,
    feel free to open an [issue](https://github.com/ASRBench/asrbench-cli/issues/new)
    to talk about it, or if you prefer you can make a PR.
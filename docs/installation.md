To install ASRBench, all you need is [Python 3.12+](https://www.python.org/downloads/) and pip. Use the
command below to install the latest version:

```sh
pip install asrbench
```

??? note "Windows users"
    To use the framework's pkg report, you need to install GTK3. Follow these simple steps:

	- Download the [GTK3 installer](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases) for Windows.
	- Run the installer and follow the on-screen instructions.
	- Make sure you add the installation directory (usually C:\Program Files\GTK3-Runtime Win64\bin) to the Windows 
    PATH environment variable.

??? warning "Torch cuda"
    There is a certain problem with the version of nvidia cuda you use,
    currently the framework and cli deal with torch+cu12, which would be
    compatible with cuda 12, if you use a different version you would have to
    upgrade or downgrade to cuda 12. I honestly don't know how to solve this
    kind of problem since the cuda version of torch is installed as an indirect
    dependency. If you know how to solve it, or have an idea of how to solve it,
    feel free to open an [issue](https://github.com/ASRBench/asrbench/issues/new)
    to talk about it, or if you prefer you can make a PR.


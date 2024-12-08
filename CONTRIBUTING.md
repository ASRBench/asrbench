This is an open source project that accepts contributions via pull requests on GitHub. This document serves to align 
contributions according to established standards. If you have any questions, please 
[open an issue](https://github.com/ASRBench/asrbench/issues/new).

### Project structure

To make it easier for you to navigate and contribute, here is an overview of the repository's structure:

    |--- asrbench # Framework code
    |        |--- report # Package that generates PDF reports
    |                |--- plots # Utilities for plotting graphs
    |                |--- templates # HTML report templates
    |        |--- transcribers # Contracts and utilities for transcription systems
    |--- docs # Documentation
    |        |--- assets # Static resources
    |        |--- learn # Framework tutorials
    |        |--- references # Documentation of docstrings in code
    |--- tests # Automated tests


### Installing dependencies

Before you start developing, install the project's dependencies. They are listed in the pyproject.toml file.

Run the following command from the root of the project to install the dependencies:
```sh
poetry install
```

Activate the virtual environment with:
```sh
poetry shell
```

After that, you can change the code, run the tests and serve the documentation without any problems.

### Using the Makefile

The Makefile was included to simplify common tasks during development. Here are the commands available:
```sh
make doc
# Serves the documentation locally, allowing viewing in the browser.
```

```sh
make test
# Runs the automated tests.
```
	
### Steps to contribute

- Fork this repository.
- Make your changes to the repository.
- Test your changes before committing.
- Make clear and descriptive commits.
- Insert a short summary of what was added in the pull request.
- Request a pull request.

### Checklist for Pull Requests

Before sending a pull request, check the following points:

- [ ] The code follows the project standard.
- [ ] Tests have been added or updated to cover the changes.
- [ ] The documentation has been updated (if applicable).
- [ ] The code has been tested locally and is working as expected.

### Commits Recommendation 

For better semantics in commits, we recommend following [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) 
patterns. This facilitates analysis and project history.
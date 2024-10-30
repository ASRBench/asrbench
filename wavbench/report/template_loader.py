from jinja2 import Environment, Template
from pathlib import Path
from typing import Optional


def _get_default_template_dir() -> str:
    return Path(__file__).joinpath("templates").__str__()


class TemplateLoader:
    def __init__(self, template_dir: Optional[str] = None) -> None:
        self._env: Environment = Environment(
            loader=template_dir or _get_default_template_dir()
        )

    def load(self, name: str) -> Template:
        return self._env.get_template(name)

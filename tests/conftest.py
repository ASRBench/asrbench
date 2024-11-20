"""Fixtures to use in tests."""
import yaml
from asrbench.config_loader import ConfigLoader
from datetime import datetime, UTC
from pathlib import Path
from pytest import fixture
from typing import Dict, Any


def create_configfile(tmp_path: Path, data: Dict[str, Any]) -> str:
    cfg_path = tmp_path.joinpath("config.yml")

    with open(cfg_path, "w") as file:
        yaml.dump(data, file)

    return cfg_path.__str__()


@fixture
def empty_configfile(tmp_path) -> str:
    return create_configfile(tmp_path, {})


@fixture
def config_data(tmp_path) -> Dict[str, Any]:
    return {
        "output": {
            "type": "json",
            "dir": tmp_path.joinpath("result").__str__(),
            "filename": "testbench"
        },
        "transcriber_dir": "./tests/custom",
        "datasets": {
            "test_dataset": {
                "audio_dir": tmp_path.joinpath("audios").__str__(),
                "reference_dir": tmp_path.joinpath("references").__str__()
            }
        },
        "custom": {
            "test_transcriber": {
                "asr": "custom"
            }
        }
    }


@fixture
def full_config_file(tmp_path, config_data) -> str:
    return create_configfile(tmp_path, config_data)


@fixture
def config_loader_with_empty_data(empty_configfile) -> ConfigLoader:
    return ConfigLoader(empty_configfile)


@fixture
def config_loader_with_full_data(full_config_file):
    return ConfigLoader(full_config_file)


@fixture
def timestamp():
    return datetime.now(UTC).strftime("%Y%m%dT%H%M%S")

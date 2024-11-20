import pytest
from .conftest import (
    config_loader_with_empty_data,
    config_loader_with_full_data,
)
from pathlib import Path
from pytest import mark


@mark.errors
@mark.configloader
def test_when_dataset_not_present(config_loader_with_empty_data):
    with pytest.raises(
            ValueError, match="Configfile dont have datasets configuration.",
    ):
        config_loader_with_empty_data.get_datasets()


@mark.errors
@mark.configloader
def test_when_transcribers_not_present(config_loader_with_empty_data):
    with pytest.raises(
            KeyError,
            match="Configfile dont have custom section.",
    ):
        config_loader_with_empty_data.get_transcribers()


@mark.configloader
def test_read_configfile(config_loader_with_full_data, config_data):
    assert config_loader_with_full_data.data == config_data


@mark.configloader
@mark.skip("Not Implemented")
def test_get_output_ctx():
    ...


@mark.configloader
def test_get_output_dir_when_no_dir(config_loader_with_empty_data):
    assert config_loader_with_empty_data.get_output_dir() == Path.cwd()


@mark.configloader
def test_get_output_dir(config_loader_with_full_data, tmp_path):
    assert (
            config_loader_with_full_data.get_output_dir()
            ==
            tmp_path.joinpath("result").__str__()
    )


@mark.configloader
def test_set_up_output_filename_with_default(config_loader_with_empty_data):
    assert config_loader_with_empty_data.get_output_filename() == "asrbench"


@mark.configloader
def test_get_output_filepath_with_default(
        config_loader_with_empty_data,
        timestamp,
):
    assert (
        config_loader_with_empty_data.get_output_filepath()
        ==
        f"./asrbench_{timestamp}",
    )


@mark.configloader
@mark.skip("Not Implemented")
def test_set_up_benchmark(config_loader_with_full_data):
    ...

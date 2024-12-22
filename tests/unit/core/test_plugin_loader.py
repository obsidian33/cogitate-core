from unittest.mock import MagicMock
from pytest import raises

from platscan.core.plugin_loader import PluginLoader


def test_plugin_loader_valid_plugins(mocker, valid_plugin1):
    def fake_import_module(name, _):
        if name == "plugin1":
            return MagicMock(Plugin=lambda: valid_plugin1)
        if name == "plugin2":
            return MagicMock(Plugin=lambda: valid_plugin1)

    mock_import_module = mocker.patch("importlib.import_module")
    mock_import_module.side_effect = fake_import_module

    plugins = PluginLoader.load_plugins(["plugin1", "plugin2"])
    assert len(plugins) == 2


def test_plugin_loader_invalid_plugin(mocker, valid_plugin1, invalid_plugin):
    def fake_import_module(name, _):
        if name == "valid_plugin":
            return MagicMock(Plugin=lambda: valid_plugin1)
        if name == "invalid_plugin":
            return MagicMock(Plugin=lambda: invalid_plugin)

    mock_import_module = mocker.patch("importlib.import_module")
    mock_import_module.side_effect = fake_import_module

    with raises(TypeError, match="Plugin 'invalid_plugin' does not conform to PluginProtocol"):
        plugins = PluginLoader.load_plugins(["valid_plugin", "invalid_plugin"])
        assert len(plugins) == 1


def test_plugin_loader_plugin_not_found():
    def fake_import_module(name, _):
        if name == "plugin1":
            raise ModuleNotFoundError(f"No module named '{name}'")

    with raises(ImportError, match="Failed to load plugin 'plugin1'"):
        system = PluginLoader.load_plugins(["plugin1"])

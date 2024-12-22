import importlib

from typing import cast
from platscan.core.models import PluginProtocol


class PluginLoader:
    @staticmethod
    def load_plugins(plugin_names: list[str]) -> list[PluginProtocol]:
        return [PluginLoader.load_plugin(plugin_name) for plugin_name in plugin_names]

    @staticmethod
    def load_plugin(plugin_name: str) -> PluginProtocol:
        try:
            module = importlib.import_module(plugin_name, ".")
            plugin_instance = module.Plugin()
        except ModuleNotFoundError as e:
            raise ImportError(f"Failed to load plugin '{plugin_name}'") from e

        if not isinstance(plugin_instance, PluginProtocol):
            raise TypeError(f"Plugin '{plugin_name}' does not conform to PluginProtocol")

        return cast(PluginProtocol, plugin_instance)

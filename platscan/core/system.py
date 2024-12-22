from platscan.core.models import PluginProtocol


class System:
    def __init__(self, plugins: list[PluginProtocol]):
        self._plugins = plugins

    def get_loaded_plugins(self) -> list:
        return self._plugins

    def run(self) -> list:
        if not self._plugins:
            raise RuntimeError("No plugins were imported.")

        return [secret for plugin in self._plugins for secret in plugin.secrets()]

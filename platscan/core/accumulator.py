from platscan.core.models import PluginProtocol


class Accumulator:
    def __init__(self, plugins: list[PluginProtocol]):
        self._plugins = plugins

    def search_name(self, text: str):
        return self._search("search_name", text)

    def search_values(self, text: str):
        return self._search("search_values", text)

    def _search(self, method_name: str, text: str) -> list:
        return [
            secret
            for client in self._plugins
            for secret in getattr(client, method_name)(text)
        ]

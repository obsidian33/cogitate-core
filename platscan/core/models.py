from typing import Protocol, runtime_checkable


class SecretData(Protocol):
    client_name: str
    name: str


class SecretValueData(Protocol):
    secret_data: SecretData
    value: str


class SecretsClient(Protocol):
    def search_name(self, text: str) -> list[SecretData]:
        pass

    def search_values(self, text: str) -> list[SecretValueData]:
        pass


@runtime_checkable
class PluginProtocol(Protocol):
    def secrets(self) -> list[SecretData]:
        pass

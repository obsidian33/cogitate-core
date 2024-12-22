import boto3

from platscan.core.models import PluginProtocol
from platscan.core.models import SecretData
from platscan.plugins.aws.secrets import Secrets


class Plugin(PluginProtocol):
    def secrets(self) -> list[SecretData]:
        client = boto3.client("secretsmanager", region_name="us-east-1")
        return Secrets(client).search_name("test")

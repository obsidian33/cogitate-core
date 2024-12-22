import jmespath

from platscan.core.models import SecretsClient


class Secrets(SecretsClient):
    def __init__(self, client):
        self.client = client

    def search_name(self, text):
        response = self.client.list_secrets(
            Filters=[{"Key": "all", "Values": [text]}]
        )
        secrets = [secret["Name"] for secret in response["SecretList"]]
        return secrets

    def search_values(self, text: str):
        secret_arns = list(
            self.client.get_paginator("list_secrets").paginate(
                PaginationConfig={"PageSize": 100}
            ).search("SecretList[].ARN")
        )
        secret_values = self.client.batch_get_secret_value(SecretIdList=secret_arns)

        return jmespath.search("SecretValues[].SecretString", secret_values)

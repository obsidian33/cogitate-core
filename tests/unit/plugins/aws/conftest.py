from pytest import fixture
from os import environ
from moto import mock_aws
import boto3


@fixture(autouse=True)
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    environ.update(
        {
            "MOTO_ALLOW_NONEXISTENT_REGION": "True",
            "AWS_ACCESS_KEY_ID": "testing",
            "AWS_SECRET_ACCESS_KEY": "testing",
            "AWS_SECURITY_TOKEN": "testing",
            "AWS_SESSION_TOKEN": "testing",
            "AWS_DEFAULT_REGION": "us-east-1",
        }
    )


@fixture
def secretsmanager_client():
    """Return a mocked Secrets Manager client."""
    with mock_aws():
        yield boto3.client("secretsmanager", region_name=environ["AWS_DEFAULT_REGION"])

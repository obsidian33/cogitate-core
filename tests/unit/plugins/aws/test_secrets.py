from platscan.plugins.aws.secrets import Secrets


def test_secrets_search_name(secretsmanager_client):
    expected = "nameOfSecret"
    secretsmanager_client.create_secret(Name=expected)
    secrets = Secrets(secretsmanager_client)

    result = secrets.search_name(expected)
    assert result == [expected]


def test_search_multiple_secrets(secretsmanager_client, mocker):
    # Moto is not working correctly with Filter Key = 'all'
    # secretsmanager_client.create_secret(Name="GoodSecret1")
    # secretsmanager_client.create_secret(Name="BadSecret2")
    # secretsmanager_client.create_secret(Name="GoodSecret3")
    mock_data = {"SecretList": [
        {"Name": "GoodSecret1"},
        {"Name": "GoodSecret3"}
    ]}
    mocker.patch.object(secretsmanager_client, "list_secrets", return_value=mock_data)

    secrets = Secrets(secretsmanager_client)

    result = secrets.search_name("ood")
    assert result == ["GoodSecret1", "GoodSecret3"]


def test_search_values(secretsmanager_client):
    secretsmanager_client.create_secret(Name="GoodSecret1", SecretString="supersecret")
    secrets = Secrets(secretsmanager_client)
    result = secrets.search_values("super")
    assert result == ["supersecret"]

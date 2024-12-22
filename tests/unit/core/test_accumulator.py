from platscan.core.models import SecretsClient
from platscan.core.accumulator import Accumulator


def test_secrets_search_name(mocker):
    mock_client1 = mocker.Mock(spec=SecretsClient)
    mock_client2 = mocker.Mock(spec=SecretsClient)
    mock_client1.search_name.return_value = [{"client_name": "Client1", "name": "Secret1"}]
    mock_client2.search_name.return_value = [{"client_name": "Client2", "name": "secret"}]

    secrets = Accumulator([mock_client1, mock_client2])
    result = secrets.search_name("sec")

    assert result == [
        {"client_name": "Client1", "name": "Secret1"},
        {"client_name": "Client2", "name": "secret"}
    ]

def test_secrets_search_values(mocker):
    mock_client1 = mocker.Mock(spec=SecretsClient)
    mock_client2 = mocker.Mock(spec=SecretsClient)
    mock_client1.search_values.return_value = [
        { "secret": {"client_name": "Client1", "name": "Secret1"}, "value": "secret1Value" }
    ]
    mock_client2.search_values.return_value = [
        { "secret": {"client_name": "Client2", "name": "secret"}, "value": "closeNitSecret" }
    ]

    secrets = Accumulator([mock_client1, mock_client2])
    result = secrets.search_values("secret")

    assert result == [
        { "secret": {"client_name": "Client1", "name": "Secret1"}, "value": "secret1Value" },
        { "secret": {"client_name": "Client2", "name": "secret"}, "value": "closeNitSecret" },
    ]
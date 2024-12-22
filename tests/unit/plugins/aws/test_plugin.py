from platscan.plugins.aws.plugin import Plugin


def test_plugin_secrets(secretsmanager_client):
    plugin = Plugin()
    result = plugin.secrets()
    assert result == [{"client_name": "aws", "name": "awsSecret"}]

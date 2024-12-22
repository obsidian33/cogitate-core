from click.testing import CliRunner
from platscan.ui.cli import cli

def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli, [])
    assert result.exit_code == 0

def test_secrets():
    runner = CliRunner()
    result = runner.invoke(cli, ["secrets"])
    assert result.exit_code == 0
    assert result.output == "CLI Secrets\n"

def test_secrets_find():
    runner = CliRunner()
    result = runner.invoke(cli, ["secrets", "find", "nameOfSecret"])
    assert result.output == "CLI Secrets\nCLI Secrets Find: nameOfSecret\n"
    # assert "Find" in result.output
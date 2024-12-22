import click

from platscan.core.plugin_loader import PluginLoader
from platscan.core.system import System


@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)


@cli.group()
@click.pass_context
def secrets(ctx):
    ctx.obj["resource"] = "secrets"


@secrets.command()
@click.argument("text")
@click.pass_context
def search(ctx, text: str):
    plugin_names = ["platscan.plugins.aws.plugin"]
    loaded_plugins = PluginLoader.load_plugins(plugin_names)
    system = System(loaded_plugins)
    results = system.run()
    click.echo(results)


if __name__ == '__main__':
    cli(obj={})

from pytest import raises
from platscan.core.system import System


def test_system(valid_plugin1, valid_plugin2):
    plugins = [valid_plugin1, valid_plugin2]
    system = System(plugins)
    assert len(system.get_loaded_plugins()) == 2


def test_system_run_with_no_plugins():
    system = System([])
    with raises(RuntimeError, match="No plugins were imported."):
        system.run()


def test_system_run(valid_plugin1, valid_plugin2):
    plugins = [valid_plugin1, valid_plugin2]
    system = System(plugins)
    result = system.run()
    assert result == ["validPlugin1Secret", "validPlugin2Secrets"]

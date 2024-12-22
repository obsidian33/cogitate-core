from unittest.mock import MagicMock
from pytest import fixture


@fixture
def valid_plugin1():
    class ValidPlugin1:
        def secrets(self):
            return ["validPlugin1Secret"]
    return ValidPlugin1()


@fixture
def valid_plugin2():
    class ValidPlugin2:
        def secrets(self):
            return ["validPlugin2Secrets"]
    return ValidPlugin2()


@fixture
def invalid_plugin():
    class InvalidPlugin:
        def missing_method(self):
            return "Oops"

from unittest import TestCase

from mock import Mock

from cloudshell.networking.juniper.runners.juniper_autoload_runner import JuniperAutoloadRunner


class TestJuniperAutoloadRunner(TestCase):
    def setUp(self):
        self._cli = Mock()
        self._logger = Mock()
        self._resource_config = Mock()
        self._api = Mock()
        self._instance = JuniperAutoloadRunner(self._cli, self._logger, self._resource_config, self._api)

    def test_init(self):
        self.assertIs(self._instance._cli, self._cli)
        self.assertIs(self._instance._logger, self._logger)
        self.assertIs(self._instance.resource_config, self._resource_config)
        self.assertIs(self._instance._api, self._api)

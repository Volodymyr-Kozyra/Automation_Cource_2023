import os
from src.config.providers.base_config import BaseConfigKeyProvider


class ConfigFromEnvProvider(BaseConfigKeyProvider):
    """_summary_
    Allows configuration through the env variables
    """
    def get(self, key):
        """
        Returns config value for the given key
        :param str key: Key to retreive
        """
        return os.environ.get(key)
    
from abc import ABC, abstractmethod
import logging
from azure.identity import EnvironmentCredential
import datadayessentials.utils
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class IAuthentication(ABC):
    """Abstract base class for all authentication classes"""

    @staticmethod
    def get_azure_credentials():
        """"

        Returns:
            EnvironmentCredential: Credential chain for authenticating with azure that looks for environment credentials first and then tries to use the browser to authenticate.
        """
        return EnvironmentCredential()

    @abstractmethod
    def get_credentials(self) -> dict:
        pass


class ISQLServerConnection:
    @abstractmethod
    def connect(self):
        """
        Connect to database/cloud provider
        """
        pass

    @abstractmethod
    def run_sql(self):
        """
        Run SQL with the connection above
        """
        pass

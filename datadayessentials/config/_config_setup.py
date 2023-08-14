from datadayessentials.config._config import GlobalConfig, LocalConfig
from pathlib import Path
from typing import Dict, List, Union, Optional, Any
import os
import logging

class ConfigAlreadyExistsError(Exception):
    pass


class ConfigSetup:
    @staticmethod
    def create_core_cache_dir_if_not_exists() -> None:
        """
        Creates a global config file if one does not already exist.

        Returns:
            None
        """
        global_cfg = GlobalConfig().read()

        # Create the local cache directory if it doesnt already exist
        cache_dir = Path(os.path.join(Path.home(), global_cfg["local_cache_dir"]))
        if Path.exists(cache_dir):
            logging.info("Local cache directory exists")
        else:
            logging.info("Local cache directory does not exist. Creating...")
            cache_dir.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def create_local_config_if_not_exists() -> None:
        """
        Creates a global config file if one does not already exist.

        Returns:
            None
        """
        LocalConfig()
        
    @staticmethod
    def initialise_core_config(
        environment_name: str,
        subscription_id: str,
        tenant_id: str,
        resource_group: str,
        machine_learning_workspace: str,
        data_lake: str,
        create_new_config: Optional[bool] = False,
        project_dataset_container: str = "projects",
    ):
        """
        Initialise the core local config. This provides the minimum config required to either load an existing config file that your team has registered in a data lake or create a new config file for your team to use.
        """
        
        LocalConfig().create_local_config()

        team_env_settings = {
            "environment_name": environment_name,
            "subscription_id": subscription_id,
            "tenant_id": tenant_id,
            "resource_group": resource_group,
            "machine_learning_workspace": machine_learning_workspace,
            "data_lake": data_lake,
            "project_dataset_container": project_dataset_container
        }

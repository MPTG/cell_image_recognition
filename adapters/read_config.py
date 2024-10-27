import json

class ReadConfig:
    """
    class that reads config files
    """
    def __init__(self, config_file:str):
        self.config_file = config_file

    def read_config(self):
        with open(self.config_file, "r") as config_file:
            config = json.load(config_file)
            return config
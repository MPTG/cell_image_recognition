class ReadModel:
    """
    class used for reading AI models from files.
    """

    def __init__(self, model_path:str):
        self.model_path = model_path

    def read_model(self):
        """
        change return to read_model from tensorflow function
        :return:
        """
        return self.model_path
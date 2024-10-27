from ultralytics import YOLO
from tensorflow.lite.tools.flatbuffer_utils import read_model
from ultralytics.data.converter import yolo_bbox2segment


class ReadModel:
    """
    class used for reading AI models from files.
    """

    def __init__(self, model_path:str):
        self.model_path = model_path

    def read_model(self) -> YOLO:
        """
        change return to read_model from tensorflow function
        """
        model = YOLO(self.model_path)
        return model
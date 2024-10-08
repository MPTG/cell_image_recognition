from ..adapters.read_model import ReadModel

def test_read_models():
    model_path = '' # model patg
    model_class = ReadModel(model_path=model_path)
    model = model_class.read_model()
    assert type(model) == ReadModel

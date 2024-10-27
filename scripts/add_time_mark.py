from datetime import datetime

class AddTimeMark:
    """
    This class helps to add time mark to other files in this repo
    """

    def add_time_mark() -> str:
        time = datetime.now()
        timestamp = time.strftime('%Y_%m_%d_%H_%M_%S')

        return timestamp

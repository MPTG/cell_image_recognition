from os import times

from cell_image_recognition.adapters.slow_down_video import SlowDownVideo
from scripts.add_time_mark import AddTimeMark


def get_captured_frames() -> None:
    dir_path = 'data/video/test_video.mp4'
    timestamp = AddTimeMark.add_time_mark()
    output_path = f'data/slowed_video/slowed_video{timestamp}.mp4'
    slow_down_video = SlowDownVideo(dir_path, output_path)
    slow_down_video.slow_video()

get_captured_frames()

import cv2

class SlowDownVideo:
    """
    Class that will be responsible for capturing video frames and slowing down video.
    """
    def __init__(self, dir_path: str, out_put_path: str) -> None:
        self.dir_path = dir_path
        self.output_path = out_put_path

    def slow_video(self) -> None:
        """
        Function responsible for slowing down the video
        """
        cap = cv2.VideoCapture(self.dir_path)
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        fps = cap.get(cv2.CAP_PROP_FPS)
        print(f"Original FPS: {fps}")

        # Adjust FPS to slow down video (e.g., slow down by 2x)
        new_fps = fps / 2
        print(f"New FPS: {new_fps}")

        output_path = self.output_path
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        output = cv2.VideoWriter(output_path, fourcc, new_fps, (width, height))

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow('frame', frame)
            output.write(frame)
            k = cv2.waitKey(int(1000 / new_fps))  # Adjust wait time based on new FPS
            if k == ord('q'):
                break

        cap.release()
        output.release()
        cv2.destroyAllWindows()

slow_vid = SlowDownVideo(
    dir_path='/Users/maciekandrzejewski/projects/cell_image_recognition/data/video/1to1_01.mp4',
    out_put_path='/Users/maciekandrzejewski/projects/cell_image_recognition/data/video/output/slowed_video.mp4')
slow_vid.slow_video()

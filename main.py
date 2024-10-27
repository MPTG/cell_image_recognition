from ultralytics import YOLO
from adapters.read_config import ReadConfig
import cv2

def main() -> None:
	config = ReadConfig(
		'/Users/maciekandrzejewski/projects/cell_image_recognition/data/config/config.json',
	).read_config()
	model = YOLO(config['model_path'])
	video_path = '/Users/maciekandrzejewski/projects/cell_image_recognition/data/video/1to1_01.mp4'
	cap = cv2.VideoCapture(video_path)

	if not cap.isOpened():
		print('Video cannot be opened!')
		exit()

	frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
	fps = cap.get(cv2.CAP_PROP_FPS)

	output_video = '/Users/maciekandrzejewski/projects/cell_image_recognition/data/video/output/output.mp4'
	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	out = cv2.VideoWriter(output_video, fourcc, fps, (frame_width, frame_height))
	f = 0 # number of frames
	t = 0 # time spend for frames

	while cap.isOpened():
		ret, frame = cap.read()
		if not ret:
			break
		results = model(frame)
		annotated_frame = results[0].plot()
		out.write(annotated_frame)
		detected_classes = [model.names[int(cls)] for cls in results[0].boxes.cls]
		print(detected_classes[0])

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cap.release()
	out.release()



if __name__ == '__main__':
	main()


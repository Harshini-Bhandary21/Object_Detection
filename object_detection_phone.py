import cv2
from typing import Optional
import torch
from ultralytics import YOLO


def load_yolov5_model() -> torch.nn.Module:
    """
    Load the YOLOv5 pretrained model from Ultralytics hub.

    Returns:
        YOLOv5 PyTorch model
    """
    return torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)


def load_yolov8_model(model_path: str = "yolov8n.pt") -> YOLO:
    """
    Load the YOLOv8 pretrained model.

    Args:
        model_path: Path to the YOLOv8 model file.

    Returns:
        YOLO model object
    """
    return YOLO(model_path)


def open_video_stream(url: str) -> Optional[cv2.VideoCapture]:
    """
    Open a video stream from a URL or device.

    Args:
        url: URL of the video stream or device index.

    Returns:
        cv2.VideoCapture object if successful, None otherwise
    """
    cap = cv2.VideoCapture(url)
    if not cap.isOpened():
        print(f"Error: Could not open video stream from {url}")
        return None
    return cap


def process_frames_yolov5(cap: cv2.VideoCapture, model: torch.nn.Module) -> None:
    """
    Perform object detection on video frames using YOLOv5.

    Args:
        cap: OpenCV VideoCapture object
        model: YOLOv5 model
    """
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        results = model(frame)
        frame = results.render()[0]

        cv2.imshow("YOLOv5 Object Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


def process_frames_yolov8(cap: cv2.VideoCapture, model: YOLO) -> None:
    """
    Perform object detection on video frames using YOLOv8.

    Args:
        cap: OpenCV VideoCapture object
        model: YOLOv8 model
    """
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame. Check URL or connection.")
            break

        results = model(frame)
        annotated_frame = results[0].plot()

        cv2.imshow("YOLOv8 Object Detection", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


def main() -> None:
    """
    Main entry point for object detection using phone webcam stream.
    """
    # Video stream URL from phone camera
    url = "http://10.203.219.49:4747/video"

    # Choose which model to use
    use_yolov8 = True

    cap = open_video_stream(url)
    if not cap:
        return

    if use_yolov8:
        model = load_yolov8_model()
        process_frames_yolov8(cap, model)
    else:
        model = load_yolov5_model()
        process_frames_yolov5(cap, model)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

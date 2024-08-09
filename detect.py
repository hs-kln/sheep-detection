from ultralytics import YOLO
import cv2
from PIL import Image
import io
import numpy as np

def detect_objects(image_bytes):
    # Load the YOLO model
    model = YOLO("best_yolov9_weights.pt")  # Replace with your model path
    
    # Convert bytes to a PIL Image
    image = Image.open(io.BytesIO(image_bytes))
    
    # Convert PIL Image to OpenCV format
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    # Perform detection
    results = model(image)
    
    # Annotate image with bounding boxes
    annotated_img = results[0].plot()
    
    # Extract categories
    categories = results[0].names  # Get category names
    detected_classes = results[0].boxes.cls  # Detected classes as indices
    detected_categories = [categories[int(cls)] for cls in detected_classes]  # Map indices to names
    
    # Convert annotated image to bytes
    _, buffer = cv2.imencode('.jpg', annotated_img)
    img_bytes = buffer.tobytes()
    
    # Convert categories to a string
    categories_str = ', '.join(detected_categories)
    
    return img_bytes, categories_str

def detect_objects_model2(image_bytes):
    # Load the second YOLO model
    model = YOLO("teeth.pt")  # Replace with your second model path
    
    # Convert bytes to a PIL Image
    image = Image.open(io.BytesIO(image_bytes))
    
    # Convert PIL Image to OpenCV format
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    # Perform detection
    results = model(image)
    
    # Annotate image with bounding boxes
    annotated_img = results[0].plot()
    
    # Extract categories
    categories = results[0].names  # Get category names
    detected_classes = results[0].boxes.cls  # Detected classes as indices
    detected_categories = [categories[int(cls)] for cls in detected_classes]  # Map indices to names
    
    # Convert annotated image to bytes
    _, buffer = cv2.imencode('.jpg', annotated_img)
    img_bytes = buffer.tobytes()
    
    # Convert categories to a string
    categories_str = ', '.join(detected_categories)
    
    return img_bytes, categories_str

def detect_objects_model3(image_bytes):
    # Load the third YOLO model
    model = YOLO("healthy.pt")  # Replace with your third model path
    
    # Convert bytes to a PIL Image
    image = Image.open(io.BytesIO(image_bytes))
    
    # Convert PIL Image to OpenCV format
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    # Perform detection
    results = model(image)
    
    # Annotate image with bounding boxes
    annotated_img = results[0].plot()
    
    # Extract categories
    categories = results[0].names  # Get category names
    detected_classes = results[0].boxes.cls  # Detected classes as indices
    detected_categories = [categories[int(cls)] for cls in detected_classes]  # Map indices to names
    
    # Convert annotated image to bytes
    _, buffer = cv2.imencode('.jpg', annotated_img)
    img_bytes = buffer.tobytes()
    
    # Convert categories to a string
    categories_str = ', '.join(detected_categories)
    
    return img_bytes, categories_str





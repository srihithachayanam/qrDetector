# train.py
from ultralytics import YOLO

# 1. Load a pre-trained model 
model = YOLO('yolov8n.pt') 

# 2. Start training
# Ensure your training data is structured correctly based on qr.yaml
results = model.train(
    data='src/datasets/qr.yaml', 
    epochs=20, 
    imgsz=640, 
    batch=16, 
    name='yolov8n_qr_detector_v1',
)

print("\n--- Training Complete ---")
print(f"Model saved to: runs/detect/{results.save_dir}/weights/best.pt")
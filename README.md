%%writefile README.md
# multiqr-hackathon

## Multi-QR Code Detection Solution (YOLOv8) - Stage 1 Detection Only

This repository contains the complete source code for our QR code detection model, adhering to the required hackathon structure and submission format for **Stage 1: Detection**.

### 1. Environment Setup

Our solution was developed using **Python 3.10**.

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/srihithachayanam/qrDetector.git
    cd multiqr-hackathon
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### 2. How to Run Training (For Reproducibility)

Training data is located within the `src/` directory structure. **Note:** You must place your training images and labels inside `src/datasets/qr_data/`.

```bash
# Example: Train for 50 epochs using a small YOLOv8 model.
python train.py --data src/datasets/qr_data/qr.yaml --model yolov8s.pt --epochs 50 --imgsz 640
```
**link for drive (includes results and weights)
https://drive.google.com/drive/folders/1PV1v6fL_shMvw8CRNmJjq8NE7RCxFazg?usp=drive_link

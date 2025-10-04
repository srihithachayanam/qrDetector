# multiqr-hackathon: Multi-QR Code Detection Solution

## Mandatory Submission: Object Detection 

This repository contains the complete source code and necessary models for our QR code detection hackathon submission. The code is complete, runnable, and reproducible, focusing on the mandatory detection task.

The given dataset does not contain labels, therefore the annotations were done manually using 'make sense' for the split data consisting of 160 train images and 40 validation images (out of 200).


### 1. Environment Setup

Our solution relies on **Git LFS** (Large File Storage) for handling the final model file(s) and requires **Python 3.10**.

1.  **Install Git LFS:**
    **The organizers MUST install Git LFS first** to download the models (our large models are tracked via LFS).
    ```bash
    # Install Git LFS (if not already present on the system)
    # Check instructions for your OS: [https://git-lfs.com/](https://git-lfs.com/)
    ```

2.  **Clone the Repository and Pull Large Files:**
    The Git LFS models must be explicitly pulled after cloning.
    ```bash
    git clone [https://github.com/srihithachayanam/qrDetector.git](https://github.com/srihithachayanam/qrDetector.git)
    cd qrDetector
    # Download the large model files:
    git lfs pull
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

### 2. Execution for Mandatory Detection

This section details the single command needed to reproduce the output for the **Detection Task** on the hidden test images.

#### 2.1 The Single Execution Command

The script `infer.py` (or `evaluate.py`, whichever generates the JSON) should be modified/used to output only the required detection bounding boxes.

**Instructions:** Place the hidden test images into a folder named `test_images/` in the root of the repository.

```bash
# RUN THIS COMMAND (Adjust script/arguments if necessary to output JSON):
python infer.py \
    --model yolov8s.pt \
    --source ./test_images/ \
    --output_path ./submission_hidden.json
```
**link for drive (includes results images along with confusion matrix)
https://drive.google.com/drive/folders/1PV1v6fL_shMvw8CRNmJjq8NE7RCxFazg?usp=drive_link

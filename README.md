# 🪖 Helmet Detection using YOLOv8

## 📌 Project Overview

This project implements a custom **Helmet Detection System** using **YOLOv8**. The model is fine-tuned on the **Hard Hat Detection** dataset to detect construction safety equipment in images.

The complete pipeline includes:

- Parsing Pascal VOC XML annotations
- Converting XML annotations to YOLO format
- Preparing train and validation datasets
- Fine-tuning a pretrained YOLOv8 model
- Evaluating the model using Precision, Recall, and mAP
- Running inference on unseen images

---

## 📂 Dataset

**Dataset:** Hard Hat Detection Dataset

Classes:

- 🪖 Helmet
- 👤 Head
- 🚶 Person

---

## 🛠️ Tech Stack

- Python
- PyTorch
- Ultralytics YOLOv8
- OpenCV
- NumPy
- Google Colab

---

## ⚙️ Project Workflow

```
Pascal VOC XML
        │
        ▼
XML → YOLO Label Conversion
        │
        ▼
Dataset Preparation
        │
        ▼
Train / Validation Split
        │
        ▼
YOLOv8 Fine-Tuning
        │
        ▼
Model Evaluation
        │
        ▼
Inference on New Images
```

---

## 📊 Model Performance

| Metric | Score |
|---------|------:|
| Precision | **94.6%** |
| Recall | **58.7%** |
| mAP@50 | **63.1%** |
| mAP@50-95 | **41.6%** |

---

## 📈 Training Curves

> Replace the image below with your `results.png`.

<p align="center">
<img src="sample_results/results.png" width="900">
</p>

---

## 🖼️ Sample Predictions

### Input Image

<p align="center">
<img src="sample_results/input.jpg" width="700">
</p>

---

### Detection Result

<p align="center">
<img src="sample_results/output.png" width="700">
</p>

---
## 🎥 Demo

![Helmet Detection Demo](demo.gif)

---
## 🚀 Running Inference

```python
from ultralytics import YOLO

model = YOLO("best.pt")

results = model.predict(
    source="image.jpg",
    conf=0.25,
    save=True
)
```

---

## 📁 Project Structure

```
Helmet-Detection-YOLOv8/
│
├── Helmet_Detection.ipynb
├── data.yaml
├── requirements.txt
├── README.md
├── best.pt
├── sample_results/
│   ├── input.jpg
│   ├── output.jpg
│   └── results.png
└── LICENSE
```

---

## 🎯 What I Learned

During this project, I learned how to:

- Prepare custom datasets for object detection
- Convert Pascal VOC XML annotations into YOLO format
- Fine-tune pretrained YOLOv8 models
- Evaluate object detection models using Precision, Recall, and mAP
- Run inference on unseen images using a custom-trained model

---

## 🔮 Future Improvements

- Improve recall by collecting additional training data
- Experiment with larger YOLOv8 models (YOLOv8s/YOLOv8m)
- Deploy the model using Streamlit
- Extend the project for real-time workplace safety monitoring

---

## 📜 License

This project is intended for educational and portfolio purposes.
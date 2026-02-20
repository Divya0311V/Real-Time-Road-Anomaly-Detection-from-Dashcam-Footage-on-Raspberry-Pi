# Real-Time Road Anomaly Detection from Dashcam Footage on Raspberry Pi

## Project Overview

Road anomalies such as potholes, cracks, and unexpected obstacles:

- Cause accidents and safety risks  
- Lead to vehicle damage and maintenance costs  
- Are difficult to monitor using manual inspection  
- Lack real-time detection systems in many regions  

This project presents a low-cost Edge AI system that detects road anomalies in real time using a Raspberry Pi and dashcam footage. The system runs entirely offline and performs real-time inference on CPU without requiring cloud connectivity.

---

## Problem Statement

Road anomalies such as potholes, cracks, and unexpected obstacles:

- Cause accidents and safety risks  
- Lead to vehicle damage and maintenance costs  
- Are difficult to monitor using manual inspection  
- Lack real-time detection systems in most regions  

---

## Project Objective

Design and implement a real-time Edge AI application on Raspberry Pi that:

- Captures live dashcam footage  
- Detects potholes and road obstacles using a lightweight AI model  
- Logs anomalies with timestamp and saved frame evidence  
- Runs entirely on Raspberry Pi CPU (No GPU / No accelerator)  
- Works fully offline for scalable deployment  

---

## Why Edge AI Instead of Cloud-Based Detection

| Cloud-Based AI | Edge AI (Proposed System) |
|---------------|---------------------------|
| Requires Internet | Works Offline |
| High Latency | Real-Time Detection |
| Privacy Concerns | Local Processing |
| Expensive Infrastructure | Low-Cost Deployment |
| Limited in Rural Areas | Easily Deployable Anywhere |

### Advantages of Edge AI

- Immediate detection without network delay  
- Suitable for moving vehicles  
- Reduced bandwidth usage  
- Reliable even in remote locations  
- Enables scalable deployment at low cost  

---

## System Architecture

### Step-by-Step Workflow

1. Camera captures live road video  
2. OpenCV reads frames from the video stream  
3. Frames are preprocessed (resize, normalize)  
4. Optimized AI model performs inference  
5. Detected anomalies are identified  
6. System logs timestamp and saves detection frame  
7. Output can be used for alerts or further analysis  

---

## Hardware Components

- Raspberry Pi 4 / Raspberry Pi 5  
  Main processing unit running AI inference  

- Raspberry Pi Camera Module v2 / USB Webcam  
  Captures real-time dashcam footage  

- High-Speed microSD Card  
  Stores OS, AI model, and detection logs  

- Power Supply and Mounting Setup  
  Enables deployment in vehicle-like environments  

---

## Software Stack

- Raspberry Pi OS  
- Python  
- OpenCV  
- TensorFlow Lite / ONNX Runtime  
- Quantized Lightweight Object Detection Model  

---

## Model Optimization Techniques

To achieve near real-time performance on ARM CPU:

- INT8 Quantization to reduce computation  
- Reduced input image size (e.g., 320 × 320)  
- Frame skipping for speed improvement  
- Efficient OpenCV preprocessing  

---

## Performance Targets

| Metric | Target |
|--------|--------|
| Speed | ≥ 5 FPS |
| Latency | < 200 ms |
| Mode | Fully Offline |
| Accuracy | High Precision |

---

## System Output

The system generates:

- Bounding boxes around detected potholes or obstacles  
- Timestamp logs  
- Saved detection images  
- Structured data for road condition monitoring  

---

## Learning Outcomes

- Edge AI deployment on constrained hardware  
- Embedded computer vision pipeline design  
- Model optimization on ARM CPU  
- Understanding real-world AI deployment constraints  

---

## Team

Team GENERATIONE  
Department of Electronics and Communication Engineering  

- Athina K A  
- Divyadharshini V  
- Adhirashree  

Event: Bharat AI-SOC Student Challenge  

---

## Future Enhancements

- GPS integration for geo-tagging anomalies  
- Real-time alert system  
- Road condition analytics dashboard  
- Integration with smart city infrastructure  

# SkiSafe: Edge AI Rear-Detection System

SkiSafe is a wearable TinyML safety platform for ski helmets that detects approaching skiers from behind and is being engineered for reliable, low-latency microcontroller deployment.

**Lead Engineer:** Diego Anderson  
**Current hardware baseline:** Adafruit Feather M4 Express  
**Project status:** Phase II - Real-world robustness and generalization

---

## Executive Summary

Ski collisions are often caused by limited rear awareness in high-speed, high-noise environments. SkiSafe addresses this by combining on-device computer vision with embedded alerting logic so that hazard detection can happen locally, without cloud dependence.

From a portfolio perspective, this project demonstrates:

- End-to-end TinyML workflow design (dataset -> training -> evaluation -> deployment constraints)
- Safety-first metric selection and validation strategy
- Structured experiment tracking and model governance for iterative improvement

From a customer perspective, SkiSafe aims to deliver:

- Faster situational awareness for recreational and competitive skiers
- Low-latency edge inference appropriate for wearable operation
- A path toward practical helmet-integrated safety assistance

---

## Problem Statement and Objective

The objective is to build a robust, real-time human detector for rear-approach awareness on ski slopes.

**Primary performance target:** Human detection recall > 85% on held-out test data.

In this domain, missing a real skier (false negative) is the highest-risk failure mode, so recall is prioritized over precision.

$$
	ext{Recall} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}
$$

---

## System Architecture

```text
Rear-facing camera
		|
		v
Microcontroller platform (in evaluation)
	|- Option A: Adafruit ESP32-S3 Feather + OV5640 (160 deg wide angle)
	|- Option B: Arduino Nano Sense Rev2 + camera
	`- Option C: ESP32-WROVER-Camera V1.2
		|
		v
TinyML object detection model (Edge Impulse)
	`- Classes: Human / _background
		|
		v
Alert layer (haptics + ToF sensor fusion, in development)
```

---

## Technical Stack

- **Modeling:** FOMO (Faster Objects, More Objects), MobileNetV2, TensorFlow Lite
- **Toolchain:** Edge Impulse, Python data scripts, R-based analytics
- **Embedded context:** Feather-class Cortex-M4 / ESP32-class targets, ToF sensors, haptic motor

---

## Model Configuration

| Property                  | Value                      |
| ------------------------- | -------------------------- |
| Framework                 | Edge Impulse               |
| Task                      | Object Detection           |
| Classes                   | `_background`, `Human`     |
| Deployment target         | int8 quantized TinyML      |
| Primary evaluation metric | Human recall on test split |

---

## Experimental Baseline (March 2026)

| Split      | Metric    | int8  | float32 |
| ---------- | --------- | ----- | ------- |
| Test       | Recall    | 47.0% | 50.3%   |
| Test       | Precision | 62.5% | 63.1%   |
| Test       | F1        | 53.7% | 56.0%   |
| Validation | Recall    | 77.7% | 81.0%   |
| Validation | Precision | 62.7% | 62.1%   |
| Validation | F1        | 69.4% | 70.3%   |

**Interpretation:** The validation-to-test recall gap indicates weak generalization and probable overfitting. Current evidence points to annotation quality issues and class imbalance as primary contributors.

---

## Dataset Profile

| Split          | Count         |
| -------------- | ------------- |
| Training       | ~1,786 images |
| Test           | ~433 images   |
| Labeling queue | ~131 images   |
| Total          | ~2,350 images |

### Known Data Risks

- Class imbalance: ~1,760 human vs ~459 background images (about 4:1)
- Annotation quality: estimated 30-40% of boxes require correction
- Domain shift: part of the data is not from true rear-helmet viewpoint

### Data Sources

- Places365 (negative/background scenes)
- GeoPose3K (negative/background mountain scenes)
- Ski competition photography (human-positive samples)

---

## Validation Philosophy

For a binary detector in this safety scenario:

- **TN:** background correctly predicted as background
- **FP:** background incorrectly predicted as human
- **FN:** human incorrectly predicted as background (highest operational risk)
- **TP:** human correctly predicted as human

Model development is optimized for deployment reality: training is often float32, while on-device execution targets int8 quantization for memory and latency constraints.

---

## Product and Research Roadmap

### Data and Model Quality

- [ ] Complete full label audit of training data
- [ ] Add ~700 additional negative/background images
- [ ] Retrain after dataset cleanup
- [ ] Reach >85% human recall on test split

### Embedded Integration

- [ ] Finalize hardware target selection
- [ ] Deploy and benchmark model on-device
- [ ] Integrate haptic and ToF-assisted alert logic
- [ ] Complete physical helmet mounting and field evaluation

---

## Monitoring and Experiment Tracking

The dashboard tool supports structured model evaluation and run logging from Edge Impulse outputs.

Recommended workflow:

1. Open the dashboard HTML in a browser
2. Paste JSON from Edge Impulse Model Testing
3. Analyze recall/precision/F1 and confusion matrix outputs
4. Record run notes and embedded constraints (latency, RAM, flash)
5. Export a run row and append to `skisafe_runs.csv`

This creates an auditable experiment history suitable for both portfolio evidence and engineering decision-making.

---

## Repository Structure

- `data_scripts/` - Data calibration and conversion scripts
- `firmware/` - Embedded code and integration logic
- `model/` - Model artifacts and training metadata
- `json files/` / `json_files/` - Evaluation metrics and labels
- `Images_jpg/` - Raw image data
- `Skier_Images_jpg/` - Curated skier image subsets
- `Training_Data/` - Processed training images
- `Data_Negatives/` - Negative/background image sets

---

## For Collaborators and Customers

SkiSafe is currently an active R&D project with a clear path to production-readiness milestones. If you are interested in collaboration, pilot testing, or technical review, outreach is welcome.

---

## Contributing

1. Fork the repository
2. Clone your fork
3. Create a branch for your feature or fix
4. Submit a pull request with a concise technical summary

---

## License

MIT License

---

## Contact

For collaboration, technical review, or project inquiries, contact Diego Anderson.

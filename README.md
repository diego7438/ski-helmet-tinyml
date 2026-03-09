# SkiSafe: Edge AI Rear-Detection System

**Lead Engineer:** Diego Anderson  
**Hardware:** Adafruit Feather M4 Express  
**Status:** Phase II — Achieving Real-World Robustness

---

## Project Overview
SkiSafe is a wearable TinyML system for ski helmets, designed to detect approaching skiers from behind using a camera and Time-of-Flight (ToF) sensors. The project leverages advanced edge AI to deliver real-time detection and haptic feedback, ensuring safety on the slopes.

---

## Technical Highlights & Progress

### Phase II: Real-World Robustness (March 8, 2026)
- **Domain Adaptation & Edge Validation:** Evolved the model beyond ski-slope datasets for flawless performance in any environment.
- **Feature Bias Neutralization:** Diagnosed and eliminated feature bias, teaching the model to recognize a *person* rather than just *ski gear*.
- **Human Base Layer:** Integrated INRIA Person Dataset to fortify the model's understanding of human form.
- **Unified Person Classification:** Streamlined on-device logic for optimal firmware performance.
- **Performance Metrics:**
    - Validation F1 Score: **73.4%**
    - Recall: **84.3%**
    - Precision: **66%** (next target for improvement)
- **Edge Efficiency:** Model footprint confirmed at **~119KB RAM**, well within Cortex-M4 constraints.

### Phase I: Mission Accomplished (March 7, 2026)
- **Dataset Calibration:** Resolved coordinate system mismatches in EPFL Ski-2DPose dataset with a custom Python calibration script.
- **Architecture Choice:** Selected FOMO (MobileNetV2 variant) for memory efficiency.
- **Input Pipeline:** Engineered 96x96 grayscale input for RAM optimization.
- **Quantization:** Achieved `int8` quantization, reducing model size to **119.4KB**.
- **Validation & Proof of Concept:**
    - Test Set F1 Score: **73.3%** (no overfitting)
    - On-device inference: **718ms**
    - Successful live edge inference in novel environments.

---

## Tech Stack
- **AI:** FOMO (Faster Objects, More Objects), MobileNetV2, TensorFlow Lite
- **Tools:** Edge Impulse, Python (Data Calibration)
- **Hardware:** Cortex-M4 (Feather M4), ToF Sensors, Haptic Motor

---

## Strategic Direction
- **Precision Focus:** Next phase targets precision improvements to eliminate false positives and achieve pixel-perfect detection.
- **Firmware Integration:** Ongoing integration with haptic feedback and ToF sensor logic.

---

## Folder Structure
- `data_scripts/` — Data calibration and conversion scripts
- `firmware/` — Embedded code for Feather M4
- `model/` — Model files and training artifacts
- `json files/` — Evaluation metrics and labels
- `Images_jpg/` — Raw image data
- `Training_Data/` — Processed training images

---

## How to Contribute
1. Fork the repository
2. Clone your fork
3. Create a new branch for your feature or fix
4. Submit a pull request with a clear description

---

## License
MIT License

---

## Contact
For questions or collaboration, contact Diego Anderson.
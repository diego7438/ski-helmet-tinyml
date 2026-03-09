# SkiSafe: Edge AI Rear-Detection System

**Lead Engineer:** Diego Anderson  
**Hardware:** Adafruit Feather M4 Express  
**Status:** Phase II — Achieving Real-World Robustness

---

## Project Overview
SkiSafe is a wearable TinyML system for ski helmets, designed to detect approaching skiers from behind using a camera and Time-of-Flight (ToF) sensors. The project leverages advanced edge AI to deliver real-time detection and haptic feedback, ensuring safety on the slopes.

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
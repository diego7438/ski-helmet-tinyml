# SkiSafe: Edge AI Rear-Detection System
**Developer:** Diego Anderson
**Hardware:** Adafruit Feather M4 Express
**Status:** Phase II (Model Optimization)

## Project Overview
A wearable TinyML system designed for ski helmets to detect approaching skiers from behind using a camera and Time-of-Flight (ToF) sensors.

## Tech Stack
- **AI:** FOMO (Faster Objects, More Objects) trained on EPFL Ski-2DPose dataset.
- **Tools:** Edge Impulse, Python (Data Calibration), TensorFlow Lite.
- **Hardware:** Cortex-M4 (Feather M4), ToF Sensors, Haptic Motor.

## Latest Progress (3/7/26)
- Successfully normalized 1,982 training images using custom Python scripts.
- Optimized model to fit in **119KB RAM** (62% device capacity).
- Achieved **84.3% Recall** in validation testing.
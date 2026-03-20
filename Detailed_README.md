# ⛷️ SkiSafe — TinyML Human Detection System

> An on-helmet machine learning system that detects skiers approaching from behind, built on Edge Impulse and designed for deployment on microcontrollers.

---

## 🎯 Project Goal

SkiSafe is a real-time human detection system designed to run on a microcontroller mounted to a ski helmet. A rear-facing camera watches for incoming skiers and triggers an alert — helping prevent collisions on the slope.

**Current model target:** Push Human Detection **Recall above 85%** on test data.

---

## 🏗️ System Architecture

```
Rear-facing camera
        │
        ▼
Microcontroller (TBD)
  ├── Option A: Adafruit ESP32-S3 Feather + OV5640 Camera (160° wide angle)
  ├── Option B: Arduino Nano Sense Rev2 + camera
  └── Option C: ESP32-WROVER-Camera V1.2
        │
        ▼
TinyML Object Detection Model (Edge Impulse)
  └── Detects: Human / _background
        │
        ▼
Alert system (in development)
```

---

## 📁 Repository Structure

```
ski-helmet-tinyml/
├── README.md                    ← You are here
├── skisafe_dashboard_v2.html    ← Model performance dashboard
├── skisafe_runs.csv             ← Master run log (append each retrain)
└── r_scripts/
    └── visualize_progress.R     ← R visualization script
```

---

## 🧠 Model Overview

| Property              | Value                          |
| --------------------- | ------------------------------ |
| **Framework**         | Edge Impulse                   |
| **Task**              | Object Detection               |
| **Classes**           | `_background`, `Human`         |
| **Deployment target** | int8 quantized (TinyML)        |
| **Key metric**        | Recall (Human class, test set) |

### Why Recall over Precision?

In this application, a **False Negative** (missing a real skier) is far more dangerous than a **False Positive** (alerting when no one is there). Recall measures how many real humans the model catches — making it the primary metric we optimize for.

```
Recall = True Positives / (True Positives + False Negatives)
```

---

## 📊 Model Performance Log

All training runs are tracked in `skisafe_runs.csv`. See the [Dashboard](#-dashboard--run-logger) section for how to log new runs.

### Current Baseline (as of March 2026)

| Split          | Metric    | int8  | float32 |
| -------------- | --------- | ----- | ------- |
| **Test**       | Recall    | 47.0% | 50.3%   |
| **Test**       | Precision | 62.5% | 63.1%   |
| **Test**       | F1        | 53.7% | 56.0%   |
| **Validation** | Recall    | 77.7% | 81.0%   |
| **Validation** | Precision | 62.7% | 62.1%   |
| **Validation** | F1        | 69.4% | 70.3%   |

> ⚠️ The gap between validation recall (77.7%) and test recall (47.0%) indicates overfitting — the model is not generalizing well to new data. Root cause: mislabeled training data and dataset imbalance.

---

## 🗂️ Dataset

| Split          | Count         |
| -------------- | ------------- |
| Training       | ~1,786 images |
| Test           | ~433 images   |
| Labeling queue | ~131 images   |
| **Total**      | ~2,350 images |

### Known Issues (being fixed)

- **Dataset imbalance:** ~1,760 Human images vs ~459 background — roughly 4:1 ratio
- **Mislabeled bounding boxes:** Estimated 30–40% of training labels were imprecise or incorrectly placed (bounding boxes over snow instead of humans)
- **Data source mismatch:** Images sourced from online datasets (Places365, GeoPose3K, competition ski photography) — not from a rear-facing helmet camera perspective

### Data Sources

- [Places365](https://www.kaggle.com/datasets/benjaminkz/places365) — scene backgrounds (negatives)
- [GeoPose3K](https://cphoto.fit.vutbr.cz/geoPose3K/) — mountain landscape images (negatives)
- Ski competition photography — human positive samples

### Improvement Plan

- [ ] Full label audit of all ~1,786 training images (fix or delete bad bounding boxes)
- [ ] Add ~700 additional negative (background) samples to balance dataset
- [ ] Retrain once after all fixes are complete
- [ ] Target: Test Recall > 85%

---

## 🖥️ Dashboard & Run Logger

`skisafe_dashboard_v2.html` is a standalone browser tool for analyzing Edge Impulse results and logging training runs.

### How to use

1. Open `skisafe_dashboard_v2.html` in any browser (double-click on Mac)
2. Paste your Edge Impulse JSON from the **Model Testing** tab
3. Click **Analyze Results** to see metrics visualized
4. Fill in run details (run type, notes, on-device performance)
5. Click **Export CSV Row** to download a row for your run log

### What it shows

- Recall, Precision, F1 with color-coded goal tracking
- Confusion matrix (True Positives, False Negatives, etc.)
- int8 vs float32 side-by-side comparison
- Progress toward the 85% recall goal

### Getting the JSON from Edge Impulse

In your Edge Impulse project, go to **Model Testing → Classify All** and copy the raw JSON output.

---

## 📈 Tracking Progress Over Time

Every training run is logged to `skisafe_runs.csv`. Each row represents one retrain or test event.

### CSV Schema

| Column                | Source   | Description              |
| --------------------- | -------- | ------------------------ |
| `date`                | Auto     | Date of run (YYYY-MM-DD) |
| `time`                | Auto     | Time of run              |
| `run_type`            | Dropdown | Type of action taken     |
| `notes`               | Manual   | What changed this run    |
| `test_recall_int8`    | JSON     | 🔴 Most important metric |
| `test_precision_int8` | JSON     |                          |
| `test_f1_int8`        | JSON     |                          |
| `val_recall_int8`     | JSON     |                          |
| `val_precision_int8`  | JSON     |                          |
| `val_f1_int8`         | JSON     |                          |
| `test_recall_f32`     | JSON     |                          |
| `test_precision_f32`  | JSON     |                          |
| `test_f1_f32`         | JSON     |                          |
| `test_cm_tn`          | JSON     | True Negatives           |
| `test_cm_fp`          | JSON     | False Positives          |
| `test_cm_fn`          | JSON     | False Negatives ⚠️       |
| `test_cm_tp`          | JSON     | True Positives ✅        |
| `inferencing_ms`      | Manual   | On-device speed (ms)     |
| `peak_ram_kb`         | Manual   | Peak RAM usage (KB)      |
| `flash_kb`            | Manual   | Flash usage (KB)         |

### Appending a new run in R

Each export from the dashboard creates a single-row CSV. Append it to the master file like this:

```r
library(tidyverse)

# Read the new run you just exported
new_run <- read_csv("~/Downloads/skisafe_run_2026-03-20.csv")

# Read the master log
master <- read_csv("~/Ski-Safe-TinyML/skisafe_runs.csv")

# Stack them together (bind_rows adds new row to the bottom)
master <- bind_rows(master, new_run)

# Save back to master
write_csv(master, "~/Ski-Safe-TinyML/skisafe_runs.csv")
```

> 💡 **First time only:** Rename your first exported CSV to `skisafe_runs.csv` — that becomes your master file. Append every run after that.

---

## 📊 R Visualization

`r_scripts/visualize_progress.R` generates three plots using `patchwork`:

```r
library(tidyverse)
library(ggplot2)
library(patchwork)

runs <- read_csv("skisafe_runs.csv")
runs$date <- as.Date(runs$date)
runs$run_number <- seq_len(nrow(runs))

# Plot 1: Recall over time with goal line
p1 <- ggplot(runs, aes(x=run_number, y=test_recall_int8)) +
  geom_line(color="#00d4ff", linewidth=1.2) +
  geom_point(color="#00d4ff", size=3) +
  geom_hline(yintercept=0.85, linetype="dashed", color="#e63946", linewidth=0.8) +
  annotate("text", x=1, y=0.86, label="Goal: 85%", color="#e63946", size=3, hjust=0) +
  geom_text(aes(label=run_type), vjust=-1.2, size=2.5, color="#7a9bb5") +
  scale_y_continuous(limits=c(0,1), labels=scales::percent) +
  labs(title="Test Recall (int8) Over Time", x="Run #", y="Recall")

# Plot 2: Precision vs Recall tradeoff
p2 <- ggplot(runs, aes(x=test_precision_int8, y=test_recall_int8, color=run_number)) +
  geom_point(size=4) +
  geom_path(linewidth=0.8) +
  geom_hline(yintercept=0.85, linetype="dashed", color="#e63946") +
  scale_color_gradient(low="#112240", high="#00d4ff") +
  scale_x_continuous(limits=c(0,1), labels=scales::percent) +
  scale_y_continuous(limits=c(0,1), labels=scales::percent) +
  labs(title="Precision vs Recall Tradeoff", x="Precision", y="Recall")

# Plot 3: F1 over time
p3 <- ggplot(runs, aes(x=run_number, y=test_f1_int8)) +
  geom_line(color="#52b788", linewidth=1.2) +
  geom_point(color="#52b788", size=3) +
  scale_y_continuous(limits=c(0,1), labels=scales::percent) +
  labs(title="F1 Score Over Time", x="Run #", y="F1")

# Combine with patchwork
(p1 / (p2 | p3)) +
  plot_annotation(title="SkiSafe Model Progress")
```

---

## 🔬 Key Concepts

### Confusion Matrix

For a binary classifier like this one:

|                        | Predicted: Background  | Predicted: Human       |
| ---------------------- | ---------------------- | ---------------------- |
| **Actual: Background** | True Negative (TN) ✅  | False Positive (FP) ⚠️ |
| **Actual: Human**      | False Negative (FN) 🔴 | True Positive (TP) ✅  |

- **False Negative (FN):** Model missed a real skier — the most dangerous failure mode for SkiSafe
- **False Positive (FP):** Model triggered when no one was there — annoying but safe

### int8 vs float32

Edge Impulse trains in float32 but quantizes to int8 for deployment on microcontrollers. int8 uses less RAM and runs faster but can lose some accuracy. We optimize for **int8** since that's what runs on-device.

### Experiment Tracking

Every retrain is logged as a row in `skisafe_runs.csv`. This is a lightweight version of tools like MLflow or Weights & Biases. The goal is to never lose track of what changed between runs and whether it helped.

---

## 🛣️ Roadmap

- [x] Build object detection model in Edge Impulse
- [x] Build performance dashboard (`skisafe_dashboard_v2.html`)
- [x] Implement CSV run logging + R visualization pipeline
- [ ] Complete full label audit of training set
- [ ] Add ~700 negative samples to balance dataset
- [ ] Retrain and hit >85% test recall
- [ ] Select final hardware (ESP32-S3 / Arduino Nano / ESP32-WROVER)
- [ ] Deploy model to microcontroller
- [ ] Build backend database for run logging (replacing CSV export)
- [ ] Physical helmet mount + alert system

---

## 🤝 Contributing

This is an active student research project. If you're working on TinyML, edge computer vision, or ski safety tech — feel free to open an issue or reach out.

---

## 📄 License

MIT License — free to use, modify, and build on.

---

_Built with Edge Impulse, R, and a lot of ski slope data. ⛷️_

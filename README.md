
# 🔐 Student Clustering Prediction App

A simple web application built with **Gradio** that predicts the student cluster/class based on 5 input numerical features using a pre-trained machine learning pipeline.

---

## 🌟 Features
- Clean, modern UI with a moving background
- User authentication (login required)
- Predicts clusters using a saved scikit-learn pipeline
- Easy deployment on Hugging Face Spaces or locally

---

## 🚀 How to Run Locally

1. Clone the repo:
    ```bash
    git clone https://github.com/yourusername/student-clustering-app.git
    cd student-clustering-app
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the app:
    ```bash
    python app.py
    ```

4. Open your browser at:
    ```
    http://127.0.0.1:7860
    ```

---

## 🔧 Usage

- Login credentials:
    | Username | Password  |
    |----------|-----------|
    | admin    | hello     |
    | student  | pass123   |

- Input the following numeric features:
    - `STG` (Study Time Grade)
    - `SCG` (Score Grade)
    - `STR` (Stress Level)
    - `LPR` (Learning Performance Rate)
    - `PEG` (Personal Engagement Grade)

- Click **Predict** to see the cluster/class prediction.

---

## 📦 Project Structure

```
├── app.py                 # Main Gradio application
├── student_cluster.pkl    # Pre-trained pipeline
├── requirements.txt       # Python dependencies
├── README.md              # This file
```

---

## ⚡ Notes

- ⚠️ Make sure the `.pkl` model was saved using scikit-learn version 1.7.1 to avoid version mismatch warnings.
- 🎯 Compatible with Hugging Face Spaces: no need for additional configuration.

---

## 📄 Link: 
https://huggingface.co/spaces/RishiiithaV/student_intelligence_cluster

## output
<img width="1891" height="783" alt="Screenshot 2025-09-08 143429" src="https://github.com/user-attachments/assets/6de7d068-56e4-4234-832d-98e0217bd688" />

<img width="1907" height="481" alt="image" src="https://github.com/user-attachments/assets/855db677-fa7c-47d6-ae19-e7b9c0029ef4" />


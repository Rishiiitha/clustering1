import joblib
import numpy as np
import gradio as gr

pipeline = joblib.load("student_cluster.pkl")


def predict(*features):
    arr = np.array(features, dtype=float).reshape(1, -1) 
    pred = pipeline.predict(arr)[0]
    return f"Predicted Cluster/Class: {pred}"


raw_features = ["STG", "SCG", "STR", "LPR", "PEG"]

with gr.Blocks(css=".gradio-container {background-color: #f4f6f9; font-family: Arial;}") as demo:
    gr.HTML("<h1 style='color:navy;'>🔐 User Login + Student Clustering App</h1>")
    with gr.Row():
        inputs = [gr.Number(label=col) for col in raw_features] 
    output = gr.Textbox(label="Result")
    btn = gr.Button("Predict")
    btn.click(fn=predict, inputs=inputs, outputs=output)

demo.launch(auth=[("admin", "hello"), ("student", "pass123")])


# WineSage – A wise predictor of wine quality 🍷

This repository contains a **Wine Quality Prediction** application built using **Streamlit** and a pre-trained machine learning model saved as `wine_model.pkl`. The app predicts wine quality based on physicochemical properties provided by the user.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

Wine quality is significantly influenced by its chemical composition. This project employs a machine learning model to predict the quality of wine using features like **citric acid content**, **residual sugar**, and **sulfur dioxide levels**. The intuitive **Streamlit web application** allows users to input these properties and instantly receive predictions.

---

## Features

- **User-Friendly Interface:**  
  Enter chemical properties (e.g., citric acid, chlorides) via interactive input fields on the Streamlit app.

- **Integrated Machine Learning Model:**  
  A pre-trained model (`wine_model.pkl`) predicts wine quality based on the input features.

- **File Uploader (Future Implementation):**  
  Placeholder functionality to upload files for batch predictions.

---

## Requirements

Before running the project, ensure you have the following:

- **Python:** Version 3.7 or later.
- **Libraries:** Install these Python libraries:
  - Streamlit
  - NumPy
  - Scikit-learn (for model training)
  - Pickle (standard library for loading the model)


# Usage

1. Launch the app in your browser (usually at `http://localhost:8501`).
2. Input the following wine properties:
    - Citric Acid
    - Residual Sugar
    - Chlorides
    - Free Sulfur Dioxide
    - Total Sulfur Dioxide
3. Click **Submit** to view the predicted wine quality.

# Code Explanation

## Key Components

### Model Loading:
The pickle module is used to load the pre-trained machine learning model:

```python
model = pickle.load(open("wine_model.pkl", "rb"))
```

### Prediction Function:
A helper function processes input features and generates predictions:

```python
def predict(citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide):  
    y_pred = model.predict([[citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide]])
    return y_pred
```

### Streamlit Application:

Users provide input through text fields.  
Clicking **Submit** triggers the prediction function, displaying results dynamically:

```python
if st.button("Submit"):  
    y_prediction = predict(
        eval(citric_acid), eval(residual_sugar), eval(chlorides), eval(free_sulfur_dioxide), eval(total_sulfur_dioxide)
    )  
    st.success(f"Predicted Quality: {y_prediction}")
```

### File Uploader (Placeholder):
Placeholder widget for batch processing:

```python
data = st.file_uploader("Upload file")  
```

# Technologies Used

- **Programming Language:** Python
- **Libraries:**
    - **Streamlit:** For building the web interface.
    - **Pickle:** To load the pre-trained model.
    - **NumPy & Scikit-learn:** For data processing and model development.


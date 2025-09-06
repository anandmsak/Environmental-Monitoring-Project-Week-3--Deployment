# Environmental Monitoring & Pollution Control using AI/ML

This project is the final submission for the AICTE internship, focusing on predicting air pollution levels using machine learning. The primary goal is to predict Benzene (C6H6) concentration based on data from other air quality sensors and deploy the model as an interactive web application.

## 🚀 Live Demo

Here is a screenshot of the final deployed web application running locally.



## ✨ Features

* **Data Cleaning:** The raw UCI Air Quality dataset was processed to handle missing values and inconsistencies.
* **Model Comparison:** Three regression models (Linear Regression, Random Forest, Gradient Boosting) were trained and evaluated.
* **High-Accuracy Prediction:** The final Random Forest model achieved an R² score of 0.998, demonstrating exceptional accuracy.
* **Insightful Analysis:** Feature importance analysis revealed potential data leakage, a critical insight for real-world model deployment.
* **Web Deployment:** The trained model is deployed using a Flask web server, providing a user-friendly interface for live predictions.

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Machine Learning:** Scikit-learn, Pandas, NumPy
* **Data Handling:** Joblib

## 📂 Project Structure

.
├── app.py              # Main Flask application
├── models/
│   └── rf_model.pkl    # Saved Random Forest model
├── templates/
│   └── index.html      # HTML for the web UI
└── requirements.txt    # Python dependencies


## ⚙️ Setup and Installation

To run this project locally, please follow these steps:

**1. Clone the repository:**
```bash
git clone <your-repository-url>
cd <repository-name>
2. Create and activate a virtual environment:

Bash

# Create the environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate
3. Install the required dependencies:

Bash

pip install -r requirements.txt
4. Run the Flask application:

Bash

python app.py
Open your web browser and navigate to http://127.0.0.1:5000 to see the application live.

📈 Key Findings & Results
The project successfully demonstrated the ability to predict Benzene concentration with high accuracy.

The Random Forest and Gradient Boosting models were the top performers, both achieving an R² of 0.998.

A key finding from the feature importance analysis was that the model's performance was overwhelmingly dependent on a single feature (PT08.S2(NMHC)). This suggests a strong case of data leakage, where one sensor's data is a direct proxy for the target variable, which is a crucial consideration for practical use.

👤 Meta
Anandha Krishnan P(Intern)

AICTE Internship Program

September 2025
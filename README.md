**Product Sales Forecasting Using Machine Learning**
📌Project Overview

Accurate sales forecasting is crucial for inventory planning, demand management, and business decision-making.
This project focuses on forecasting product sales using historical transactional data by combining EDA, hypothesis testing, machine learning modeling, Tableau dashboards, and model deployment.

🎯 **Problem Statement**

To predict future sales by identifying key factors influencing sales such as:

Store type

Location and region

Discounts

Holidays

Order volume

Time-based trends

📊 **Dataset Description**

The dataset contains transactional sales data with the following features:

Store\_id

Store\_Type

Location\_Type

Region\_Code

Date

Holiday

Discount

Number of Orders

Sales

🔍 **Exploratory Data Analysis (EDA)**

EDA was conducted to understand sales patterns and drivers:

Sales distribution and trends over time

Impact of discounts and holidays

Regional and store-type performance

Relationship between number of orders and sales

🧪 **Hypothesis Testing**

Statistical tests were performed to validate business assumptions:

Discounts significantly impact sales

Holidays influence sales behavior

Sales vary across store types and regions

⚙️ **Feature Engineering**

The following features were engineered:

Time-based features: Year, Month, Day, Weekday, Week

Store-level statistical features:

Mean sales

Median sales

Sales standard deviation

7-day rolling average

Categorical variables were label encoded.

🤖\*\* Machine Learning Model\*\*

Model Used: LightGBM Regressor

Reason: Handles non-linear relationships efficiently and performs well on tabular data

Evaluation Metrics:

Mean Absolute Error (MAE)

Root Mean Squared Error (RMSE)

The model demonstrated strong predictive performance.

📈 **Tableau Dashboards**

Interactive dashboards were created using Tableau to visualize:

Sales over time

Region-wise sales performance

Discount impact on sales

Holiday vs non-holiday sales

Orders vs sales relationship

🔗 **Tableau Public Link:**
https://public.tableau.com/views/ProductSalesForecasting\_17861952617980/Dashboard?:language=en-US\&:sid=\&:redirect=auth\&:display\_count=n\&:origin=viz\_share\_link

🚀 **Deployment**

The trained model was deployed using a Flask REST API.

\*\*Features:

/predict endpoint

Accepts JSON input

Returns predicted sales

Handles preprocessing and feature alignment

A web-based UI was also created to allow users to input data and view predictions visually.\*\*

🧪 How to Run the Project

# Navigate to deployment folder

cd deployment

# Install dependencies

pip install -r requirements.txt

# Run the Flask app

python app.py

Product Sales Forecasting Using Machine Learning
📌 Project Overview

Accurate sales forecasting is crucial for inventory planning, demand management, and business decision-making.
This project focuses on forecasting product sales using historical transactional data by combining EDA, hypothesis testing, machine learning modeling, Tableau dashboards, and model deployment.

🎯 Problem Statement

To predict future sales by identifying key factors influencing sales such as:

Store type

Location and region

Discounts

Holidays

Order volume

Time-based trends

📊 Dataset Description

The dataset contains transactional sales data with the following features:

Store\_id

Store\_Type

Location\_Type

Region\_Code

Date

Holiday

Discount

Number of Orders

Sales

🔍 Exploratory Data Analysis (EDA)

EDA was conducted to understand sales patterns and drivers:

Sales distribution and trends over time

Impact of discounts and holidays

Regional and store-type performance

Relationship between number of orders and sales

🧪 Hypothesis Testing

Statistical tests were performed to validate business assumptions:

Discounts significantly impact sales

Holidays influence sales behavior

Sales vary across store types and regions

⚙️ Feature Engineering

The following features were engineered:

Time-based features: Year, Month, Day, Weekday, Week

Store-level statistical features:

Mean sales

Median sales

Sales standard deviation

7-day rolling average

Categorical variables were label encoded.

🤖 Machine Learning Model

Model Used: LightGBM Regressor

Reason: Handles non-linear relationships efficiently and performs well on tabular data

Evaluation Metrics:

Mean Absolute Error (MAE)

Root Mean Squared Error (RMSE)

The model demonstrated strong predictive performance.

📈 Tableau Dashboards

Interactive dashboards were created using Tableau to visualize:

Sales over time

Region-wise sales performance

Discount impact on sales

Holiday vs non-holiday sales

Orders vs sales relationship

🔗 Tableau Public Link:
https://public.tableau.com/views/ProductSalesForecasting\_17861952617980/Dashboard?:language=en-US\&:sid=\&:redirect=auth\&:display\_count=n\&:origin=viz\_share\_link

🚀 Deployment

The trained model was deployed using a Flask REST API.

Features:

/predict endpoint

Accepts JSON input

Returns predicted sales

Handles preprocessing and feature alignment

A web-based UI was also created to allow users to input data and view predictions visually.

🧪 How to Run the Project

# Navigate to deployment folder

cd deployment

# Install dependencies

pip install -r requirements.txt

# Run the Flask app

python app.py



📌 Project Highlights

End-to-end data science pipeline

Business-driven insights

Interactive dashboards

Real-time prediction system

🔮 **Future Enhancements**

Advanced time-series models (Prophet, LSTM)

Cloud deployment

Automated data ingestion

Enhanced UI


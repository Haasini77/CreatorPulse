# CreatorPulse 📊
### Social Media Content Intelligence & Engagement Prediction

CreatorPulse is a data analytics and machine learning project that analyzes social media content performance and predicts engagement rates. It uses Python, SQL, Machine Learning, and Power BI to identify engagement patterns across platforms, content types, topics, and posting times.

## 🎯 Project Objectives

- Analyze social media engagement patterns.
- Compare engagement across different platforms and content types.
- Identify topics and posting hours associated with higher engagement.
- Predict engagement rates using a Machine Learning model.
- Visualize insights through an interactive Power BI dashboard.

## ✨ Features

- **Data Generation:** Creates a synthetic dataset of 1,000 social media posts.
- **Database Management:** Stores and analyzes data using SQLite.
- **Exploratory Data Analysis:** Examines platform, topic, content type, posting hour, and hashtag count.
- **Engagement Prediction:** Uses Random Forest Regression to predict engagement rates.
- **Model Evaluation:** Evaluates predictions using MAE and R² score.
- **Power BI Dashboard:** Presents engagement trends and model insights visually.

## 🛠️ Tech Stack

- **Programming:** Python
- **Data Analysis:** Pandas
- **Database:** SQLite
- **Machine Learning:** Scikit-learn, Random Forest Regression
- **Visualization:** Microsoft Power BI
- **Data Storage:** CSV

## 📂 Project Structure

```text
CreatorPulse/
├── data/
│   ├── social_media_data.csv
│   ├── creatorpulse.db
│   └── predictions.csv
├── src/
│   ├── generate_data.py
│   ├── database.py
│   ├── analyze_data.py
│   └── predict_model.py
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Haasini77/CreatorPulse.git
cd CreatorPulse
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Generate the dataset

```bash
python src/generate_data.py
```

### 4. Create and populate the database

```bash
python src/database.py
```

### 5. Analyze the data

```bash
python src/analyze_data.py
```

### 6. Train the prediction model

```bash
python src/predict_model.py
```

The generated predictions are saved to `data/predictions.csv`.

> Run the scripts in the order shown above. The commands assume your scripts use these paths and that the required Python packages are listed in `requirements.txt`.

## 📈 Model Performance

The Random Forest Regression model produced the following results in the recorded run:

| Metric | Result |
|---|---:|
| Mean Absolute Error (MAE) | 0.62 |
| R² Score | 0.93 |

- **MAE:** Measures the average absolute difference between actual and predicted engagement values. Lower is generally better.
- **R² Score:** Measures how well the model explains variation in the target values. A score closer to 1 generally indicates a better fit.

These results are from the generated dataset and should not be interpreted as proven performance on real-world social media data.

## 📊 Power BI Dashboard

The Power BI dashboard explores:
- Engagement by social media platform.
- Engagement by content type and topic.
- Posting-hour and hashtag-count patterns.
- Actual versus predicted engagement.
- Overall engagement KPIs.

Open the Power BI report locally if you have the report file. Add dashboard screenshots here when available.

## 📁 Dataset

This project uses a **synthetic dataset of 1,000 social media posts**, generated using Python for educational and analytical purposes. It is not collected from real social media accounts or platforms.

The dataset includes fields such as platform, content type, topic, posting hour, followers, views, likes, comments, shares, saves, and hashtag count.

## 🚀 Future Improvements

- Evaluate the model on real-world, appropriately licensed social media data.
- Compare multiple machine learning algorithms.
- Improve validation using cross-validation and a separate test dataset.
- Develop an interactive web application for engagement prediction.
- Add more visual insights and dashboard filters.

## 👩‍💻 Author

**Haasini Obilisetty**

B.Tech — Artificial Intelligence & Data Science

GitHub: [Haasini77](https://github.com/Haasini77)

---

⭐ If you find this project interesting, consider starring the repository!

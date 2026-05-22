# 🎬 Netflix Data Cleaning & Visualization Dashboard
## 🌐 Live Dashboard

[Click here to view the live Streamlit dashboard](https://thiranex-netflix-dashboard.streamlit.app/)

## 📌 Thiranex Internship Task 1

This project is developed as part of the Thiranex Internship Task 1.  
The objective of this project is to clean, analyze, and visualize a real-world dataset using Python and build an interactive dashboard using Streamlit.

---

## 📊 Project Overview

This project uses the Netflix Movies and TV Shows dataset to perform:

- Data cleaning
- Missing value handling
- Duplicate removal
- Feature extraction
- Exploratory data analysis
- Interactive data visualization

The final output is a professional Streamlit dashboard that displays insights from the cleaned Netflix dataset.

---

## 🛠️ Technologies Used

- Python
- Pandas
- Plotly
- Streamlit
- GitHub
- GitHub Codespaces

---

## 🧹 Data Cleaning Steps

The following cleaning operations were performed:

1. Removed duplicate records
2. Filled missing values in:
   - Director
   - Cast
   - Country
   - Rating
   - Duration
3. Converted `date_added` into datetime format
4. Extracted `year_added` from the date column
5. Extracted numeric values from duration
6. Prepared the dataset for visualization

---

## 📈 Dashboard Features

The Streamlit dashboard includes:

- Total number of Netflix titles
- Movie count
- TV show count
- Number of countries
- Movies vs TV Shows distribution
- Top 10 content-producing countries
- Netflix content added over the years
- Content rating distribution
- Top 10 Netflix genres
- Cleaned dataset preview
- Sidebar filters for content type and rating

---

## 📁 Project Structure

```text
thiranex-data-cleaning
├── data
│   └── netflix_titles.csv
├── app.py
├── requirements.txt
└── README.md

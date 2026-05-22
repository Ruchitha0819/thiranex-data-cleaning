import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Netflix Data Cleaning & Visualization",
    page_icon="🎬",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv("data/netflix_titles.csv")

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df["director"] = df["director"].fillna("Unknown Director")
    df["cast"] = df["cast"].fillna("Unknown Cast")
    df["country"] = df["country"].fillna("Unknown Country")

    if df["rating"].mode().empty:
        df["rating"] = df["rating"].fillna("Unknown Rating")
    else:
        df["rating"] = df["rating"].fillna(df["rating"].mode()[0])

    df["duration"] = df["duration"].fillna("Unknown")

    # Convert date column
    df["date_added"] = pd.to_datetime(df["date_added"].astype(str).str.strip(), errors="coerce")
    df["year_added"] = df["date_added"].dt.year

    # Extract numeric duration
    df["duration_num"] = df["duration"].astype(str).str.extract(r"(\d+)").astype(float)

    return df


df = load_data()

st.title("🎬 Netflix Data Cleaning & Visualization Dashboard")
st.caption("Thiranex Internship Task 1 | Python + Pandas + Plotly + Streamlit")

st.divider()

# KPI cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Titles", f"{len(df):,}")
col2.metric("Movies", f"{len(df[df['type'] == 'Movie']):,}")
col3.metric("TV Shows", f"{len(df[df['type'] == 'TV Show']):,}")
col4.metric("Countries", f"{df['country'].str.split(',').explode().str.strip().nunique():,}")

st.divider()

# Sidebar filters
st.sidebar.header("🔍 Filter Data")

content_type = st.sidebar.multiselect(
    "Select Content Type",
    options=df["type"].dropna().unique(),
    default=df["type"].dropna().unique()
)

ratings = st.sidebar.multiselect(
    "Select Rating",
    options=df["rating"].dropna().unique(),
    default=df["rating"].dropna().unique()
)

filtered_df = df[
    (df["type"].isin(content_type)) &
    (df["rating"].isin(ratings))
]

st.subheader("📊 Visual Insights")

col_a, col_b = st.columns(2)

with col_a:
    type_count = filtered_df["type"].value_counts().reset_index()
    type_count.columns = ["Type", "Count"]

    fig1 = px.pie(
        type_count,
        names="Type",
        values="Count",
        title="Movies vs TV Shows Distribution",
        hole=0.4
    )
    st.plotly_chart(fig1, use_container_width=True)

with col_b:
    top_countries = (
        filtered_df["country"]
        .str.split(",")
        .explode()
        .str.strip()
        .value_counts()
        .head(10)
        .reset_index()
    )
    top_countries.columns = ["Country", "Count"]

    fig2 = px.bar(
        top_countries,
        x="Count",
        y="Country",
        orientation="h",
        title="Top 10 Content-Producing Countries"
    )
    fig2.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig2, use_container_width=True)

yearly = (
    filtered_df.dropna(subset=["year_added"])
    .groupby(["year_added", "type"])
    .size()
    .reset_index(name="Count")
)

fig3 = px.line(
    yearly,
    x="year_added",
    y="Count",
    color="type",
    markers=True,
    title="Netflix Content Added Over Years"
)
st.plotly_chart(fig3, use_container_width=True)

col_c, col_d = st.columns(2)

with col_c:
    rating_count = filtered_df["rating"].value_counts().reset_index()
    rating_count.columns = ["Rating", "Count"]

    fig4 = px.bar(
        rating_count,
        x="Rating",
        y="Count",
        title="Content Rating Distribution"
    )
    st.plotly_chart(fig4, use_container_width=True)

with col_d:
    genres = (
        filtered_df["listed_in"]
        .str.split(",")
        .explode()
        .str.strip()
        .value_counts()
        .head(10)
        .reset_index()
    )
    genres.columns = ["Genre", "Count"]

    fig5 = px.bar(
        genres,
        x="Count",
        y="Genre",
        orientation="h",
        title="Top 10 Netflix Genres"
    )
    fig5.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig5, use_container_width=True)

st.divider()

st.subheader("🧹 Data Cleaning Summary")

st.write("""
This project performs data cleaning and visualization on the Netflix Movies and TV Shows dataset.

Cleaning steps performed:
- Removed duplicate records
- Filled missing values in director, cast, country, rating, and duration columns
- Converted date_added column into datetime format
- Extracted year_added from date_added
- Extracted numeric duration values
""")

st.subheader("📁 Cleaned Dataset Preview")
st.dataframe(filtered_df.head(50), use_container_width=True)
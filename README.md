# 🎬  Movie Recommendation System

An  Content-Based Movie Recommendation System built using Natural Language Processing (NLP), TF-IDF Vectorization, and Cosine Similarity.

This project recommends movies similar to the selected movie based on genres, movie tags, and semantic content analysis.

---

# 🚀 Features

* 🔍 Search movies by title
* 🎯 Select the correct movie from multiple matches
* 🤖 AI-based recommendation engine
* 🧠 NLP-powered semantic similarity
* ⭐ Displays movie ratings
* 🌐 Interactive web interface using Streamlit
* 📊 Processes 87K+ movies dataset

---

# 🧠 How the Recommendation System Works

The system uses a **Content-Based Recommendation Approach**.

## Workflow

1. User enters a movie name
2. System searches matching movie titles
3. User selects the correct movie
4. TF-IDF vectors are generated from:

   * Genres
   * Tags
5. Cosine Similarity compares the selected movie vector with all movie vectors
6. Top similar movies are returned

---

# 🏗️ Project Architecture

```text
User Input
    ↓
Movie Search
    ↓
Movie Selection
    ↓
TF-IDF Vector Retrieval
    ↓
Cosine Similarity Calculation
    ↓
Top Recommended Movies
```

---

# 📂 Project Structure

```text
Movie_system/
│
├── ml-32m/
│   ├── movies.csv
│   ├── ratings.csv
│   ├── tags.csv
│   └── links.csv
│
├── datasets/
│   ├── movie_dataset.csv
│   └── processed_movies.csv
│
├── models/
│   ├── tfidf_matrix.pkl
│   ├── tfidf_vectorizer.pkl
│   └── scaler.pkl
│
├── app.py
├── search.py
├── recommendation.py
├── data_processing.py
├── data_encoding.py
│
├── requirements.txt
└── README.md
```

---

# 📊 Dataset Information

Dataset Used:
MovieLens Dataset

Dataset contains:

* 87K+ movies
* 32M+ ratings
* 2M+ tags

Files Used:

* movies.csv
* ratings.csv
* tags.csv

---

# ⚙️ Technologies Used

## Programming Language

* Python

## Libraries

* Pandas
* Scikit-learn
* Joblib
* Streamlit

## Machine Learning / NLP

* TF-IDF Vectorization
* Cosine Similarity

---

# 🧹 Data Processing

The following preprocessing steps were performed:

* Removed null values
* Merged movie genres and tags
* Created combined content column
* Calculated:

  * average ratings
  * rating count
* Saved processed dataset

---

# 🔤 TF-IDF Encoding

The content column is converted into numerical vectors using TF-IDF Vectorization.

TF-IDF helps identify important words in movie descriptions, genres, and tags.

Example:

```text
Action Adventure Superhero DC Comic
```

gets converted into vector representations for semantic comparison.

---

# 📐 Cosine Similarity

Cosine Similarity measures similarity between movie vectors.

Movies with similar genres, themes, and tags receive higher similarity scores.

---

# 🌐 Streamlit Web App

The project includes a web-based interface using Streamlit.

Features:

* Movie search box
* Movie selection dropdown
* Recommendation display
* Ratings display

---

# ▶️ Installation

## 1. Clone Repository

```bash
git clone <your-github-repo-link>
cd Movie_system
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

## Step 1 — Data Processing

```bash
python data_processing.py
```

## Step 2 — Data Encoding

```bash
python data_encoding.py
```

## Step 3 — Run Web App

```bash
python -m streamlit run app.py
```

---

# 💡 Example Recommendation

Input Movie:

```text
Batman v Superman
```

Recommended Movies:

* Man of Steel
* Justice League
* Zack Snyder's Justice League
* Green Lantern: First Flight

---

# 📈 Future Improvements

Planned upgrades:

* 🎥 Movie posters using TMDB API
* 🤝 Collaborative Filtering
* 🧬 Hybrid Recommendation System
* ❤️ User Favorites & History
* 🔎 Fuzzy Search
* ☁️ Cloud Deployment

---

# 🎯 Learning Outcomes

Through this project, I learned:

* NLP fundamentals
* TF-IDF Vectorization
* Cosine Similarity
* Recommendation System Architecture
* Data Preprocessing
* Model Serialization
* Streamlit Web App Development

---

# 📌 Author

Developed by November_

---

# ⭐ If You Like This Project

Give this repository a star on GitHub ⭐

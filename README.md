# 🎬 Movies Recommender System

A content-based movie recommendation web app built with Python and Streamlit. Pick a movie you like, and the app suggests similar titles based on genre, cast, crew, and plot keywords — powered by the TMDB dataset from Kaggle.

**🔗 Live App:** [moviesz-recommender-system.streamlit.app](https://moviesz-recommender-system.streamlit.app/)

---

## 📌 Overview

This project uses **content-based filtering** to recommend movies similar to one selected by the user. Movie metadata (genres, keywords, cast, crew, and overview) is combined into a single "tags" feature, vectorized, and compared using **cosine similarity** to find the closest matches. The result is served through an interactive **Streamlit** web interface, with posters fetched live from the **TMDB API**.

## ✨ Features

- 🔍 Search and select from thousands of movies
- 🎯 Get top 5 similar movie recommendations instantly
- 🖼️ Movie posters fetched dynamically via the TMDB API
- ⚡ Fast, lightweight, and deployed for free on Streamlit Community Cloud
- 📓 Full model-building process documented in a Jupyter Notebook

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Data Processing | Pandas, NumPy |
| ML / NLP | Scikit-learn (CountVectorizer / Cosine Similarity), NLTK |
| Web App | Streamlit |
| Notebook | Jupyter |
| Data Source | [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) (Kaggle) |
| Deployment | Streamlit Community Cloud |

## 📂 Project Structure

```
Movies-Recommender-System/
├── model_training.ipynb     # EDA, preprocessing, and model-building notebook
├── app.py                   # Streamlit application
├── movie_dict.pkl           # Serialized processed movie data
├── similarity.pkl           # Precomputed cosine similarity matrix
├── requirements.txt         # Python dependencies
└── README.md
```
> Note: adjust file/folder names above if they differ from your actual repo layout.

## ⚙️ How It Works

1. **Data Collection** – Movies and credits data loaded from the TMDB 5000 dataset (Kaggle).
2. **Preprocessing** – Genres, keywords, cast, and crew are extracted and cleaned; text is merged into a single `tags` column.
3. **Vectorization** – Tags are converted into vectors using `CountVectorizer` (bag-of-words).
4. **Similarity Computation** – Cosine similarity is computed between all movie vectors.
5. **Recommendation** – For a selected movie, the top 5 most similar movies (by similarity score) are returned.
6. **Frontend** – Streamlit renders the UI, and the TMDB API fetches poster images in real time.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- A free [TMDB API key](https://www.themoviedb.org/settings/api)

### Installation

```bash
# Clone the repository
git clone https://github.com/ShivanshMishra659/Movies-Recommender-System.git
cd Movies-Recommender-System

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run Locally

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

> If the app fetches posters via the TMDB API, add your API key as an environment variable or in `.streamlit/secrets.toml`:
> ```toml
> TMDB_API_KEY = "your_api_key_here"
> ```

## 📊 Dataset

This project uses the **[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)** from Kaggle, which includes metadata for ~5000 movies — genres, keywords, cast, crew, overview, popularity, and more.

## 🖼️ Screenshots

> Add a screenshot or short GIF of the app in action here for extra polish:
> `![App Screenshot](assets/screenshot.png)`

## 🧩 Future Improvements

- [ ] Add collaborative filtering for personalized recommendations
- [ ] Include user ratings and reviews
- [ ] Add genre/language filters
- [ ] Improve UI/UX with movie trailers and cast details

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo, open an issue, or submit a pull request.

```bash
git checkout -b feature/your-feature
git commit -m "Add your feature"
git push origin feature/your-feature
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Shivansh Mishra**
GitHub: [@ShivanshMishra659](https://github.com/ShivanshMishra659)

---

⭐ If you found this project helpful, consider giving it a star on GitHub!

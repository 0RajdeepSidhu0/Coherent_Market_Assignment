from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


# load data
df = pd.read_csv("../data/startups_clean.csv")

# vectorize names
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(df["name"])

# compute similarity matrix
similarity = cosine_similarity(X)


def get_similar_startups(slug, top_n=5):
    idx = df[df["slug"] == slug].index

    if len(idx) == 0:
        return []

    idx = idx[0]

    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

    results = []
    for i, score in scores:
        results.append({
            "name": df.iloc[i]["name"],
            "slug": df.iloc[i]["slug"],
            "score": float(score)
        })

    return results
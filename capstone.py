import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load the clustering labels
with open('clustering_labels.pkl', 'rb') as f:
    labels = pickle.load(f)

z = []
for i in range(15):
    try:
        # Load the TF-IDF vectorized matrix
        with open(f'tfidf_matrix_{i}.pkl', 'rb') as f:
            z.append(pickle.load(f))
    except:
        pass        
    # print(f'read tfidf_matrix_{i}.pkl')

X = np.vstack(z)  

# Load the vectorizer
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('cluster_centroids.pkl', 'rb') as f:
    cluster_centroids = pickle.load(f)

# Load the YouTube data
df = pd.read_excel("youtube_data.xlsx")

def recommend_videos_using_clustering(keyword, vectorizer, X, labels, df, cluster_centroids, top_n=5):
    # Preprocess the keyword
    keyword_vector = vectorizer.transform([keyword]).toarray()

    # Find the most similar cluster to the keyword
    cluster_similarities = cosine_similarity(keyword_vector, cluster_centroids)
    most_similar_cluster_id = np.argmax(cluster_similarities)

    # Get all videos in the most similar cluster
    cluster_indices = np.where(labels == most_similar_cluster_id + 1)[0]  # +1 because labels are 1-indexed
    cluster_vectors = X[cluster_indices]

    # Calculate similarity of the keyword to all videos in the cluster
    video_similarities = cosine_similarity(keyword_vector, cluster_vectors)[0]

    # Get the indices of the top N matches within the cluster
    top_indices = np.argsort(video_similarities)[::-1][:top_n]

    # Retrieve the corresponding titles and video URLs
    recommendations = df.iloc[cluster_indices[top_indices]][['title_list', 'video_url_list']]

    return recommendations

st.title("YouTube like Application")

# Create a text input widget
user_input = st.text_input("Enter some text:")

# Display the input back to the user
if user_input:
    st.write("Showing the best matches for ", user_input)
    recommendations = recommend_videos_using_clustering(user_input, vectorizer, X, labels, df, cluster_centroids)
    st.write(len(recommendations))
    titles=recommendations["title_list"]
    video_URLs=recommendations["video_url_list"]
    for title,url in zip(titles,video_URLs):
         st.write(f"{title}")
         st.write(f"[Click here to watch the video]({url})")

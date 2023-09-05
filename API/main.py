import requests
import random
import tkinter as tk
from tkinter import ttk

# API Key
api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmMjU3Y2VmMWMxMDgyNjJkYTdjNGJmZTFiMGI1NjQwOSIsInN1YiI6IjY0ZjFkNGI5NzdkMjNiMDE1MDM5Nzk4NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.CufkqHh1F1o8m772_qkqb8oGn77lSeFraxu_2RCLVdw"


# API Base URL
base_url = "https://api.themoviedb.org/3"
headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Fetch and print genres
genre_url = f"{base_url}/genre/movie/list?language=en"
genre_response = requests.get(genre_url, headers=headers)
genre_response.raise_for_status()
genres = genre_response.json()
list_genres = [genre["name"] for genre in genres["genres"]]

# Create a Tkinter window
root = tk.Tk()
root.title("Movie Genre Suggestion")

# Create a label
label = tk.Label(root, text="Select a genre:")
label.pack()

# Create a dropdown list with genres
genre_var = tk.StringVar()
genre_dropdown = ttk.Combobox(root, textvariable=genre_var, values=list_genres)
genre_dropdown.pack()


# Function to suggest a random movie based on the selected genre
def suggest_movie():
    selected_genre = genre_var.get()

    # Fetch a list of popular movies
    popular_url = f"{base_url}/movie/popular?language=en-US&page=1"
    response = requests.get(popular_url, headers=headers)
    response.raise_for_status()
    popular_movies = response.json()

    # Filter movies by selected genre
    movies_in_genre = [movie for movie in popular_movies.get("results", []) if
                       selected_genre in [genre["name"] for genre in genres["genres"] if
                                          genre["id"] in movie.get("genre_ids", [])]]

    if movies_in_genre:
        random_movie = random.choice(movies_in_genre)
        suggestion_label.config(text=f"Random Movie Suggestion: {random_movie['title']}")
    else:
        suggestion_label.config(text="No movies found in this genre.")


# Create a button to trigger movie suggestion
suggest_button = tk.Button(root, text="Get Movie Suggestion", command=suggest_movie)
suggest_button.pack()

# Label to display the movie suggestion
suggestion_label = tk.Label(root, text="")
suggestion_label.pack()

# Run the Tkinter main loop
root.mainloop()
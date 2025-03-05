from pywebio import start_server
from pywebio.input import *
from pywebio.input import input
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *
import pandas as pd
import joblib

# Read Dataset
data = pd.read_csv("movies.csv")

# Upload models
with open('models/cosine_similarity.pkl', 'rb') as cosine:
    cosine_sim = joblib.load(cosine)

with open('models/movie_indices.pkl', 'rb') as indices:
    indice = joblib.load(indices)

def get_recommendations(title):
    idx = indice[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:9]  
    movie_indices = [i[0] for i in sim_scores]
    return data['title'].iloc[movie_indices]
      
def App():
    put_html('<center><h3>Movies Recommendation System</h3></center>').style('background-color:black; color:white; padding:10px; font-weight:bold')
    put_html('<p>Welcome to movies recommendation system</p>').style('text-align:center; font-weight:bold')
    put_image(open('image/img1.jpg','rb').read())
    
    movie = input('Enter movie name:')
    recommendation = get_recommendations(movie)
    put_text('Recommended Movies:').style('font-weight:bold; color:#17a589')
    for f in recommendation:
        put_text(f)
    hold()

start_server(App, port=4567, debug=True)
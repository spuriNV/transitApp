import json
import pandas as pd
import requests

url = 'https://api.themoviedb.org/3/movie/top_rated?api_key=aaa7de53dcab3a19afed86880f364e54&language=en-US&page=1'

response = requests.get(
    'https://api.themoviedb.org/3/movie/top_rated?api_key=aaa7de53dcab3a19afed86880f364e54&language=en-US&page=1')
df = pd.DataFrame()  # Creating a DataFrame

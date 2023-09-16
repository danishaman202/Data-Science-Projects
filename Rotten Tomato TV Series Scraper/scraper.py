'''
This file contains the RottenTomatoesScraper class which handles the web scraping functionality.
'''
import requests
from bs4 import BeautifulSoup

class RottenTomatoesScraper:
    def __init__(self):
        self.base_url = "https://www.rottentomatoes.com/tv/"

    def get_scores(self, series_name):
        search_url = self.base_url + series_name
        response = requests.get(search_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        series_link = soup.find_all("score-board")
        if series_link:
            series_scores = self._get_series_scores(series_link[0])
            return series_scores
        else:
            raise Exception("TV series not found.")

    def _get_series_scores(self, series_url):
        tomato_score = series_url['audiencescore']
        audience_score = series_url['tomatometerscore']

        if tomato_score and audience_score:
            pass
        else:
            tomato_score = "N/A"
            audience_score = "N/A"

        return {
            "rotten_tomato_score": tomato_score,
            "audience_score": audience_score
        }

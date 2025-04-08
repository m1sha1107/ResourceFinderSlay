import os
import urllib.parse
from flask import Blueprint, request, render_template
from dotenv import load_dotenv
import feedparser
from serpapi import GoogleSearch
import requests
import google.generativeai as genai

# Load API keys from .env
load_dotenv()

main = Blueprint("main", __name__)

# Route to render home page
@main.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Fetch research papers from arXiv
def fetch_arxiv_papers(query, max_results=3):
    base_url = "http://export.arxiv.org/api/query?"
    encoded_query = urllib.parse.quote(query)
    search_url = f"{base_url}search_query=all:{encoded_query}&start=0&max_results={max_results}"
    feed = feedparser.parse(search_url)

    results = []
    for entry in feed.entries:
        results.append({
            "title": entry.title,
            "type": "Research Paper",
            "link": entry.link,
            "description": entry.summary[:300] + "..."  # Trim long summaries
        })
    return results

# Fetch web articles using SerpAPI
def fetch_web_results(query, max_results=5):
    api_key = os.getenv("SERPAPI_API_KEY")
    search = GoogleSearch({
        "q": query,
        "api_key": api_key,
        "num": max_results
    })
    results = search.get_dict()

    cards = []
    if "organic_results" in results:
        for result in results["organic_results"]:
            cards.append({
                "title": result.get("title"),
                "type": "Web Article",
                "link": result.get("link"),
                "description": result.get("snippet", "No description available.")
            })
    return cards

# Route to process search and show results
@main.route("/search", methods=["POST"])
@main.route("/search", methods=["POST"])
def search():
    keywords = request.form.get("keywords")

    # Fetch all content
    papers = fetch_arxiv_papers(keywords)
    web_articles = fetch_web_results(keywords)
    yt_videos = fetch_youtube_videos(keywords)

    all_resources = papers + web_articles + yt_videos

    return render_template("results.html", keywords=keywords, resources=all_resources)

def fetch_youtube_videos(query, max_results=3):
    api_key = os.getenv("YOUTUBE_API_KEY")
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": max_results,
        "key": api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    videos = []
    for item in data.get("items", []):
        video_id = item["id"]["videoId"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        snippet = item["snippet"]

        videos.append({
            "title": snippet["title"],
            "type": "YouTube Video",
            "link": video_url,
            "description": snippet["description"][:200] + "..."
        })
    return videos

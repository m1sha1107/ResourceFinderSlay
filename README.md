# Sagey

Sagey is your cozy research assistant, designed to help you find and organize information from various sources like research papers, web articles, and YouTube videos. With a simple and intuitive interface, Sagey makes it easy to brew the perfect results for your queries.

## Features

- **Search Research Papers**: Fetches research papers from arXiv based on your keywords.
- **Web Articles**: Retrieves relevant web articles using SerpAPI.
- **YouTube Videos**: Finds YouTube videos related to your search.
- **Dynamic Results Page**: Displays results in a clean and organized layout.
- **Responsive Design**: Works seamlessly across devices.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd web-scraper-aggregator
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add the following keys:
     ```env
     SERPAPI_API_KEY=<your-serpapi-key>
     YOUTUBE_API_KEY=<your-youtube-api-key>
     ```

## Usage

1. Run the application:
   ```bash
   python run.py
   ```

2. Open your browser and navigate to `http://127.0.0.1:5000`.

3. Enter your query in the search bar and click "Brew Results".

4. Explore the results, including research papers, web articles, and YouTube videos.

## Demo

Check out the [demo video](https://youtu.be/LuI4r41VIjU) to see Sagey in action!

## File Structure

```
web-scraper-aggregator/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── static/
│   │   └── style.css
│   └── templates/
│       ├── index.html
│       ├── layout.html
│       └── results.html
├── run.py
├── requirements.txt
└── README.md
```

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [Feedparser](https://feedparser.readthedocs.io/) for parsing RSS feeds.
- [SerpAPI](https://serpapi.com/) for web search results.
- [YouTube Data API](https://developers.google.com/youtube/registering_an_application) for fetching video data.

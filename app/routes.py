from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        keywords = request.form.get("keywords")
        # Later: pass to search/scraper
        results = [
            {"title": "Dummy Result 1", "url": "http://example.com", "summary": "Lorem ipsum..."},
            {"title": "Dummy Result 2", "url": "http://example.org", "summary": "Dolor sit amet..."},
        ]
    return render_template("index.html", results=results)

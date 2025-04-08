from flask import Blueprint, request, render_template

main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@main.route("/search", methods=["POST"])
def search():
    keywords = request.form.get("keywords")

    # ✨ Dummy resource list (simulate real results)
    resources = [
        {
            "title": "Understanding AI Ethics",
            "type": "Research Paper",
            "link": "https://arxiv.org/abs/2301.00001",
            "description": "A foundational paper on ethical concerns in AI."
        },
        {
            "title": "AI Explained Simply",
            "type": "YouTube Video",
            "link": "https://www.youtube.com/watch?v=abcd1234",
            "description": "A beginner-friendly video on how AI works."
        },
        {
            "title": "Recent Breakthrough in AI",
            "type": "News Article",
            "link": "https://techcrunch.com/sample-news",
            "description": "Latest news on cutting-edge AI research."
        }
    ]

    return render_template("results.html", keywords=keywords, resources=resources)

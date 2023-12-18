from flask import *
import os
from dotenv import load_dotenv
import json
import peewee

from models.Post import Post

cfg = os.path.join(os.path.dirname(__name__), ".env")
if not os.path.exists(cfg):
    open(".env", "a+").close()
load_dotenv(cfg)

app = Flask(__name__)
app.config.from_object(__name__)

db = peewee.SqliteDatabase(os.environ.get("DB_CONN"))


@app.errorhandler(404)
def page404(e):
    return render_template("errors/404.html")


@app.errorhandler(500)
def page500(e):
    return render_template("errors/500.html")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/glossary")
def articles_list():
    try:
        articles = (Post
                    .select(Post.post_id, Post.title, Post.img, Post.created_at)
                    .order_by(Post.title))
        data = list(
            {
                "id": selected_articles.post_id,
                "title": selected_articles.title,
                "img": selected_articles.img,
                "created_at": selected_articles.created_at
            }
            for selected_articles in articles
        )
    except:
        abort(502)
    return render_template("glossary/index.html", data=data)


@app.route("/glossary/<string:article_id>")
def article(article_id: str):
    try:
        article_id = int(article_id)
        selected_article = (Post()
                            .select(Post.title, Post.text, Post.img, Post.created_at)
                            .where(Post.post_id == article_id)
                            .get())
        data = {
            "title": selected_article.title,
            "text": selected_article.text,
            "img": selected_article.img,
        }
        print(selected_article.text)
    except:
        abort(404)
    return render_template("glossary/articles.html", data=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/links")
def links():
    return render_template("links.html")


# @app.route("/search")
# def search():
#     return render_template("search.html")


# @app.route("/create_post", methods=["POST"])
# def create_post():
#     try:
#         data = json.loads(request.data)
#         new_post = Post.create()
#         new_post.title = data["title"]
#         new_post.text = data["text"]
#         new_post.img = data["img"]
#         new_post.save()
#     except:
#         abort(500)
#     return Response(status=200)
#
#
# @app.route("/new_post")
# def new_post():
#     return render_template("create_new_article.html")


if __name__ == "__main__":
    app.run(
        debug=os.environ.get("DEBUG"),
        port=os.environ.get("PORT"),
        host=os.environ.get("HOST")
    )

from server import *


@app.route("/api/news", methods=["GET"])
def get_news():
    # Instantiate News class and call the get method
    news = News(None, session["uid"])
    news.get(True)
    return render_template("/news/news.html")


@app.route("/api/news/create", methods=["POST", "GET"])
@app.route("/api/news/create/", methods=["POST", "GET"])
def create_news():
    if request.method == "POST":
        # Extract news data from request form
        title = request.form["title"]
        description = request.form["description"]
        tags = request.form["tags"]
        sender_uid = session["uid"]
        community_id = request.form["communityID"]

        # Instantiate News class and call the create method
        news = News(None, session["uid"])
        news.create(title, description, tags, sender_uid, community_id)

    return render_template("/news/create_news.html")


@app.route("/api/news/update/<string:news_id>", methods=["PUT", "GET"])
@app.route("/api/news/update/<string:news_id>/", methods=["PUT", "GET"])
def update_news(news_id):
    # Instantiate News class with news ID and user UID
    news = News(news_id, session["uid"])

    if request.method == "PUT":
        # Extract news data from request form
        title = request.form["title"]
        description = request.form["description"]
        tags = request.form["tags"]
        sender_uid = session["uid"]
        community_id = request.form["communityID"]

        # Call the update method
        news.update(news_id, title, description, tags, sender_uid, community_id)
    news_details = news.get(False)
    return render_template("/news/update_news.html", details=news_details)


@app.route("/api/news/delete/<string:news_id>", methods=["DELETE"])
@app.route("/api/news/delete/<string:news_id>/", methods=["DELETE"])
def delete_news(news_id):
    # Instantiate News class with user UID
    news = News(news_id, session["uid"])

    # Call the delete method
    news.delete("newsID")

    flash("News deleted successfully", "success")
    return redirect("/api/news")

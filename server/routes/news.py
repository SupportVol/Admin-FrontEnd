from server import *


@app.route("/api/news", methods=["GET"])
def get_news():
    """
    Route to get news.
    """
    # Instantiate News class and call the get method
    news = News(None, session["uid"])
    news.get(True)

    # Render the news template
    return render_template("/news/news.html")


@app.route("/api/news/create", methods=["POST", "GET"])
@app.route("/api/news/create/", methods=["POST", "GET"])
def create_news():
    """
    Route to create news.
    """
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

    # Render the create news template
    return render_template("/news/create_news.html")


@app.route("/api/news/update/<string:news_id>", methods=["PUT", "GET"])
@app.route("/api/news/update/<string:news_id>/", methods=["PUT", "GET"])
def update_news(news_id):
    """
    Route to update news.
    """
    if not login_verification():
        return redirect("/auth")
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

    # Get the news details
    news_details = news.get(False)

    # Render the update news template with news details
    return render_template("/news/update_news.html", details=news_details)


@app.route("/api/news/delete/<string:news_id>", methods=["DELETE"])
@app.route("/api/news/delete/<string:news_id>/", methods=["DELETE"])
def delete_news(news_id):
    """
    Route to delete news.
    """
    if not login_verification():
        return redirect("/auth")
    # Instantiate News class with user UID
    news = News(news_id, session["uid"])

    # Call the delete method
    news.delete("newsID")

    # Flash a success message
    flash("News deleted successfully", "success")

    # Redirect to the news page
    return redirect("/api/news")

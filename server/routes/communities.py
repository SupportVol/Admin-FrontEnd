from server import *


@app.route("/api/community", methods=["GET"])
@app.route("/api/community/", methods=["GET"])
def get_communities():
    uid = session["uid"]  # Assuming user UID is stored in session
    communities = Communities(community_uid, uid)
    all_communities = communities.get(True)
    return render_template("/community/communities.html", communities=all_communities)


@app.route("/api/community/create", methods=["POST", "GET"])
@app.route("/api/community/create/", methods=["POST", "GET"])
def create_community():
    if request.method == "POST":
        # Extract community data from request form
        name = request.form["name"]
        title = request.form["title"]
        description = request.form["description"]
        photo_url = request.form["photoUrl"]
        banner = request.form["banner"]
        theme = request.form["theme"]
        members = request.form["members"]

        # Instantiate Communities class and call the create method
        communities = Communities(None, session["uid"])
        communities.create(name, title, description, photo_url, banner, theme, members)
    return render_template("/community/create_community.html")


@app.route("/api/community/update/<string:community_uid>", methods=["PUT", "GET"])
@app.route("/api/community/update/<string:community_uid>/", methods=["PUT", "GET"])
def update_community(community_uid):
    communities = Communities(community_uid, session["uid"])
    if request.method == "PUT":
        # Extract community data from request form
        name = request.form["name"]
        title = request.form["title"]
        description = request.form["description"]
        photo_url = request.form["photoUrl"]
        banner = request.form["banner"]
        theme = request.form["theme"]
        members = request.form["members"]
        # Instantiate Communities class and call the update method
        communities.update(name, title, description, photo_url, banner, theme, members)
    community = communities.get()
    return render_template("/community/update_community.html", details=community)


@app.route("/api/community/delete/<string:community_uid>", methods=["DELETE"])
def delete_community(community_uid):
    # Instantiate Communities class and call the delete method
    communities = Communities(None, session["uid"])
    communities.delete(community_uid)
    flash("Community deleted successfully", "success")
    return redirect("/api/community")

from server import *


@app.route("/api/community", methods=["GET"])
@app.route("/api/community/", methods=["GET"])
def get_communities():
    """
    Endpoint to get all communities.
    """
    if not login_verification():
        return redirect("/auth")
    # Assuming user UID is stored in session
    uid = session["uid"]

    # Instantiate Communities class
    communities = Communities(community_uid, uid)

    # Get all communities
    all_communities = communities.get(True)

    # Render the communities page with all communities
    return render_template("/community/communities.html", communities=all_communities)


@app.route("/api/community/create", methods=["POST", "GET"])
@app.route("/api/community/create/", methods=["POST", "GET"])
def create_community():
    """
    Endpoint to create a new community.
    """
    if not login_verification():
        return redirect("/auth")
    if request.method == "POST":
        # Extract community data from request form
        name = request.form["name"]
        title = request.form["title"]
        description = request.form["description"]
        photo_url = request.form["photoUrl"]
        banner = request.form["banner"]
        theme = request.form["theme"]
        members = request.form["members"]

        # Instantiate Communities class
        communities = Communities(None, session["uid"])

        # Call the create method to create a new community
        communities.create(
            name=name,
            title=title,
            description=description,
            photo_url=photo_url,
            banner=banner,
            theme=theme,
            members=members,
        )

    # Render the create community page
    return render_template("/community/create_community.html")


@app.route("/api/community/update/<string:community_uid>", methods=["PUT", "GET"])
@app.route("/api/community/update/<string:community_uid>/", methods=["PUT", "GET"])
def update_community(community_uid):
    """
    Endpoint to update a community.
    """
    if not login_verification():
        return redirect("/auth")
    # Instantiate Communities class
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

        # Call the update method to update the community
        communities.update(
            name=name,
            title=title,
            description=description,
            photo_url=photo_url,
            banner=banner,
            theme=theme,
            members=members,
        )

    # Get the updated community
    community = communities.get(False)

    # Render the update community page with the updated community details
    return render_template("/community/update_community.html", details=community)


@app.route("/api/community/delete/<string:community_uid>", methods=["DELETE"])
@app.route("/api/community/delete/<string:community_uid>/", methods=["DELETE"])
def delete_community(community_uid):
    """
    Endpoint to delete a community.
    """
    if not login_verification():
        return redirect("/auth")
    # Instantiate Communities class
    communities = Communities(community_uid, session["uid"])

    # Call the delete method to delete the community
    communities.delete("communityUID")

    # Flash a success message
    flash("Community deleted successfully", "success")

    # Redirect to the communities page
    return redirect("/api/community")

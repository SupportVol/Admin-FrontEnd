from server import *


# Route to get all API keys
@app.route("/api/keys", methods=["GET"])
@app.route("/api/keys/", methods=["GET"])
def get_keys():
    """
    Function to get all API keys.
    """
    if not login_verification():
        return redirect("/auth")
    # Create an API Key object
    ak = Api_Key(session["uid"])
    # Get all keys
    all_keys = ak.get(True)
    print(all_keys)
    # Render the keys on the template
    return render_template("api_key/show_keys.html", keys=all_keys)


# Route to create a new API key
@app.route("/api/keys/create", methods=["POST", "GET"])
@app.route("/api/keys/create/", methods=["POST", "GET"])
def create_key():
    """
    Function to create a new API key.
    """
    if not login_verification():
        return redirect("/auth")
    # If the request method is POST
    if request.method == "POST":
        # Get the owner details from the form
        owner_name, owner_uid, owner_email = (
            request.form["owner_name"],
            request.form["owner_uid"],
            request.form["owner_email"],
        )
        # Create an API Key object
        ak = Api_Key(session["uid"])
        # Create a new key
        response = ak.create(
            ownerName=owner_name, ownerUid=owner_uid, ownerEmail=owner_email
        )
        # Redirect to the create key page
        return redirect("/api/keys/create")
    # Render the create key template
    return render_template("api_key/create_key.html", create_or_update="Create")


# Route to update an existing API key
@app.route("/api/keys/update/<string:api_key>", methods=["POST", "GET"])
@app.route("/api/keys/update/<string:api_key>/", methods=["POST", "GET"])
def update_key(api_key):
    """
    Function to update an existing API key.
    """
    if not login_verification():
        return redirect("/auth")
    # Create an API Key object
    ak = Api_Key(api_key, session["uid"])
    # If the request method is POST
    if request.method == "POST":
        # Get the owner details from the form
        owner_name, owner_uid, owner_email = (
            request.form["owner_name"],
            request.form["owner_uid"],
            request.form["owner_email"],
        )
        # Update the key
        response = ak.update(
            ownerName=owner_name,
            ownerUid=owner_uid,
            ownerEmail=owner_email,
            ownerApiKey=api_key,
        )
        print(response)
        # Redirect to the keys page
        return redirect("/api/keys")
    # Get the key details
    key_details = ak.get(False)
    # Render the update key template
    return render_template(
        "api_key/update_key.html", details=key_details, create_or_update="Update"
    )


# Route to delete an API key
@app.route("/api/keys/delete/<string:api_key>")
@app.route("/api/keys/delete/<string:api_key>/")
def delete_key(api_key):
    """
    Function to delete an API key.
    """
    if not login_verification():
        return redirect("/auth")
    # Create an API Key object
    ak = Api_Key(api_key, session["uid"])
    # Delete the key
    ak.delete("ownerApiKey")
    # Flash a success message
    flash("successful", "success")
    # Redirect to the keys page
    return redirect("/api/keys")

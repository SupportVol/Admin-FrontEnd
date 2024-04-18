from server import *
from server.api.api_key import *


@app.route("/api/keys", methods=["GET"])
@app.route("/api/keys/", methods=["GET"])
def get_keys():
    ak = Api_Key(session["uid"])
    all_keys = ak.get_all()
    print(all_keys)
    return render_template("api_key/show_keys.html", keys=all_keys)


@app.route("/api/keys/create", methods=["POST", "GET"])
@app.route("/api/keys/create/", methods=["POST", "GET"])
def create_key():
    if request.method == "POST":
        owner_name, owner_uid, owner_email = (
            request.form["owner_name"],
            request.form["owner_uid"],
            request.form["owner_email"],
        )
        ak = Api_Key(session["uid"])
        response = ak.create(owner_name, owner_uid, owner_email)
        print(response)
    return render_template("api_key/create_key.html", create_or_update="Create")


@app.route("/api/keys/update", methods=["POST", "GET"])
@app.route("/api/keys/update/", methods=["POST", "GET"])
def update_key():
    ak = Api_Key(session["uid"])
    if request.method == "POST":
        owner_name, owner_uid, owner_email = (
            request.form["owner_name"],
            request.form["owner_uid"],
            request.form["owner_email"],
        )

        response = ak.update(owner_name, owner_uid, owner_email)
        print(response)
        return redirect("/api/keys")
    key_details = ak.get_one()
    print(key_details)
    return render_template(
        "api_key/create_key.html", details=key_details, create_or_update="Update"
    )


@app.route("/api/keys/delete/<string:api_key>")
@app.route("/api/keys/delete/<string:api_key>/")
def delete_key(api_key):
    ak = Api_Key(session["uid"])
    ak.delete()
    flash("successful", "success")
    return redirect("/api/keys")

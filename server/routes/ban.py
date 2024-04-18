from server import *


@app.route("/ban", methods=["PUT", "POST", "GET"])
def ban_user():
    ban = Ban(
        session["banUserUID"] if "banUserUID" in session else None, session["uid"]
    )
    if request.method == "POST":
        ban.ban_user()
        flash("Banned User", "success")
        return redirect("/ban")
    elif request.method == "PUT":
        ban.un_ban_user()
        flash("Unbanned User", "success")
        return redirect("/ban")
    result = ban.get_all_users()
    return render_template("/ban/index.html", users=result)

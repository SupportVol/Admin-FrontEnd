from server import *


# Define the route for banning users
@app.route("/ban", methods=["PUT", "POST", "GET"])
def ban_user():
    """
    Function to ban or unban a user.

    If the request method is POST, the user is banned.
    If the request method is PUT, the user is unbanned.
    If the request method is GET, it returns all users.

    Returns:
        redirect to "/ban" after banning or unbanning a user.
        render_template with all users if the request method is GET.
    """
    if not login_verification():
        return redirect("/auth")
    # Create a Ban object with the user's session information
    ban = Ban(
        session["banUserUID"] if "banUserUID" in session else None, session["uid"]
    )

    # If the request method is POST, ban the user
    if request.method == "POST":
        ban.ban_user()
        flash("Banned User", "success")
        return redirect("/ban")

    # If the request method is PUT, unban the user
    elif request.method == "PUT":
        ban.un_ban_user()
        flash("Unbanned User", "success")
        return redirect("/ban")

    # If the request method is GET, get all users
    result = ban.get_all_users()
    return render_template("/ban/index.html", users=result)

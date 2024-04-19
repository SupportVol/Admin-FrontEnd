from server import *


# Define the route for authentication
@app.route("/auth", methods=["POST", "GET"])
@app.route("/auth/", methods=["POST", "GET"])
def auth():
    """
    This function handles the authentication of users.
    It supports both POST and GET methods.
    For POST, it takes email and password, and tries to log the user in.
    For GET, it simply renders the authentication page.
    """
    # If the request method is POST, try to log the user in
    if request.method == "POST":
        # Get the email and password from the form
        email = encode(request.form["email"])
        password = encode(request.form["password"])

        # Create an Authentication object
        auth = Authentication()

        # Try to log the user in
        response = auth.login(email, password)

        # If the login was unsuccessful, flash a message and redirect to the auth page
        if not response:
            session["temp"] = {"email": decode(email), "password": decode(password)}
            flash("Wrong Credentials", "danger")
            return redirect("/auth")

        # If the login was successful, redirect to the home page
        return redirect("/")

    # If the request method is GET, render the auth page
    temp = None
    if "temp" in session:
        temp = session["temp"]
    return render_template("auth.html", temp=temp)

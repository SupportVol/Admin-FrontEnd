from server import *


@app.route("/auth", methods=["POST", "GET"])
@app.route("/auth/", methods=["POST", "GET"])
def auth():
    if request.method == "POST":
        email = encode(request.form["email"])
        password = encode(request.form["password"])
        auth = Authentication()
        response = auth.login(email, password)
        if not response:
            session["temp"] = {"email": decode(email), "password": decode(password)}
            flash("Wrong Credentials", "danger")
            return redirect("/auth")
        return redirect("/")
    temp = None
    if "temp" in session:
        temp = session["temp"]
    return render_template("auth.html", temp=temp)

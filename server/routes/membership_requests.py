from server import *


# Define route for getting membership requests
@app.route("/api/organizations/requests", methods=["GET"])
@app.route("/api/organizations/requests/", methods=["GET"])
def membership_requests():
    """
    Function to handle GET requests for membership requests.
    Returns a rendered template with pending membership requests.
    """
    if not login_verification():
        return redirect("/auth")
    # Assuming user UID is stored in session
    uid = session["uid"]

    # Instantiate Membership_Requests class and call the get method
    membership_requests = Membership_Requests(uid)

    # Render template with pending requests
    return render_template(
        "/membership_requests/membership_requests.html",
        pending_requests=membership_requests.get(True),
    )


# Define route for accepting membership requests
@app.route("/api/organizations/requests/accept/<string:requestID>", methods=["POST"])
@app.route("/api/organizations/requests/accept/<string:requestID>/", methods=["POST"])
def accept_organization_request(requestID):
    """
    Function to handle POST requests for accepting membership requests.
    Returns a redirect to the membership requests page.
    """
    if not login_verification():
        return redirect("/auth")
    # Assuming user UID is stored in session
    uid = session["uid"]

    # Instantiate Membership_Requests class and call the approve method
    membership_requests = Membership_Requests(uid, requestID)
    membership_requests.approve()

    # Flash success message
    flash("Approved Organization!", "success")

    # Redirect to membership requests page
    return redirect("/api/organizations/requests")


# Define route for declining membership requests
@app.route("/api/organizations/requests/decline/<string:requestID>", methods=["PUT"])
@app.route("/api/organizations/requests/decline/<string:requestID>/", methods=["PUT"])
def decline_organization_request(requestID):
    """
    Function to handle PUT requests for declining membership requests.
    Returns a redirect to the membership requests page.
    """
    if not login_verification():
        return redirect("/auth")
    # Assuming user UID is stored in session
    uid = session["uid"]

    # Instantiate Membership_Requests class and call the decline method
    membership_requests = Membership_Requests(uid, requestID)
    membership_requests.decline()

    # Flash danger message
    flash("Declined Organization!", "danger")

    # Redirect to membership requests page
    return redirect("/api/organizations/requests")

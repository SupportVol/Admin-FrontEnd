from server import *


@app.route("/api/organizations/requests", methods=["GET"])
@app.route("/api/organizations/requests/", methods=["GET"])
def membership_requests():
    uid = session["uid"]  # Assuming user UID is stored in session
    # Instantiate Membership_Requests class and call the get method
    membership_requests = Membership_Requests(uid)
    return render_template(
        "/membership_requests/membership_requests.html",
        pending_requests=membership_requests.get(True),
    )


@app.route(
    "/api/organizations/requests/accept/<string:requestID>",
    methods=[
        "POST",
    ],
)
@app.route("/api/organizations/requests/accept/<string:requestID>", methods=["POST"])
def accept_organization_request(requestID):
    uid = session["uid"]  # Assuming user UID is stored in session
    # Instantiate Membership_Requests class and call the get method
    membership_requests = Membership_Requests(uid, requestID)
    membership_requests.approve()
    flash("Approved Organization!", "success")
    return redirect("/api/organizations/requests")


@app.route(
    "/api/organizations/requests/decline/<string:requestID>",
    methods=[
        "PUT",
    ],
)
@app.route("/api/organizations/requests/decline/<string:requestID>", methods=["PUT"])
def decline_organization_request(requestID):
    uid = session["uid"]  # Assuming user UID is stored in session
    # Instantiate Membership_Requests class and call the get method
    membership_requests = Membership_Requests(uid, requestID)
    membership_requests.decline()
    flash("Declined Organization!", "danger")
    return redirect("/api/organizations/requests")

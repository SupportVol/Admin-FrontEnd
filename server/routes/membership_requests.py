from server import *


@app.route("/api/organizations/requests", methods=["GET"])
@app.route("/api/organizations/requests/", methods=["GET"])
def get_membership_requests():
    uid = session["uid"]  # Assuming user UID is stored in session

    # Instantiate Membership_Requests class and call the get method
    membership_requests = Membership_Requests(uid)
    membership_requests.get()

    return render_template("/membership_requests/membership_requests.html")


@app.route("/api/organizations/requests/create", methods=["POST", "GET"])
@app.route("/api/organizations/requests/create/", methods=["POST", "GET"])
def create_membership_request():
    if request.method == "POST":
        # Extract membership request data from request form
        registration_certificate_url = request.form["registrationCertificateUrl"]
        annual_report_url = request.form["annualReportUrl"]
        legal_documents_url = request.form["legalDocumentsUrl"]
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        description = request.form["description"]

        # Instantiate Membership_Requests class and call the create method
        membership_requests = Membership_Requests(session["uid"])
        membership_requests.create(
            registration_certificate_url,
            annual_report_url,
            legal_documents_url,
            name,
            email,
            password,
            description,
        )

    return render_template("/membership_requests/create_membership_request.html")


@app.route(
    "/api/organizations/requests/update/<string:request_id>", methods=["PUT", "GET"]
)
@app.route(
    "/api/organizations/requests/update/<string:request_id>/", methods=["PUT", "GET"]
)
def update_membership_request(request_id):
    # Instantiate Membership_Requests class with request ID and user UID
    membership_requests = Membership_Requests(session["uid"], request_id)

    if request.method == "PUT":
        # Extract membership request data from request form
        registration_certificate_url = request.form["registrationCertificateUrl"]
        annual_report_url = request.form["annualReportUrl"]
        legal_documents_url = request.form["legalDocumentsUrl"]
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        description = request.form["description"]

        # Call the update method
        membership_requests.update(
            registration_certificate_url,
            annual_report_url,
            legal_documents_url,
            name,
            email,
            password,
            description,
        )
    membership_details = membership_requests.get(False)
    return render_template(
        "/membership_requests/update_membership_request.html",
        details=membership_details,
    )


@app.route("/api/organizations/requests/delete/<string:request_id>", methods=["DELETE"])
@app.route(
    "/api/organizations/requests/delete/<string:request_id>/", methods=["DELETE"]
)
def delete_membership_request(request_id):
    # Instantiate Membership_Requests class with user UID
    membership_requests = Membership_Requests(session["uid"])

    # Call the delete method
    membership_requests.delete(request_id)

    flash("Membership request deleted successfully", "success")
    return redirect("/api/organizations/requests")

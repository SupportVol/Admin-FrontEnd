from server import *

# Importing necessary modules from server


# Error handler for 404 error
@app.errorhandler(404)
def page_not_found():
    """
    This function handles the 404 error. returns a custom 404 page.
    """

    # Render and return the custom 404 page
    return render_template(
        "/errors/404.html",
        link="https://i.pinimg.com/originals/86/41/80/86418032b715698a4dfa6684b50c12af.gif",
    )


# Error handler for 500 error
@app.errorhandler(500)
def server_error():
    """
    This function handles the 500 error. returns a custom 500 page.
    """
    if not login_verification():
        return redirect("/auth")
    # Try to render and return the custom 500 page
    return render_template(
        "/errors/500.html",
        link="https://media0.giphy.com/media/TqiwHbFBaZ4ti/giphy.gif",
    )

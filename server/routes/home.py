from server import *

# Import all necessary modules from the server package


# Define the route for the home page
@app.route("/")
def home():
    """
    Function to render the home page.

    Returns:
        render_template: Renders the home.html template for the home page.
    """
    if not login_verification():
        return redirect("/auth")
    # Render the home.html template
    return render_template("home.html")

from server import *


@app.errorhandler(404)
def page_not_found():
    log_ip_address(url_trying_to_access="404", ip_address=request.remote_addr)
    return render_template(
        "/error/404.html",
        link="https://i.pinimg.com/originals/86/41/80/86418032b715698a4dfa6684b50c12af.gif",
    )


@app.errorhandler(500)
def server_error():
    log_ip_address(url_trying_to_access="500", ip_address=request.remote_addr)
    try:
        return render_template(
            "/error/500.html",
            link="https://media0.giphy.com/media/TqiwHbFBaZ4ti/giphy.gif",
        )
    except:
        return abort(404)

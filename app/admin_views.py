from app import app

# administration paths for the application.

# a render_template import path for admin dashboard HTML to appear.
from flask import render_template


# every route needs a forward slash at the beginning.
@app.route("/admin/dashboard")
# writing a function called admin_dashboard
def admin_dashboard():
    # return "admin dashboard"
    return render_template("admin/dashboard.html")

# asking the route of about to return a h1 HTML tag with styling.
@app.route("/admin/profile")
    # writing a function called admin_profile
    # importing the new views.
def admin_profile():
        return "admin_profile"

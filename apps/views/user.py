from flask import render_template

class views:
    def index():
        return render_template("user/index.html")
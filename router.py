from apps import app
from apps.views.user import views

@app.route("/",methods=["get"])
def index():
    return views.index()



app.run(debug=True)

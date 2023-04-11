import os
import pathlib

import requests
from flask import Flask, session, abort, redirect, request, render_template
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
from os import environ

app = Flask(__name__, template_folder="templates")
app.secret_key = "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" # make sure this matches with that's in client_secret.json
EMPLOYEE_URL = "http://127.0.0.1:5001/employees/get_employee_details/"

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1" # to allow Http traffic for local dev

GOOGLE_CLIENT_ID = "853461678196-e1b584mbdtsq60l4g3vorcr4kt05ruq5.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5450/callback"
)


def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()
    return wrapper


@app.route("/login")
def googlelogin():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    next_url = request.args.get("next") or "/"
    return redirect(authorization_url + f"&next={next_url}")


@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    # session['id_info'] = id_info
    session['id_info'] = id_info
    session['email'] = id_info.get("email")     
    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    session["picture"] = id_info.get("picture")

    email_id = session['email']
    url = f"{EMPLOYEE_URL}{email_id}"
    response = requests.get(url)
    # print(response)
    if response.status_code == 200:

        employee_id = response.json()['data']['id']
        session['employee_id'] = employee_id
        
        return render_template("homepage.html", email=session['email'], id_info=session['id_info'], name=session['name'], picture=session['picture'], employee_id=session["employee_id"])

    else:
        return render_template("signup.html")

# our html pages
@app.route("/")
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route('/display_all_scripts')
def display_all_scripts():
    return render_template("display_all_scripts.html", email=session['email'], id_info=session['id_info'], name=session['name'], picture=session['picture'], employee_id=session["employee_id"])

@app.route('/request_for_a_script')
def request_for_a_script():
    return render_template("request_for_a_script.html", email=session['email'], id_info=session['id_info'], name=session['name'], picture=session['picture'], employee_id=session["employee_id"])

@app.route('/display_all_requests')
def display_all_requests():
    return render_template("display_requests.html", email=session['email'], id_info=session['id_info'], name=session['name'], picture=session['picture'], employee_id=session["employee_id"])

@app.route('/homepage')
def homepage():
    return render_template("homepage.html", email=session['email'], id_info=session['id_info'], name=session['name'], picture=session['picture'], employee_id=session["employee_id"])


# # driver
# @app.route("/dSignUp")
# def dsignup():
#     name = session['name']
#     email = session['email']
#     return render_template("driver/dSignUp.html", name=name, email=email)

# @app.route("/dCreateCarpool")
# def dCreateCarpool():
#     DID = session['driver_id']
#     return render_template("driver/dCreateCarpool.html", DID=DID)

# @app.route("/dHome")

# def dHome():
#     DID = session['driver_id']
#     return render_template("driver/dHome.html", DID=DID)

# @app.route("/dPastRides")
# def dPastRides():
#     DID = session['driver_id']
#     return render_template("driver/dPastRides.html", DID=DID)

# @app.route("/dProfile")
# def dProfile():
#     DID = session['driver_id']
#     return render_template("driver/dProfile.html", DID=DID)

# @app.route("/dUpcoming")
# def dUpcoming():
#     DID = session['driver_id']
#     return render_template("driver/dUpcoming.html", DID=DID)

# # passenger
# @app.route("/pSignUp")
# def psignup():
#     name = session['name']
#     email = session['email']
#     return render_template("passenger/pSignUp.html", name=name, email=email) 

# @app.route("/pFindCarpool")
# def pFindCarpool():
#     PID = session['passenger_id']
#     return render_template("passenger/pFindCarpool.html", PID=PID)

# @app.route("/pHome")
# def pHome():
#     PID = session['passenger_id']
#     return render_template("passenger/pHome.html", PID=PID)

# @app.route("/pPastRides")
# def pPastRides():
#     PID = session['passenger_id']
#     return render_template("passenger/pPastRides.html", PID=PID)

# @app.route("/pProfile")
# def pProfile():
#     PID = session['passenger_id']
#     return render_template("passenger/pProfile.html", PID=PID)

# @app.route("/pUpcoming")
# def pUpcoming():
#     PID = session['passenger_id']
#     return render_template("passenger/pUpcoming.html", PID=PID)

# @app.route("/pRefund")
# def refund():
#     PID = session['passenger_id']
#     return render_template("passenger/pRefund.html", PID=PID)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5450, debug=True)


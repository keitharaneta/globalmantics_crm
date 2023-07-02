from flask import Flask, render_template, request
from mvcmodeldatabase import Database

app = Flask(__name__)
path = Database('jsondata.json')

@app.route("/", methods=["GET", "POST"])
def index():
    """
    This is a view function which responds to requestes for the top-level URL.
    It serves as the "controller" in MVC as it accesses both the model and the view.
    """

    # The button click within the view kicks off a POST request ...
    if request.method == "POST":

        # This collects the user input from the view. The controller`s job
        # is to process this information, which includes using methods from
        # the "model" to get the information we need (in this case, the account balance).
        acct_id = request.form["acctid"]
        results = path.output(acct_id)
        app.logger.debug("balance for {}: {}".format(acct_id, results))
    else:

        # During a normal GET request, no need to perform any calculations
        acct_balance = "N/A"

    # This is the view, which i the jinja2 templated HTML data that is presented to the user.
    # The user interacts with this webpage and provides information that the controller then processes.
    # The controller passess the account balance into the view so it can be displayed back to the user.
    return render_template("index.html", acct_balance=acct_balance)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
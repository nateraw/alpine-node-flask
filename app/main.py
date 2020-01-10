import sys

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    version = "{}.{}".format(sys.version_info.major, sys.version_info.minor)
    msg_1 = "We are in a Docker container running Python {} with Meinheld and Gunicorn on Alpine (default).".format(
        version
    )
    msg_2 = "Also, we used node on build to include src of bootstrap, jquery, and popper.js!!"
    return render_template('index.html', msg_1=msg_1, msg_2=msg_2)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

from flask import Flask, request
import git

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, vladiksdsd!</p>"

@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo.clone_from('https://github.com/dehaon2/getit', 'getit/app', branch='master')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

from flask import Flask, request
import git
import router

app = Flask(__name__)

r = router.Router(app)
r.routes()

@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo.clone_from('https://github.com/dehaon2/getit', 'getit/app', branch='master')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

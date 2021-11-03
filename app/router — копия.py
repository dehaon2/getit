class Router:
    def __init__(self, app):
        self.app = app

    def routes(self):
        @self.app.route("/")
        def hello_world():
            return "<p>Hello, vladiksdasdasddsdsdsddas123123asdasd!</p>"

        @self.app.route("/heh")
        def hello_world():
            return "<p>mda</p>"

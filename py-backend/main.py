import webapp2

class Hello(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello, world from Python')

application = webapp2.WSGIApplication([
    # In order to make dispatch.yaml work, we handle /.*, so /py/*
    # is served by Hello handler.
    ('/.*', Hello)
], debug=True)

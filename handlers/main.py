import time
import datetime as dt
from datetime import datetime
from google.appengine.api import users

import webapp2
from webapp2_extras import jinja2

from model.libro import Libro

from add import AddHandler
from edit import EditHandler
from delete import DeleteHandler

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            jinja = jinja2.get_jinja2(app=self.app)
            #libros = Libro.query().order(-Libro.fecha)
            libros = Libro.query(Libro.user == user.user_id()).order(-Libro.fecha)

            values = {
                "logout": users.create_logout_url('/'),
                "nickname": user.nickname(),
                "libros": libros
            }

            self.response.write(jinja.render_template("index.html", **values))
        else:
            jinja = jinja2.get_jinja2(app=self.app)

            values = {
                "login": users.create_login_url('/')
            }
            self.response.write(jinja.render_template("login.html", **values))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ("/add", AddHandler),
    ("/edit", EditHandler),
    ("/delete", DeleteHandler)
], debug=True)

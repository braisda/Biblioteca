import time
import datetime as dt
from datetime import datetime
from google.appengine.api import users
from google.appengine.ext import ndb

import webapp2
from webapp2_extras import jinja2

from model.libro import Libro

class DeleteHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            jinja = jinja2.get_jinja2(app=self.app)

            try:
                id = self.request.GET['id']
            except:
                id = None

            if id == None:
                self.redirect("/")
            else:
                libro = ndb.Key(urlsafe = id).get()

                values = {
                    "logout": users.create_logout_url('/'),
                    "nickname": user.nickname(),
                    "libro": libro
                }

                self.response.write(jinja.render_template("delete.html", **values))
        else:
            jinja = jinja2.get_jinja2(app=self.app)

            values = {
                "login": users.create_login_url('/')
            }
            self.response.write(jinja.render_template("login.html", **values))

    def post(self):
        id = self.request.GET['id']
        libro = ndb.Key(urlsafe = id).get()

        libro.key.delete()
        time.sleep(1)
        self.redirect("/")
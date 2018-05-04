import time
import datetime as dt
from datetime import datetime
from google.appengine.api import users
from google.appengine.ext import ndb

import webapp2
from webapp2_extras import jinja2

from model.libro import Libro

class EditHandler(webapp2.RequestHandler):
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

                self.response.write(jinja.render_template("edit.html", **values))
        else:
            jinja = jinja2.get_jinja2(app=self.app)

            values = {
                "login": users.create_login_url('/')
            }
            self.response.write(jinja.render_template("login.html", **values))

    def post(self):
        user = users.get_current_user()

        if user:
            try:
                id = self.request.GET['id']
            except:
                id = None

            if id == None:
                self.redirect("/")
            else:
                libro = ndb.Key(urlsafe = id).get()

                libro.titulo = self.request.get("titulo").strip()
                libro.autor = self.request.get("autor").strip()
                libro.genero = self.request.get("genero").strip()
                libro.opinion = self.request.get("opinion").strip()
                libro.descripcion = self.request.get("descripcion").strip()
                try:
                    libro.fecha = datetime.strptime(self.request.get("fecha").strip(), '%Y-%m-%d')
                except:
                    self.response.write("Error, ")
                libro.calificacion = self.request.get("calificacion").strip()

                if(len(libro.titulo) == 0 or len(libro.autor) == 0 or len(libro.genero) == 0 or len(libro.opinion) == 0 or len(libro.descripcion) == 0 or len(libro.calificacion) == 0):
                    self.response.write("Debes rellenar todos los datos")
                    return

                libro.put()
                time.sleep(1)
                self.redirect("/")
        else:
            jinja = jinja2.get_jinja2(app=self.app)

            values = {
                "login": users.create_login_url('/')
            }
            self.response.write(jinja.render_template("login.html", **values))
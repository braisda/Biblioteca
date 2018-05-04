import time
import datetime as dt
from datetime import datetime
from google.appengine.api import users

import webapp2
from webapp2_extras import jinja2

from model.libro import Libro

class AddHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:

            jinja = jinja2.get_jinja2(app=self.app)

            values = {
                "logout": users.create_logout_url('/')
            }

            self.response.write(jinja.render_template("add.html", **values))
        else:
            jinja = jinja2.get_jinja2(app=self.app)

            values = {
                "login": users.create_login_url('/')
            }
            self.response.write(jinja.render_template("login.html", **values))

    def post(self):
        user = users.get_current_user()

        if user:

            titulo = self.request.get("titulo", "").strip()
            autor = self.request.get("autor", "").strip()
            genero = self.request.get("genero", "").strip()
            opinion = self.request.get("opinion", "").strip()
            descripcion = self.request.get("descripcion", "").strip()
            try:
                fecha = datetime.strptime(self.request.get("fecha", "").strip(), '%Y-%m-%d')
            except:
                self.response.write("Error, ")
            calificacion = self.request.get("calificacion", "").strip()

            if(len(titulo) == 0 or len(autor) == 0 or len(genero) == 0 or len(opinion) == 0 or len(descripcion) == 0 or len(calificacion) == 0):
                self.response.write("Debes rellenar todos los datos")
                return

            libro = Libro(user=user.user_id(), titulo=titulo, autor=autor, genero=genero, opinion=opinion, descripcion=descripcion, fecha=fecha, calificacion=calificacion)
            libro.put()
            time.sleep(1)
            self.redirect("/")
        else:
            jinja = jinja2.get_jinja2(app=self.app)

            values = {
                "login": users.create_login_url('/')
            }
            self.response.write(jinja.render_template("login.html", **values))
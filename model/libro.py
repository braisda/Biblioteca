import google.appengine.ext.ndb as ndb

class Libro(ndb.Model):
    user = ndb.StringProperty(required=True)
    titulo = ndb.StringProperty()
    autor = ndb.StringProperty()
    genero = ndb.StringProperty()
    opinion = ndb.StringProperty()
    descripcion = ndb.StringProperty()
    fecha = ndb.DateProperty(auto_now_add=True, indexed=True)
    calificacion = ndb.StringProperty()
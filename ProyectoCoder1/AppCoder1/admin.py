from django.contrib import admin

from AppCoder1.models import Curso, Estudiante, Profesor, Entregable

# Register your models here.
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)

from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_title = 'Mi sitio personalizado'
    site_header = 'Mi sitio personalizado'
    index_title = 'Bienvenido al sitio personalizado'

    def index(self, request, extra_context=None):
        self.disable_action('history')
        return super().index(request, extra_context)

custom_admin_site = MyAdminSite(name='customadmin')

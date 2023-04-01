from django.urls import path, include
from AppCoder1 import views

from AppCoder1.views import curso, estudiante, base_inicio, crearCurso, busquedaNombreCurso, busquedaApellidoEstudiante, \
    profesor, busquedaProfesionProfesor

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from AppCoder1.admin import custom_admin_site

urlpatterns = [
    path('', base_inicio, name="AppCoder1Base"),
    path('busqCurso/', busquedaNombreCurso, name="AppCoderBusqCurso"),
    path('curso/', curso, name="AppCoder1Curso"),
    path("alumno/", estudiante, name="AppCoder1Alumno"),
    path("profesor/", profesor, name="AppCoder1Profesor"),
    path("busqAlumno/", busquedaApellidoEstudiante, name="AppCoder1BusqAlumno"),
    path("busqProfesion/", busquedaProfesionProfesor, name="AppCoder1BusqProfesion"),
    path("guardar/<nombre>/<idc>", crearCurso, name="AppCoder1Guardar"),
    path('admin/', custom_admin_site.urls)
]


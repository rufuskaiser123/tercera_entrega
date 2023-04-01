from django.http import HttpResponse
from datetime import datetime

from django.shortcuts import render, redirect

from AppCoder1.forms import CursoForm, BusqCursoForm, EstudianteForm, BusqEstudianteForm, ProfesorForm, BusqProfesorForm
from AppCoder1.models import Curso, Estudiante, Profesor


def busquedaNombreCurso(request):
    mi_form = BusqCursoForm(request.GET)
    if mi_form.is_valid():
        informacion = mi_form.cleaned_data
        cursos_filtrados = Curso.objects.filter(name__contains=informacion["nombre"])
        contexto = {
            "cursos": cursos_filtrados
        }
        return render(request, "pages/courses_search.html", context=contexto)


def curso(request):
    if request.method == "POST":
        mi_form = CursoForm(request.POST)
        if mi_form.is_valid():
            informacion = mi_form.cleaned_data
            curso_save = Curso(name=informacion["nombre"], idc=informacion["comision"])
            curso_save.save()
            return HttpResponse("Curso agregado.")
    all_cursos = Curso.objects.all()
    contexto = {
        "cursos": all_cursos,
        "forms": CursoForm(),
        "formsBusqCamada": BusqCursoForm,
    }
    return render(request, "pages/courses.html", context=contexto)


def crearCurso(request, nombre, idc):
    newcurso = Curso(name=nombre, idc=idc)
    newcurso.save()
    contexto = {
        "nombre": nombre,
        "idc": idc,
    }
    return render(request, "pages/add_courses.html", context=contexto)


def estudiante(request):
    if request.method == "POST":
        mi_form = EstudianteForm(request.POST)
        if mi_form.is_valid():
            informacion = mi_form.cleaned_data
            estudiante_save = Estudiante(apellido=informacion["apellido"], nombre=informacion["nombre"],
                                         email=informacion["email"])
            estudiante_save.save()
            return HttpResponse("Estudiante agregado.")

    all_estudiante = Estudiante.objects.all()
    contexto = {
        "alumnos": all_estudiante,
        "formsEstudiante":EstudianteForm(),
        "formsBusqEst":BusqEstudianteForm
    }
    return render(request, "pages/students.html", context=contexto)

def busquedaApellidoEstudiante(request):
    if request.method == "POST":
        mi_form = BusqEstudianteForm(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            estudiantes_filtrados = Estudiante.objects.filter(apellido__contains=info["apellido"])
            contexto= {
                "estudiantes":estudiantes_filtrados
            }
            return render(request, "pages/students_search.html", context=contexto)

def profesor(request):
    if request.method == "POST":
        mi_form = ProfesorForm(request.POST)
        if mi_form.is_valid():
            informacion = mi_form.cleaned_data
            profesor_save = Profesor(profesion=informacion["profesion"],apellido=informacion["apellido"], nombre=informacion["nombre"],
                                         email=informacion["email"])
            profesor_save.save()
            return HttpResponse("Profesor agregado.")


    all_profesores = Profesor.objects.all()
    contexto={
        "profesores":all_profesores,
        "formsProfesor":ProfesorForm,
        "formsBusqProf":BusqProfesorForm
    }
    return render(request, "pages/teachers.html", context=contexto)

def busquedaProfesionProfesor(request):
    if request.method == "POST":
        mi_form = BusqProfesorForm(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            profesor_filtrado = Profesor.objects.filter(profesion__icontains=info["profesion"])
            contexto= {
                "profesores":profesor_filtrado
            }
            return render(request, "pages/teachers_search.html", context=contexto)

def base_inicio(request):
    return (render(request, "home.html"))

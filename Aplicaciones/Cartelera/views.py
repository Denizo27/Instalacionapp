from django.shortcuts import redirect, render
from Aplicaciones.Cartelera.models import Director, Genero, Pais, Peliculas, Cine
from django.contrib import messages
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    return render(request, "home.html")

def listadoGeneros(request):
    # Obtener todos los géneros
    generosBdd = Genero.objects.all()

    # Preparar los datos para el gráfico de Google Charts
    chart_data = [['Nombre', 'Número de Películas']]  # Encabezados del gráfico

    # Aquí deberías contar el número de películas por género si tienes esa información
    # Ejemplo simple con conteo fijo para ilustrar:
    for genero in generosBdd:
        # Reemplaza '5' con el conteo real de películas por género si tienes esa información
        chart_data.append([genero.nombre, 5])  

    # Pasar los datos a la plantilla
    context = {
        'generos': generosBdd,
        'chart_data': chart_data
    }
    
    return render(request, 'listadoGeneros.html', context)

def listadoDirectores(request):
    # Obtén todos los directores
    directoresBdd = Director.objects.all()
    
    # Contar directores activos e inactivos
    num_activos = Director.objects.filter(estado=True).count()
    num_inactivos = Director.objects.filter(estado=False).count()
    
    # Datos para el gráfico de Google Charts
    chart_data = [
        ['Estado', 'Cantidad'],
        ['Activos', num_activos],
        ['Inactivos', num_inactivos]
    ]
    
    return render(request, "listadoDirectores.html", {
        'directores': directoresBdd,  # Nota: Debe ser 'directores' en lugar de 'director'
        'chart_data': chart_data
    })

def listadoPaises(request):
    paisesBdd = Pais.objects.all()
    return render(request, "listadoPaises.html", {'pais': paisesBdd})

def listadoPeliculas(request):
    peliculasBdd = Peliculas.objects.all()
    return render(request, "listadoPeliculas.html", {'pelicula': peliculasBdd})

def eliminarGenero(request, id):
    generoEliminar = Genero.objects.get(id=id)
    generoEliminar.delete()
    messages.success(request, "Genero eliminado existosamente.")
    return redirect('listadoGeneros')

def nuevoGenero(request):
    return render(request, 'nuevoGenero.html')

def guardarGenero(request):
    nom = request.POST["nombre"]
    des = request.POST["descripcion"]
    fot = request.FILES.get("foto")
    nuevoGenero = Genero.objects.create(nombre=nom, descripcion=des, foto=fot)
    messages.success(request, "Genero Guardado existosamente.")
    return redirect('listadoGeneros')

def editarGenero(request, id):
    generoEditar = Genero.objects.get(id=id)
    return render(request, 'editarGenero.html', {'generoEditar': generoEditar})

def procesarActualizacionGenero(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    generoConsultado = Genero.objects.get(id=id)
    generoConsultado.nombre = nombre
    generoConsultado.descripcion = descripcion
    generoConsultado.save()
    messages.success(request, 'Genero actualizado exitosamente')
    return redirect('listadoGeneros')

def eliminarDirector(request, id):
    directorEliminar = Director.objects.get(id=id)
    directorEliminar.delete()
    messages.success(request, "Director eliminado existosamente.")
    return redirect('listadoDirectores')

def editarDirector(request, id):
    directorEditar = Director.objects.get(id=id)
    return render(request, 'editarDirector.html', {'directorEditar': directorEditar})

def procesarActualizacionDirector(request):
    id = request.POST['id']
    dni = request.POST['dni']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    estado = request.POST['estado']
    directorConsultado = Director.objects.get(id=id)
    directorConsultado.dni = dni
    directorConsultado.nombre = nombre
    directorConsultado.apellido = apellido
    directorConsultado.estado = estado
    directorConsultado.save()
    messages.success(request, 'Director actualizado exitosamente')
    return redirect('listadoDirectores')

def guardarDirector(request):
    dni = request.POST["dni"]
    apellido = request.POST["apellido"]
    nombre = request.POST["nombre"]
    estado = request.POST["estado"] == "True"
    fot = request.FILES.get("foto")
    nuevoDirector = Director.objects.create(dni=dni, apellido=apellido, nombre=nombre, estado=estado, foto=fot)
    messages.success(request, "Director registrado exitosamente.")
    return redirect('listadoDirectores')

def nuevoDirector(request):
    return render(request, 'nuevoDirector.html')

def gestionCines(request):
    return render(request, "gestionCines.html")

@csrf_exempt
def guardarCine(request):
    if request.method == 'POST':
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body)
            else:
                data = request.POST
                
            if isinstance(data, list):
                respuesta = []
                for cine_data in data:
                    nom = cine_data.get("nombre")
                    dir = cine_data.get("direccion")
                    tel = cine_data.get("telefono")
                    nuevoCine = Cine.objects.create(nombre=nom, direccion=dir, telefono=tel)
                    respuesta.append({
                        'estado': True,
                        'mensaje': 'Cine registrado exitosamente.',
                        'cine': nuevoCine.id
                    })
                return JsonResponse(respuesta, safe=False)
            else:
                nom = data.get("nombre")
                dir = data.get("direccion")
                tel = data.get("telefono")
                nuevoCine = Cine.objects.create(nombre=nom, direccion=dir, telefono=tel)
                return JsonResponse({
                    'estado': True,
                    'mensaje': 'Cine registrado exitosamente.',
                    'cine': nuevoCine.id
                })
        except json.JSONDecodeError:
            return JsonResponse({
                'estado': False,
                'mensaje': 'JSON inválido.'
            })
    elif request.method == 'GET':
        cines = Cine.objects.all()
        cines_json = serializers.serialize('json', cines)
        return JsonResponse(cines_json, safe=False)
    else:
        return JsonResponse({
            'estado': False,
            'mensaje': 'Método no permitido.'
        })

def listadoCines(request):
    cines=Cine.objects.all()
    return render(request,"listadoCines.html",{'cines':cines})

def chartview(request):
    # Aquí es donde deberías pasar los datos necesarios para el gráfico
    context = {
        'chart_data': [
            ['Year', 'Sales', 'Expenses'],
            ['2013', 1000, 400],
            ['2014', 1170, 460],
            ['2015', 660, 1120],
            ['2016', 1030, 540]
        ]
    }
    return render(request, 'chart.html', context)
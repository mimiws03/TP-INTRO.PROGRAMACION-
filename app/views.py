# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services.services import getAllImages
from .layers.services.services import filterByHouse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .layers.services.services import saveFavourite as saveFavouriteadd
from .layers.services.services import deleteFavourite as deleteFavouriteservice
from .layers.services.services import getAllFavourites


def index_page(request):
    return render(request, 'index.html')



#----------------------------- COMPLETADO ------------------------------------
#INICIO. ---------------------------------------------------------------------
# esta función obtiene 2 listados: uno de las imágenes de la API y otro de favoritos, ambos en formato Card, y los dibuja en el template 'home.html'.
def home(request):
    images = getAllImages()
    favourite_list = [] #PREGUNTAR COMO HACER ESTO !!! 

    return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })
#FIN. ---------------------------------------------------------------------



# función utilizada en el buscador.
def search(request):
    name = request.POST.get('query', '')

    # si el usuario ingresó algo en el buscador, se deben filtrar las imágenes por dicho ingreso.
    if (name != ''):
        images = []
        favourite_list = []

        return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })
    else:
        return redirect('home')


#----------------------------- COMPLETADO ------------------------------------
#INICIO. ---------------------------------------------------------------------
# función utilizada para filtrar por casa Gryffindor o Slytherin.
def filter_by_house(request):
    house = request.POST.get('house', '')

    if house:
        images = filterByHouse(house) # debe traer un listado filtrado de imágenes, según la casa.
        favourite_list = []

        return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })
    else:
        return redirect('home')
#FIN. ---------------------------------------------------------------------



# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    pass

@login_required
def saveFavourite(request):
    saveFavouriteadd(request)
    return redirect('home')

@login_required
def deleteFavourite(request):
    deleteFavouriteservice(request)
    return redirect('home')

@login_required
def exit(request):
    logout(request)
    return redirect('home')
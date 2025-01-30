# capa de servicio/lógica de negocio

from ..transport.transport import getAllImages as getAllImagesTransport
from ..persistence import repositories
from ..utilities.translator import fromRequestIntoCard as fromRequestIntoCardTranslator
from django.contrib.auth import get_user
import random

# función que devuelve un listado de cards. Cada card representa una imagen de la API de HP.
def getAllImages():
    raw_images=getAllImagesTransport()
    cards=[]

    for personaje in raw_images:
        card=fromRequestIntoCardTranslator(personaje)
        if isinstance(card.alternate_names, list) and card.alternate_names:
            card.alternate_names = random.choice(card.alternate_names)  
        else:
            card.alternate_names = f"{card.name} (sin nombres alternativos)"
        print(f"Personaje: {card.name}, Nombres alternativos: {card.alternate_names}")
        cards.append(card)
    return cards
    # debe ejecutar los siguientes pasos:
    # 1) traer un listado de imágenes crudas desde la API (ver transport.py)
    # 2) convertir cada img. en una card.
    # 3) añadirlas a un nuevo listado que, finalmente, se retornará con todas las card encontradas.
    # ATENCIÓN: contemplar que los nombres alternativos, para cada personaje, deben elegirse al azar. Si no existen nombres alternativos, debe mostrar un mensaje adecuado.
    
    pass

# función que filtra según el nombre del personaje.
def filterByCharacter(name):
    filtered_cards = []

    for card in getAllImages():
        # debe verificar si el name está contenido en el nombre de la card, antes de agregarlo al listado de filtered_cards.
        filtered_cards.append(card)

    return filtered_cards

# función que filtra las cards según su casa.
def filterByHouse(house_name):
    filtered_cards = [] 
    for card in getAllImages():  # Obtener todas las imágenes
        if card.house and card.house.lower() == house_name.lower():  
            # Si la casa del personaje coincide con la seleccionada, se añade a la lista
            filtered_cards.append(card)

    return filtered_cards 

# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    fav = '' # transformamos un request en una Card (ver translator.py)
    fav.user = get_user(request) # le asignamos el usuario correspondiente.

    return repositories.save_favourite(fav) # lo guardamos en la BD.

# usados desde el template 'favourites.html'
def getAllFavourites(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)

        favourite_list = [] # buscamos desde el repositories.py TODOS Los favoritos del usuario (variable 'user').
        mapped_favourites = []

        for favourite in favourite_list:
            card = '' # convertimos cada favorito en una Card, y lo almacenamos en el listado de mapped_favourites que luego se retorna.
            mapped_favourites.append(card)

        return mapped_favourites

def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.delete_favourite(favId) # borramos un favorito por su ID
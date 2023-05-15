"""
Archivo de funciones usadas en el proyecto de visualización de la bootcamp
de Data Analytics de IRONHACK de Abril - 2023
"""
import time
import requests as rq
from .password import *


def get_coordinates(x):
    """
    Función que dada una query, se envía la query a google maps, y recoge
    la información de latitud y logintud

    """
    global API_KEY_GOOGLE
    address = x.replace(' ', '%20')
    url = f'https://maps.googleapis.com/maps/api/geocode/json?\
            address={address}&key={API_KEY_GOOGLE}'
    try:
        response = rq.get(url)
        lat, long = response.json(
        )['results'][0]['geometry']['location'].values()
        country = response.json(
        )['results'][0]['address_components'][-2]['long_name']
        return {'Coordenadas': {'Latitud': lat,
                                'Longitud': long}}
    except:
        return {'Coordenadas': {'Latitud': None,
                                'Longitud': None}}


def get_top_10_tracks(art_url, headers):  # recibe diccionario key:artista

    # Pausamos el tiempo entre consultas. Evitamos que nos baneen
    time.sleep(0.20)
    temp_lst = []
    try:
        response = rq.get(art_url['url'], headers=headers)
    except:
        temp_dict['artist'] = None
        temp_dict['name'] = None
        temp_dict['track_id'] = None
        temp_dict['popularity'] = None
        temp_dict['href'] = None
        temp_dict['album '] = None
        temp_dict['album_id'] = None
        temp_dict['album_href'] = None
        temp_dict['release_date'] = None

    tracks = response.json()['tracks']  # Lista con el top 10 de tracks

    for track in tracks:
        temp_dict = dict()
        temp_dict['artist'] = art_url['artist']
        temp_dict['name'] = track['name']
        temp_dict['track_id'] = track['id']
        temp_dict['popularity'] = track['popularity']
        temp_dict['href'] = track['href']
        temp_dict['album '] = track['album']['name']
        temp_dict['album_id'] = track['album']['id']
        temp_dict['album_href'] = track['album']['href']
        temp_dict['release_date'] = track['album']['release_date']
        temp_lst.append(temp_dict)
    return temp_lst


def get_audio_feautures(lst_tracks, headers):  # recibe diccionario key:artista

    # Pausamos el tiempo entre consultas. Evitamos que nos baneen
    time.sleep(0.11)
    lst_id = '%2'.join(lst_tracks)
    url = f'https://api.spotify.com/v1/audio-features?ids={lst_id}'

    response = rq.get(url, headers)
    return response.json()


def get_audio_analysis(track_id, headers):  # recibe diccionario key:artista

    # Pausamos el tiempo entre consultas. Evitamos que nos baneen
    time.sleep(0.11)
    url = f'https://api.spotify.com/v1/audio-analysis/{track_id}'

    response = rq.get(url, headers)
    return response.json()

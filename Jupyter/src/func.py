"""
Archivo de funciones usadas en el proyecto de visualización de la bootcamp
de Data Analytics de IRONHACK de Abril - 2023
"""
import time
import requests as rq


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

def def get_audio_analysis(track_id, headers):  # recibe diccionario key:artista

    # Pausamos el tiempo entre consultas. Evitamos que nos baneen
    time.sleep(0.11)
    url = f'https://api.spotify.com/v1/audio-analysis/{track_id}'

    response = rq.get(url, headers)
    return response.json()
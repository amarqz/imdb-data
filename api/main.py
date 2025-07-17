import docker
from db import *
from fastapi import FastAPI, HTTPException
from models import *

app = FastAPI()

@app.get('/checkdata')
def check_data():
    return check_last_uploaded_data()

@app.post('/updatedata')
def update_data():
    last_uploaded_data: DataControl = check_last_uploaded_data()

    if last_uploaded_data:
        if last_uploaded_data.status == 'ON':
            raise HTTPException(409, 'Another update process is already running.')
        
        if last_uploaded_data.uploadDate.date() == datetime.now().date():
            raise HTTPException(403, 'Data was updated within the last 24 hours.')

    client = docker.from_env()
    try:
        container = client.containers.run(
            'imdb_ingestion',
            name='imdb_ingestion',
            detach=True,
            remove=True,
            network='imdb'
        )

        return {'status': 'Started', "container_id": container.id}
    except docker.errors.APIError as e:
        raise HTTPException(500, str(e))

@app.get('/person/{id}')
def get_name_by_id(id: str):
    person_name = get_person_name_by_id(id)
    if not person_name:
        raise HTTPException(404, 'Not found!')
    return person_name

@app.get('/person')
def get_person(name: str, role: str):
    person = get_person_info(name, role)
    if not person:
        raise HTTPException(404, 'Not found!')
    return person

@app.get('/principals/{id}')
def get_principals_from_title(id: str, order: int):
    principal = get_principals_info_from_title_and_order(id, order)
    if not principal:
        raise HTTPException(404, 'Not found!')
    return principal

@app.get('/rating/{id}')
def get_rating(id: str):
    rating_info = get_title_rating_info(id)
    if not rating_info:
        raise HTTPException(404, 'Not found!')
    return rating_info

@app.get('/title/{id}')
def get_title_by_id(id: str):
    title_name = get_title_name_by_id(id)
    if not title_name:
        raise HTTPException(404, 'Not found!')
    return title_name

@app.get('/title')
def get_title(name: str, kind: str):
    title = get_title_info(name, kind)
    if not title:
        raise HTTPException(404, 'Not found!')
    return title
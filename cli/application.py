from datetime import datetime
from dotenv import load_dotenv
from rich.console import Console
from typing import List
from utils import cmd_info
import os
import requests
import typer

load_dotenv()
app = typer.Typer()
console = Console()

@app.command()
def check():
    response = api_request('GET', 'checkdata')
    if not response:
        return

    if response.json()['status'] == 'NC':
        console.print('[bold orange1]WARNING! [/bold orange1] It seems this is the first use of the application. The database structure has been created.')
        console.print('[bold orange1]WARNING! [/bold orange1] Additionally, a data ingestion process has been summoned. It will take a few hours.')
        update()
        return
    
    if datetime.strptime(response.json()['uploadDate'], "%Y-%m-%dT%H:%M:%S.%f").date() < datetime.now().date():
        console.print('[bold orange1]WARNING! [/bold orange1] The database has not been updated today. Please, run the command [dark_sea_green4]update[/dark_sea_green4] to update it with the latest data.')
        console.print('Please, keep in mind that the update process will last a few hours. Until then, the served data will be the last loaded version.')

@app.command()
def help():
    for command in cmd_info:
        console.print('[bold yellow]{0:40}[/bold yellow]  {1}'.format(command['name'], command['explanation']))

@app.command()
def person(role: str, name: List[str]):
    response = api_request('GET', 'person', role=role, name=' '.join(name))
    if not response:
        return

    response = response.json()
    primaryTitles: List[str] = []
    for title in response['knownForTitles'].split(','):
        primaryTitles.append(api_request('GET', f'title/{title}').json())

    formatted_response = f'{response['primaryName']}{'' if not response['birthYear'] else f' (born in {response['birthYear']})'} is a {response['primaryProfession'].replace(',', ', ')}{'' if not primaryTitles else '. Known for working on titles such as '}{', '.join(primaryTitles)}.'
    console.print('[bold dark_sea_green4]RESULT:[/bold dark_sea_green4]', formatted_response)

@app.command()
def title(kind: str, name: List[str]):
    response = api_request('GET', 'title', kind=kind, name=' '.join(name))
    if not response:
        return
    
    response = response.json()
    rating = api_request('GET', f'rating/{response['tconst']}').json()

    principals = ''
    for order in range(1, 4):
        principal = api_request('GET', f'principals/{response['tconst']}', order=order).json()
        principal_name = api_request('GET', f'person/{principal['nconst']}').json()
        principals += f', {principal_name} (as {principal['characters'].split('"')[1]})'
    principals = principals[1:] + '.'

    formatted_response = f"{response['primaryTitle']}, originally titled '{response['originalTitle']}', is a {response['genres'].replace(',', ', ')}. It is rated with a score of {rating['averageRating']} ({rating['numVotes']} votes)."
    console.print('[bold dark_sea_green4]RESULT:[/bold dark_sea_green4]', formatted_response)
    console.print('Some of the principals in this title are the following:', principals)

@app.command()
def update():
    response = api_request('POST', 'updatedata')
    if not response:
        return
    
    if response['status'] == 'Started':
        console.print('Data update process started! It will take a few hours, thank you for your patience.')
        console.print(f'container_id: [i]{response['container_id']}[/i]')


def api_request(verb: str, endpoint: str, **params) -> requests.Response | None:
    if verb == 'GET':
        response = requests.get(url=f'http://{os.getenv("API_HOST")}:{os.getenv("API_PORT")}/{endpoint}', params=params)
    elif verb == 'POST':
        response = requests.post(url=f'http://{os.getenv("API_HOST")}:{os.getenv("API_PORT")}/{endpoint}', params=params)

    if response.status_code != 200:
        print_error(response)
        return None
    return response


def print_error(response: requests.Response) -> None:
    console.print(f'[bold bright_red]ERROR {response.status_code}: [/bold bright_red][deep_pink2]{response.json()['detail']}[/deep_pink2]')
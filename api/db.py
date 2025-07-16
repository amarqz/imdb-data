import os
from dotenv import load_dotenv
from models import *
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlmodel import Session, select

load_dotenv()

db_url = URL.create(
    os.getenv("DB_KIND"),
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=f"{os.getenv("DB_HOST")}",
    database=os.getenv("DB_NAME")
)

engine = create_engine(db_url)

def check_last_uploaded_data() -> DataControl:
    with Session(engine) as session:
        statement = select(DataControl).order_by(DataControl.uploadDate.desc())
        last_upload: DataControl = session.exec(statement).first()
    return last_upload

def get_person_name_by_id(id: str) -> ProNameBasics:
    with Session(engine) as session:
        statement = select(ProNameBasics).where(ProNameBasics.nconst == id)
        person_match: ProNameBasics = session.exec(statement).first()
    return person_match.primaryName

def get_person_info(name: str, role: str) -> ProNameBasics:
    with Session(engine) as session:
        statement = select(ProNameBasics).where((ProNameBasics.primaryName.ilike(f'{name}%')) & ProNameBasics.primaryProfession.ilike(f'%{role}%')).order_by(ProNameBasics.nconst)
        person_match: ProNameBasics = session.exec(statement).first()
    return person_match

def get_principals_info_from_title_and_order(id: str, order: int) -> ProTitlePrincipals:
    with Session(engine) as session:
        statement = select(ProTitlePrincipals).where((ProTitlePrincipals.tconst == id) & (ProTitlePrincipals.ordering == order))
        principal_match: ProTitlePrincipals = session.exec(statement).first()
    return principal_match

def get_title_info(name: str, kind: str) -> ProTitleBasics:
    with Session(engine) as session:
        statement = select(ProTitleBasics).where((ProTitleBasics.primaryTitle.ilike(f'%{name}%')) & ProTitleBasics.titleType.ilike(f'%{kind}%')).order_by(ProTitleBasics.tconst)
        title_match: ProTitleBasics = session.exec(statement).first()
    return title_match

def get_title_name_by_id(id: str) -> str:
    with Session(engine) as session:
        statement = select(ProTitleBasics).where(ProTitleBasics.tconst == id)
        title_match: ProTitleBasics = session.exec(statement).first()
    return title_match.primaryTitle

def get_title_rating_info(id: str) -> str:
    with Session(engine) as session:
        statement = select(ProTitleRatings).where((ProTitleRatings.tconst == id))
        title_match: ProTitleRatings = session.exec(statement).first()
    return title_match
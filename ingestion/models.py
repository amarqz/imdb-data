from datetime import datetime
from sqlmodel import Field, SQLModel

class TitleAkas(SQLModel, table=True):
    titleId: str | None = Field(primary_key=True)
    ordering: int | None = Field(primary_key=True)
    title: str | None
    region: str | None
    language: str | None
    types: str | None
    attributes: str | None
    isOriginalTytle: int | None = Field(max_digits=1)

class TitleBasics(SQLModel, table=True):
    tconst: str | None = Field(primary_key=True)
    titleType: str | None
    primaryTitle: str | None
    originalTitle: str | None
    isAdult: int | None = Field(max_digits=1)
    startYear: int | None = Field(max_digits=4)
    endYear: int | None = Field(max_digits=4)
    runtimeMinutes: int | None = Field(max_digits=4)
    genres: str | None

class TitleCrew(SQLModel, table=True):
    tconst: str | None = Field(primary_key=True)
    directors: str | None
    writers: str | None

class TitleEpisode(SQLModel, table=True):
    tconst: str | None= Field(primary_key=True)
    parentTconst: str | None
    seasonNumber: int | None = Field(max_digits=3)
    episodeNumber: int | None = Field(max_digits=3)

class TitlePrincipals(SQLModel, table=True):
    tconst: str | None = Field(primary_key=True)
    ordering: int | None = Field(primary_key=True)
    nconst: str | None
    category: str | None
    job: str | None
    characters: str | None

class TitleRatings(SQLModel, table=True):
    tconst: str | None = Field(primary_key=True)
    averageRating: float | None = Field(max_digits=2, decimal_places=1)
    numVotes: int | None = Field(max_digits=8)

class NameBasics(SQLModel, table=True):
    nconst: str | None = Field(primary_key=True)
    primaryName: str | None
    birthYear: int | None = Field(max_digits=4)
    deathYear: int | None = Field(max_digits=4)
    primaryProfession: str | None
    knownForTitles: str | None

class DataControl(SQLModel, table=True):
    uploadDate: datetime = Field(primary_key=True, default_factory=lambda: datetime.now())
    status: str = Field(max_length=2)

file_class_map = {
    'name.basics.tsv': NameBasics,
    'title.akas.tsv': TitleAkas,
    'title.basics.tsv': TitleBasics,
    'title.crew.tsv': TitleCrew,
    'title.episode.tsv': TitleEpisode,
    'title.principals.tsv': TitlePrincipals,
    'title.ratings.tsv': TitleRatings
}

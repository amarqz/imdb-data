from datetime import datetime
from sqlmodel import Field, SQLModel

class TitleAkas(SQLModel):
    titleId: str | None = Field(primary_key=True)
    ordering: int | None = Field(primary_key=True)
    title: str | None
    region: str | None
    language: str | None
    types: str | None
    attributes: str | None
    isOriginalTytle: int | None = Field(max_digits=1)

class StgTitleAkas(TitleAkas, table=True):
    __tablename__ = 'titleakas'

class ProTitleAkas(TitleAkas, table=True):
    __tablename__ = 'pro_titleakas'

class TitleBasics(SQLModel):
    tconst: str | None = Field(primary_key=True)
    titleType: str | None
    primaryTitle: str | None
    originalTitle: str | None
    isAdult: int | None = Field(max_digits=1)
    startYear: int | None = Field(max_digits=4)
    endYear: int | None = Field(max_digits=4)
    runtimeMinutes: int | None = Field(max_digits=4)
    genres: str | None

class StgTitleBasics(TitleBasics, table=True):
    __tablename__ = 'titlebasics'

class ProTitleBasics(TitleBasics, table=True):
    __tablename__ = 'pro_titlebasics'

class TitleCrew(SQLModel):
    tconst: str | None = Field(primary_key=True)
    directors: str | None
    writers: str | None

class StgTitleCrew(TitleCrew, table=True):
    __tablename__ = 'titlecrew'

class ProTitleCrew(TitleCrew, table=True):
    __tablename__ = 'pro_titlecrew'

class TitleEpisode(SQLModel):
    tconst: str | None= Field(primary_key=True)
    parentTconst: str | None
    seasonNumber: int | None = Field(max_digits=3)
    episodeNumber: int | None = Field(max_digits=3)

class StgTitleEpisode(TitleEpisode, table=True):
    __tablename__ = 'titleepisode'

class ProTitleEpisode(TitleEpisode, table=True):
    __tablename__ = 'pro_titleepisode'

class TitlePrincipals(SQLModel):
    tconst: str | None = Field(primary_key=True)
    ordering: int | None = Field(primary_key=True)
    nconst: str | None
    category: str | None
    job: str | None
    characters: str | None

class StgTitlePrincipals(TitlePrincipals, table=True):
    __tablename__ = 'titleprincipals'

class ProTitlePrincipals(TitlePrincipals, table=True):
    __tablename__ = 'pro_titleprincipals'

class TitleRatings(SQLModel):
    tconst: str | None = Field(primary_key=True)
    averageRating: float | None = Field(max_digits=2, decimal_places=1)
    numVotes: int | None = Field(max_digits=8)

class StgTitleRatings(TitleRatings, table=True):
    __tablename__ = 'titleratings'

class ProTitleRatings(TitleRatings, table=True):
    __tablename__ = 'pro_titleratings'

class NameBasics(SQLModel):
    nconst: str | None = Field(primary_key=True)
    primaryName: str | None
    birthYear: int | None = Field(max_digits=4)
    deathYear: int | None = Field(max_digits=4)
    primaryProfession: str | None
    knownForTitles: str | None

class StgNameBasics(NameBasics, table=True):
    __tablename__ = 'namebasics'

class ProNameBasics(NameBasics, table=True):
    __tablename__ = 'pro_namebasics'

class DataControl(SQLModel, table=True):
    uploadDate: datetime = Field(primary_key=True, default_factory=lambda: datetime.now())
    status: str = Field(max_length=2)
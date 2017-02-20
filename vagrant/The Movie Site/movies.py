from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Movie

engine = create_engine('sqlite:///movies.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Genre Codes
# 1000000 = None
# 1000001 = Drama
# 1000010 = Comedy
# 1000100 = Thriller
# 1001000 = Action
# 1010000 = Horror
# 1100000 = Animation


# Movie Items
movie1 = Movie(name="Forrest Gump",
    year="1994",
    poster="https://images-na.ssl-images-amazon.com/images/M/MV5BYThjM2MwZGMtMzg3Ny00NGRkLWE4M2EtYTBiNWMzOTY0YTI4XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,757,1000_AL_.jpg",
    description="Bubba Gump Shrimp",
    trailer="https://www.youtube.com/watch?v=bLvqoHBptjg",
    genre="1000001")
session.add(movie1)
session.commit()

movie2 = Movie(name="Apollo 13",
    year="1995",
    poster="https://images-na.ssl-images-amazon.com/images/M/MV5BMmIyM2Y2NTQtZWM4ZC00YjFjLWFhMjgtNzNkOTQ0OGZlMTNhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY999_CR0,0,673,999_AL_.jpg",
    description="Houston, we have a problem.",
    trailer="https://www.youtube.com/watch?v=nEl0NsYn1fU",
    genre="1000101")
session.add(movie2)
session.commit()

movie3 = Movie(name="Saving Private Ryan",
    year="1998",
    poster="https://images-na.ssl-images-amazon.com/images/M/MV5BZjhkMDM4MWItZTVjOC00ZDRhLThmYTAtM2I5NzBmNmNlMzI1XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,679,1000_AL_.jpg",
    description="Tom Hanks saves Europe.",
    trailer="https://www.youtube.com/watch?v=zwhP5b4tD6g",
    genre="1001001")
session.add(movie3)
session.commit()

print "added movies!"
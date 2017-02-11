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
movie1 = Movie(name="Forest Gump", year="1994", poster="here", genre="1000001")
session.add(movie1)
session.commit()

print "added movies!"
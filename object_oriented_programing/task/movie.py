"""
Movie title,language,year,director,genre 
    -setmovie(title,language,year,director,genre)
    -getmovie(self)
"""

class Movie:

    title:str

    language:str

    year:int

    director:str

    genre:str

    def __init__(self,title,language,year,director,genre):

        self.title = title

        self.language = language

        self.year = year

        self.director = director

        self.genre = genre

    def get_back(self):

        print(self,self.title,self.language,self.year,self.director,self.genre)

bazooka_instant = Movie("Bazooka","Malayalam",2025,"Unkown","Action")            
bazooka_instant.get_back()
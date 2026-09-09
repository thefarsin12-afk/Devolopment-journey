class Movie_data:

    def __init__(self):

        self.movies = [

            {"id":1,"title":"Jhon wick","genre":"action","rating":8,"run_time":130,"director":"jhons"}
    
        ]

    def post(self,**kwargs):

        requirement_field = {"id","title","genre","rating","run_time","director"}

        missing_fields = requirement_field.difference(kwargs)

        if missing_fields:

            raise ValueError(missing_fields,"Is missing")

        else:
            self.movies.append(kwargs)
            print("Movie has been added")


    def get(self):

        if len(self.movies)==0:
            print("Movie Note Found")

        else:
            for m in self.movies:
                print(m)    

    def retrive(self,id=None):

        if not id:
            raise ValueError ("id missing...")

        else:
            details = [m for m in self.movies if m.get("id")==id][0]
            print(details)
                 

    def put(self,id=None,**kwargs):

        movie = [m for m in self.movies if m.get("id")==id][0]

        movie.update(kwargs)
        print("Movie updated")
        print(movie)

    def delete(self,id=None):    

        movie_remove = [m for m in self.movies if m.get("id")== id][0]

        self.movies.remove(movie_remove)
        print("Movie has been removed")
        self.get()


movie_instant = Movie_data()
movie_instant.post(id=2,title="bheeshma",genre="action",rating=8,run_time=150,director="amal neerad")
movie_instant.post(id=3,title="obsession",genre="thriller",rating=8,run_time=140,director="amal neerad")
movie_instant.get()
movie_instant.put(id=1 ,rating= 10,run_time = 120)
movie_instant.delete(id=2)



        
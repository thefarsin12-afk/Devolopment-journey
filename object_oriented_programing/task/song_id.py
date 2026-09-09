"""
Song  id,moviename,title,trackno,singer,duration
        -setsong(id,moviename,title,trackno,singer,duration)
        -getsong()
"""

class Song_id:

    id = int

    movie_name = str

    title = str

    track_no = int

    singer = str

    duration = float

    def __init__(self,id,movie_name,title,track_no,singer,duration):

        self.id = id

        self.movie_name = movie_name

        self.title = title

        self.track_no = track_no

        self.singer = singer

        self.duration = duration

    def get_back(self):

        print(self,self.id,self.movie_name,self.title,self.track_no,self.singer,self.duration) 

malare = Song_id(2331,"Premam","Malare",3214,"unkown",3.20)
malare.get_back()
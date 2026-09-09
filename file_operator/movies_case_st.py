fr = open("file_operator\\movie_1.csv","r",encoding="UTF-8")

movies = []

for line in fr:

    line = line.rstrip("\n")

    id,title,language,year,run_time,rating,genre = line.split(",")
    
    movie_details = {

          "id":"id",
          "title":"title",
          "language":"language",
          "year":"year",
          "run_time":"run_time",
          "rating":"rating",
          "genre":"genre"
    }

    movies.append(movie_details)

print(len(movies))

movies = [

    ["kgf","kannada",150,2005,8],
    ["balan","malayalam",130,2026,7],
    ["ramayan","hindi",150,2026,8.5],
    ["abcd","malayalam",140,2008,6],
    ["goatlife","malayalam",160,2024,9]
]

#abcd movie duration,year,rating
print(movies[3][2:])

reslut = [m [0] for m in movies]
print (reslut)

#display all movies year
all_years = [m [-2]for m in movies]

all_langusages = [m [1]for m in movies]

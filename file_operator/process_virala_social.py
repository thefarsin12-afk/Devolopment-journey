from csv import DictReader

fr = open("file_operator\\Cleaned_Viral_Social_Media_Trends.csv","r",encoding="UTF-8")

viral_post = list(DictReader(fr))

"""unique_platforms = {p.get("Platform") for p in viral_post}

print(unique_platforms)

t = 0
for p in viral_post:

    if p.get("Region") == "India":

     t += int(p.get("Views"))

print(t)     """

platform_views = {}

for p in viral_post:

    platform = p.get("Platform")

    views = int(p.get("Views"))

    if platform not in platform_views:

        platform_views[platform] = 0

    else:
        platform_views[platform] += views 

highest = max(platform_views, key= lambda p:platform_views[p])

print(highest)
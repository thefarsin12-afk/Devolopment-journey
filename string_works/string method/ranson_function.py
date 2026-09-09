def is_ranson(note,magazine):

    magazine = "chicken"

    for chara in note:
        if chara not in magazine:
            print(False)
            break

    else:print(True)

is_ranson("ken","chicken")        

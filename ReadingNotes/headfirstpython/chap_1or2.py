# -*- coding: utf-8 -*-
"""
Learning python.
date:2017-3-27.
Reference:<Head First Python>
"""
 
movies=["The Holy Grail","The Life of Brian",
        "The Meaning of Life"]
print(movies)
cast=["cleese","palin",'Jones',
      "Idle"]
print(len(cast))
print(cast[1])
"append: insert behind"
cast.append("Gilliam")
print(cast)
"""take out the last one"""
cast.pop()
print(cast)
""" insert with another list"""
cast.extend(["Gilliam","Chapman"])
print(cast)
"""remove"""
cast.remove("Gilliam")
print(cast)
"""insert at any place"""
cast.insert(0,"Gilliam")
print(cast)

movies=["the holy grail","the life of brian","the meaning of life"]
movies.insert(1,1975)
movies.insert(3,1979)
movies.append(1983)
print(movies)

movies=["the holy grail",1975,"the life of brian",1979,"the meaning of life",1983]
print(movies)

fav_movies=["The holy grail","The life of brian"]
for each_item in fav_movies:
    print(each_item)
movies=[
        "the holy grail",1975,"Terry Jones & Terry Gilliam",91,
        ["Graham Chapman",
         ["Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]]]
print(movies)
"""index"""
print(movies[4][1][3])
for each_item in movies:
    print(each_item)

    
names=['Michael','Terry']
"""check for type"""
isinstance(names,list)
num_names=len(names)
isinstance(num_names,list)

for each_item in movies:
    if isinstance(each_item,list):
        for each_entry in each_item:
            if isinstance(each_entry,list):
                for deeper_item in each_entry:
                    print(deeper_item)
            else:
                print(each_entry)
    else:
        print(each_item)

"""a function for printing all the movies' names even if it is in a list of list"""
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)

print_lol(movies)        

for num in range(4):
    print(num)
    
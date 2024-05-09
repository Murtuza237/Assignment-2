#lists operations
l1=[1,2,3,4,5,6]
l2=[]
#adding values using insert(),append() and extend()
l1.insert(6,9)
l1.append(6)
print(l1)
l2.extend([8,9,10])
print(l2) 
#reversing the list using reverse()
l1.reverse()
print(l1)
#removing values using pop() and remove()
l1.pop()
print(l1)
l1.remove(5)
print(l1)
#sorting the list using sort()
l1.sort()
print(l1)
#acccessing index of a value in a list using .index()
print(l1.index(6))
#creating a copy of list1 and storing it in list2
l2=l1.copy()
print(l2)
#counting repeated values using count()
print(l1.count(6))
#adding two lists into one list
l3=l1+l2
print(l3)
#adding to sliced list into one list
l4=l1[:4]+l2[4:8]
print(l4)
#tuple opertions
t1=(1,2,3,4,5,5,5,6,7,7)
t2=(3,4,5,6)
#counting repeated values using count()
print(t1.count(6))
#adding two tuples into one tuple
t3=t1+t2
print(t3)

print(t1.index(5))
print(t1.count(5))
t4=t1*2
print(t4)
#dictionory operations
#creating a dictinory namely dic 
dic={}
#adding values to dic
dic["name"]="Murtuza Ali"
dic["enrollmentno."]="AU23B1027"
dic["year"]="1st Year"
dic["course"]="Btech"
print(dic)
#accessing values using keys
print(dic["name"])
print(dic["enrollmentno."])
print(dic["course"])
print(dic["year"])
print(dic.keys())
print(dic.values())
#removing  values by key using pop() and popitems()
dic.pop("year")
print(dic)
dic.popitem()
print(dic)

#using list Tuples and dictionary together
#case1-here a list namely cafe is used to store mulitple dictionary containing what itema are there for order in form of tuples and lists
cafe=[{("ice cream"):["butterscotch","mango","orange","pineapple"],
       ("shakes"):["mango shake","pineapple shake","strawberry shake"]},
       {("fast food"):["pizza","burger","french fries","maggi","pasta"],
        ("drinks"):["coca cola","7up","sprit"]}]






#scenrio-> using list tuples and dictionaries to create a longitutude and latitiude finding program
earth={("india"):["latitudes:8° 4'N and 37° 6N","longitudes: 68° 7'E and 97° 25'E"],
        ("north america"):["latitudes:7'N to 85'N","longitudes:20'W to 179'W"],
        ("south america"):["latitudes:12°N to 55°S","longitudes:35°W to 81°W"],
        ("china"):["latitudes:18°N to 53°N ","longitudes:73°E to 135°E"],
        ("london"):["latitudes:55.3781° N ","longitudes:3.4360° W"],
        ("australia"):["latitudes: 10.45° to43.39° south ","longitudes:7113.9° to 153.39° east"]
        }
print(earth.keys())
x=input("which country latitudes and longitudes do you want:")

if x in earth.keys():
    print(earth[x])
else:
    print("currently not updated")

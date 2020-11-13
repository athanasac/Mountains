def read_vouna():          #returns a list with items place-name-height
    f=open("vouna2.txt","r",encoding="utf-8")
    list_ola=[]
    for i in f :
        name, height, place=i.strip().split("\t")
        list_ola.append((name, height, place))
    return(list_ola)


def dict_vouna():   #returns the dict with keys-places-values-mounts
    dict_1={}
    list_ola=read_vouna()
    for i in list_ola :
        name,height,place=i[0],i[1],i[2]
        place="{}".format(place)                #convert place,name to strings
        name="{}".format(name)
        key = place
        dict_1.setdefault(key, [])
        dict_1[key].append(name)
        
        
    return(dict_1)

print(dict_vouna())
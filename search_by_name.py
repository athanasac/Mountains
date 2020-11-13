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
        dict_1.setdefault(key, [])          #adding a second value, if key is the same
        dict_1[key].append(name)
        
    return(dict_1)

def main():
    keys1=dict_vouna().keys()
    print("-------------WELCOME-----------------")
    while True :
        UserInput=input("Επιλέξτε μια γεωγραφική περιοχή:\n")
        if not UserInput : break
        found=0
        for i in keys1 :
            if UserInput.lower() in i.lower() :
                print("Στην περιοχή {}, βρίσκονται τα όρη : {}".format(i,dict_vouna()[i]))
                found+=1
        if not found :
            print('Δυστυχώς δεν υπάρχουν πληροφορίες για την περιοχή αυτήν')
        found=0
    print("Ευχαριστούμε")


main()

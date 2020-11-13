def read_vouna():
    max_height= -1
    max_name=""
    taVouna=[]
    for line in open("vouna2.txt","r",encoding="utf-8") :
        name,height,place=line.strip().split("\t")
        height = int(height.replace(".",""))
        taVouna.append((name,height,place))
        if height > max_height :
            max_height = height
            max_name=name
        #print max_heigt,max_name
    return taVouna, max_height, max_name

def print_vouno(name,height,place,max_height,max_name):
    out = "Το όρος {} έχει ύψος {} μ. και βρίσκεται στην {} .".format(name, height, place)
    if height == max_height :
        compare= "Είναι το ψηλότερο βουνό μας."
    else :
        compare ="Είναι {} μ. πιο χαμηλό απο το όρος {}.".format((max_height-height),max_name)
    return out + compare

def main() :
    taVouna, max_height, max_name = read_vouna()
    print("Καλωσήρθες στον ορεινό παντογνώστη")
    while True :
        userInput=input("Για ποιο βουνό θέλεις να μάθεις ;")
        if not userInput : break
        found=0
        for v in taVouna:
                if userInput.lower() in v[0].lower():
                    print(print_vouno(v[0],v[1],v[2],max_height,max_name))
                    found+=1
        if not found :
            print("Δυστυχώς δεν έχουμε πληροφορίες για το όρος {} .".format(userInput)) 
    print("Ευχαριστούμε!!") 

#### main programm

if __name__ == "__main__": main()

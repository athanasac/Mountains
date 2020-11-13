def read_vouna():
    vouna_list=[]
    for line in open("vouna2.txt","r",encoding="utf-8") :
        name,height,place = line.strip().split("\t")
        height=int(height.replace(".",""))

        if height>2000 : vouna_list.append((name,   height, place))
        
    return (vouna_list)

def string_to_list(element):
    name,height,place=list(element)[0],list(element)[1],list(element)[2]
    str2="{}\t{}\t{}".format(name,height,place)
    return (str2)


f=open("height2000.txt","w",encoding="utf-8")
v=read_vouna()
print("<<<ΤΑ ΨΗΛΟΤΕΡΑ ΒΟΥΝΑ ΤΗΣ ΕΛΛΑΔΑΣ (ΥΨΟΣ ΑΝΩ ΤΩΝ 2000 μ.)>>>",end="\n\n",file=f)
for el in v :
    print("{}\n".format(string_to_list(el)),file = f)
f.close()
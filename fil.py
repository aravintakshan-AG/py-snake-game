def dat(nam,sco):
    z=open("data.txt","r+")
    tot=[]
    tot=z.readlines()
    s = str(sco)
    if len(tot)==0:
        ad=nam+"-"+s
    else:
        ad=" "+nam+"-"+s
    tot.append(ad)
    z.seek(0)
    z.writelines(tot)
    z.close()
    return
def pri():
    x=open("data.txt","r")
    to=x.readline()
    red=to.split(" ")
    x.close()
    return red
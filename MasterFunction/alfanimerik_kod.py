import random
import string 

def alfa(tout_let_chif):
    kod =""
    while tout_let_chif >=1:
        alfabe= random.choice(string.ascii_lowercase+string.digits)
        if alfabe not in kod:
            kod+=alfabe
            tout_let_chif-=1
    print(kod)
alfa(12)

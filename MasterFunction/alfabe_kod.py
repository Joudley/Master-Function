import random
import string

def alfa(tout_let):
    kod =""
    while tout_let >=1:
        alfabe= random.choice(string.ascii_lowercase)
        if alfabe not in kod:
            kod+=alfabe
            tout_let-=1
    print(kod)
alfa(8)


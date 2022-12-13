import re
def komansman_mo(non):
    inisyal=""
    lis = re.split(r' |-' , non )
    for name in lis:
        inisyal += name[0]
    print(inisyal)
komansman_mo("Jean-Baptiste Jean")    
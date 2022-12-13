import string

def dekripte(dek):
    mo_dekripte=""
    lis=dek.split("-")
    for eleman in lis:
        el= int(eleman)
        mo_dekripte += string.ascii_uppercase[el]
    print(mo_dekripte)
dekripte("0-11-14")        
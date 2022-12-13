import string

def kripte (kr):
    mo_kripte=""
    for let in kr:
        t=string.ascii_lowercase.index(let)
        at=str(t)
        mo_kripte+=at + "-"
    print(mo_kripte)
kripte("alo")        
import string
def slug (sl):
    karakte=""
    for n in sl:
        if n in (string.ascii_letters + string.digits + "_"):
         karakte+=n
    print(karakte)     
slug("Jea3@#$42AN-re554_vvgv")    
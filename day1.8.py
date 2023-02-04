def isnumeric(s):
    s=s.strip()
    try:
        s=float(s)
        return True
    except:
        return False
print(isnumeric("0"))
print(isnumeric("e"))
print(isnumeric(""))
print(isnumeric("."))
print(isnumeric("%"))

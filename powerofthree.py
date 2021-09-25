def pot(n):
    if n==1:
        return True
    if n%3!=0 :
        return False
    return pot(n/3)
    
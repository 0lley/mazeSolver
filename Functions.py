def fileHeight(fname):
    i = 0
    for i in open(fname):
        i += 1
    return(i)
    #Returns amount of rows in maze

def fileWidth(fname):
    i = 0
    for i in fname.readline():
        i += 1
    return(i)
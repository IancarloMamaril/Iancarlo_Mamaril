for x in range (11, 0, -1):
    for y in range (1, x +1):
        print (" ", end = " ")
    for z in range (11, x, -1):
        print ("$", end = " ")
    for a in range (11,x, -1):
        print ("^", end = " ")
    print ()


for x in range (0, 11):
    for y in range (1, x +1):
        print (" ", end = " ")
    for z in range (11, x, -1):
        print ("*", end = " ")
    for a in range (11,x, -1):
        print ("@", end = " ")
    print ()
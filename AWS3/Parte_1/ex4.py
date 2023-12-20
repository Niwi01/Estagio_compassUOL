for x in range(2,101):
    primo = True
    for div in range(2,x):
        if x % div == 0:
            primo = False
            break
    if primo:
        print(x)
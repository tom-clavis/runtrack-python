i=0
while i<=1000:
    b=2
    mul =0

    if i<=3:
        print(i)
    else:
        while b<i:
            if i%b == 0:
                mul += 1
            b+=1
        if mul == 0:
            print(i)
    i+=1
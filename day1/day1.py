with open('data.txt', 'r') as f:
    ls  = [int(x) for x in f.read().splitlines()]
ls2 = ls
while ls:
    x = ls.pop()
    for y in ls:
        if (x + y) == 2020:
            print("Answer 1 {}".format(x*y))
        for z in ls[1:]:
            if (x + y + z) == 2020:
                print("Answer 2 {}".format(x*y*z))

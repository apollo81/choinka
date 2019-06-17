# wysokość choinki
height = int(input('podaj wysokość choinki: ' ))

for i in range(1, height + 1):
    print(((height-1) * " ") + ((i-1) * "#") + (i * "#"))


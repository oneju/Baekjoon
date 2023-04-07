#직사각형에서 탈출
position = input()
lst_pos = position.split(" ")
x = int(lst_pos[0])
y = int(lst_pos[1])
w = int(lst_pos[2])
h = int(lst_pos[3])

print(min(x,w-x,y,h-y))

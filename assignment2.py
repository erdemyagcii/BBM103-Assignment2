print("<-----RULES----->")
print("1. BRUSH DOWN")
print("2. BRUSH UP")
print("3. VEHICLE ROTATES RIGHT")
print("4. VEHICLE ROTATES LEFT")
print("5. MOVE UP TO X")
print("6. JUMP")
print("7. REVERSE DIRECTION")
print("8. VIEW THE MATRIX")
print("0. EXIT")
print("Please enter the commands with a plus sign (+) between them.")


x = 0
y = 0
brush = 0
direction = 1

list1 = input()
list1 = list1.split("+")
lenght = int(list1[0])
list1.pop(0)

a = lenght
matrix = [["0" for z in range(a)] for z in range(a)]

def show_matrix(matrix, length):
    print("+" * (length+2))
    for x in matrix:
        print("+",*x,"+", sep="")
    print("+" * (length+2))





def reverse():
    global direction
    if direction == 1:
        direction = 3
    elif direction == 2:
        direction = 4
    elif direction == 3: 
        direction = 1
    else:
        direction = 2   

def brushp(k):
    global brush
    global matrix
    global x,y
    if k == 1:
        brush = 0
    else:
        brush = 1
        matrix[y][x] = "1"

def turn(x):
    global direction
    if x == 3 and (direction == 1 or direction == 2 or direction == 3):
        direction = direction+1
    elif x == 3 and direction == 4:
        direction = 1
    elif x == 4 and (direction == 2 or direction == 3 or direction == 4):
        direction = direction-1
    else:
        direction = 4





def move(steps,x,y,direction,brush,lenght,matrix):
    if direction == 1:
        for step in range(1, steps + 1):
            if brush == 1:
                x = (x + 1) % lenght
                matrix[y][x % lenght] = "1"
            else:
                x = (x + 1) % lenght
    elif direction == 2:
        for step in range(1, steps + 1):
            if brush == 1:
                y = (y + 1) % lenght
                matrix[y % lenght][(x)] = "1"               
            else:
                y = (y + 1) % lenght
    elif direction == 3:
        for step in range(1, steps + 1):
            if brush == 1:
                x = (x - 1) % lenght
                matrix[y][x % lenght] = "1"
            else:
                x = (x - 1) % lenght
    elif direction == 4:
        for step in range(1, steps + 1):
            if brush == 1:
                y = (y - 1) % lenght
                matrix[y % lenght][(x)] = "1"
            else:
                y = (y - 1) % lenght
    return matrix,x,y

for com in list1:
    if com == "1":
        brushp(0)
    elif com == "2":
        brushp(1)
    elif com == "3":
        turn(3)
    elif com == "4":
        turn(4)
    elif com[0] == "5":
        matrix,x,y=move(int(com[2:]),x,y,direction,brush,lenght,matrix)
    elif com ==  "6":
        brushp(1)
        matrix,x,y=move(3,x,y,direction,brush,lenght,matrix)
    elif com == "7":
        reverse()
    elif com == "8":
        for h in range(len(matrix)):
            for g in range(len(matrix)):
                if matrix[h][g] == "0":
                    matrix[h][g] = " "
                else:
                    matrix[h][g] = "*"
        show_matrix(matrix, lenght)
    elif com == "0":
        exit()
    else:
        print("You entered an incorrect command. Please try again!")
        
  




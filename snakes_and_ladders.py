
def numb_of_moves(list_ladder,list_snake):
    dict_ladder = {}
    dict_snake = {}

    #creating the SNL dictionary
    for x,y in list_ladder:
        dict_ladder[int(x)] = int(y)
    for x,y in list_snake:
        dict_snake[int(x)] = int(y)
    query = [(1, 0)]

    while True:
        pos, step = query[0]
        if pos >= 100:
            break
        step += 1
        query.pop(0)
        die_steps = [1,2,3,4,5,6]

        for i in range(1,7):
            curpos = pos + i
            if curpos in dict_ladder.keys():
                query.append((dict_ladder[curpos],step))
                die_steps.remove(i)
            if(curpos in dict_snake.keys()):
                query.append((dict_snake[curpos],step))
                die_steps.remove(i)
        if len(die_steps) == 0:
            continue
        curpos = pos + max(die_steps)
        query.append((curpos,step))
    return step




numT = int(input())
for i in range(numT):
    numLadder = int(input())
    ladder = []
    for _ in range(numLadder):
        i, j = input().split(" ")
        ladder.append((int(i),int(j)))


    numSnakes = int(input())
    snakes = []
    for _ in range(numSnakes):
        i, j = input().split(" ")
        snakes.append((int(i),int(j)))



    print(numb_of_moves(snakes, ladder))

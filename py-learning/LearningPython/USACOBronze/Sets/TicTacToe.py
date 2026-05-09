def tictactoe(line1, line2, line3):
    wins = 0
    set_check = {}
    set_check = set(line1)
    if len(set_check)  <= 2:
        wins += 1
    set_check = set(line2)
    if len(set_check)  <= 2:
        wins += 1
    set_check = set(line3)
    if len(set_check)  <= 2:
        wins += 1
    column1 = [line1[0], line2[0], line3[0]]
    column2 = [line1[1], line2[1], line3[1]]
    column3 = [line1[2], line2[2], line3[2]]
    set_check = set(column1)
    if len(set_check)  <= 2:
        wins += 1
    set_check = set(column2)
    if len(set_check)  <= 2:
        wins += 1 
    set_check = set(column3)
    if len(set_check)  <= 2:
        wins += 1

    return wins

print(tictactoe([1, 2, 2], [1, 3, 1], [1, 34, 2]))
print(tictactoe([1, 2, 2], [1, 3, 1], [1, 1, 1]))
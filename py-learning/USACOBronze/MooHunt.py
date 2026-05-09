

num_cells, num_moves = map(int, input().split())

moves = []
for _ in range(num_moves):
    first, second, third = map(int, input().split())
    moves.append((first - 1, second - 1, third - 1))

moves_that_use = [[] for _ in range(num_cells)]
i = 0
while i < num_moves:
    a, b, c = moves[i]
    moves_that_use[a].append(i)
    moves_that_use[b].append(i)
    moves_that_use[c].append(i)
    i += 1


board = ['O'] * num_cells

move_scores = [False] * num_moves

current_score = 0
best_score = 0
num_best_boards = 0

def move_forms_moo(move_index):
    a, b, c = moves[move_index]
    return board[a] == 'M' and board[b] == 'O' and board[c] == 'O'

def flip_cell(cell):
    global current_score

    if board[cell] == 'O':
        board[cell] = 'M'
    else:
        board[cell] = 'O'

    j = 0
    while j < len(moves_that_use[cell]):
        move_index = moves_that_use[cell][j]
        before = move_scores[move_index]
        after = move_forms_moo(move_index)

        if before != after:
            move_scores[move_index] = after
            if after:
                current_score += 1
            else:
                current_score -= 1
        j += 1

def try_all_boards(cell_index):
    global best_score, num_best_boards

    if cell_index == num_cells:
        if current_score > best_score:
            best_score = current_score
            num_best_boards = 1
        elif current_score == best_score:
            num_best_boards += 1
        return

    try_all_boards(cell_index + 1)

    flip_cell(cell_index)
    try_all_boards(cell_index + 1)
    flip_cell(cell_index)

try_all_boards(0)
print(best_score, num_best_boards)

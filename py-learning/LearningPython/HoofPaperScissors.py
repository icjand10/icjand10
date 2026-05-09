fin = open("hps.in", "r")
lines = [line.strip() for line in fin]
fin.close()

N = int(lines[0])
moves = lines[1:]

beats = {'H': 'S', 'S': 'P', 'P': 'H'}

total = {'H': 0, 'P': 0, 'S': 0}
for m in moves:
    total[m] += 1

prefix = {'H': 0, 'P': 0, 'S': 0}
suffix = total.copy()

best = 0

for g1 in ['H', 'P', 'S']:
    for g2 in ['H', 'P', 'S']:
        wins = prefix[beats[g1]] + suffix[beats[g2]]
        if wins > best:
            best = wins
for m in moves:
    prefix[m] += 1
    suffix[m] -= 1

    for g1 in ['H', 'P', 'S']:
        for g2 in ['H', 'P', 'S']:
            wins = prefix[beats[g1]] + suffix[beats[g2]]
            if wins > best:
                best = wins

print = open("hps.out", "w")
print.write(str(best) + "\n")
print.close()

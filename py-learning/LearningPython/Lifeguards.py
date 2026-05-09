fin = open("lifeguards.in", "r")
num_guards = int(fin.readline())

shifts = []
for guard_id in range(num_guards):
    start, end = map(int, fin.readline().split())
    shifts.append((start, end, guard_id))
fin.close()

events = []
for start, end, guard_id in shifts:
    events.append((start, 1, guard_id))
    events.append((end, -1, guard_id))

events.sort()

active_guards = []
unique_time = [0] * num_guards
total_time = 0
last_time = events[0][0]

for time, event_type, guard_id in events:
    if len(active_guards) > 0:
        total_time += time - last_time
        if len(active_guards) == 1:
            unique_time[active_guards[0]] += time - last_time

    if event_type == 1:
        active_guards.append(guard_id)
    else:
        active_guards.remove(guard_id)

    last_time = time

if num_guards == 1:
    answer = 0
else:
    answer = total_time - min(unique_time)

fout = open("lifeguards.out", "w")
fout.write(str(answer) + "\n")
fout.close()
print(answer)

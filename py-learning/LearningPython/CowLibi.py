import bisect

def squared_distance(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    return dx*dx + dy*dy

def main():
    num_grazings, num_cows = map(int, input().split())

    grazings = []
    for _ in range(num_grazings):
        gx, gy, gt = map(int, input().split())
        grazings.append((gt, gx, gy))
    grazings.sort()

    grazing_times = [g[0] for g in grazings]
    grazing_x = [g[1] for g in grazings]
    grazing_y = [g[2] for g in grazings]

    def cow_could_be_guilty(cow_x, cow_y, cow_t):

        insert_pos = bisect.bisect_left(grazing_times, cow_t)


        if insert_pos == 0:
            time_gap = grazing_times[0] - cow_t
            return squared_distance(cow_x, cow_y, grazing_x[0], grazing_y[0]) <= time_gap * time_gap
        if insert_pos == num_grazings:
            time_gap = cow_t - grazing_times[-1]
            return squared_distance(cow_x, cow_y, grazing_x[-1], grazing_y[-1]) <= time_gap * time_gap


        prev_idx = insert_pos - 1

        time_gap_prev = cow_t - grazing_times[prev_idx]
        if squared_distance(cow_x, cow_y, grazing_x[prev_idx], grazing_y[prev_idx]) > time_gap_prev * time_gap_prev:
            return False

  
        time_gap_next = grazing_times[insert_pos] - cow_t
        if squared_distance(cow_x, cow_y, grazing_x[insert_pos], grazing_y[insert_pos]) > time_gap_next * time_gap_next:
            return False

        return True

    innocent_count = 0
    for _ in range(num_cows):
        cx, cy, ct = map(int, input().split())
        if not cow_could_be_guilty(cx, cy, ct):
            innocent_count += 1

    print(innocent_count)

main()

def solve():
    boys_count, girls_count = map(int, input().split())
    boys_min = list(map(int, input().split()))
    girls_max = list(map(int, input().split()))

    strongest_boy_min = max(boys_min)
    weakest_girl_max = min(girls_max)

    if weakest_girl_max < strongest_boy_min:
        print(-1)
        return

    base_total = sum(boys_min) * girls_count


    extra_total = sum(girls_max) - strongest_boy_min

    print(base_total + extra_total)

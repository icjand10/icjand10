trail_length, num_stops, fj_rate, bessie_rate = map(int, input().split())

def read_stop(_):
    return tuple(map(int, input().split()))

rest_stops = list(map(read_stop, range(num_stops)))

optimal_stops = []
max_tastiness_ahead = 0

for position, tastiness in reversed(rest_stops):
    if tastiness > max_tastiness_ahead:
        optimal_stops.append((position, tastiness))
        max_tastiness_ahead = tastiness

optimal_stops.reverse()

total_tastiness = 0
previous_position = 0
extra_time_per_meter = fj_rate - bessie_rate

for position, tastiness in optimal_stops:
    distance = position - previous_position
    available_extra_time = distance * extra_time_per_meter
    total_tastiness += available_extra_time * tastiness
    previous_position = position

print(total_tastiness)

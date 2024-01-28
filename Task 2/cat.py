import sys

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f'Cannot open "{file_path}"!')
        sys.exit(1)

def analyze_log(lines):
    cat_visits = 0
    other_cats = 0
    total_time_in_house = 0
    durations = []

    for line in lines:
        if line.strip() == 'END':
            break

        parts = line.strip().split(',')
        cat_name, entry_time, exit_time = parts[0], int(parts[1]), int(parts[2])
        duration = exit_time - entry_time

        if cat_name == 'OURS':
            cat_visits += 1
            total_time_in_house += duration
            durations.append(duration)
        else:
            other_cats += 1

    return cat_visits, other_cats, total_time_in_house, durations

def format_duration(minutes):
    hours = minutes // 60
    minutes %= 60
    return f"{hours} Hours, {minutes} Minutes"

def main():
    if len(sys.argv) != 2:
        print('Missing command line argument!')
        sys.exit(1)

    file_path = sys.argv[1]
    lines = read_file(file_path)

    cat_visits, other_cats, total_time_in_house, durations = analyze_log(lines)

    if cat_visits == 0:
        print(f'No cat visits found in "{file_path}".')
    else:
        average_duration = sum(durations) // cat_visits
        longest_duration = max(durations)
        shortest_duration = min(durations)

        print("\nLog File Analysis")
        print("==================\n")
        print(f'Cat Visits: {cat_visits}')
        print(f'Other Cats: {other_cats}\n')
        print(f'Total Time in House: {format_duration(total_time_in_house)}\n')
        print(f'Average Visit Length: {format_duration(average_duration)}')
        print(f'Longest Visit:        {format_duration(longest_duration)}')
        print(f'Shortest Visit:       {format_duration(shortest_duration)}')

if __name__ == "__main__":
    main()

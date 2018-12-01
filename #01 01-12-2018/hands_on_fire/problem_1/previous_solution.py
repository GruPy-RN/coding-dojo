def count_time(input_file="input.txt"):
    with open(input_file) as f:
        lines = f.readlines()
    momentos_ordenados = sorted([int(i) for i in lines[1].split()])
    total = 10
    for i in range(1, len(momentos_ordenados)):
        if momentos_ordenados[i] - momentos_ordenados[i-1] > 10:
            total += 10
        else:
            total += momentos_ordenados[i] - momentos_ordenados[i-1]
    return total
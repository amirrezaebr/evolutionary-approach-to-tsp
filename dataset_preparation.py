def create_distance_matrix(input_path: str):
    distance_matrix = [[0 for _ in range(30)] for _ in range(30)]
    coordinates = read_data(input_path)

    for i in range(0, 30):
        for j in range(0, 30):
            if i != j:
                distance_matrix[i][j] = calculate_euclidean_distance(coordinates[i], coordinates[j])
    return distance_matrix


def read_data(input_path: str):  # read data from the file
    coordinates = []
    input_path += ".txt"
    with open(input_path, 'r') as file:
        for line in file:
            x, y = map(int, line.replace(',', '').split())
            coordinates.append((x, y))
    return coordinates


def calculate_euclidean_distance(coordination1: tuple,
                                 coordination2: tuple):  # calculate euclidean distance of data points
    return (((coordination1[0] - coordination2[0]) ** 2) + ((coordination1[1] - coordination2[1]) ** 2)) ** 0.5

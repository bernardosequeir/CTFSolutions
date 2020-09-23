def find_lattice_paths_count(grid_size):
    paths = 1
    for i in range(0, grid_size):
        paths *= (2*grid_size) - i
        paths /= i+1
    return paths


if __name__ == "__main__":
    print(f"Number of lattice paths: {find_lattice_paths_count(20)}")

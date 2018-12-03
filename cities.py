def read_cities(file_name):
    # no unit tests
    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 
       [(state, city, latitude, longitude), ...] 
     Use this as your initial `road_map`, that is, the cycle 
       Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
    fin = open(file_name)

    cities_list = []

    for line in fin:
        #print(line)
        cities_list.append(line.split())

     for city in cities_list:
        print(city)
  
def print_cities(road_map):
    # no unit tests
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """
    pass

 def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    pass

 def swap_adjacent_cities(road_map, index):
    """
    Take the city at location `index` in the `road_map`, and the city at 
    location `index+1` (or at `0`, if `index` refers to the last element 
    in the list), swap their positions in the `road_map`, compute the 
    new total distance, and return the tuple 
         (new_road_map, new_total_distance)
    """
    pass

 def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 
         (new_road_map, new_total_distance)
     Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    pass

 def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `swap_adjacent_cities`, 
    try `10000` swaps, and each time keep the best cycle found so far. 
    After `10000` swaps, return the best cycle found so far.
    """
    pass

 def print_map(road_map):
    # no unit tests
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
    pass

 def main():
    # no unit tests
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    read_cities('city-data-test-file-4-cities.txt')

 if __name__ == "__main__":
    main()

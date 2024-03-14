from route_finder import RouteFinder

def main():
    route_finder = RouteFinder('tubedata.csv')
    start_station = 'Harrow & Wealdstone'
    end_station = 'Waterloo'
    for method in ['DFS', 'BFS', 'UCS', 'Heuristic BFS']:
        print(f'\nUsing {method}:')
        route, cost, nodes_expanded = route_finder.find_route(start_station, end_station, method)
        print(f'Shortest route from {start_station} to {end_station}:')
        print(route)
        print(f'Cost: {cost}')
        print(f'Number of nodes expanded: {nodes_expanded}')

if __name__ == "__main__":
    main()

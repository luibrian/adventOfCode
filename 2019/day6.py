#2019 Advent of Code Day 6

from Node import Planet
from typing import Dict
import queue

def part1(data):
    """
    Find total number of direct and indirect orbits in map data
    """
    planet_dict = build_tree(data)
    print(planet_dict['B1J'].children)
    count = count_orbits(planet_dict)
    return count


def part2(data,start,goal):
    """
    Find number of orbital transfers
    Basically a bfs question. If answer is -1, they do not both exist
    """
    planet_dict = build_tree(data)
    count = dist_transfer_map(start,goal,planet_dict)
    return count


def read_input(in_text):
    """
    Reads the input text file and outputs array of values
    """
    data = []
    with open(in_text, 'r') as f:
        for line in f.readlines():
            data.append(line.strip().split(')'))
    return data


def build_tree(data) -> Dict:
    """Built the tree based on data of orbits.
    Returns set of all planets in the graph
    4 possible states, slightly different adding of stuff 
    """
    planet_dict = dict()
    for orbit in data:
        in_planet_name = orbit[0]
        out_planet_name = orbit[1]
        if in_planet_name in planet_dict and out_planet_name in planet_dict:  # both planets in
            planet_dict[out_planet_name].parent = planet_dict[in_planet_name]
            planet_dict[in_planet_name].children.add(planet_dict[out_planet_name])
        elif in_planet_name in planet_dict and out_planet_name not in planet_dict: # inner planet is in, outer not
            out_planet = Planet(out_planet_name, planet_dict[in_planet_name])
            planet_dict[out_planet_name] = out_planet
            in_planet = planet_dict[in_planet_name]
            in_planet.children.add(out_planet)
        elif in_planet_name not in planet_dict and out_planet_name in planet_dict:  # outer planet in, inner planet not:
            out_planet = planet_dict[out_planet_name]
            in_planet = Planet(in_planet_name, child=out_planet)
            planet_dict[in_planet_name] = in_planet
            out_planet.parent = in_planet
        else: # Both planets not in
            in_planet = Planet(in_planet_name)
            out_planet = Planet(out_planet_name, parent=in_planet)
            in_planet.children.add(out_planet)
            planet_dict[in_planet_name] = in_planet
            planet_dict[out_planet_name] = out_planet
    return planet_dict


def count_orbits(planet_dict: Dict) -> int:
    """Counts the number of direct and indirect orbits for planets in the dict.
    For part 1
    """
    count = 0
    for planet_name in planet_dict:
        planet = planet_dict[planet_name]
        while planet.parent is not None:
            count += 1
            planet = planet.parent
    return count


def add_planet_queue(planet: Planet, seen_planets: set[Planet], 
                    unchecked_planets: 'Queue[Planet]', depth: int) -> None:
    """Add planet to the queue
    """
    if planet not in seen_planets:
        seen_planets[planet] = depth
    if planet.parent is not None and planet.parent not in seen_planets:
        unchecked_planets.put((planet.parent,depth))
    for child in planet.children:
        if child not in seen_planets and child is not None:
            unchecked_planets.put((child,depth))


def dist_transfer_map(start: str, goal: str, planet_dict: 'Dict[Planet]'):
    """
    Solved using a BFS. This question can also be done recursively
    """
    start_planet = planet_dict[start]
    goal_planet = planet_dict[goal]
    
    unchecked_planets = queue.Queue()
    seen_planets = {start_planet: 0}

    add_planet_queue(start_planet,seen_planets,unchecked_planets,0)

    while goal_planet not in seen_planets:
        planet,depth = unchecked_planets.get()
        add_planet_queue(planet,seen_planets,unchecked_planets,depth+1)
    return seen_planets[goal_planet]-2


if __name__ == "__main__":
    data = read_input('day6_in.txt')
    part1_out = part1(data) 
    print("This is part 1: " + str(part1_out))

    part2_out = part2(data,'YOU','SAN')
    print("This is part 2: " + str(part2_out))

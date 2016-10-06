"""
Text Adventure Game
https://www.reddit.com/r/dailyprogrammer/comments/pjbuj/intermediate_challenge_2/
"""

import pickle  # Allows us to read a dictionary from a file
from challenges.challenge_12.nicole import position

if __name__ == "__main__":
    # Using the maze class and object
    m = position.Maze()

    # Setting coordinates from a dictionary stored in a txt file
    with open('maze_coordinates.txt', 'rb') as handle:
        coordinates = pickle.loads(handle.read())
        m.set_coordinates(coordinates, coordinates.get('Entry'), coordinates.get('Exit'))

    # Displaying the game to the user
    m.default_maze()

"""
This is the main module for the game.
All other modules should be imported here to be ran for the full game experience.
"""

from challenges.challenge_12.game_final import position

if __name__ == '__main__':
    # Using the position class and object to create a map
    game = position.Location()

    # Reading coordinates and locations from a text file
    game.set_coordinates_and_locations_from_file('coordinates.txt')

    # Displaying the game to the user
    print('Enter text to describe the start of the text adventure game (the story).\n')
    game.default_navigation()
    print('\nEnter text to describe the end of the text adventure game (the story).')
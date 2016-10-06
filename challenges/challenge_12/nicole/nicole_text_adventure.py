"""
Text Adventure Game
https://www.reddit.com/r/dailyprogrammer/comments/pjbuj/intermediate_challenge_2/
"""

import pickle # Used for exporting/importing dictionaries

from challenges.challenge_12.nicole import position

if __name__ == "__main__":
    # Using the position module to track movements
    # Creating three objects because there are three parts of the map
    p1 = position.Position()
    p2 = position.Position()
    p3 = position.Position()

    # Setting the coordinates
    with open('coordinates_part_1.p', 'rb') as handle:
        coordinates = pickle.loads(handle.read())
        p1.set_coordinates(coordinates, (0, 14), (10, 9))
    with open('coordinates_part_2.p', 'rb') as handle:
        coordinates = pickle.loads(handle.read())
        p2.set_coordinates(coordinates, (10, 9), (18, 18))
    with open('coordinates_part_3.p', 'rb') as handle:
        coordinates = pickle.loads(handle.read())
        p3.set_coordinates(coordinates, (18, 18), None)

    # Pulling in descriptions for what is at the coordinates
    coordinate_descriptions = {}
    with open('coordinates_all_descriptions.p', 'rb') as handle:
        coordinate_descriptions = pickle.loads(handle.read())

    # Setting the story
    story_elements = {
        'Open': 'You walk through the field.',
        'Door': 'You have found a door.  It requires a key to unlock.',
        'Key': 'You have found a key.',
        'Potion': 'You have found a potion.',
        'Location': 'You have entered a building.',
        'NPC': 'You have encountered an NPC.',
        'Boss': 'You have encountered a boss.'
    }

    # Allowing the user to move around
    print(p1.instructions)
    while p1.current_position != p1.exit_coord:
        p1.user_interaction()
        p1.set_story_directions(story_elements.get(coordinate_descriptions.get(p1.new_position)),
                                'You cannot go {0}.  There is a fence.'.format(p1.direction))
        p1.validate_direction()
    while p2.current_position != p2.exit_coord:
        p2.user_interaction()
        p2.set_story_directions(story_elements.get(coordinate_descriptions.get(p2.new_position)),
                                'You cannot go {0}.  There is a fence.'.format(p2.direction))
        p2.validate_direction()
    while p3.current_position != p3.exit_coord:
        p3.user_interaction()
        p3.set_story_directions(story_elements.get(coordinate_descriptions.get(p3.new_position)),
                                'You cannot go {0}.  There is a fence.'.format(p3.direction))
        p3.validate_direction()

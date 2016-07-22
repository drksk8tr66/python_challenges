'''
Morse Code
https://www.reddit.com/r/dailyprogrammer/comments/pr2xr/2152012_challenge_7_easy/
'''

import sys


def translate_morse(m):
    # Morse code dictionary
    to_morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
                'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
                'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
                '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                '8': '---..', '9': '----.', 'Ä': '.-.-', 'Á': '.--.-', 'Å': '.--.-', 'Ch': '----',
                'É': '..-..', 'Ñ': '--.--', 'Ö': '---.', 'Ü': '..--', '.': '.-.-.-', ',': '--..--',
                ':': '---...', '?': '..--..', '\'': '.----.', '-': '-....-', '/': '-..-.', '()': '-.--.-',
                '"': '.-..-.', '@': '.--.-.', '=': '-...-', ' ': '/', '\n': '.-.-', '…': '.-...',
                '\n\n': '-...-.-', '\n\n': '-...-', ' ': '/'}
    from_morse = {v: k for k, v in to_morse.items()}

    # Translate the message
    is_morse = len(m) == m.count(' ') + m.count('.') + m.count('-') + m.count('/')
    if is_morse == 1:
        morse = m
        message = ''.join(from_morse.get(char, char) for char in m.split())
    elif is_morse == 0:
        message = m
        morse = ''.join(to_morse.get(char, char) + ' ' for char in m)

    return is_morse, message, morse


def play_morse(morse, message):
    import winsound
    import time
    import pygame

    # Function called to display the code on the screen
    def display(morse, message):
        # Font setup
        font = pygame.font.Font(None, 64)

        # Display morse
        text = font.render(morse, True, (255, 255, 255))
        textpos = text.get_rect()
        textpos.right = 800
        textpos.centery = background.get_rect().centery - 64

        # Display message
        text2 = font.render(message, True, (255, 255, 255))
        textpos2 = text2.get_rect()
        textpos2.right = 800
        textpos2.centery = background.get_rect().centery + 64

        # Blit everything to the screen
        screen.blit(text, textpos)
        screen.blit(text2, textpos2)
        pygame.display.flip()
        pygame.display.update()

    # Initialize screen
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Morse Code')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Used for sounds
    duration = 160
    frequency = 500

    # Loop for each sound and display
    display_morse = ''
    display_message = ''
    prev_char = ''
    message += ' '
    for char in morse + ' ':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        display_morse += char
        if char == '.':
            display(display_morse, display_message)
            winsound.Beep(frequency, duration)
        elif char == '-':
            display(display_morse, display_message)
            winsound.Beep(frequency, duration * 3)
        elif char == ' ' or char == '/':
            if prev_char != '/':
                display_message += message[len(display_message)]
            display(display_morse, display_message)
            time.sleep(duration * 4 / 1000)

        prev_char = char
        screen.blit(background, (0, 0))


def main():
    # Get message from user
    print('Enter the message you would like to encrypt/decrypt.  When finished, press Enter, then CTRL+D.')
    user_input = sys.stdin.read().upper().rstrip()

    # Translate message
    is_morse, message, morse = translate_morse(user_input)
    if is_morse is True:
        print(message)
    elif is_morse is False:
        print(morse)

    # Play the message for the user to see/hear
    play_morse(morse, message)


if __name__ == "__main__":
    main()
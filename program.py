from mektige_knut.screens import *
from mektige_knut.chapters import *

# Global variables.

# Dictionary of screens for access by keyword.
__screens = {}

# Array of chapters for access by index.
__chapters = []


# Initialization.

__screens["CHARACTER_CUSTOMIZATION"] = CharacterCustomization()
__screens["HOME"] = Home()


# Game-loop.

def run():
    __screens["CHARACTER_CUSTOMIZATION"].show()
    __screens["HOME"].show()
    input()

if __name__ == "__main__":
    run()
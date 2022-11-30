# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    e "Choose your pizza topping!"

menu:

    "pepperoni":
        e "Wise but basic choice!"

        jump after_pizza_menu

    "ham":
        jump special_choice

    "chorizo":
        jump after_pizza_menu

    "pineapple":
        e "I... can't believe this. I'm out of this game!"
        jump after_pizza_menu

label special_choice:

    e "Oh my! It's my favorite! We have something in common~"

label after_pizza_menu:

    e "You picked something! Yay!"

    return

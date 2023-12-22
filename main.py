num = 0
def Show(num2: number):
    index = 0
    if index == 0:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
    elif index == 1:
        basic.show_leds("""
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            """)
    elif index == 2:
        basic.show_leds("""
            # . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . #
            """)
    elif index == 3:
        basic.show_leds("""
            # . . . #
            . . . . .
            . . . . .
            . . . . .
            # . . . #
            """)
    elif index == 4:
        basic.show_leds("""
            # . . . #
            . . . . .
            . . # . .
            . . . . .
            # . . . #
            """)
    else:
        basic.show_leds("""
            # . . . #
            . . . . .
            # . . . #
            . . . . .
            # . . . #
            """)

def on_gesture_shake():
    global num
    num = randint(0, 5)
    for index2 in range(6):
        Show(1)
        if index2 == num:
            pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

import curses

class Color:
    # Basic colors
    WHITE = 1
    GREEN = 2
    CYAN = 3
    BLUE = 4
    MAGENTA = 5
    RED = 6
    YELLOW = 7
    # Custom colors
    JAPAN = 101



def init_colors():
    curses.start_color()
    curses.init_pair(Color.WHITE, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(Color.GREEN, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(Color.CYAN, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(Color.BLUE, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(Color.MAGENTA, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(Color.RED, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(Color.YELLOW, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    curses.init_pair(Color.JAPAN, curses.COLOR_RED, curses.COLOR_WHITE)


    # Overwrite the values in the Colors class to correspond to the actual attribute value
    Color.WHITE = curses.color_pair( Color.WHITE )
    Color.GREEN = curses.color_pair( Color.GREEN )
    Color.CYAN = curses.color_pair( Color.CYAN )
    Color.BLUE = curses.color_pair( Color.BLUE )
    Color.MAGENTA = curses.color_pair( Color.MAGENTA )
    Color.RED = curses.color_pair( Color.RED )
    Color.YELLOW = curses.color_pair( Color.YELLOW )

    Color.JAPAN = curses.color_pair( Color.JAPAN )

# Simply a module to print out a header with borders


import curses


def draw_header(window, title: str, text_color: int = 0, border_color: int = 0):
    # Clears the window
    window.clear()

    # Draw border
    window.attron(border_color | curses.A_BOLD)
    window.border('|', '|', '=', '=', ' ',' ', ' ', ' ')
    window.attroff(border_color | curses.A_BOLD)

    # Draw the text at center of the "box"
    x_offset = window.getmaxyx()[0] // 2
    y_offset = (window.getmaxyx()[1] - len(title) ) // 2
    window.addstr(x_offset, y_offset, title, text_color | curses.A_BOLD )

    window.refresh()

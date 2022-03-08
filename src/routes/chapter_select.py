
import curses

from src.utils.enums import Topic, ReturnTo, MenuOption
from src.utils.japanese import GOJUON_ROWS, get_characters
from src.utils.colors import Color
from src.curses_menu import CheckboxMenu, draw_header
from src.routes.game_mode_select import game_mode_route


def chapter_select_route(stdscr, topic: Topic):
    height, width = stdscr.getmaxyx()

    # Subwindowing
    header_win = stdscr.derwin(5, width, 0, 0)
    desc_win = stdscr.derwin(2, width, 6, 0)
    choices_win = stdscr.derwin( len(GOJUON_ROWS) + 3, width, 9, 0)
    prompt_win = stdscr.derwin(2, width, 13 + len(GOJUON_ROWS), 0)

    # CLI Loop
    return_to = ReturnTo.CHAPTER_SELECT

    while return_to >= ReturnTo.CHAPTER_SELECT:
        # Clear
        stdscr.clear()

        # header
        draw_header(
            header_win,
            "✰♫♪•*¨·٠•●♥✿  ▁▁▂▂▃▃▅▅▆▆▇▇  Chapter Select 选 择 章 节  ▇▇▆▆▅▅▃▃▂▂▁▁  ✿♥●•٠·¨*•♪♫✰",
            text_color=Color.RED
        )

        # Description
        desc_win.clear()
        desc_win.addstr(
            'The chart consists of 46 basic letters, each divided into separate rows. Select the ones you want '
            'to include: '
        )

        # Prompt
        prompt_win.clear()
        prompt_win.addstr(
            "[Use UP/DOWN arrow to change selection.]\n"
            "[Use ENTER to select/deselect]",
            Color.GREEN | curses.A_BOLD
        )

        stdscr.refresh()

        # Selection menu
        values = CheckboxMenu(
            choices_win,
            GOJUON_ROWS,
            highlight_color=Color.CYAN
        ).run()

        # Branching
        if values == MenuOption.CANCEL:
            return_to = ReturnTo.TOPIC_SELECT
        elif not any(values):
            stdscr.clear()
            stdscr.addstr("You must select at least (1) chapters to proceed!\n\n", Color.RED | curses.A_BOLD)
            stdscr.addstr("[Press any key to continue...]", )
            stdscr.getch()
        else:
            characters = get_characters(values)
            return_to = game_mode_route(stdscr, topic, characters)

    return return_to

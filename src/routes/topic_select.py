import curses

from src.utils.enums import Topic, ReturnTo
from src.utils.colors import Color
from src.curses_menu import SelectionMenu, draw_header
from src.routes.chapter_select import chapter_select_route



def topic_select_route(stdscr):
    height, width = stdscr.getmaxyx()
    options = ['Hiragana 平 假 名 ', 'Katakana 片 假 名 ', 'Mixed 混 ', 'Exit 退 出 ']

    # Subwindowing
    header_win = stdscr.derwin(5, width, 0, 0)
    desc_win = stdscr.derwin(2, width, 6, 0)
    choices_win = stdscr.derwin( len(options), width, 9, 0)
    prompt_win = stdscr.derwin(2, width, 10 + len(options), 0)

    # CLI Loop
    return_to = ReturnTo.TOPIC_SELECT

    while return_to >= ReturnTo.TOPIC_SELECT:
        # Clear
        stdscr.clear()

        # header
        draw_header(
            header_win,
            "✰♫♪•*¨·٠•●♥✿  ▁▁▂▂▃▃▅▅▆▆▇▇  Japanese Memorizer 日 语 小 助 手  ▇▇▆▆▅▅▃▃▂▂▁▁  ✿♥●•٠·¨*•♪♫✰",
            text_color=Color.RED
        )

        # Description
        desc_win.clear()
        desc_win.addstr(
            'Memorizing Hiragana and Katakana is challenging to Japanese newbies. This program aims to '
            'ease this process by putting your knowledge to test. REPETITION IS KEY',
        )

        # Prompt
        prompt_win.clear()
        prompt_win.addstr(
            "[Use UP/DOWN arrow to change selection.]\n"
            "[Use ENTER to select]",
            Color.GREEN | curses.A_BOLD
        )

        stdscr.refresh()

        # Selection menu
        selection = SelectionMenu(
            choices_win,
            options,
            highlight_color=Color.CYAN
        ).run()

        # Branching
        if selection == 0: return_to = chapter_select_route(stdscr, Topic.HIRAGANA)
        elif selection == 1: return_to = chapter_select_route(stdscr, Topic.KATAKANA)
        elif selection == 2: return_to = chapter_select_route(stdscr, Topic.MIXED)
        else: return_to = ReturnTo.EXIT

    return return_to

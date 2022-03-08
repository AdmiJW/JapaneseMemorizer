import curses

from src.utils.enums import ReturnTo
from src.utils.colors import Color
from src.curses_menu import SelectionMenu

def return_route(stdscr):
    stdscr.clear()
    stdscr.refresh()

    # Subwindow
    height, width = stdscr.getmaxyx()
    title_subwin = stdscr.derwin(3, width, 0, 0)
    menu_subwin = stdscr.derwin(10, width, 4, 0)

    title_subwin.addstr("<< Select your action >>", Color.RED | curses.A_BOLD)
    title_subwin.refresh()

    value = SelectionMenu(
        menu_subwin,
        [
            'Challenge again 重 试 ',
            'Return to Mode select 返 回 模 式 选 择 ',
            'Return to Chapter select 返 回 章 节 选 择 ',
            'Return to Main Menu 返 回 主 菜 单 ',
            'Exit Program 关 闭 '
        ],
        highlight_color=Color.CYAN
    ).run()

    if value == 0: return ReturnTo.CHALLENGE
    elif value == 1: return ReturnTo.GAMEMODE_SELECT
    elif value == 2: return ReturnTo.CHAPTER_SELECT
    elif value == 3: return ReturnTo.TOPIC_SELECT
    else: return ReturnTo.EXIT

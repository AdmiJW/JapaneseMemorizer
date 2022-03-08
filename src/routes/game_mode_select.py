import curses

from src.utils.enums import Topic, ReturnTo, GameMode, MenuOption
from src.utils.colors import Color
from src.utils.japanese import Character
from src.curses_menu import Menu, NumberMenuItem, ButtonMenuItem, draw_header
from src.routes.challenge import challenge_route


def game_mode_route(stdscr, topic: Topic, characters: list[Character]):
    height, width = stdscr.getmaxyx()

    # Subwindowing
    header_win = stdscr.derwin(5, width, 0, 0)
    menu_win = stdscr.derwin( 6, width, 6, 0)
    prompt_win = stdscr.derwin(3, width, 13, 0)

    # menu initialization
    menu = Menu(menu_win)
    menu.add_menu_item('NumQuestion', NumberMenuItem.factory(
        "Number of questions 题 数 : ",
        min_val=1,
        max_val=len(characters),
        initial_value=len(characters),
        highlight_color=Color.CYAN
    ))
    menu.add_menu_item('divider', ButtonMenuItem.factory(
        '――――――――――――――――――――――――――――――',
        lambda: None,
        highlight_color=Color.CYAN
    ))
    menu.add_menu_item('Writing', ButtonMenuItem.factory(
        'Writing 书 写 ',
        lambda: GameMode.WRITING,
        highlight_color=Color.CYAN
    ))
    menu.add_menu_item('Recognition', ButtonMenuItem.factory(
        'Recognition 辨 识 ',
        lambda: GameMode.RECOGNITION,
        highlight_color=Color.CYAN
    ))
    menu.add_menu_item('Mixed', ButtonMenuItem.factory(
        'Mixed 混 合 ',
        lambda: GameMode.MIXED,
        highlight_color=Color.CYAN
    ))
    menu.add_menu_item('Cancel', ButtonMenuItem.factory(
        'Cancel 返 回 ',
        lambda: MenuOption.CANCEL,
        highlight_color=Color.CYAN
    ))


    # CLI Loop
    return_to = ReturnTo.GAMEMODE_SELECT

    while return_to >= ReturnTo.GAMEMODE_SELECT:
        # Clear
        stdscr.clear()

        # header
        draw_header(
            header_win,
            "✰♫♪•*¨·٠•●♥✿  ▁▁▂▂▃▃▅▅▆▆▇▇  Mode Select 选 择 模 式  ▇▇▆▆▅▅▃▃▂▂▁▁  ✿♥●•٠·¨*•♪♫✰",
            text_color=Color.RED
        )

        # Prompt
        prompt_win.clear()
        prompt_win.addstr(
            "[Use UP/DOWN arrow to change selection.]\n"
            "[Use ENTER to select.]\n"
            "[LEFT/RIGHT arrow to change number value]",
            Color.GREEN | curses.A_BOLD
        )

        stdscr.refresh()

        # menu to select number of questions, and select game mode
        game_mode = menu.run()
        question_limit = menu.get_menu_item('NumQuestion').get_value()

        # Branching
        if game_mode == MenuOption.CANCEL:
            return_to = ReturnTo.CHAPTER_SELECT
        else:
            # Reduce number of characters in the list of characters until specified limit
            while len(characters) > question_limit: characters.pop()
            return_to = challenge_route(stdscr, topic, game_mode, characters)

    return return_to

# Writing Game Mode:
#
# <header>
# <Progress>
# <Question No>
# <Question Description>
# <menu>
#       <Done, Proceed>
#       <Show Answer>
#       <Quit>
# <Answer?>
# <Prompt>


import curses
import random

from src.utils.enums import Topic, ReturnTo, GameMode, MenuOption
from src.utils.colors import Color
from src.utils.japanese import Character
from src.utils.question import QuestionGenerator, Question
from src.curses_menu import SelectionMenu, Menu, TextMenuItem, ButtonMenuItem, ProgressBar, ExtendingText, draw_header
from src .routes.summary import summary_route



def challenge_route(stdscr, topic: Topic, game_mode: GameMode, characters: list[Character]):
    height, width = stdscr.getmaxyx()

    # Subwindowing
    header_win = stdscr.derwin(5, width, 0, 0)
    progress_win = stdscr.derwin(1, width, 6, 0)
    question_no_win = stdscr.derwin(1, width, 8, 0)
    question_win = stdscr.derwin(2, width, 10, 0)
    menu_win = stdscr.derwin(5, width, 13, 0)
    answer_win = stdscr.derwin(4, width, 18, 0)
    prompt_win = stdscr.derwin(4, width, 23, 0)

    # CLI Loop
    return_value = ReturnTo.CHALLENGE

    while return_value >= ReturnTo.CHALLENGE:
        stdscr.clear()
        stdscr.refresh()

        characters_copy_shuffled: list[Character] = [*characters]
        random.shuffle(characters_copy_shuffled)

        # Initialize QuestionGenerator. Pass in the copy of characters array,
        # Do not pass in original copy because the player might want to try again later
        question_gen = QuestionGenerator(
            topic,
            game_mode,
            characters_copy_shuffled
        )

        # Progress initialization
        progress_bar = ProgressBar.preset_shade(
            progress_win,
            maximum=len(characters),
            text_color=Color.YELLOW | curses.A_BOLD
        )

        # header
        title = 'Writing 书 写' if game_mode == GameMode.WRITING else \
                'Recognition 辨 识' if game_mode == GameMode.RECOGNITION else \
                'Mixed 混 合'
        draw_header(
            header_win,
            f"✰♫♪•*¨·٠•●♥✿  ▁▁▂▂▃▃▅▅▆▆▇▇  {title}  ▇▇▆▆▅▅▃▃▂▂▁▁  ✿♥●•٠·¨*•♪♫✰",
            text_color=Color.RED
        )


        # Question Loop
        for i, question in enumerate(question_gen):
            # Progress bar update
            progress_bar.update(i + 1)

            # Clear the windows before question number animates (blocking)
            menu_win.clear()
            menu_win.refresh()
            question_win.clear()
            question_win.refresh()
            answer_win.clear()
            answer_win.refresh()

            # Question number
            ExtendingText(
                question_no_win,
                f'Question {i+1}',
                delay=0.05,
                text_color=Color.BLUE | curses.A_BOLD
            ).run()

            # Question
            question_win.addstr( question.question, curses.A_BOLD )
            question_win.refresh()

            # Menu - Enclose in a loop to avoid redrawing the progress bar & questions
            # The question handlers return either True or False.
            # True - Continue to next question (Next iteration of for loop)
            # False - User selected "Quit". Continue to summary.
            if question.game_mode == GameMode.WRITING:
                if not writing_question_handler(question, menu_win, answer_win, prompt_win):
                    break
            else:
                if not recognition_question_handler(question, menu_win, answer_win, prompt_win):
                    break

        return_value = summary_route(stdscr, question_gen)
    return return_value






# Handles display and input for a GameMode.WRITING question
# Returns FALSE if the user selects to QUIT; True if user selects to proceed
def writing_question_handler(
    question: Question,
    menu_win,
    answer_win,
    prompt_win
):
    # Prompt window
    prompt_win.clear()
    prompt_win.addstr(
        "[Use UP/DOWN arrow to change selection.]\n"
        "[Use ENTER to select.]\n",
        Color.GREEN | curses.A_BOLD
    )
    prompt_win.refresh()

    # Menu handling
    menu = SelectionMenu(
        menu_win,
        ['Done. Proceed', 'Peek answer', 'Quit'],
        highlight_color=Color.CYAN
    )

    while True:
        value = menu.run()
        # Proceed
        if value == 0:
            return True
        # Peek answer
        elif value == 1:
            question.peeked = True
            answer_win.clear()
            answer_win.addstr(f"Answer: ({question.answer} )")
            answer_win.refresh()
        else:
            return False





# Handles display and input for a GameMode.RECOGNITION question
# Returns FALSE if the user selects to QUIT; True if user selects to proceed
def recognition_question_handler(
    question: Question,
    menu_win,
    answer_win,
    prompt_win
):
    # Prompt window
    prompt_win.clear()
    prompt_win.addstr(
        "[Use UP/DOWN arrow to change selection.]\n"
        "[Use ENTER to select.]\n"
        "[Type in the romaji, BACKSPACE to delete, and ENTER to proceed]",
        Color.GREEN | curses.A_BOLD
    )
    prompt_win.refresh()

    # Menu handling
    menu = Menu(menu_win)
    menu.add_menu_item('0', TextMenuItem.factory(
        'Enter the romaji: ',
        return_on_enter=True,
        highlight_color=Color.CYAN
    ))
    menu.add_menu_item('1', ButtonMenuItem.factory(
        'Peek Answer',
        lambda: MenuOption.PEEK_ANS,
        highlight_color=Color.CYAN
    ))
    menu.add_menu_item('2', ButtonMenuItem.factory(
        'Quit',
        lambda: MenuOption.CANCEL,
        highlight_color=Color.CYAN
    ))

    while True:
        value = menu.run()
        # Peek answer
        if value == MenuOption.PEEK_ANS:
            question.peeked = True
            answer_win.clear()
            answer_win.addstr(f"Answer: ({question.answer} )")
            answer_win.refresh()
        # Quit
        elif value == MenuOption.CANCEL: return False
        # Check answer, show the correct one and ask to press any key before proceeding.
        else:
            question.player_ans = value

            answer_win.clear()
            answer_win.addstr(f"Your answer is: ")
            answer_win.addstr(value, curses.A_BOLD)

            if value == question.answer:
                answer_win.addstr("\nYou answered correctly!", Color.GREEN | curses.A_BOLD)
            else:
                answer_win.addstr(f"\nThat is incorrect. Answer: ({question.answer} )", Color.RED | curses.A_BOLD)

            answer_win.addstr(f'\n\nPress any key to continue...', Color.YELLOW | curses.A_BOLD)
            answer_win.refresh()
            answer_win.getch()
            return True

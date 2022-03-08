# The route for summary on the challenge session
#
# <--------------Header-------------->
# <General summary>|<Pagination>
# <Prompt>         |

import curses

from src.utils.enums import Topic, ReturnTo, GameMode, MenuOption
from src.utils.colors import Color
from src.utils.question import QuestionGenerator, Question
from src.curses_menu import ExtendingText, TypedText, draw_header
from src.routes.return_route import return_route


def summary_route(stdscr, question_generator: QuestionGenerator):
    height, width = stdscr.getmaxyx()
    stdscr.clear()
    stdscr.refresh()

    # Derive general summary
    questions_answered = len(question_generator.records)
    questions_hiragana = sum(q.topic == Topic.HIRAGANA for q in question_generator.records)
    questions_katakana = sum(q.topic == Topic.KATAKANA for q in question_generator.records)
    questions_writing = sum(q.game_mode == GameMode.WRITING for q in question_generator.records)
    questions_recognition = sum(q.game_mode == GameMode.RECOGNITION for q in question_generator.records)
    questions_correct = sum(q.player_ans == q.answer for q in question_generator.records)
    questions_peeked = sum(q.peeked for q in question_generator.records)

    # Subwindowing
    LEFT_WIDTH = width // 2 - 5
    RIGHT_WIDTH = width // 2 + 1
    header_win = stdscr.derwin(5, width, 0, 0)
    summary_win = stdscr.derwin(18, LEFT_WIDTH, 6, 0)
    prompt_win = stdscr.derwin(6, LEFT_WIDTH, 17, 0)
    pagination_win = stdscr.derwin(height - 8, RIGHT_WIDTH, 6, width // 2 - 4)

    # Header
    draw_header(
        header_win,
        f"✰♫♪•*¨·٠•●♥✿  ▁▁▂▂▃▃▅▅▆▆▇▇  Summary 总 结  ▇▇▆▆▅▅▃▃▂▂▁▁  ✿♥●•٠·¨*•♪♫✰",
        text_color=Color.RED
    )

    # Summary (Fancy)
    ExtendingText(
        summary_win.derwin(1, LEFT_WIDTH, 0, 0),
        'Overall',
        delay=0.02,
        text_color=Color.YELLOW | curses.A_BOLD
    ).run()
    TypedText(
        summary_win.derwin(16, LEFT_WIDTH, 2, 0),
        f'Questions: {questions_answered}\n'
        f'Hiragana questions: {questions_hiragana}\n'
        f'Katakana questions: {questions_katakana}\n'
        f'Writing questions: {questions_writing}\n'
        f'Recognition questions: {questions_recognition}\n'
        f'Correct: {questions_correct}\n'
        f'Peeked at answer: {questions_peeked}',
        delay=0.001,
        text_color=Color.CYAN | curses.A_BOLD
    ).run()

    # Prompt
    prompt_win.addstr(
        '[LEFT/RIGHT arrow to flip pages]\n'
        '[ENTER key to continue]',
        Color.GREEN | curses.A_BOLD
    )
    prompt_win.refresh()

    # Pagination
    current_page = 0

    def draw_pagination():
        if questions_answered:
            pagination_win.clear()
            pagination_win.addstr(question_generator.records[current_page].get_summary())
            pagination_win.refresh()

    draw_pagination()

    # Key input
    while True:
        key = stdscr.getch()
        # Enter - Continue
        if key in (curses.KEY_ENTER, 10, 13):
            break
        # LEFT arrow
        elif key == curses.KEY_LEFT and questions_answered:
            current_page = questions_answered - 1 if current_page == 0 else current_page - 1
            draw_pagination()
        elif key == curses.KEY_RIGHT:
            current_page = (current_page + 1) % questions_answered
            draw_pagination()

    return return_route(stdscr)

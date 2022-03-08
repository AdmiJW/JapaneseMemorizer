import curses
from curses import wrapper

import sys
import traceback

from src.utils.colors import init_colors
from src.routes.topic_select import topic_select_route

# The general route for the program goes as follows:
#
#   (Topic select)
#        |
#   (Chapter select)
#        |
#   (--filter--)
#        |     \        \
#   (Writing)(Recognition)(Mixed) + Limit question number
#        |      /        /
#   (Challenge)
#        |
#   (Summary) #Scrollable
#        |
#   (Return to?)
#
# Some of the logic can be easily reused, therefore will be implemented in this route.

def main(stdscr):
    init_colors()
    curses.curs_set(0)  # Invisible cursor
    curses.noecho()  # No echo-ing of input characters

    topic_select_route(stdscr)


# TODO: Remove the development try...catch, or maybe no need?
if __name__ == '__main__':
    # To catch any error in the program execution and display to terminal on the error stack trace
    try:
        wrapper(main)
    except Exception as e:
        # Get current system exception
        ex_type, ex_value, ex_traceback = sys.exc_info()

        # Extract unformatter stack traces as tuples
        trace_back = traceback.extract_tb(ex_traceback)

        print("Exception type : %s " % ex_type.__name__)
        print("Exception message : %s" % ex_value)
        for trace in trace_back[-3:]:
            print(f"\nFile : {trace[0]}\n, Line : {trace[1]}\n, Func.Name : {trace[2]}\n, Message : {trace[3]}\n")

# Creates an effect of each character appearing one by one, when the run() is invoked.
# Note that run() is blocking and synchronous
import curses
import time



class TypedText:
    def __init__(
        self,
        screen,
        text: str,
        delay: float = 0.2,
        text_color: int = 0
    ):
        self._screen = screen
        self._text = text
        self._delay = delay
        self._text_color = text_color


    def run(self):
        self._screen.clear()

        for c in self._text:
            self._screen.addstr(c, self._text_color)
            self._screen.refresh()
            time.sleep(self._delay)
        # Flush away any input when animation is running
        curses.flushinp()



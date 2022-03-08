# Creates an effect of each character appearing one by one, when the run() is invoked.
# Note that run() is blocking and synchronous
import curses
import time



class ExtendingText:
    def __init__(
        self,
        screen,
        text: str,
        delay: float = 0.2,
        text_color: int = 0
    ):
        self._screen = screen
        self._sequence = (
            f'               {text}               ',
            f'            ▇  {text}  ▇            ',
            f'           ▇▇  {text}  ▇▇           ',
            f'          ▆▇▇  {text}  ▇▇▆          ',
            f'         ▆▆▇▇  {text}  ▇▇▆▆         ',
            f'        ▅▆▆▇▇  {text}  ▇▇▆▆▅        ',
            f'       ▅▅▆▆▇▇  {text}  ▇▇▆▆▅▅       ',
            f'      ▃▅▅▆▆▇▇  {text}  ▇▇▆▆▅▅▃      ',
            f'     ▃▃▅▅▆▆▇▇  {text}  ▇▇▆▆▅▅▃▃     ',
            f'    ▂▃▃▅▅▆▆▇▇  {text}  ▇▇▆▆▅▅▃▃▂    ',
            f'   ▂▂▃▃▅▅▆▆▇▇  {text}  ▇▇▆▆▅▅▃▃▂▂   ',
            f'   ▂▂▃▃▅▅▆▆▇▇  {text}  ▇▇▆▆▅▅▃▃▂▂   ',
            f'  ▁▂▂▃▃▅▅▆▆▇▇  {text}  ▇▇▆▆▅▅▃▃▂▂▁  ',
            f' ▁▁▂▂▃▃▅▅▆▆▇▇  {text}  ▇▇▆▆▅▅▃▃▂▂▁▁ ',
        )
        self._delay = delay
        self._text_color = text_color


    def run(self):
        for seq in self._sequence:
            self._screen.clear()
            self._screen.addstr(seq, self._text_color)
            self._screen.refresh()
            time.sleep(self._delay)
        # Flush away any input when animation is running
        curses.flushinp()




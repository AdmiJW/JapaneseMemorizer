from src.curses_menu.menu_item.IMenuItem import IMenuItem
import curses

# The simplest menu item button - One that can be selected and triggered using ENTER key.
#
# When the button is triggered by ENTER key while highlighted, the on_trigger callback is executed,
# and if the return value is not None, will return it from the key_listener() function, which causes
# the curses_menu instance to detect the menu operation is completed.
class ButtonMenuItem(IMenuItem):
    def __init__(
        self,
        window,
        text: str,
        on_trigger,
        text_color=0,
        highlight_color=0
    ):
        self._window = window                        # curses window
        self._text = text                            # button label
        self._on_trigger = on_trigger                # on_trigger callback function
        self._text_color = text_color                # button label color
        self._highlight_color = highlight_color      # button label (highlighted color)


    @staticmethod
    def factory(
        text: str,
        on_trigger,
        text_color=0,
        highlight_color=0
    ):
        return lambda window: ButtonMenuItem(window, text, on_trigger, text_color, highlight_color)


    def get_value(self): return self._on_trigger()


    def set_value(self, value): raise NotImplementedError("Cannot set value on ButtonMenuItem!")


    def key_listener(self, key: int):
        if key in (curses.KEY_ENTER, 10, 13):
            return self._on_trigger()


    def draw(self, highlighted: bool = False):
        self._window.clear()
        if highlighted:
            self._window.addstr(f'=> {self._text}', self._highlight_color | curses.A_BOLD)
        else:
            self._window.addstr(f'   {self._text}', self._text_color)
        self._window.refresh()


from src.curses_menu.menu.Menu import Menu
from src.curses_menu.menu_item.ButtonMenuItem import ButtonMenuItem


# Selection menu - one of the simplest types of menu, where user is provided with N options and they have to select
# one of them via ENTER key.
class SelectionMenu(Menu):
    def __init__(
        self,
        screen,
        choices: list[str],
        text_color=0,
        highlight_color=0
    ):
        super().__init__(screen)

        # Careful of lambda variable capturing:
        # https://stackoverflow.com/questions/33983980/lambda-in-for-loop-only-takes-last-value
        for i, choice in enumerate(choices):
            self.add_menu_item(str(i), ButtonMenuItem.factory(
                choice,
                lambda n=i: n,
                text_color=text_color,
                highlight_color=highlight_color
            ))

import curses
from src.curses_menu.menu_item.IMenuItem import IMenuItem
from src.curses_menu.menu.IMenu import IMenu


# The direct concrete implementation of IMenu: Does not fall under any specified categories of curses_menu,
# unlike SelectionMenu or CheckboxMenu
#
# All the MenuItems has to be added manually via add_menu_item(tag, factory). Then the menu has to be run().
# Although this involves more manual work, it provides greater flexibility as you can mix and match any MenuItems
# yourself
class Menu(IMenu):
    def __init__(self, screen):
        self._screen = screen
        self._item_dict: dict[str, IMenuItem] = dict()
        self._item_list: list[IMenuItem] = []
        self._position: int = 0



    def run(self):
        if not len(self._item_list):
            raise RuntimeError(f"The {__name__} is run() without any MenuItems!")

        while True:
            # Printing
            self._screen.clear()
            for i, v in enumerate(self._item_list):
                v.draw(i == self._position)
            self._screen.refresh()

            # Key input
            return_value = self.key_handler( self._screen.getch() )
            if return_value is not None: return return_value



    def key_handler(self, key):
        if key == curses.KEY_DOWN:
            self._position = (self._position + 1) % len(self._item_list)
        elif key == curses.KEY_UP:
            self._position = len(self._item_list) - 1 if self._position == 0 else self._position - 1
        else:
            return self._item_list[self._position].key_listener(key)



    def add_menu_item(self, tag: str, factory):
        if tag in self._item_dict:
            raise ValueError(f"Tag {tag} already exists in {__name__}!")

        derwin = self._screen.derwin(1, self._screen.getmaxyx()[1], len(self._item_list), 0)
        menu_item = factory(derwin)
        self._item_dict[tag] = menu_item
        self._item_list.append(menu_item)


    def get_menu_item(self, tag: str) -> IMenuItem:
        if tag not in self._item_dict:
            raise ValueError(f"Tag {tag} does not exist in {__name__}!")
        return self._item_dict[tag]



    def get_menu_item_dict(self) -> dict[str, IMenuItem]:
        return { k:v for k,v in self._item_dict }



    def get_menu_item_list(self) -> list[IMenuItem]:
        return [ *self._item_list ]


from src.utils.enums import MenuOption
from src.curses_menu.menu.Menu import Menu
from src.curses_menu.menu_item.CheckboxMenuItem import CheckboxMenuItem
from src.curses_menu.menu_item.ButtonMenuItem import ButtonMenuItem


# Checkbox menu - user is presented with N options where they can switch each one of them on or off.
# User will be presented with a cancel or proceed button as an exit to this menu or simply to move on
#
# In addition to the options provided through the constructor argument, the CheckboxMenu will provide
# 2 more buttons: OK (To proceed) and Cancel
#
# If user selects OK, run() will return a boolean list indicating the value of each checkbox options
# If user selects Cancel, run() will simply return CheckboxMenu.CANCEL
class CheckboxMenu(Menu):

    def __init__(
        self,
        screen,
        options: list[str],
        initial_values: list[bool] = None,
        text_color=0,
        highlight_color=0
    ):
        if initial_values is not None and len(initial_values) != len(options):
            raise RuntimeError(f"Length of checkbox initial values does not match length of options in {__name__}!")
        elif initial_values is None:
            initial_values = (False,) * len(options)

        super().__init__(screen)

        for i, option in enumerate(options):
            super().add_menu_item(str(i), CheckboxMenuItem.factory(
                option,
                initial_values[i],
                text_color=text_color,
                highlight_color=highlight_color
            ))
        # Select/Deselect all option
        self.add_menu_item(str(len(options)), ButtonMenuItem.factory(
            'Select/deselect all',
            lambda: MenuOption.SELECT_DESELECT,
            text_color=text_color,
            highlight_color=highlight_color
        ))
        # Ok button
        self.add_menu_item(str(len(options)+1), ButtonMenuItem.factory(
            'OK',
            lambda: MenuOption.OK,
            text_color=text_color,
            highlight_color=highlight_color
        ))
        # Cancel button
        self.add_menu_item(str(len(options)+2), ButtonMenuItem.factory(
            'Cancel',
            lambda: MenuOption.CANCEL,
            text_color=text_color,
            highlight_color=highlight_color
        ))


    # Need to return the list of boolean values of checkboxes if OK is pressed
    # If cancel is pressed, return CheckboxMenu.CANCEL
    # Otherwise whatever is returned will be returned
    def key_handler(self, key):
        return_value = super().key_handler(key)

        # OK pressed - Return a list of booleans indicating all checkbox values
        if return_value == MenuOption.OK:
            return [ i.get_value() for i in self._item_list[:-3] ]
        # Select all / Deselect all - Switch the checkboxes
        elif return_value == MenuOption.SELECT_DESELECT:
            any_selected = any( i.get_value() for i in self._item_list[:-3] )
            for i in self._item_list[:-3]: i.set_value( not any_selected )
        else: return return_value

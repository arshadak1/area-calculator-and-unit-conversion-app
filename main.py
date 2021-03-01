import math
import functions
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDFlatButton


class AreaWindow(Screen):
    # function to calculate area of triangle with three sides given
    area_total = 0  # initializing total area to zero

    def area(self):
        try:
            a1 = float(self.a.text)  # side a
            b1 = float(self.b.text)  # side b
            c1 = float(self.c.text)  # side c
            s = (a1 + b1 + c1) / 2
            ar = math.sqrt(s * (s - a1) * (s - b1) * (s - c1))  # Heron's Formulae
            AreaWindow.area_total += ar
            AreaWindow.area_total = round(AreaWindow.area_total, 3)
            self.result.text = str(AreaWindow.area_total) + ' m\u00b2'
        # when an invalid input is entered a pop up will appear
        except Exception:
            close = MDFlatButton(text="Close", on_release=self.dialog_close)
            self.dialog = MDDialog(title="Value Error", text="Invalid Input", size_hint=(0.7, 1), buttons=[close])
            self.dialog.open()

    def dialog_close(self, obj):
        # when 'Close' button in dialog box pressed, it will call this function
        self.dialog.dismiss()


class ConversionWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MainApp(MDApp):
    # main app
    # the ids present in the .kv files
    a = ObjectProperty(None)
    b = ObjectProperty(None)
    c = ObjectProperty(None)
    result = ObjectProperty(None)
    window = ObjectProperty(None)
    # initializing variables used in the app
    dropdown1 = None
    dropdown2 = None
    unit1 = None
    unit2 = None

    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.build_app = Builder.load_file('strings.kv')  # loads the .kv file and stores it in the variable

        # items in the dropdown list of conversion screen
        item = [{'text': i, "callback": self.callback1} for i in ('sq ft', 'sq m', 'cent', 'ares')]
        # dropdown menu of the 'From' button in the conversion screen
        self.dropdown1 = MDDropdownMenu(width_mult=3,
                                        caller=self.build_app.window.get_screen('conversion').ids.drop1,
                                        items=item, callback=self.callback1)
        # dropdown menu of the 'To' button in the conversion screen
        self.dropdown2 = MDDropdownMenu(width_mult=3,
                                        caller=self.build_app.window.get_screen('conversion').ids.drop2,
                                        items=item, callback=self.callback2)

    def callback1(self, unit):
        # function called when a list item of the 'From' button is pressed
        self.root.window.get_screen('conversion').ids.drop1.text = unit.text  # the text in the button is changed
        self.unit1 = unit.text  # the text in the selected menu item is saved
        self.dropdown1.dismiss()  # closes the dropdown menu after a menu item is selected

    def callback2(self, unit):
        # function called when a list item of the 'To' button is pressed
        self.root.window.get_screen('conversion').ids.drop2.text = unit.text  # the text in the button is changed
        self.unit2 = unit.text  # the text in the selected menu item is saved
        self.dropdown1.dismiss()  # closes the dropdown menu after a menu item is selected

    def conv(self):

        # function called when 'CONVERT' button is pressed
        if self.unit1 is None or self.unit2 is None:  # when no units are chosen, dialog box will appear
            close = MDFlatButton(text="Close", on_release=self.dialog_close)  # close button for the dialog box
            self.dialog = MDDialog(title="Unit Error", text="Select units", size_hint=(0.7, 1), buttons=[close])
            self.dialog.open()

        else:
            try:
                # conversion from one unit to the other
                value = float(self.root.window.get_screen('conversion').ids.unity.text)
                # conversion function from the functions module
                res = round(functions.conversion(self.unit1, self.unit2, value), 3)
                self.root.window.get_screen('conversion').ids.convert.text = f'{str(res)} {self.unit2}'

            except Exception:
                # when the input value is invalid(not a number) dialog box will appear
                close = MDFlatButton(text="Close", on_release=self.dialog_close)
                self.dialog = MDDialog(title="Value Error", text="Invalid Input", size_hint=(0.7, 1), buttons=[close])
                self.dialog.open()

    def dialog_close(self, obj):
        # to close the dialog box when 'Close' button is pressed
        self.dialog.dismiss()

    def build(self):
        Window.size = (360, 600)
        return self.build_app  # returning the loaded .kv file

    def to_convert(self, ins):
        # function to change the screen the floating action button is pressed
        self.root.current = 'conversion'

    def to_area(self, ins):
        # function to change the screen the floating action button is pressed
        self.root.current = 'areawindow'
        self.root.transition.direction = "right"


if __name__ == '__main__':
    MainApp().run()

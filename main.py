from kivy.properties import ListProperty, NumericProperty, StringProperty, ObjectProperty, BooleanProperty
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition, SlideTransition, FadeTransition, \
    WipeTransition, RiseInTransition
from kivymd.app import MDApp
import random
from kivy.core.window import Window
from kivymd.uix.list import OneLineIconListItem, OneLineAvatarIconListItem, TwoLineIconListItem, TwoLineListItem

from bt import finddevices, connectdevice

Window.size = (400, 800)

class HomeScreen(Screen):
    pass


class FullList(TwoLineIconListItem):
    text = StringProperty()
    secondary_text = StringProperty()



class MainApp(MDApp):

    def on_start(self):
        self.theme_cls.set_colors(
            "Teal", "500", "200", "800", "BlueGray", "500", "200", "800"
        )

        self.title = "i-Cricket"
        self.overlay_color = self.theme_cls.accent_dark
        self.progress_round_color = self.theme_cls.accent_light
        abc = finddevices()
        for addr, name in abc:
            self.root.ids.home_screen.ids.listv.add_widget(FullList(text=f'{addr}', secondary_text=f'{name}'))

    def change_screen(self, from_screen, screen_name, direction='forward', mode=""):
        # Get the screen manager from the kv file.
        screen_manager = self.root.ids.screen_manager

        if direction == "None":
            screen_manager.transition = NoTransition()
            screen_manager.current = screen_name
            return

        screen_manager.current = screen_name

        if screen_name == "home_screen":
            pass
            # self.root.ids.titlename.title = "Impromtu Cricket"

    def connect_bt(self,addr,name):
        print(addr,name)
        connectdevice(addr)

MainApp().run()

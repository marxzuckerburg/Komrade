from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.app import App
import asyncio
from kivymd.uix.dialog import MDDialog
from comrad.app.screens.dialog import MDDialog2


### Layout

### Base screens
class BaseScreen(MDScreen):

    def on_pre_enter(self):
        # self.clear_widgets()
        # if hasattr(self.app,'msg_dialog') and self.app.msg_dialog:
            
            # self.root.remove_widget(self.app.msg_dialog)
        # if hasattr(self.app,'msg_dialog0') and self.app.msg_dialog0: self.root.remove_widget(self.app.msg_dialog0)
        # self.app.clear_widget_tree(MDDialog)
        # self.app.clear_widget_tree(MDDialog2)
        # self.log('app',self.app)
        # screen_name = self.app.root.scr_mngr.current
        # self.log('screen_name',self.app.screen)
        pass

    @property
    def root(self):
        return self.app.root

    @property
    def app(self):
        return App.get_running_app()

    def log(self,*x,**y):
        return self.app.log(*x)

    @property
    def channel(self):
        return self.app.channel

    def stat(self,*x,**y): return self.app.stat(*x,**y)







class ProtectedScreen(BaseScreen):
    def on_pre_enter(self):
        super().on_pre_enter()
        if not hasattr(self.app,'is_logged_in') or not self.app.is_logged_in or not hasattr(self.app,'comrad') or not self.app.comrad:
            self.root.change_screen('login')
            self.log('changing screen???')
            return None
        return True
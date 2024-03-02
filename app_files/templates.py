import random
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.graphics import Line,Color
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import ScreenManager

from kivymd.uix.widget import MDWidget
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard

bg_colors={
    "bg_one":get_color_from_hex("#27374D"),
    "bg_two":get_color_from_hex("#DDE6ED"),
    "bg_three":get_color_from_hex("#526D82"),
    "bg_four":get_color_from_hex("#9DB2BF"),
    "bg_five":get_color_from_hex("#FFFFFF")
}
text_colors={
    "txt_one":get_color_from_hex("#1597BB"),
    "txt_two":get_color_from_hex("#FF4C29"),
    "txt_three":get_color_from_hex("#EEEEEE"),
    "txt_four":get_color_from_hex("#46C2CB")
}


class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super(Manager,self).__init__(**kwargs)
        self.homescreen=HomeScreen(
            name="homescreen"
        )
        self.createscreen=CreateTask(
            name="createtask"
        )
        self.add_widget(self.createscreen)
class HomeScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super(HomeScreen,self).__init__(*args, **kwargs)
        self.grid_task:MDWidget=self.ids["grid_task"]
        self.progress:MDWidget=self.ids["progress"]
        self.task_categories=[
            "Personal",
            "Health",
            "Study",
            "Social",
            "Work"
        ]
        for category in self.task_categories:
            task_card=TaskCard()
            self.grid_task.add_widget(task_card)

        with self.progress.canvas:
            Color(
                rgb=bg_colors["bg_two"]
            )
            Line(
                points=(self.progress.x+dp(5),self.progress.center_y,Window.width-dp(30),self.progress.center_y),
                width=dp(4)
            )
            Color(
                rgb=bg_colors["bg_one"]
            )
            Line(
                points=(self.progress.x+dp(5),self.progress.center_y,random.randrange(self.progress.x+dp(5),Window.width-dp(30)),self.progress.center_y),
                width=dp(3)
            )

class CreateTask(MDScreen):
    pass
# components
    
class TaskCard(MDCard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.c_progess=self.ids["c_progress"]
        with self.c_progess.canvas:
            Color(
                rgb=bg_colors["bg_two"]
            )
            Line(
                circle=(Window.width-dp(40),self.c_progess.y,dp(13)),
                width=dp(3)
            )
            Color(
                rgb=text_colors["txt_two"]
            )
            Line(
                circle=(Window.width-dp(40),self.c_progess.y,dp(13),0,random.randrange(10,360)),
                width=dp(2)
            )

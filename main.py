
from kivy.factory import Factory
from kaki.app import App
from kivymd.app import MDApp
class HotReload(App,MDApp):
    CLASSES={'Manager':'app_files.templates'}
    KV_FILES=['kivy_files/kivy_lang.kv',"kivy_files/components.kv"]
    AUTORELOADER_PATHS=[('app_files',{'recursive':True}),('kivy_files',{'recursive':True})]
    AUTORELOADER_IGNORE_PATTERNS=["todo_app*"]
    def build_app(self):
        return Factory.Manager()

if __name__=='__main__':
    HotReload().run()

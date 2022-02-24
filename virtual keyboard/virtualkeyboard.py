import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.vkeyboard import Vkeyboard
class test(Vkeyboard):
    player = Vkeyboard(App)
class VkeyboardApp(App):
    def build(self):
        return test()
if __name__ == '__main__':
    Vkeyboard().run()
    
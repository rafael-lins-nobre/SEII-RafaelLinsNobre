from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout #https://kivy.org/doc/stable/api-kivy.uix.boxlayout.html
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

class MyRootWidget(BoxLayout):
    pass
# Para funcionar com o .kv, tem que ser criada essa classe de widget

class MyApp(App):
    def build(self): #It needs to have a class named build that receives as atribute the APP (imported module)        
        return MyRootWidget()

if __name__ == "__main__":
    MyApp().run()

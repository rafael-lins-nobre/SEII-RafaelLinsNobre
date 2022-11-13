from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # Adicionando widgets na janela

        # Image widget
        self.window.add_widget(Image(source="gorillaz.jpg"))

        # Label widget
        self.greeting = Label(
            text="Qual o seu nome?",
            font_size=18,
            color='#FF8C00'
        )
        self.window.add_widget(self.greeting)

        # Text input widget
        self.user = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(1, 0.5)
        )
        self.window.add_widget(self.user)

        # Button widget
        self.button = Button(
            text="GREET",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#FF8C00',
            background_normal='')
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        self.greeting.text = "Ola " + self.user.text + "!"


if __name__ == "__main__":
    SayHello().run()
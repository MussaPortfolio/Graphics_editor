from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.widget import Widget

# Установка параметров окна программы
# Config.set('graphics', 'resizable', '0') # Заблокировать разворот окна на весь экран
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')


class GraphEditApp(App):
    def upload_img(self, instance):
        path = self.path.text
        self.im_in.source = path
        self.im_in.reload()

    def contrast_plus(self):
        pass

    def contrast_minus(self):
        pass

    def bregtnes_plus(self):
        pass

    def bregtnes_minus(self):
        pass

    def build(self):
        padding_param = 10
        bl = BoxLayout(orientation='vertical', padding=padding_param)
        bl1 = BoxLayout(orientation='horizontal', padding=0, spacing=5)
        bl2 = BoxLayout(orientation='horizontal', padding=[0, padding_param, 0, padding_param], spacing=5)
        bl3 = BoxLayout(orientation='horizontal', padding=[0, 0, 0, padding_param], spacing=5)
        bl4 = BoxLayout(orientation='horizontal', padding=0, spacing=5)

        al = AnchorLayout(anchor_x='center', anchor_y='center', size_hint=(3, 0.3))
        self.path = TextInput(text='3', font_size=30, halign='center', size_hint=(1, 1))
        al.add_widget(self.path)
        bl1.add_widget(al)

        al = AnchorLayout(anchor_x='center', anchor_y='center', size_hint=(1, 0.3))
        al.add_widget(Button(text='Upload', on_press=self.upload_img))
        bl1.add_widget(al)

        self.im_in = Image(source='logotip.jpg')
        Clock.schedule_interval(lambda dt: self.im_in.reload(), 0.2)
        bl2.add_widget(self.im_in)

        self.im_out = Image(source='logotip.jpg')
        bl2.add_widget(self.im_out)

        al = AnchorLayout(anchor_x='center', anchor_y='center', size_hint=(.8, 0.4))
        self.koef = TextInput(text='Коэффициент', font_size=30, halign='center', size_hint=(.4, 1))
        al.add_widget(self.koef)
        bl3.add_widget(al)

        bl4.add_widget(Button(text='Contrast+'))
        bl4.add_widget(Button(text='Contrast-'))
        bl4.add_widget(Button(text='bregtnes+'))
        bl4.add_widget(Button(text='bregtnes-'))

        bl.add_widget(bl1)
        bl.add_widget(bl2)
        bl.add_widget(bl3)
        bl.add_widget(bl4)

        return bl


if __name__ == '__main__':
    GraphEditApp().run()

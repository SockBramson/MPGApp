from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button



class mpgcalc(App):
    def build(self):
        b = BoxLayout()
        g = GridLayout(cols=2,
                        row_default_height = '40dp',
                        row_force_default = True)
        l1 = Label(text='Miles')
        t1 = TextInput(id = 'miles',
                        hint_text = 'Enter mileage',
                        input_type = 'number',
                        input_filter = 'float')
        l2 = Label(text = 'Gallons')
        t2 = TextInput(id = 'gallons',
                        hint_text = 'Enter gallons',
                        input_type = 'number',
                        input_filter = 'float')
        b.add_widget(g)
        g.add_widget(l1)
        g.add_widget(t1)
        g.add_widget(l2)
        g.add_widget(t2)
        return b


if __name__ == "__main__":
    mpgcalc().run()

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout

    #    miles = 277.89
    #    gallons = 11.275
    #    print(round(miles / gallons, 2))
 
class MPGCalculator(App):
    def mpg():
        miles = ObjectProperty()
        gallons = ObjectProperty()
      
        print(round(miles / gallons, 2))
 
MPGCalculator().run()

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from io import open
#import os
import time

# Builder.load_string("""
# <Calc>:
#     # These are attributes of the class Calc now
#     miles: _miles
#     gallons: _gallons
#     mpg: _mpg
#     AnchorLayout:
#         anchor_x: 'center'
#         anchor_y: 'top'
#         ScreenManager:
#             size_hint: 1, .9
#             id: _screen_manager
#             Screen:
#                 name: 'screen1'
#                 GridLayout:
#                     cols:1
#                     TextInput:
#                         id: _miles
#                         focus: True
#                         input_filter: float #This doesn't seem to work.
#                         hint_text: 'Enter mileage'
#                     TextInput:
#                         id: _gallons
#                         hint_text: 'Enter gallons'
#                     Label:
#                         id: _mpg
#                     Button:
#                         text: 'Direct'
#                         # You can do the opertion directly
#                         on_press: _mpg.text = str(float(_miles.text) / float(_gallons.text))
#                     Button:
#                         text: 'Function'
#                         # Or you can call a method from the root class (instance of calc)
#                         on_press: root.mpgs(*args)
#             Screen:
#                 name: 'screen2'
#                 Label: 
#                     text: 'The second screen'
#     AnchorLayout:
#         anchor_x: 'center'
#         anchor_y: 'bottom'
#         BoxLayout:
#             orientation: 'horizontal'
#             size_hint: 1, .1
#             Button:
#                 text: 'Go to Screen 1'
#                 on_press: _screen_manager.current = 'screen1'
#             Button:
#                 text: 'Go to Screen 2'
#                 on_press: _screen_manager.current = 'screen2'""")

class Calc(FloatLayout):
    # define the multiplication of a function
    def mpgs(self, instance):
        # self.result, self.a and self.b where defined explicitely in the kv
        units = ' MPGs'
        miles = self.miles.text
        gallons = self.gallons.text
        if float(miles) > 0 and float(gallons) > 0:
            self.mpg.text = str(
                            round(
                                float(
                                    miles) / float(gallons), 2)
                                    ) + '{}'.format(units
                                        )
        if float(miles) == 0 or float(gallons) == 0:
            self.mpg.txt = 'Divide by zero? '


    
    # def storevalue(m, g, mpgs):
    #     save_file = self.user_data_dir + '\mpg.csv'
    #     secs = str(int(time.time())) # need a string, but converted to int to remove decimals.
    #     payload = ",".join(secs, m, g, mpgs).encode('utf-8')
    #     with open(save_file, 'a+b') as f:  # 'with' opens the file and closes the file. 'a+' append and 'b' binary, just in case.
    #         f.write(payload + '\n')            

# class Store():
#     def storevalue(m, g, mpgs):
#         save_file = self.user_data_dir + '\mpg.csv'
#         secs = str(int(time.time())) # need a string, but converted to int to remove decimals.
#         payload = ",".join(secs, m, g, mpgs).encode('utf-8')
#         with open(save_file, 'a+b') as f:  # 'with' opens the file and closes the file. 'a+' append and 'b' binary, just in case.
#             f.write(payload + '\n')


class MPGApp(App):
    def build(self):
        save_file = self.user_data_dir + '\mpg.csv'
        print save_file
        _calc = Calc()
        m = _calc.miles.text
        g = _calc.gallons.text
        mpgs = _calc
        print m
        print g
        print mpgs
        secs = str(int(time.time())) # need a string, but converted to int to remove decimals.
        payload = secs.encode('utf-8') #",".join(secs, m, g, mpgs).encode('utf-8')
        with open(save_file, 'a+b') as f:  # 'with' opens the file and closes the file. 'a+' append and 'b' binary, just in case.
            f.write(payload + ',' + m + ',' + g + '\n') # Can't include m and g because they have not value until after function runs.
            #f.write(g)
            #f.write(mpgs)
            #f.write(payload + '\n')
        #storage = Store()75
        #_calc = Calc()
        #storage.storevalue(_calc.miles.text, _calc.gallons.text, _calc)
        return Calc()



if __name__ == '__main__':
    MPGApp().run()
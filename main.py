from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from io import open
import time

class num_input(FloatLayout):
    
    def mpgs(self, instance):
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

class MPGApp(App):
    
    def build(self):
        save_file = self.user_data_dir + '\mpg.csv'
        print save_file
        _num_input = num_input()
        m = _num_input.miles.text
        g = _num_input.gallons.text
        mpgs = _num_input
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
        #_num_input = num_input()
        #storage.storevalue(_num_input.miles.text, _num_input.gallons.text, _num_input)
        return num_input()

if __name__ == '__main__':
    MPGApp().run()
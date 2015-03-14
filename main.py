#!/usr/bin/kivy
import kivy
kivy.require('1.8.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
#from io import open
import time
import sqlite3


class num_input(BoxLayout):
    
    def mpgs(self, instance):
        units = ' MPGs'
        miles = self.miles.text
        gallons = self.gallons.text
        print(miles)
        if float(miles) > 0 and float(gallons) > 0:
            self.mpg.text = str(
                            round(
                                float(
                                    miles) / float(gallons), 2)
                                    ) + '{}'.format(units
                                        )
        elif float(miles) == 0 or float(gallons) == 0:
            self.mpg.txt = 'Divide by zero? '
        else:
            self.mpg.txt = 'Input not recognized. '

    def history(self, instance):
        save_file = (self.user_data_dir + '\mpg.db')
        db = sqlite3.connect(save_file)
        c = db.cursor()
        layout = GridLayout(cols=4)
        for row in c.execute('SELECT * FROM mpgs ORDER BY tsepoch'):
            for field in row:
                x = 1
                field = row[x]
                x += 1
                layout.add_widget(Label(text = field))


class MPGApp(App):
    
    def build(self):
        return num_input()

    def dbstore(self, miles, gallons, mpgs):
        mpgs = mpgs.replace(' MPGs','')
        secs = int(time.time()) # converted to int to remove decimals.
        save_file = (self.user_data_dir + '\mpg.db')
        db = sqlite3.connect(save_file)
        c = db.cursor()
        # Create table
        c.execute('''CREATE TABLE IF NOT EXISTS mpgs(tsepoch INTEGER, miles REAL, gallons REAL, mpg REAL)''')
        # The following two lines convert epoch time to human readable, for future reference:
        #ts = time.time()
        #datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        c.execute('''INSERT INTO mpgs VALUES(?,?,?,?)''', (secs, miles, gallons, mpgs))
        db.commit()
        db.close()
   



if __name__ == '__main__':
    MPGApp().run()

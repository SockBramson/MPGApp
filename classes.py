# learning classes.
import time
import os.path

fame = 'values.csv'
floc = 'C:\\Users\\marielr\\AppData\\Roaming\mpg\\'


class derta(object):
    '''data received as a result of our mpg calcs.

    attributes:
    miles: float of miles driven since last fill up.
    gallons: float of gallons purchased.
    date: the date of fill up.
    mpg: float of the current miles divided by current gallons.
    '''

    def __init__(self, miles, gallons):
        self.miles = miles
        self.gallons = gallons
        secs = str(int(time.time())) # need a string, but converted to int to remove decimals.
        self.date = secs # .encode('utf-8')

    def mpg(self):
        if self.gallons >= 1 and self.miles >= 1:
            mpgs = self.miles / self.gallons
            return str(round(mpgs, 2))
        else:
            raise RuntimeError("Value is empty")

class sterage(object):
    ''' Where we are saving stuff. 
    Attributes:
    location: where to save this.
    data: what to save.
    '''
    terst = derta(261.23, 11.161)
    payload = ",".join([terst.date, terst.mpg(), str(terst.miles), str(terst.gallons)])

    def __init__(self, fname, flocation):
        self.fname = fname
        self.flocation = flocation 

    def fread(self):
        save_file = self.flocation + self.fname
        with open(save_file, 'rb') as f:  # 'with' opens the file and closes the file. 'a+' append and 'b' binary, just in case.
            data = f.read()
        return data

    def fwrite(self, payload):
        save_file = self.flocation + self.fname
        with open(save_file, 'a+b') as f:  # 'with' opens the file and closes the file. 'a+' append and 'b' binary, just in case.
            f.write(bytes(payload + '\n', 'utf-8'))

    def fexists(self, flocation):
        save_file = self.flocation + self.fname
        os.path.isfile(save_file)



#print(terst.mpg())
#print(terst.date)
#sterst = sterage('values.csv', 'C:\\Users\\marielr\\AppData\\Roaming\mpg\\')
# sterst = sterage(fame, floc)

# sterst.fwrite(payload)
# print(sterst.fread())


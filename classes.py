import time
import os.path

fame = 'values.csv'
floc = 'C:\\Users\\marielr\\AppData\\Roaming\mpg\\'


class calc(object):
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
        self.mpgs = self.mpg()

    def mpg(self):
        if self.gallons >= 1 and self.miles >= 1:
            mpgs = self.miles / self.gallons
            return str(round(mpgs, 2))
        else:
            raise RuntimeError("Value is empty")

class storage(object):
    ''' Where we are saving stuff. 
    Attributes:
    fname: name of file
    flocation: where to save this.
    payload: what to save.
    save_file: path and filename
    '''
    
    def __init__(self, fname, flocation, payload):
        self.fname = fname
        self.flocation = flocation
        self.payload = payload
        self.save_file = self.flocation + self.fname
        
    
    def fread(self):
        with open(self.save_file, 'rb') as f:  # 'with' opens the file and closes the file. 'r' to read and 'b' binary, just in case.
            data = f.read()
            return data

    def fwrite(self):
        with open(self.save_file, 'a+b') as f:  # 'with' opens the file and closes the file. 'w' to overwrite, a+ to append and 'b' binary, just in case.
            f.write(bytes(self.payload + '\n', 'utf-8'))
        
    def fexists(self):
        if os.path.isfile(self.save_file) == False:
            default_payload = "Date,MPG,Miles,Gallons"
            with open(self.save_file, 'wb') as f:
                f.write(bytes(default_payload + '\n', 'utf-8'))
        
                
                

class pload(object):
    ''' The data written to file.

    Attributes:
    date: current time of calculations
    mpgs: result of calculations.
    miles: Miles driven
    Gallons: Gallons used.
    '''

    def __init__(self, miles, gallons):
        #secs = str(int(time.time())) # need a string, but converted to int to remove decimals.
        self.date = time.strftime("%d/%m/%Y") #secs # .encode('utf-8')
        self.miles = str(calc(miles, gallons).miles)
        self.gallons = str(calc(miles, gallons).gallons)
        self.mpgs = str(calc(miles, gallons).mpgs)

    def final(self):
        payload = ",".join([self.date, self.mpgs, self.miles, self.gallons])
        return payload


pload_input = pload(251.0, 19.121).final()
storage_object = storage(fame, floc, pload_input)
storage_object.fexists()
storage_object.fwrite()
print(storage_object.fread())
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.garden.graph import Graph, MeshLinePlot

graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
        x_ticks_major=25, y_ticks_major=1,
        y_grid_label=True, x_grid_label=True, padding=5,
        x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-1, ymax=1)
plot = MeshLinePlot(color=[1, 0, 0, 1])
plot.points = [(x, sin(x / 10.)) for x in xrange(0, 101)]
graph.add_plot(plot)

    #    miles = 277.89
    #    gallons = 11.275
    #    print(round(miles / gallons, 2))
 


class ScatterTextWidget(App):
    def build(self):
        return ScatterTextWidget()
    #def mpg():
     #   miles = ObjectProperty()
      #  gallons = ObjectProperty()
      
       # print(round(miles / gallons, 2))

if __name__ == "__main__":
    TutorialApp().run() 

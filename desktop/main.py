import sys
import pyqtgraph as pg
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from numpy import random
import requests
from API.api import data_init

from GUI.GUI import Ui_MainWindow


class MainWindow(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.show()

        self.ui.actionClose.triggered.connect(self.close)
        self.ui.actionNew.triggered.connect(self.new_instance)

        self.timer = qtc.QTimer()
        self.temp_pen = pg.mkPen(color=(255, 0, 0), width=1)
        self.humidity_pen = pg.mkPen(color=(0, 255, 0), width=1)

        self.temp_timer = qtc.QTimer()
        self.humidity_timer = qtc.QTimer()
        
        self.ui.temp_graph.setBackground('w')
        self.ui.temp_graph.showGrid(x=True, y=True)
        self.ui.temp_graph.setLabel('left', 'Temperature', units='°C')
        self.ui.temp_graph.setLabel('bottom', 'Time', units='timestamp')

        self.ui.humidity_graph.setBackground('w')
        self.ui.humidity_graph.showGrid(x=True, y=True)
        self.ui.humidity_graph.setLabel('left', 'Humidity', units='%')
        self.ui.humidity_graph.setLabel('bottom', 'Time', units='timestamp')
        self.ui.temperature_btn.clicked.connect(self.plot_temp)
        self.ui.humidity_btn.clicked.connect(self.plot_humidity)

        self.graph = {"temp": {"graph": self.ui.temp_graph, "pen": self.temp_pen, "timer": self.temp_timer, "data": [], "timestamp": 0},
                    "humidity": {"graph": self.ui.humidity_graph, "pen": self.humidity_pen, "timer": self.humidity_timer}}

        self.upToDatePlots = {"temp": None, "humidity": None}
        self.pointsToAppend = {"temp": 0, "humidity": 0}

    def new_instance(self) -> None:
        self.child_window = MainWindow()
        self.child_window.show()

    def plot_temp(self, channel: str) -> None:
        list_of_readings = []

        temp = data_init('temp', self.graph["temp"]["timestamp"])
        for i in range(len(temp)):
            list_of_readings.append(temp[i][channel])
        self.graph[channel]["timestamp"] = temp[-1]["timestamp"]
        self.graph[channel]["data"].append(list_of_readings)

        self.plot_graph(channel)

    def plot_graph(self, channel: str) -> None:
        self.upToDatePlots[channel] = self.graph[channel]["graph"].plot(
            self.graph[channel]["timer"], self.amplitude[channel], name='Temperature', pen=self.graph[channel]["pen"])
        self.graphChannels[channel].plotItem.setLimits(
            xMin=0, xMax=1.0, yMin=min(self.amplitude[channel]), yMax=max(self.amplitude[channel]))

        self.pointsToAppend[channel] = 0
        self.graph[channel]["timer"].setInterval(500)
        self.graph[channel]["timer"].timeout.connect(lambda: self.updatePlot(channel))
        self.graph[channel]["timer"].start()

    def updatePlot(self, channel: str) -> None:
        xaxis = self.time[channel][:self.pointsToAppend[channel]]
        yaxis = self.amplitude[channel][:self.pointsToAppend[channel]]
        self.pointsToAppend[channel] += 20
        if self.pointsToAppend[channel] > len(self.time[channel]):
            self.graph[channel]["timer"].stop()

        if self.time[channel][self.pointsToAppend[channel]] > 1.0:
            self.graph[channel]["graph"].setLimits(xMax=max(
                xaxis, default=0))
        self.graph[channel]["graph"].plotItem.setXRange(
            max(xaxis, default=0)-1.0, max(xaxis, default=0))

        self.upToDatePlots[channel].setData(xaxis, yaxis)

    def plot_Temp(self):
        self.ui.humidity_graph.clear()
        self.temp_pen = pg.mkPen(color=(0, 0, 0))
        response = requests.get(
        "https://remote-monitoring-api.herokuapp.com/readings/temp",json={
        "timestamp": "0"
            })
        list_of_temp=[]
        for i in range(len(response.json()['temperatures'])):
            list_of_temp.append(list(response.json()['temperatures'][i].values())[1])
        # y=random.randint(1000, size=(100))
        x = list(range(1,len(list_of_temp)))
        self.plot = self.ui.temp_graph.plot(x, list_of_temp,pen = self.pen)
    def plot_Humidity(self):
        self.ui.temp_graph.clear()
        self.pen = pg.mkPen(color=(0, 0, 0))
        y=random.randint(1000, size=(100))
        x = list(range(1,100+1))
        self.plot = self.ui.humidity_graph.plot(x, y,pen = self.pen)



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())

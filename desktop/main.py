import sys
import pyqtgraph as pg
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from API.api import fetch_data

from GUI.GUI import Ui_RemoteMonitoringService


class MainWindow(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_RemoteMonitoringService()
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
        self.ui.temperature_btn.clicked.connect(
            lambda: self.plot_sensor("temp"))
        self.ui.humidity_btn.clicked.connect(
            lambda: self.plot_sensor("humidity"))
        self.ui.reset_btn.clicked.connect(self.reset_graphs)

        self.graph = {"temp": {"graph": self.ui.temp_graph, "pen": self.temp_pen, "timer": self.temp_timer, "data": [], "time": [], "timestamp": 0, "name": "Temperature", "unit": "°C"},
                      "humidity": {"graph": self.ui.humidity_graph, "pen": self.humidity_pen, "timer": self.humidity_timer, "data": [], "time": [], "timestamp": 0, "name": "Humidity", "unit": "%"}}

        self.upToDatePlots = {"temp": None, "humidity": None}
        self.pointsToAppend = {"temp": 0, "humidity": 0}

    def new_instance(self) -> None:
        self.child_window = MainWindow()
        self.child_window.show()

    def plot_sensor(self, channel: str) -> None:
        list_of_readings = []

        temp = fetch_data(channel, self.graph[channel]["timestamp"])
        if temp:
            for i in range(len(temp)):
                list_of_readings.append(
                    temp[i]["temperature" if channel == "temp" else "humidity"])
            self.graph[channel]["timestamp"] = temp[-1]["timestamp"]
            for i in range(len(list_of_readings)):
                self.graph[channel]["data"].append(list_of_readings[i])

            self.graph[channel]["time"] = [i for i in range(
                1, len(self.graph[channel]["data"]) + 1)]

            self.plot_graph(channel)
        else:
            for graphType, graphComponents in self.graph.items():
                if graphType == channel:
                    continue
                else:
                    graphComponents["timer"].stop()

    def plot_graph(self, channel: str) -> None:
        for graphType, graphComponents in self.graph.items():
            if graphType == channel:
                continue
            else:
                graphComponents["timer"].stop()

        self.upToDatePlots[channel] = self.graph[channel]["graph"].plot(
            self.graph[channel]["time"], self.graph[channel]["data"], name=self.graph[channel]["name"], pen=self.graph[channel]["pen"])
        self.graph[channel]["graph"].plotItem.setLimits(
            xMin=0, xMax=100, yMin=min(self.graph[channel]["data"]), yMax=max(self.graph[channel]["data"]))

        self.pointsToAppend[channel] = 0
        self.graph[channel]["timer"].setInterval(1000)
        self.graph[channel]["timer"].timeout.connect(
            lambda: self.updatePlot(channel))
        self.graph[channel]["timer"].start()

    def updatePlot(self, channel: str) -> None:
        xaxis = self.graph[channel]["time"][:self.pointsToAppend[channel]]
        yaxis = self.graph[channel]["data"][:self.pointsToAppend[channel]]
        self.pointsToAppend[channel] += 1
        if self.pointsToAppend[channel] > len(self.graph[channel]["time"]):
            self.graph[channel]["timer"].stop()

            self.plot_sensor(channel)

        self.upToDatePlots[channel].setData(xaxis, yaxis)

    def reset_graphs(self) -> None:
        for graphType, graphComponents in self.graph.items():
            graphComponents["timer"].stop()
            graphComponents["data"] = []
            graphComponents["time"] = []
            graphComponents["timestamp"] = 0
            self.upToDatePlots[graphType] = None
            self.pointsToAppend[graphType] = 0
            graphComponents["graph"].clear()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())

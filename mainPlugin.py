from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
from qgis.gui import QgsVertexMarker
from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtGui import QIcon
from PyQt5.QtGui import QColor
from qgis.core import QgsGeometry, QgsPointXY
from random import randrange


# # initialize Qt resources from file resources.py
# from . import resources

class TestPlugin:

  def __init__(self, iface):
    # save reference to the QGIS interface
    self.iface = iface


  def initGui(self):
    # create action that will start plugin configuration
    self.action = QAction(QIcon(":/plugins/testplug/icon.png"), "Test plugin", self.iface.mainWindow())
    self.action.setObjectName("testAction")
    self.action.setWhatsThis("Configuration for test plugin")
    self.action.setStatusTip("This is status tip")
    self.action.triggered.connect(self.run)

    vertex_items = [ i for i in self.iface.mapCanvas().scene().items() if issubclass(type(i), QgsVertexMarker)]
    for ver in vertex_items:
        if ver in self.iface.mapCanvas().scene().items():
            self.iface.mapCanvas().scene().removeItem(ver)


    # add toolbar button and menu item
    self.iface.addToolBarIcon(self.action)
    self.iface.addPluginToMenu("&Test plugins", self.action)

    # connect to signal renderComplete which is emitted when canvas
    # rendering is done
    self.iface.mapCanvas().renderComplete.connect(self.renderTest)
	


  def unload(self):
    # remove the plugin menu item and icon
    self.iface.removePluginMenu("&Test plugins", self.action)
    self.iface.removeToolBarIcon(self.action)
    vertex_items = [ i for i in self.iface.mapCanvas().scene().items() if issubclass(type(i), QgsVertexMarker)]
    for ver in vertex_items:
        if ver in self.iface.mapCanvas().scene().items():
            self.iface.mapCanvas().scene().removeItem(ver)
    # disconnect form signal of the canvas
    self.iface.mapCanvas().renderComplete.disconnect(self.renderTest)

  def run(self):
    print("TestPlugin: run called!")

  def renderTest(self, painter):
    m = QgsVertexMarker(self.iface.mapCanvas())
    m.setCenter(QgsPointXY(float(randrange(4000000)), float(5000000)))
    m.setColor(QColor(0, 255, 0))
    m.setIconSize(5)
    m.setIconType(QgsVertexMarker.ICON_BOX) # or ICON_CROSS, ICON_X
    m.setPenWidth(3)

    # use painter for drawing to map canvas
    print("TestPlugin: renderTest called!")
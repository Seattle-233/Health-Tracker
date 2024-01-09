# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DataInterface(object):
    def setupUi(self, DataInterface):
        DataInterface.setObjectName("DataInterface")
        DataInterface.resize(993, 672)
        self.gridLayout = QtWidgets.QGridLayout(DataInterface)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(966, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TitleLabel = TitleLabel(DataInterface)
        self.TitleLabel.setProperty("pixelFontSize", 50)
        self.TitleLabel.setObjectName("TitleLabel")
        self.horizontalLayout.addWidget(self.TitleLabel)
        self.themeButton = ToolButton(DataInterface)
        self.themeButton.setObjectName("themeButton")
        self.horizontalLayout.addWidget(self.themeButton)
        self.GitHubButton = ToolButton(DataInterface)
        self.GitHubButton.setObjectName("GitHubButton")
        self.horizontalLayout.addWidget(self.GitHubButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(DataInterface)
        self.stackedWidget.setObjectName("stackedWidget")
        self.caloriesPage = QtWidgets.QWidget()
        self.caloriesPage.setObjectName("caloriesPage")
        self.caloriesGridLayout = QtWidgets.QGridLayout(self.caloriesPage)
        self.caloriesGridLayout.setObjectName("caloriesGridLayout")
        self.caloriesCardWidget = CardWidget(self.caloriesPage)
        self.caloriesCardWidget.setObjectName("caloriesCardWidget")
        self.verticalLayout_1_1 = QtWidgets.QVBoxLayout(self.caloriesCardWidget)
        self.verticalLayout_1_1.setObjectName("verticalLayout_1_1")
        self.caloriesGridLayout.addWidget(self.caloriesCardWidget, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.caloriesPage)
        self.floorPage = QtWidgets.QWidget()
        self.floorPage.setObjectName("floorPage")
        self.floorGridLayout = QtWidgets.QGridLayout(self.floorPage)
        self.floorGridLayout.setObjectName("floorGridLayout")
        self.floorCardGridLayout = QtWidgets.QGridLayout()
        self.floorCardGridLayout.setObjectName("floorCardGridLayout")
        self.caloriesCardWidget1 = CardWidget(self.floorPage)
        self.caloriesCardWidget1.setObjectName("caloriesCardWidget1")
        self.verticalLayout_2_1 = QtWidgets.QVBoxLayout(self.caloriesCardWidget1)
        self.verticalLayout_2_1.setObjectName("verticalLayout_2_1")
        self.floorCardGridLayout.addWidget(self.caloriesCardWidget1, 0, 0, 1, 1)
        self.floorGridLayout.addLayout(self.floorCardGridLayout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.floorPage)
        self.distancePage = QtWidgets.QWidget()
        self.distancePage.setObjectName("distancePage")
        self.distanceGridLayout = QtWidgets.QGridLayout(self.distancePage)
        self.distanceGridLayout.setObjectName("distanceGridLayout")
        self.distanceCardGridLayout = QtWidgets.QGridLayout()
        self.distanceCardGridLayout.setObjectName("distanceCardGridLayout")
        self.caloriesCardWidget2 = CardWidget(self.distancePage)
        self.caloriesCardWidget2.setObjectName("caloriesCardWidget2")
        self.verticalLayout_3_1 = QtWidgets.QVBoxLayout(self.caloriesCardWidget2)
        self.verticalLayout_3_1.setObjectName("verticalLayout_3_1")
        self.distanceCardGridLayout.addWidget(self.caloriesCardWidget2, 0, 0, 1, 1)
        self.distanceGridLayout.addLayout(self.distanceCardGridLayout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.distancePage)
        self.stepPage = QtWidgets.QWidget()
        self.stepPage.setObjectName("stepPage")
        self.stepGridLayout = QtWidgets.QGridLayout(self.stepPage)
        self.stepGridLayout.setObjectName("stepGridLayout")
        self.stepCardGridLayout = QtWidgets.QGridLayout()
        self.stepCardGridLayout.setObjectName("stepCardGridLayout")
        self.caloriesCardWidget3 = CardWidget(self.stepPage)
        self.caloriesCardWidget3.setObjectName("caloriesCardWidget3")
        self.verticalLayout_4_1 = QtWidgets.QVBoxLayout(self.caloriesCardWidget3)
        self.verticalLayout_4_1.setObjectName("verticalLayout_4_1")
        self.stepCardGridLayout.addWidget(self.caloriesCardWidget3, 0, 0, 1, 1)
        self.stepGridLayout.addLayout(self.stepCardGridLayout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.stepPage)
        self.gridLayout.addWidget(self.stackedWidget, 3, 0, 1, 1)
        self.pivot = SegmentedWidget(DataInterface)
        self.pivot.setAutoFillBackground(False)
        self.pivot.setObjectName("pivot")
        self.gridLayout.addWidget(self.pivot, 2, 0, 1, 1)

        self.retranslateUi(DataInterface)
        QtCore.QMetaObject.connectSlotsByName(DataInterface)

    def retranslateUi(self, DataInterface):
        _translate = QtCore.QCoreApplication.translate
        DataInterface.setWindowTitle(_translate("DataInterface", "Form"))
        self.TitleLabel.setText(_translate("DataInterface", "My Data"))
from qfluentwidgets import CardWidget, SegmentedWidget, TitleLabel, ToolButton

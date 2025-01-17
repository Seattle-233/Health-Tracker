# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Study\University\Y2T1\OOP\Health-Tracker\health_tracker\health_app_pyqt\ui\device_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DeviceInterface(object):
    def setupUi(self, DeviceInterface):
        DeviceInterface.setObjectName("DeviceInterface")
        DeviceInterface.resize(1003, 462)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DeviceInterface.sizePolicy().hasHeightForWidth())
        DeviceInterface.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(DeviceInterface)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(966, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.TitleLabel = TitleLabel(DeviceInterface)
        self.TitleLabel.setProperty("pixelFontSize", 50)
        self.TitleLabel.setObjectName("TitleLabel")
        self.horizontalLayout_4.addWidget(self.TitleLabel)
        self.themeButton = ToolButton(DeviceInterface)
        self.themeButton.setObjectName("themeButton")
        self.horizontalLayout_4.addWidget(self.themeButton)
        self.GitHubButton = ToolButton(DeviceInterface)
        self.GitHubButton.setObjectName("GitHubButton")
        self.horizontalLayout_4.addWidget(self.GitHubButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.deviceCard1 = SimpleCardWidget(DeviceInterface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deviceCard1.sizePolicy().hasHeightForWidth())
        self.deviceCard1.setSizePolicy(sizePolicy)
        self.deviceCard1.setMinimumSize(QtCore.QSize(0, 100))
        self.deviceCard1.setMaximumSize(QtCore.QSize(16777215, 60))
        self.deviceCard1.setObjectName("deviceCard1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.deviceCard1)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.deviceIcon1 = IconWidget(self.deviceCard1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deviceIcon1.sizePolicy().hasHeightForWidth())
        self.deviceIcon1.setSizePolicy(sizePolicy)
        self.deviceIcon1.setMinimumSize(QtCore.QSize(60, 60))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\Study\\University\\Y2T1\\OOP\\Health-Tracker\\health_tracker\\health_app_pyqt\\ui\\../resource/images/icon/smartwatch-app.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deviceIcon1.setIcon(icon)
        self.deviceIcon1.setObjectName("deviceIcon1")
        self.horizontalLayout_2.addWidget(self.deviceIcon1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.deviceName1 = TitleLabel(self.deviceCard1)
        self.deviceName1.setObjectName("deviceName1")
        self.verticalLayout_2.addWidget(self.deviceName1)
        self.deviceDescrp1 = BodyLabel(self.deviceCard1)
        self.deviceDescrp1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.deviceDescrp1.setObjectName("deviceDescrp1")
        self.verticalLayout_2.addWidget(self.deviceDescrp1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.deviceButton1 = PrimaryDropDownToolButton(self.deviceCard1)
        self.deviceButton1.setObjectName("deviceButton1")
        self.horizontalLayout_2.addWidget(self.deviceButton1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addWidget(self.deviceCard1)
        self.deviceCard2 = SimpleCardWidget(DeviceInterface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deviceCard2.sizePolicy().hasHeightForWidth())
        self.deviceCard2.setSizePolicy(sizePolicy)
        self.deviceCard2.setMinimumSize(QtCore.QSize(0, 100))
        self.deviceCard2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.deviceCard2.setObjectName("deviceCard2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.deviceCard2)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.deviceIcon2 = IconWidget(self.deviceCard2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deviceIcon2.sizePolicy().hasHeightForWidth())
        self.deviceIcon2.setSizePolicy(sizePolicy)
        self.deviceIcon2.setMinimumSize(QtCore.QSize(60, 60))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("d:\\Study\\University\\Y2T1\\OOP\\Health-Tracker\\health_tracker\\health_app_pyqt\\ui\\../resource/images/icon/smart-band.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deviceIcon2.setIcon(icon1)
        self.deviceIcon2.setObjectName("deviceIcon2")
        self.horizontalLayout_3.addWidget(self.deviceIcon2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.deviceName2 = TitleLabel(self.deviceCard2)
        self.deviceName2.setObjectName("deviceName2")
        self.verticalLayout_3.addWidget(self.deviceName2)
        self.deviceDescrp2 = BodyLabel(self.deviceCard2)
        self.deviceDescrp2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.deviceDescrp2.setObjectName("deviceDescrp2")
        self.verticalLayout_3.addWidget(self.deviceDescrp2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.deviceButton2 = PrimaryDropDownToolButton(self.deviceCard2)
        self.deviceButton2.setObjectName("deviceButton2")
        self.horizontalLayout_3.addWidget(self.deviceButton2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout.addWidget(self.deviceCard2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addDeviceButton = PrimaryToolButton(DeviceInterface)
        self.addDeviceButton.setMinimumSize(QtCore.QSize(50, 50))
        self.addDeviceButton.setObjectName("addDeviceButton")
        self.horizontalLayout.addWidget(self.addDeviceButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DeviceInterface)
        self.deviceButton1.clicked.connect(self.deviceCard1.hide) # type: ignore
        self.deviceButton2.clicked.connect(self.deviceCard2.hide) # type: ignore
        self.addDeviceButton.clicked.connect(self.deviceCard1.show) # type: ignore
        self.addDeviceButton.clicked.connect(self.deviceCard2.show) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DeviceInterface)

    def retranslateUi(self, DeviceInterface):
        _translate = QtCore.QCoreApplication.translate
        DeviceInterface.setWindowTitle(_translate("DeviceInterface", "Form"))
        self.TitleLabel.setText(_translate("DeviceInterface", "My Device"))
        self.deviceName1.setText(_translate("DeviceInterface", "Apple Watch Series 9"))
        self.deviceDescrp1.setText(_translate("DeviceInterface", "Smart Watch"))
        self.deviceButton1.setText(_translate("DeviceInterface", "Remove"))
        self.deviceName2.setText(_translate("DeviceInterface", "Mi Band 7"))
        self.deviceDescrp2.setText(_translate("DeviceInterface", "Smart Band"))
        self.deviceButton2.setText(_translate("DeviceInterface", "Remove"))
from qfluentwidgets import BodyLabel, IconWidget, PrimaryDropDownToolButton, PrimaryToolButton, SimpleCardWidget, TitleLabel, ToolButton

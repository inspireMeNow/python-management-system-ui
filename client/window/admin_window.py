import json
import ssl

from PyQt6 import QtCore, QtGui, QtWidgets
import random

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox, QCheckBox, QItemDelegate, QPushButton
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from utils import client_encrypt
from pojo.user import User
import socket


class Ui_admin_window(object):
    def __init__(self, admin_window):
        self.setupUi(admin_window)

    def setupUi(self, part_window):
        # for i in range(9):
        #     if i == 0:
        #         self.label = QtWidgets.QLabel('人员管理')
        #     elif i == 1:
        #         self.label = QtWidgets.QLabel('登录管理')
        #     elif i == 2:
        #         self.label = QtWidgets.QLabel('仓库管理')
        #     elif i == 3:
        #         self.label = QtWidgets.QLabel('货架管理')
        #     elif i == 4:
        #         self.label = QtWidgets.QLabel('电脑配件信息管理')
        #     elif i == 5:
        #         self.label = QtWidgets.QLabel('库存管理')
        #     elif i == 6:
        #         self.label = QtWidgets.QLabel('入库订单管理')
        #     elif i == 7:
        #         self.label = QtWidgets.QLabel('出库订单管理')
        #     else:
        #         self.label = QtWidgets.QLabel('')
        # label.setAlignment(Qt.AlignCenter)
        # 设置label的背景颜色(这里随机)
        # 这里加了一个margin边距(方便区分QStackedWidget和QLabel的颜色)
        # label.setStyleSheet('background: rgb(%d, %d, %d);margin: 50px;' % (
        #     randint(0, 255), randint(0, 255), randint(0, 255)))
        #     self.label.setStyleSheet('background: rgb(%d, %d, %d);margin: 50px;' % (
        #         random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        #     self.stackedWidget.addWidget(self.label)

        part_window.setObjectName("part_window")
        part_window.resize(854, 601)
        self.treeView = QtWidgets.QTreeView(parent=part_window)
        self.treeView.setGeometry(QtCore.QRect(0, 0, 211, 601))
        self.treeView.setObjectName("treeView")
        self.treeView.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        font = QtGui.QFont()
        font.setFamily("文鼎ＰＬ简中楷")
        font.setPointSize(13)
        self.treeView.setObjectName("treeView")
        # 创建 StandardItemModel 实例，用于存储数据
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['duan'])

        # 初始化模型数据
        items = [
            ('用户管理', '人员管理', '登录管理'),
            ('设施管理', '仓库管理', '货架管理'),
            ('存储管理', '电脑配件信息管理', '库存管理'),
            ('订单管理', '入库订单管理', '出库订单管理'),
        ]
        for name, desc, qty in items:
            # 创建节点，并设置文本和元数据
            parent = QtGui.QStandardItem(name)
            parent.setEditable(False)
            parent.appendRow([QtGui.QStandardItem(desc)])
            parent.appendRow([QtGui.QStandardItem(qty)])

            # 将父节点加入到模型中
            self.model.appendRow(parent)

        # 将模型设置为 TreeView 的数据源
        self.treeView.setModel(self.model)
        self.treeView.selectionModel().selectionChanged.connect(self.change_ui)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=part_window)
        self.stackedWidget.setGeometry(QtCore.QRect(210, 0, 641, 601))
        self.stackedWidget.setObjectName("stackedWidget")

        for i in range(9):
            match i:
                case 0:
                    self.page = QtWidgets.QWidget()
                    self.page.setObjectName("page")
                    _translate = QtCore.QCoreApplication.translate
                    self.label = QtWidgets.QLabel(parent=self.page)
                    self.label.setGeometry(QtCore.QRect(20, 10, 111, 61))
                    font = QtGui.QFont()
                    font.setPointSize(20)
                    self.label.setFont(font)
                    self.label.setObjectName("label")
                    self.label_3 = QtWidgets.QLabel(parent=self.page)
                    self.label_3.setGeometry(QtCore.QRect(20, 60, 81, 31))
                    font = QtGui.QFont()
                    font.setPointSize(15)
                    self.label_3.setFont(font)
                    self.label_3.setObjectName("label_3")
                    self.lineEdit = QtWidgets.QLineEdit(parent=self.page)
                    self.lineEdit.setGeometry(QtCore.QRect(470, 100, 113, 21))
                    self.lineEdit.setObjectName("lineEdit")
                    self.toolButton = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton.setGeometry(QtCore.QRect(590, 100, 42, 20))
                    self.toolButton.setObjectName("toolButton")
                    self.toolButton_3 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_3.setGeometry(
                        QtCore.QRect(20, 100, 42, 20))
                    self.toolButton_3.setObjectName("toolButton_3")
                    self.tableView_0 = QtWidgets.QTableView(parent=self.page)
                    self.tableView_0.setGeometry(
                        QtCore.QRect(0, 131, 651, 401))
                    self.tableView_0.setObjectName("tableView")
                    self.label.setText(_translate("part_window", "用户管理"))
                    self.label_3.setText(_translate("part_window", "人员管理"))
                    self.lineEdit.setPlaceholderText(
                        _translate("part_window", "输入工号查询"))
                    self.toolButton.setText(_translate("part_window", "搜索"))
                    self.toolButton_3.setText(_translate("part_window", "新建"))
                    self.toolButton_4 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_4.setGeometry(
                        QtCore.QRect(70, 100, 42, 20))
                    self.toolButton_4.setObjectName("toolButton_4")
                    self.toolButton_5 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_5.setGeometry(
                        QtCore.QRect(120, 100, 42, 20))
                    self.toolButton_5.setObjectName("toolButton_5")
                    self.toolButton_4.setText(_translate("part_window", "查询"))
                    self.toolButton_5.setText(_translate("part_window", "修改"))
                    self.toolButton_6 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_6.setGeometry(
                        QtCore.QRect(170, 100, 42, 20))
                    self.toolButton_6.setObjectName("toolButton_6")
                    self.toolButton_6.setText(_translate("part_window", "删除"))

                case 1:
                    self.page = QtWidgets.QWidget()
                    self.page.setObjectName("page")
                    _translate = QtCore.QCoreApplication.translate
                    self.label = QtWidgets.QLabel(parent=self.page)
                    self.label.setGeometry(QtCore.QRect(20, 10, 111, 61))
                    font = QtGui.QFont()
                    font.setPointSize(20)
                    self.label.setFont(font)
                    self.label.setObjectName("label")
                    self.label_3 = QtWidgets.QLabel(parent=self.page)
                    self.label_3.setGeometry(QtCore.QRect(20, 60, 81, 31))
                    font = QtGui.QFont()
                    font.setPointSize(15)
                    self.label_3.setFont(font)
                    self.label_3.setObjectName("label_3")
                    self.lineEdit = QtWidgets.QLineEdit(parent=self.page)
                    self.lineEdit.setGeometry(QtCore.QRect(470, 100, 113, 21))
                    self.lineEdit.setObjectName("lineEdit")
                    self.toolButton = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton.setGeometry(QtCore.QRect(590, 100, 42, 20))
                    self.toolButton.setObjectName("toolButton")
                    self.toolButton_3 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_3.setGeometry(
                        QtCore.QRect(20, 100, 42, 20))
                    self.toolButton_3.setObjectName("toolButton_3")
                    self.tableView_1 = QtWidgets.QTableView(parent=self.page)
                    self.tableView_1.setGeometry(
                        QtCore.QRect(0, 131, 651, 401))
                    self.tableView_1.setObjectName("tableView")
                    self.label.setText(_translate("part_window", "用户管理"))
                    self.label_3.setText(_translate("part_window", "登录管理"))
                    self.lineEdit.setPlaceholderText(
                        _translate("part_window", "输入工号查询"))
                    self.toolButton.setText(_translate("part_window", "搜索"))
                    self.toolButton_3.setText(_translate("part_window", "新建"))
                    self.toolButton_4 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_4.setGeometry(
                        QtCore.QRect(70, 100, 42, 20))
                    self.toolButton_4.setObjectName("toolButton_4")
                    self.toolButton_5 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_5.setGeometry(
                        QtCore.QRect(120, 100, 42, 20))
                    self.toolButton_5.setObjectName("toolButton_5")
                    self.toolButton_4.setText(_translate("part_window", "查询"))
                    self.toolButton_5.setText(_translate("part_window", "修改"))
                    self.toolButton_6 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_6.setGeometry(
                        QtCore.QRect(170, 100, 42, 20))
                    self.toolButton_6.setObjectName("toolButton_6")
                    self.toolButton_6.setText(_translate("part_window", "删除"))
                    self.toolButton_4.clicked.connect(self.find_all_user)
                    self.toolButton_6.clicked.connect(self.delete_user_by_id)
                    self.toolButton_3.clicked.connect(self.insert_user)

                case 2:
                    self.page = QtWidgets.QWidget()
                    self.page.setObjectName("page")
                    _translate = QtCore.QCoreApplication.translate
                    self.label = QtWidgets.QLabel(parent=self.page)
                    self.label.setGeometry(QtCore.QRect(20, 10, 111, 61))
                    font = QtGui.QFont()
                    font.setPointSize(20)
                    self.label.setFont(font)
                    self.label.setObjectName("label")
                    self.label_3 = QtWidgets.QLabel(parent=self.page)
                    self.label_3.setGeometry(QtCore.QRect(20, 60, 81, 31))
                    font = QtGui.QFont()
                    font.setPointSize(15)
                    self.label_3.setFont(font)
                    self.label_3.setObjectName("label_3")
                    self.lineEdit = QtWidgets.QLineEdit(parent=self.page)
                    self.lineEdit.setGeometry(QtCore.QRect(470, 100, 113, 21))
                    self.lineEdit.setObjectName("lineEdit")
                    self.toolButton = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton.setGeometry(QtCore.QRect(590, 100, 42, 20))
                    self.toolButton.setObjectName("toolButton")
                    self.toolButton_3 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_3.setGeometry(
                        QtCore.QRect(20, 100, 42, 20))
                    self.toolButton_3.setObjectName("toolButton_3")
                    self.tableView_2 = QtWidgets.QTableView(parent=self.page)
                    self.tableView_2.setGeometry(
                        QtCore.QRect(0, 131, 651, 401))
                    self.tableView_2.setObjectName("tableView")

                    self.label.setText(_translate("part_window", "设施管理"))
                    self.label_3.setText(_translate("part_window", "仓库管理"))
                    self.lineEdit.setPlaceholderText(
                        _translate("part_window", "输入仓库号查询"))
                    self.toolButton.setText(_translate("part_window", "搜索"))
                    self.toolButton_3.setText(_translate("part_window", "新建"))
                    self.toolButton_4 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_4.setGeometry(
                        QtCore.QRect(70, 100, 42, 20))
                    self.toolButton_4.setObjectName("toolButton_4")
                    self.toolButton_5 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_5.setGeometry(
                        QtCore.QRect(120, 100, 42, 20))
                    self.toolButton_5.setObjectName("toolButton_5")
                    self.toolButton_4.setText(_translate("part_window", "查询"))
                    self.toolButton_5.setText(_translate("part_window", "修改"))
                    self.toolButton_6 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_6.setGeometry(
                        QtCore.QRect(170, 100, 42, 20))
                    self.toolButton_6.setObjectName("toolButton_6")
                    self.toolButton_6.setText(_translate("part_window", "删除"))

                case 3:
                    self.page = QtWidgets.QWidget()
                    self.page.setObjectName("page")
                    _translate = QtCore.QCoreApplication.translate
                    self.label = QtWidgets.QLabel(parent=self.page)
                    self.label.setGeometry(QtCore.QRect(20, 10, 111, 61))
                    font = QtGui.QFont()
                    font.setPointSize(20)
                    self.label.setFont(font)
                    self.label.setObjectName("label")
                    self.label_3 = QtWidgets.QLabel(parent=self.page)
                    self.label_3.setGeometry(QtCore.QRect(20, 60, 81, 31))
                    font = QtGui.QFont()
                    font.setPointSize(15)
                    self.label_3.setFont(font)
                    self.label_3.setObjectName("label_3")
                    self.lineEdit = QtWidgets.QLineEdit(parent=self.page)
                    self.lineEdit.setGeometry(QtCore.QRect(470, 100, 113, 21))
                    self.lineEdit.setObjectName("lineEdit")
                    self.toolButton = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton.setGeometry(QtCore.QRect(590, 100, 42, 20))
                    self.toolButton.setObjectName("toolButton")
                    self.toolButton_3 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_3.setGeometry(
                        QtCore.QRect(20, 100, 42, 20))
                    self.toolButton_3.setObjectName("toolButton_3")
                    self.tableView_3 = QtWidgets.QTableView(parent=self.page)
                    self.tableView_3.setGeometry(
                        QtCore.QRect(0, 131, 651, 401))
                    self.tableView_3.setObjectName("tableView")
                    self.label.setText(_translate("part_window", "设施管理"))
                    self.label_3.setText(_translate("part_window", "货架管理"))
                    self.lineEdit.setPlaceholderText(
                        _translate("part_window", "输入货架类型查询"))
                    self.toolButton.setText(_translate("part_window", "搜索"))
                    self.toolButton_3.setText(_translate("part_window", "新建"))
                    self.toolButton_4 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_4.setGeometry(
                        QtCore.QRect(70, 100, 42, 20))
                    self.toolButton_4.setObjectName("toolButton_4")
                    self.toolButton_5 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_5.setGeometry(
                        QtCore.QRect(120, 100, 42, 20))
                    self.toolButton_5.setObjectName("toolButton_5")
                    self.toolButton_4.setText(_translate("part_window", "查询"))
                    self.toolButton_5.setText(_translate("part_window", "修改"))
                    self.toolButton_6 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_6.setGeometry(
                        QtCore.QRect(170, 100, 42, 20))
                    self.toolButton_6.setObjectName("toolButton_6")
                    self.toolButton_6.setText(_translate("part_window", "删除"))

                case 4:
                    self.page = QtWidgets.QWidget()
                    self.page.setObjectName("page")
                    _translate = QtCore.QCoreApplication.translate
                    self.label = QtWidgets.QLabel(parent=self.page)
                    self.label.setGeometry(QtCore.QRect(20, 10, 111, 61))
                    font = QtGui.QFont()
                    font.setPointSize(20)
                    self.label.setFont(font)
                    self.label.setObjectName("label")
                    self.label_3 = QtWidgets.QLabel(parent=self.page)
                    self.label_3.setGeometry(QtCore.QRect(20, 60, 161, 31))
                    font = QtGui.QFont()
                    font.setPointSize(15)
                    self.label_3.setFont(font)
                    self.label_3.setObjectName("label_3")
                    self.lineEdit = QtWidgets.QLineEdit(parent=self.page)
                    self.lineEdit.setGeometry(QtCore.QRect(470, 100, 113, 21))
                    self.lineEdit.setObjectName("lineEdit")
                    self.toolButton = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton.setGeometry(QtCore.QRect(590, 100, 42, 20))
                    self.toolButton.setObjectName("toolButton")
                    self.toolButton_3 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_3.setGeometry(
                        QtCore.QRect(20, 100, 42, 20))
                    self.toolButton_3.setObjectName("toolButton_3")
                    self.tableView_4 = QtWidgets.QTableView(parent=self.page)
                    self.tableView_4.setGeometry(
                        QtCore.QRect(0, 131, 651, 401))
                    self.tableView_4.setObjectName("tableView")
                    self.label.setText(_translate("part_window", "存储管理"))
                    self.label_3.setText(_translate("part_window", "电脑配件信息管理"))
                    self.lineEdit.setPlaceholderText(
                        _translate("part_window", "输入产品类型查询"))
                    self.toolButton.setText(_translate("part_window", "搜索"))
                    self.toolButton_3.setText(_translate("part_window", "新建"))
                    self.toolButton_4 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_4.setGeometry(
                        QtCore.QRect(70, 100, 42, 20))
                    self.toolButton_4.setObjectName("toolButton_4")
                    self.toolButton_5 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_5.setGeometry(
                        QtCore.QRect(120, 100, 42, 20))
                    self.toolButton_5.setObjectName("toolButton_5")
                    self.toolButton_4.setText(_translate("part_window", "查询"))
                    self.toolButton_5.setText(_translate("part_window", "修改"))
                    self.toolButton_6 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_6.setGeometry(
                        QtCore.QRect(170, 100, 42, 20))
                    self.toolButton_6.setObjectName("toolButton_6")
                    self.toolButton_6.setText(_translate("part_window", "删除"))

                case 5:
                    self.page = QtWidgets.QWidget()
                    self.page.setObjectName("page")
                    _translate = QtCore.QCoreApplication.translate
                    self.label = QtWidgets.QLabel(parent=self.page)
                    self.label.setGeometry(QtCore.QRect(20, 10, 111, 61))
                    font = QtGui.QFont()
                    font.setPointSize(20)
                    self.label.setFont(font)
                    self.label.setObjectName("label")
                    self.label_3 = QtWidgets.QLabel(parent=self.page)
                    self.label_3.setGeometry(QtCore.QRect(20, 60, 81, 31))
                    font = QtGui.QFont()
                    font.setPointSize(15)
                    self.label_3.setFont(font)
                    self.label_3.setObjectName("label_3")
                    self.lineEdit = QtWidgets.QLineEdit(parent=self.page)
                    self.lineEdit.setGeometry(QtCore.QRect(470, 100, 113, 21))
                    self.lineEdit.setObjectName("lineEdit")
                    self.toolButton = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton.setGeometry(QtCore.QRect(590, 100, 42, 20))
                    self.toolButton.setObjectName("toolButton")
                    self.toolButton_3 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_3.setGeometry(
                        QtCore.QRect(20, 100, 42, 20))
                    self.toolButton_3.setObjectName("toolButton_3")
                    self.tableView_5 = QtWidgets.QTableView(parent=self.page)
                    self.tableView_5.setGeometry(
                        QtCore.QRect(0, 131, 651, 401))
                    self.tableView_5.setObjectName("tableView")
                    self.label.setText(_translate("part_window", "存储管理"))
                    self.label_3.setText(_translate("part_window", "库存管理"))
                    self.lineEdit.setPlaceholderText(
                        _translate("part_window", "输入产品类型查询"))
                    self.toolButton.setText(_translate("part_window", "搜索"))
                    self.toolButton_3.setText(_translate("part_window", "新建"))
                    self.toolButton_4 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_4.setGeometry(
                        QtCore.QRect(70, 100, 42, 20))
                    self.toolButton_4.setObjectName("toolButton_4")
                    self.toolButton_5 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_5.setGeometry(
                        QtCore.QRect(120, 100, 42, 20))
                    self.toolButton_5.setObjectName("toolButton_5")
                    self.toolButton_4.setText(_translate("part_window", "查询"))
                    self.toolButton_5.setText(_translate("part_window", "修改"))
                    self.toolButton_6 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_6.setGeometry(
                        QtCore.QRect(170, 100, 42, 20))
                    self.toolButton_6.setObjectName("toolButton_6")
                    self.toolButton_6.setText(_translate("part_window", "删除"))

                case 6:
                    self.page = QtWidgets.QWidget()
                    self.page.setObjectName("page")
                    _translate = QtCore.QCoreApplication.translate
                    self.label = QtWidgets.QLabel(parent=self.page)
                    self.label.setGeometry(QtCore.QRect(20, 10, 111, 61))
                    font = QtGui.QFont()
                    font.setPointSize(20)
                    self.label.setFont(font)
                    self.label.setObjectName("label")
                    self.label_3 = QtWidgets.QLabel(parent=self.page)
                    self.label_3.setGeometry(QtCore.QRect(20, 60, 81, 31))
                    font = QtGui.QFont()
                    font.setPointSize(15)
                    self.label_3.setFont(font)
                    self.label_3.setObjectName("label_3")
                    self.lineEdit = QtWidgets.QLineEdit(parent=self.page)
                    self.lineEdit.setGeometry(QtCore.QRect(470, 100, 113, 21))
                    self.lineEdit.setObjectName("lineEdit")
                    self.toolButton = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton.setGeometry(QtCore.QRect(590, 100, 42, 20))
                    self.toolButton.setObjectName("toolButton")
                    self.toolButton_3 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_3.setGeometry(
                        QtCore.QRect(20, 100, 42, 20))
                    self.toolButton_3.setObjectName("toolButton_3")
                    self.tableView_6 = QtWidgets.QTableView(parent=self.page)
                    self.tableView_6.setGeometry(
                        QtCore.QRect(0, 131, 651, 401))
                    self.tableView_6.setObjectName("tableView")

                    self.label.setText(_translate("part_window", "订单管理"))
                    self.label_3.setText(_translate("part_window", "入库订单管理"))
                    self.lineEdit.setPlaceholderText(
                        _translate("part_window", "输入订单号查询"))
                    self.toolButton.setText(_translate("part_window", "搜索"))
                    self.toolButton_3.setText(_translate("part_window", "新建"))
                    self.toolButton_4 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_4.setGeometry(
                        QtCore.QRect(70, 100, 42, 20))
                    self.toolButton_4.setObjectName("toolButton_4")
                    self.toolButton_5 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_5.setGeometry(
                        QtCore.QRect(120, 100, 42, 20))
                    self.toolButton_5.setObjectName("toolButton_5")
                    self.toolButton_4.setText(_translate("part_window", "查询"))
                    self.toolButton_5.setText(_translate("part_window", "修改"))
                    self.toolButton_6 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_6.setGeometry(
                        QtCore.QRect(170, 100, 42, 20))
                    self.toolButton_6.setObjectName("toolButton_6")
                    self.toolButton_6.setText(_translate("part_window", "删除"))
                    self.toolButton_4.clicked.connect(self.find_all_in_order)

                case 7:
                    self.page = QtWidgets.QWidget()
                    self.page.setObjectName("page")
                    _translate = QtCore.QCoreApplication.translate
                    self.label = QtWidgets.QLabel(parent=self.page)
                    self.label.setGeometry(QtCore.QRect(20, 10, 111, 61))
                    font = QtGui.QFont()
                    font.setPointSize(20)
                    self.label.setFont(font)
                    self.label.setObjectName("label")
                    self.label_3 = QtWidgets.QLabel(parent=self.page)
                    self.label_3.setGeometry(QtCore.QRect(20, 60, 81, 31))
                    font = QtGui.QFont()
                    font.setPointSize(15)
                    self.label_3.setFont(font)
                    self.label_3.setObjectName("label_3")
                    self.lineEdit = QtWidgets.QLineEdit(parent=self.page)
                    self.lineEdit.setGeometry(QtCore.QRect(470, 100, 113, 21))
                    self.lineEdit.setObjectName("lineEdit")
                    self.toolButton = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton.setGeometry(QtCore.QRect(590, 100, 42, 20))
                    self.toolButton.setObjectName("toolButton")
                    self.toolButton_3 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_3.setGeometry(
                        QtCore.QRect(20, 100, 42, 20))
                    self.toolButton_3.setObjectName("toolButton_3")
                    self.tableView_7 = QtWidgets.QTableView(parent=self.page)
                    self.tableView_7.setGeometry(
                        QtCore.QRect(0, 131, 651, 401))
                    self.tableView_7.setObjectName("tableView")
                    self.label.setText(_translate("part_window", "订单管理"))
                    self.label_3.setText(_translate("part_window", "出库订单管理"))
                    self.lineEdit.setPlaceholderText(
                        _translate("part_window", "输入订单号查询"))
                    self.toolButton.setText(_translate("part_window", "搜索"))
                    self.toolButton_3.setText(_translate("part_window", "新建"))
                    self.toolButton_4 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_4.setGeometry(
                        QtCore.QRect(70, 100, 42, 20))
                    self.toolButton_4.setObjectName("toolButton_4")
                    self.toolButton_5 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_5.setGeometry(
                        QtCore.QRect(120, 100, 42, 20))
                    self.toolButton_5.setObjectName("toolButton_5")
                    self.toolButton_4.setText(_translate("part_window", "查询"))
                    self.toolButton_5.setText(_translate("part_window", "修改"))
                    self.toolButton_6 = QtWidgets.QToolButton(parent=self.page)
                    self.toolButton_6.setGeometry(
                        QtCore.QRect(170, 100, 42, 20))
                    self.toolButton_6.setObjectName("toolButton_6")
                    self.toolButton_6.setText(_translate("part_window", "删除"))
                    self.toolButton_4.clicked.connect(self.find_all_in_order)

                case _:
                    self.page = QtWidgets.QWidget()
                    self.page.setObjectName("page")

            # # label.setAlignment(Qt.AlignCenter)
            # # 设置label的背景颜色(这里随机)
            # # 这里加了一个margin边距(方便区分QStackedWidget和QLabel的颜色)
            # # label.setStyleSheet('background: rgb(%d, %d, %d);margin: 50px;' % (
            # #     randint(0, 255), randint(0, 255), randint(0, 255)))
            # self.label.setStyleSheet('background: rgb(%d, %d, %d);margin: 50px;' % (
            #     random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            self.stackedWidget.addWidget(self.page)

        # self.page = QtWidgets.QWidget()
        # self.page.setObjectName("page")

        # self.label_2 = QtWidgets.QLabel(parent=self.page)
        # self.label_2.setGeometry(QtCore.QRect(150, 60, 101, 21))
        # font = QtGui.QFont()
        # font.setPointSize(15)
        # self.label_2.setFont(font)
        # self.label_2.setText("")
        # self.label_2.setObjectName("label_2")
        # self.stackedWidget.addWidget(self.page)
        # self.page_2 = QtWidgets.QWidget()
        # self.page_2.setObjectName("page_2")
        # self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(part_window)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(part_window)

    def retranslateUi(self, part_window):
        _translate = QtCore.QCoreApplication.translate
        part_window.setWindowTitle(_translate("part_window", "Dialog"))

    def change_ui(self):
        selected_indexes = self.treeView.selectedIndexes()
        for idx in selected_indexes:

            if idx.data() == '人员管理':
                self.stackedWidget.setCurrentIndex(0)
            elif idx.data() == '登录管理':
                self.stackedWidget.setCurrentIndex(1)
            elif idx.data() == '仓库管理':
                self.stackedWidget.setCurrentIndex(2)
            elif idx.data() == '货架管理':
                self.stackedWidget.setCurrentIndex(3)
            elif idx.data() == '电脑配件信息管理':
                self.stackedWidget.setCurrentIndex(4)
            elif idx.data() == '库存管理':
                self.stackedWidget.setCurrentIndex(5)
            elif idx.data() == '入库订单管理':
                self.stackedWidget.setCurrentIndex(6)
            elif idx.data() == '出库订单管理':
                self.stackedWidget.setCurrentIndex(7)
            else:
                self.stackedWidget.setCurrentIndex(8)

    def send_to_server(self, json_data):
        try:
            host = 'localhost'
            port = 8888
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            context.load_verify_locations(cafile="client/cert/cert.pem")
            # context.check_hostname=False

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                with context.wrap_socket(sock, server_hostname=host) as s:
                    s.connect((host, port))
                    send_data = json_data
                    s.send(json.dumps(send_data).encode())
                    # receive data from the server
                    data = s.recv(8192)
                    new_data = json.loads(data.decode())
                    s.close()
                    return new_data

        except Exception as e:
            print(str(e))
            dialog('连接失败!')
            return

    def insert_user(self):
        user = User()
        user.set_args('y000004', client_encrypt.md5(
            'y000004'), 'casad@123.com', 1)
        choose = QStandardItem()
        choose.setCheckable(True)
        choose.setCheckState(Qt.CheckState.Unchecked)
        choose.setEditable = False
        items = [choose, QStandardItem(''), QStandardItem(''),
                 QStandardItem(''), QStandardItem('')]
        self.model_1.appendRow(items)

    def delete_user_by_id(self):
        i = 0
        while i < self.user_count:
            value = self.choose_0[i].checkState()
            table_model = self.tableView_1.model()
            if value == Qt.CheckState.Checked:
                index = table_model.index(i, 1)
                new_data = table_model.data(index)
                print(new_data)
                send_data = {
                    'key': 'delete_user_by_id', 'value': new_data}
                new_data = self.send_to_server(send_data)
                if new_data is None:
                    break
                else:
                    print(new_data)
                    self.model_1.removeRow(i)
                    self.tableView_1.setModel(self.model_1)
                    self.tableView_1.update()
            i += 1

        # for x in new_data:
        #     print(str(x.keys()) + '\n'+str(x.values()))

        # print(new_data[0])
        # for row in new_data:
        self.tableView_1.setModel(self.model_1)
        self.tableView_1.update()

    def find_all_user(self):
        self.model_1 = QStandardItemModel()
        i = 0
        send_data = {'key': 'find_all_user', 'value': ''}
        data = self.send_to_server(send_data)
        new_data = list(json.loads(json.dumps(data)).values())
        self.model_1.setHorizontalHeaderLabels(
            ['选择', '用户名', '密码', '邮箱', '身份类型'])
        self.choose_0 = [QStandardItem()
                         for i in range(len(new_data))]
        while i < len(new_data):
            if new_data[i]['idtype'] == 1:
                q = QStandardItem("普通员工")
            else:
                q = QStandardItem("管理员")
            # delegate = CheckBoxDelegate()
            # self.tableView_1.setItemDelegateForColumn(0, delegate)
            self.choose_0[i].setCheckable(True)
            self.choose_0[i].setCheckState(Qt.CheckState.Unchecked)
            self.choose_0[i].setEditable = False
            items = [self.choose_0[i], QStandardItem(new_data[i]['id']), QStandardItem('*********'),
                     QStandardItem(new_data[i]['email']), q]
            items[0].setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHorizontal_Mask)
            i += 1
            self.user_count = i
            self.model_1.appendRow(items)
        # for x in new_data:
        #     print(str(x.keys()) + '\n'+str(x.values()))

        # print(new_data[0])
        # for row in new_data:
        self.tableView_1.setModel(self.model_1)
        self.tableView_1.update()

    def find_all_in_order(self):
        send_data = {'key': 'find_all_in_order', 'value': ''}
        data = self.send_to_server(send_data)
        self.model = QStandardItemModel()
        i = 0
        new_data = list(json.loads(json.dumps(
            data, ensure_ascii=False)).values())
        self.model.setHorizontalHeaderLabels(
            ['选择', '订单编号', '配件号', '数量', '入库时间', '仓库号', '货架类型', '处理人工号', ])
        self.choose_6 = [QStandardItem()
                         for i in range(len(new_data))]
        while i < len(new_data):
            self.choose_6[i].setCheckable(True)
            self.choose_6[i].setCheckState(Qt.CheckState.Unchecked)
            self.choose_6[i].setEditable = False
            items = [self.choose_6[i], QStandardItem(new_data[i]['in_code']),
                     QStandardItem(new_data[i]['p_code']),
                     QStandardItem(str(new_data[i]['num'])), QStandardItem(
                new_data[i]['in_time']),
                QStandardItem(new_data[i]['r_code']), QStandardItem(
                new_data[i]['s_type']),
                QStandardItem(new_data[i]['u_code'])]
            i += 1
            self.model.appendRow(items)
        # for x in new_data:
        #     print(str(x.keys()) + '\n'+str(x.values()))

        # print(new_data[0])
        # for row in new_data:

        self.tableView_6.setModel(self.model)
        self.tableView_6.update()

    def on_state_changed(self, state):
        if (state == QtCore.Qt.CheckState.Checked):
            return 1
        else:
            return 0


class CheckBoxDelegate(QItemDelegate):
    def init(self, parent=None):
        super(CheckBoxDelegate, self).init(parent)

    # 创建CheckBox控件
    def createEditor(self, parent, option, index):
        editor = QCheckBox(parent)
        editor.setCheckState(Qt.CheckState.Unchecked)
        return editor

    # 设置CheckBox控件的状态
    def setEditorData(self, editor, index):
        value = index.model().data(index, Qt.DisplayRole)
        editor.setChecked(value)

    # 获取CheckBox控件的状态
    def setModelData(self, editor, model, index):
        value = editor.checkState()
        model.setData(index, value, Qt.EditRole)


def dialog(string):
    msg = QMessageBox()
    msg.setGeometry(240, 210, 81, 41)
    msg.setText(string)
    msg.setWindowTitle('提示')
    msg.setFixedSize(500, 200)
    msg.exec()

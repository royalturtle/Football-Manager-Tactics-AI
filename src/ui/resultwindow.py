import sys
import os
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QTabWidget, QVBoxLayout, QGroupBox, \
    QApplication, QMenu, QAction, qApp, QActionGroup, QLabel, QTreeView, QTableWidget, QPushButton
from PyQt5.QtGui import QIcon, QStandardItemModel
from PyQt5 import QtSvg


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        def init_menu(obj):
            menubar = obj.menuBar()

            file = menubar.addMenu('&File')

            zoom = QMenu('Zoom', obj)
            group = QActionGroup(zoom)
            zoom100 = QAction('100%', zoom, checkable=True)
            zoom100.setChecked(True)
            zoom.addAction(zoom100)
            group.addAction(zoom100)
            zoom50 = QAction('50%', zoom, checkable=True)
            zoom.addAction(zoom50)
            group.addAction(zoom50)
            group.setExclusive(True)
            file.addMenu(zoom)

            check1 = QAction('check1', obj, checkable=True)
            check1.triggered.connect(obj.toggle)
            file.addAction(check1)

            exit = QAction(QIcon('exit.png'), '&Exit', obj)
            exit.setShortcut('Ctrl+Q')
            exit.setStatusTip('Exit App')
            exit.triggered.connect(qApp.quit)

            file.addSeparator()
            file.addAction(exit)

            obj.statusBar().showMessage('PyQt5 StatusBar')

        def init_ui(obj: QMainWindow):
            main_widget = QWidget(obj)
            main_layout = QHBoxLayout(obj)

            # Left Screen
            group_left = QGroupBox("Input")
            left_layout = QVBoxLayout(obj)

            group_team_A = QGroupBox("Team A")
            team_labels = ["uid", "name"]
            my_team = QTableWidget(obj)
            my_team.setColumnCount(2)
            my_team.setHorizontalHeaderLabels(team_labels)
            my_team.setFixedWidth(250)
            group_team_A_layout = QVBoxLayout(obj)
            group_team_A_layout.addWidget(my_team)
            group_team_A.setLayout(group_team_A_layout)

            group_team_B = QGroupBox("Team B")
            your_team = QTableWidget(obj)
            your_team.setColumnCount(2)
            your_team.setHorizontalHeaderLabels(team_labels)
            your_team.setFixedWidth(250)
            group_team_B_layout = QVBoxLayout(obj)
            group_team_B_layout.addWidget(your_team)
            group_team_B.setLayout(group_team_B_layout)

            team_act_layout = QHBoxLayout(obj)
            team_act_load_A = QPushButton("Load TeamA", obj)
            team_act_load_B = QPushButton("Load TeamB", obj)
            team_act_result = QPushButton("Get Result", obj)
            team_act_layout.addWidget(team_act_load_A)
            team_act_layout.addWidget(team_act_load_B)
            team_act_layout.addWidget(team_act_result)

            left_layout.addWidget(group_team_A)
            left_layout.addWidget(group_team_B)
            left_layout.addLayout(team_act_layout)
            group_left.setLayout(left_layout)

            # Right Screen
            group_right = QGroupBox("Output")
            right_layout = QVBoxLayout(obj)

            svg_viewer = QtSvg.QSvgWidget(obj)
            path = os.getcwd()[:-6] + "\\ui\\rsc\\football ground.svg"
            print(path)
            svg_viewer.load(path)
            svg_viewer.setGeometry(0, 0, 600, 600)
            svg_viewer.show()

            right_layout.addWidget(svg_viewer)
            group_right.setLayout(right_layout)


            main_layout.addWidget(group_left)
            main_layout.addLayout(group_right)

            main_widget.setLayout(main_layout)
            obj.setCentralWidget(main_widget)



        init_menu(self)
        init_ui(self)
        self.resize(1000, 700)
        self.show()

    def toggle(self, state):
        print(state)

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        act_new = cmenu.addAction("New")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == act_new:
            print("do new action")


def run_ui():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
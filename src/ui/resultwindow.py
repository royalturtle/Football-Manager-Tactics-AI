import sys
import os
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QTabWidget, QVBoxLayout, QGroupBox, \
    QApplication, QMenu, QAction, qApp, QActionGroup, QLabel, QTreeView, QTableWidget, QPushButton
from PyQt5.QtGui import QIcon, QStandardItemModel
from PyQt5 import QtSvg

# for Graphs
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MyApp(QMainWindow):
    def __init__(self, ai=None):
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
            group_team_A_layout = QVBoxLayout(obj)
            group_team_A_layout.addWidget(my_team)
            group_team_A.setLayout(group_team_A_layout)

            group_team_B = QGroupBox("Team B")
            your_team = QTableWidget(obj)
            your_team.setColumnCount(2)
            your_team.setHorizontalHeaderLabels(team_labels)
            group_team_B_layout = QVBoxLayout(obj)
            group_team_B_layout.addWidget(your_team)
            group_team_B.setLayout(group_team_B_layout)

            team_act_layout = QHBoxLayout(obj)
            team_act_load_A = QPushButton("Load A", obj)
            team_act_load_B = QPushButton("Load B", obj)
            team_act_result = QPushButton("Get Result", obj)
            team_act_layout.addWidget(team_act_load_A)
            team_act_layout.addWidget(team_act_load_B)
            team_act_layout.addWidget(team_act_result)

            left_layout.addWidget(group_team_A)
            left_layout.addWidget(group_team_B)
            left_layout.addLayout(team_act_layout)
            group_left.setLayout(left_layout)
            group_left.setFixedWidth(250)

            # Right Screen
            group_right = QGroupBox("Output")
            right_layout = QVBoxLayout(obj)

            # Right Screen 1
            right_layout_1 = QHBoxLayout(obj)
            result_list = QTableWidget(obj)
            result_list.setColumnCount(5)
            result_list.setHorizontalHeaderLabels(["", "Name", "Goal Difference", "GF", "GA"])
            result_list.setFixedHeight(300)

            # http://www.gisdeveloper.co.kr/?p=8343
            fig = plt.Figure()
            graph_view = FigureCanvas(fig)

            right_layout_1.addWidget(result_list)
            right_layout_1.addWidget(graph_view)

            # Right Screen 2
            right_layout_2 = QHBoxLayout(obj)

            svg_viewer = QtSvg.QSvgWidget(obj)
            path = os.getcwd()[:-6] + "\\ui\\rsc\\football ground.svg"
            print(path)
            svg_viewer.load(path)
            svg_viewer.setGeometry(0, 0, 600, 600)
            svg_viewer.show()

            tactics_tab = QTabWidget(obj)
            tab1 = QWidget()
            tab2 = QWidget()
            tactics_tab.addTab(tab1, "Tab 1")
            tactics_tab.addTab(tab2, "Tab 2")
            tactics_tab.setFixedWidth(200)

            right_layout_2.addWidget(svg_viewer)
            right_layout_2.addWidget(tactics_tab)

            right_layout.addLayout(right_layout_1)
            right_layout.addLayout(right_layout_2)
            group_right.setLayout(right_layout)

            main_layout.addWidget(group_left)
            main_layout.addWidget(group_right)

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

from src.AIs.models.TestModel.TestModel import TestModel


def run_ui(test_ai=False):
    if test_ai is True:
        ai = TestModel(
            mode="TEST_TACTICS",
            epochs=1,
            players=1
        )
    else:
        ai = None

    app = QApplication(sys.argv)
    ex = MyApp(ai)
    sys.exit(app.exec_())

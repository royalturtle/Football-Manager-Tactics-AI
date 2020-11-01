import sys
import os
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QTabWidget, QVBoxLayout, QGroupBox, \
    QApplication, QMenu, QAction, qApp, QActionGroup, QLabel, QTreeView, QTableWidget, QPushButton, QTableWidgetItem
from PyQt5.QtGui import QIcon, QStandardItemModel
from PyQt5 import QtSvg

from src.ui.widgets.InputTacticsWidget import InputTacticsWidget, Lineup

# for Graphs
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from src.AIs.models.TabNetCv1.TabNetCv1 import TabNetCv1


class LineupListWidget(QWidget):
    def __init__(self, parent=None, team_name: str = "Team"):
        super(LineupListWidget, self).__init__(parent)
        self.ly_main = QVBoxLayout(self)

        self.wg_group_team = QGroupBox(team_name)
        self.team_labels = ["Name", "Formation"]
        self.wg_list_team = QTableWidget(self)
        self.wg_list_team.setColumnCount(2)
        self.wg_list_team.setHorizontalHeaderLabels(self.team_labels)
        self.ly_team = QVBoxLayout(self)
        self.ly_team.addWidget(self.wg_list_team)
        self.wg_group_team.setLayout(self.ly_team)

        self.ly_main.addWidget(self.wg_group_team)
        self.setLayout(self.ly_main)

    def set_lineups(self, lineups):
        try:
            self.wg_list_team.setRowCount(len(lineups))

            for row, lineup in enumerate(lineups):
                item = QTableWidgetItem(os.path.basename(lineup.title))
                self.wg_list_team.setItem(row, 0, item)
                item = QTableWidgetItem(lineup.formation_string)
                self.wg_list_team.setItem(row, 1, item)
        except Exception as e:
            print(e)


class LineupManageWidget(QWidget):
    def __init__(self, parent=None, lineup_lists=None, ai: TabNetCv1 = None, result_widget = None):
        assert lineup_lists is not None and result_widget is not None
        super(LineupManageWidget, self).__init__(parent)
        self.ai = ai
        self.lineup_lists = lineup_lists
        self.result_widget = result_widget
        # [UI] DIALOGUE
        self.dg_input_tactics_A = InputTacticsWidget(self, lineup_lists[0])
        self.dg_input_tactics_B = InputTacticsWidget(self, lineup_lists[1])

        self.ly_main = QVBoxLayout(self)
        self.ly_main.setContentsMargins(0, 0, 0, 0)
        self.ly_main.setSpacing(0)

        self.wg_group_team_a = LineupListWidget(self)
        self.wg_group_team_b = LineupListWidget(self)

        self.ly_team_actions = QHBoxLayout(self)
        self.wg_button_manage_team_a = QPushButton("Add A", self)
        self.wg_button_manage_team_b = QPushButton("Add B", self)
        self.wg_button_get_result = QPushButton("Get Result", self)
        self.ly_team_actions.addWidget(self.wg_button_manage_team_a)
        self.ly_team_actions.addWidget(self.wg_button_manage_team_b)
        self.ly_team_actions.addWidget(self.wg_button_get_result)

        self.ly_main.addWidget(self.wg_group_team_a)
        self.ly_main.addWidget(self.wg_group_team_b)
        self.ly_main.addLayout(self.ly_team_actions)
        self.setLayout(self.ly_main)

        self.wg_button_manage_team_a.clicked.connect(self.show_dg_input_tactics_A)
        self.wg_button_manage_team_b.clicked.connect(self.show_dg_input_tactics_B)
        self.wg_button_get_result.clicked.connect(self.calculate_result)

        self.dg_input_tactics_A.closeEvent = self.close_dialogue_tactics_A
        self.dg_input_tactics_B.closeEvent = self.close_dialogue_tactics_B

    def show_dg_input_tactics_A(self):
        self.dg_input_tactics_A.show()

    def close_dialogue_tactics_A(self, event):
        self.wg_group_team_a.set_lineups(self.lineup_lists[0])

    def show_dg_input_tactics_B(self):
        self.dg_input_tactics_B.show()

    def close_dialogue_tactics_B(self, event):
        self.wg_group_team_b.set_lineups(self.lineup_lists[1])

    def calculate_result(self):
        # self.ai.run(self.ai.scenario)
        result = list()
        averages = list()
        for me in self.lineup_lists[0]:
            sum = 0
            for you in self.lineup_lists[1]:
                win_prob = self.ai.get_result(me.get_list_data(), you.get_list_data())
                sum += win_prob
                result.append((os.path.basename(me.title), os.path.basename(you.title), win_prob))
            averages.append(sum / len(self.lineup_lists[1]))

        self.result_widget.update_result(result, averages, self.lineup_lists[0], self.lineup_lists[1])


class TacticsResultWidget(QWidget):
    def __init__(self, parent=None):
        super(TacticsResultWidget, self).__init__(parent)


class ResultListWidget(QWidget):
    def __init__(self, parent=None):
        super(ResultListWidget, self).__init__(parent)
        self.ly_main = QVBoxLayout(self)

        self.wg_list_result = QTableWidget(self)
        self.wg_list_result.setColumnCount(2)
        self.wg_list_result.setHorizontalHeaderLabels(["Tactics", "Win Avg"])

        self.ly_main.addWidget(self.wg_list_result)
        self.setLayout(self.ly_main)

    def update_result(self, result, averages, my_tactics, opponent_tactics):
        try:
            self.wg_list_result.setColumnCount(2 + len(opponent_tactics))
            labels = ["Tactics", "Win Avg"]

            for i in opponent_tactics:
                labels.append(os.path.basename(i.title))

            self.wg_list_result.setHorizontalHeaderLabels(labels)
            self.wg_list_result.setRowCount(len(my_tactics))
            for i in range(len(result)):

                row = i // len(my_tactics)
                col = i % len(opponent_tactics)

                item = QTableWidgetItem(result[i][0])
                self.wg_list_result.setItem(row, 0, item)
                item = QTableWidgetItem(str(averages[row]))
                self.wg_list_result.setItem(row, 1, item)
                item = QTableWidgetItem(str(result[i][2]))
                self.wg_list_result.setItem(row, 2 + col, item)
        except Exception as e:
            print(e)


class LineupPictureWidget(QWidget):
    def __init__(self, parent=None):
        super(LineupPictureWidget, self).__init__(parent)
        self.ly_main = QVBoxLayout(self)

        self.wg_position_viewer = QtSvg.QSvgWidget(self)
        path = os.getcwd() + "\\src\\ui\\rsc\\football ground.svg"
        self.wg_position_viewer.load(path)
        self.wg_position_viewer.setGeometry(0, 0, 600, 600)
        self.wg_position_viewer.show()

        self.ly_main.addWidget(self.wg_position_viewer)
        self.setLayout(self.ly_main)


class MyApp(QMainWindow):
    def __init__(self, ai=None):
        super().__init__()

        self.menubar = self.menuBar()
        self.ai = TabNetCv1(mode="LEARN_FROM_FILE", epochs=1)

        self.lineupA = list()
        self.lineupB = list()
        self.statusBar().showMessage('PyQt5 StatusBar')

        def init_ui(obj: QMainWindow):
            wg_main = QWidget(obj)
            ly_main = QHBoxLayout(obj)

            # Left Screen
            wg_group_left = QGroupBox("Input")
            ly_left = QHBoxLayout(obj)

            # tmp
            wg_list_result = ResultListWidget()

            wg_lineup_manager = LineupManageWidget(obj, (obj.lineupA, obj.lineupB), self.ai, wg_list_result)
            ly_left.addWidget(wg_lineup_manager)
            wg_group_left.setLayout(ly_left)
            wg_group_left.setFixedWidth(250)

            # Right Screen
            wg_group_right = QGroupBox("Output")
            ly_right = QVBoxLayout(obj)

            # Right Screen 1
            ly_right_1 = QHBoxLayout(obj)
            wg_list_result.setFixedHeight(300)

            # http://www.gisdeveloper.co.kr/?p=8343
            #fig = plt.Figure()
            #wg_result_graph = FigureCanvas(fig)

            ly_right_1.addWidget(wg_list_result)
            #ly_right_1.addWidget(wg_result_graph)

            # Right Screen 2
            ly_right_2 = QHBoxLayout(obj)
            wg_position_viewer = LineupPictureWidget(obj)
            ly_right_2.addWidget(wg_position_viewer)

            ly_right.addLayout(ly_right_1)
            ly_right.addLayout(ly_right_2)
            wg_group_right.setLayout(ly_right)

            ly_main.addWidget(wg_group_left)
            ly_main.addWidget(wg_group_right)

            wg_main.setLayout(ly_main)
            obj.setCentralWidget(wg_main)

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

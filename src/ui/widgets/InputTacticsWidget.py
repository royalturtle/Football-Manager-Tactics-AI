from PyQt5.QtWidgets import QWidget, QMainWindow, QHBoxLayout, QTableWidget, QVBoxLayout, QGroupBox, QLabel, QLineEdit
from PyQt5 import QtSvg
import os


class Stats:
    @staticmethod
    def technique():
        return ["crossing", "dribbling", "finishing", "first touch", "heading",
                          "long shots", "long throws", "marking", "passing", "tackling", "technique"]

    @staticmethod
    def mental():
        return ["aggression", "anticipation", "bravery", "composure", "concentration", "vision",
                       "decisions", "determination", "flair", "off the ball", "positioning", "teamwork", "work rate"]

    @staticmethod
    def physics():
        return ["acceleration", "agility", "balance", "jumping", "natural fitness", "pace", "stamina",
                        "strength", "l foot", "r foot"]


class Player:
    def __init__(self):
        self.data = {
            "name": "Unknown",
            "crossing": 1,
            "dribbling": 1,
            "finishing": 1,
            "first touch": 1,
            "heading": 1,
            "long shots": 1,
            "long throws": 1,
            "marking": 1,
            "passing": 1,
            "tackling": 1,
            "technique": 1,
            "aggression": 1,
            "anticipation": 1,
            "bravery": 1,
            "composure": 1,
            "concentration": 1,
            "vision": 1,
            "decisions": 1,
            "determination": 1,
            "flair": 1,
            "off the ball": 1,
            "positioning": 1,
            "teamwork": 1,
            "work rate": 1,
            "acceleration": 1,
            "agility": 1,
            "balance": 1,
            "jumping": 1,
            "natural fitness": 1,
            "pace": 1,
            "stamina": 1,
            "strength": 1,
            "l foot": 1,
            "r foot": 1,
        }

    def set_data(self, input:list=None):
        assert input is not None


class Lineup:
    def __init__(self):
        self.players = dict()

        default_formation = [1, 2, 4, 5, 11, 12, 14, 15, 21, 23]
        for item in default_formation:
            self.players[item] = Player()


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


class LabelAndInputWidget(QWidget):
    def __init__(self, parent=None, label: str = "text", value=1):
        super(LabelAndInputWidget, self).__init__(parent)
        self.ly_main = QHBoxLayout(self)
        self.wg_text = QLineEdit(self)
        self.wg_text.setText(str(value))

        self.ly_main.addWidget(QLabel(label, self))
        self.ly_main.addWidget(self.wg_text)
        self.setLayout(self.ly_main)


class LabelAndInputListWidget(QWidget):
    def __init__(self, parent=None, items:list=None):
        super(LabelAndInputListWidget, self).__init__(parent)
        self.ly_main = QVBoxLayout(self)


        self.setLayout(self.ly_main)


class PlayerStatWidget(QWidget):
    def __init__(self, parent=None):
        super(PlayerStatWidget, self).__init__(parent)
        self.ly_main = QVBoxLayout(self)

        self.setLayout(self.ly_main)


class InputTacticsWidget(QMainWindow):
    def __init__(self, parent=None):
        super(InputTacticsWidget, self).__init__(parent)
        self.wg_main = QWidget(self)
        self.ly_main = QHBoxLayout(self)

        self.wg_group_left = QGroupBox("Tactics List", self)
        self.ly_group_left = QVBoxLayout(self)
        self.wg_group_right = QGroupBox("Modify Tactics", self)
        self.ly_group_right = QVBoxLayout(self)

        self.wg_list_tactics = QTableWidget(self)
        self.wg_lineup_picture = LineupPictureWidget(self)
        self.wg_player_stats = PlayerStatWidget(self)

        self.ly_group_left.addWidget(self.wg_list_tactics)
        self.ly_group_right.addWidget(self.wg_lineup_picture)
        self.ly_group_right.addWidget(self.wg_player_stats)

        self.wg_group_left.setLayout(self.ly_group_left)
        self.wg_group_right.setLayout(self.ly_group_right)

        self.ly_main.addWidget(self.wg_group_left)
        self.ly_main.addWidget(self.wg_group_right)

        self.wg_list_tactics.setColumnCount(2)

        self.wg_main.setLayout(self.ly_main)
        self.setCentralWidget(self.wg_main)


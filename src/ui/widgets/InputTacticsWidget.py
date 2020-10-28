from PyQt5.QtWidgets import QWidget, QMainWindow, QHBoxLayout, QTableWidget, QVBoxLayout, QGroupBox, QLabel, \
    QLineEdit, QGridLayout, QPushButton, QFileDialog, QTableWidgetItem
from PyQt5 import QtSvg
from PyQt5.QtGui import QDrag, QPixmap, QIcon
from PyQt5.QtCore import Qt, QMimeData, QPoint
import os

import numpy as np
import pandas as pd

PLAYERS = 11


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

    @staticmethod
    def all():
        columns = ["position"]
        columns.extend(Stats.technique())
        columns.extend(Stats.mental())
        columns.extend(Stats.physics())
        return columns


def list_as_formation_string(input: list = None):
    assert input is not None
    result = ""
    count = [0, 0, 0, 0, 0]

    for i in input[1:]:
        count[(i - 1) // 5] += 1

    for i in count:
        if i != 0:
            result += str(i)

    print(result)
    return result


class Player:
    def __init__(self):
        self.data = {
            "position": 1,
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

    def set_data(self, input=None):
        columns = Stats.all()
        assert input is not None and len(input) == len(columns)
        for i in range(len(input)):
            self.data[columns[i]] = input[i]

class Lineup:
    def __init__(self, formation=None, title: str = "Default"):
        self.players = dict()
        self.title = title

        if formation is None:
            self.formation = [0, 1, 2, 4, 5, 11, 12, 14, 15, 21, 23]
        else:
            self.formation = formation

        for item in range(PLAYERS):
            self.players[item] = Player()

    def get_formation(self):
        return self.formation

    def set_title(self, title):
        self.title = title

    def set_data_by_filename(self, filename):
        print(filename)
        try:
            data = np.genfromtxt(filename, delimiter=',', dtype=np.int8)
            assert len(data) == 11
            for i in range(len(data)):
                self.formation[i] = data[i][0]
                self.players[i].set_data(data[i])

            print(self.players[10].data)
            print(self.formation)

        except Exception as e:
            print(e)


class LineupIconsWidget(QWidget):
    def __init__(self, parent=None, lineup: list = None):
        assert lineup is not None
        super(LineupIconsWidget, self).__init__(parent)
        self.target = None
        self.lineup = lineup
        self.setAcceptDrops(True)
        self.wg_position = list()
        for i in range(24):
            layout = QVBoxLayout()
            item = QtSvg.QSvgWidget(self)
            if i == 0:
                path = os.getcwd() + "\\src\\ui\\rsc\\players node keeper.svg"
            elif i in lineup:
                path = os.getcwd() + "\\src\\ui\\rsc\\players node.svg"
            else:
                path = os.getcwd() + "\\src\\ui\\rsc\\players node empty.svg"
            item.load(path)
            item.setFixedSize(32, 32)
            layout.addWidget(item)
            self.wg_position.append(layout)
            item.show()

        self.ly_players = QGridLayout(self)
        self.ly_players.addLayout(self.wg_position[0], 2, 0)
        for i in range(1, 21):
            self.ly_players.addLayout(self.wg_position[i], (i - 1) % 5, (i - 1) // 5 + 1)
        self.ly_players.addLayout(self.wg_position[21], 1, 5)
        self.ly_players.addLayout(self.wg_position[22], 2, 5)
        self.ly_players.addLayout(self.wg_position[23], 3, 5)
        self.setLayout(self.ly_players)

    def get_index(self, pos):
        for i in range(self.ly_players.count()):
            if self.ly_players.itemAt(i).geometry().contains(pos) and i != self.target:
                return i

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.target = self.get_index(event.localPos().toPoint())
        else:
            self.target = None

    def mouseReleaseEvent(self, event):
        self.target = None

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and self.target is not None and self.target in self.lineup:
            drag = QDrag(self.ly_players.itemAt(self.target))
            pix = self.ly_players.itemAt(self.target).itemAt(0).widget().grab()
            mimedata = QMimeData()
            mimedata.setImageData(pix)
            drag.setMimeData(mimedata)
            drag.setPixmap(pix)
            to_middle = (pix.height() // 2)
            drag.setHotSpot(QPoint(to_middle, to_middle))
            drag.exec_()

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if not event.source().geometry().contains(event.pos()):
            source = self.get_index(event.pos())
            if source is None:
                return

            i, j = max(self.target, source), min(self.target, source)
            p1, p2 = self.ly_players.getItemPosition(i), self.ly_players.getItemPosition(j)

            self.ly_players.addItem(self.ly_players.takeAt(i), *p2)
            self.ly_players.addItem(self.ly_players.takeAt(j), *p1)


class LineupPictureWidget(QWidget):
    def __init__(self, parent=None, lineup: list = None):
        assert lineup is not None
        super(LineupPictureWidget, self).__init__(parent)

        self.ly_main = QVBoxLayout(self)

        self.wg_position_viewer = QtSvg.QSvgWidget(self)
        path = os.getcwd() + "\\src\\ui\\rsc\\football ground.svg"
        self.wg_position_viewer.load(path)
        self.wg_position_viewer.show()

        self.wg_players = LineupIconsWidget(self, lineup)
        self.auto_resize_table()

        self.ly_main.addWidget(self.wg_position_viewer)
        self.setLayout(self.ly_main)

        self.setMinimumSize(400, 200)

    def auto_resize_table(self):
        overlay_pos = self.wg_position_viewer.geometry()
        width = self.wg_position_viewer.geometry().width()
        height = self.wg_position_viewer.geometry().height()
        self.wg_players.setGeometry(overlay_pos.x(), overlay_pos.y(), width, height)

    def resizeEvent(self, event):
        self.auto_resize_table()


class LabelAndInputWidget(QWidget):
    def __init__(self, parent=None, label: str = "text", value=1, input_width: int = 30, editable=True):
        super(LabelAndInputWidget, self).__init__(parent)
        self.ly_main = QHBoxLayout(self)
        self.wg_text = QLineEdit(self)
        self.wg_text.setText(str(value))
        self.wg_text.setFixedWidth(input_width)
        self.wg_text.setEnabled(editable)
        self.ly_main.addWidget(QLabel(label, self))
        self.ly_main.addWidget(self.wg_text)
        self.setLayout(self.ly_main)
        self.setContentsMargins(0, 0, 0, 0)
        self.setFixedHeight(35)


class PlayerStatWidget(QWidget):
    def __init__(self, parent=None, lineup: Lineup = None):
        assert lineup is not None
        super(PlayerStatWidget, self).__init__(parent)
        self.lineup = lineup

        self.ly_main = QHBoxLayout(self)

        self.ly_stat_technique = QVBoxLayout(self)
        self.ly_stat_mental = QVBoxLayout(self)
        self.ly_stat_physics = QVBoxLayout(self)


        widget_position = LabelAndInputWidget(self, label="position", editable=False)
        widget_position.setObjectName("stats position")
        self.ly_stat_physics.addWidget(widget_position)

        for layout, items in [
            (self.ly_stat_physics, Stats.physics()),
            (self.ly_stat_technique, Stats.technique()),
            (self.ly_stat_mental, Stats.mental())
        ]:
            layout.setSpacing(0)
            for item in items:
                widget = LabelAndInputWidget(self, label=item)
                widget.setObjectName("stats " + item)
                layout.addWidget(widget)

            self.ly_main.addLayout(layout)

        self.setLayout(self.ly_main)
        self.setFixedHeight(400)


class TacticsListWidget(QWidget):
    def __init__(self, parent=None):
        super(TacticsListWidget, self).__init__(parent)
        self.tactics_list = list()

        self.ly_main = QVBoxLayout(self)
        self.ly_actions = QHBoxLayout(self)

        self.wg_btn_add = QPushButton()
        self.wg_btn_delete = QPushButton()
        self.wg_btn_copy = QPushButton()
        self.wg_btn_save = QPushButton()
        self.wg_btn_load = QPushButton()
        icon_path = os.getcwd() + "\\src\\ui\\rsc\\"
        buttons = [
            (self.wg_btn_add, "plus.svg", None),
            (self.wg_btn_delete, "minus.svg", None),
            (self.wg_btn_copy, "clipboard.svg", None),
            (self.wg_btn_save, "save.svg", None),
            (self.wg_btn_load, "download.svg", self.load_tactics)
        ]

        for widget, icon, action in buttons:
            widget.setIcon(QIcon(QPixmap(icon_path + icon)))
            if action is not None:
                widget.clicked.connect(action)
            self.ly_actions.addWidget(widget)

        self.wg_list_tactics = QTableWidget(self)
        self.wg_list_tactics.setColumnCount(2)
        self.wg_list_tactics.setHorizontalHeaderLabels(["Name", "Formation"])

        self.ly_main.addLayout(self.ly_actions)
        self.ly_main.addWidget(self.wg_list_tactics)

        self.setLayout(self.ly_main)
        self.setFixedWidth(250)

    def load_tactics(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', os.getcwd() + "\\tactics", "CSV File (*.csv)")[0]
        try:
            row = len(self.tactics_list)
            lineup = Lineup(title=filename)
            lineup.set_data_by_filename(filename)
            self.tactics_list.append(lineup)

            self.wg_list_tactics.insertRow(row)
            item = QTableWidgetItem(os.path.basename(filename))
            self.wg_list_tactics.setItem(row, 0, item)
            item = QTableWidgetItem(list_as_formation_string(lineup.get_formation()))
            self.wg_list_tactics.setItem(row, 1, item)
        except Exception as e:
            print(e)


class InputTacticsWidget(QMainWindow):
    def __init__(self, parent=None):
        super(InputTacticsWidget, self).__init__(parent)
        self.lineup = Lineup()

        self.wg_main = QWidget(self)
        self.ly_main = QHBoxLayout(self)

        self.wg_group_left = QGroupBox("Tactics List", self)
        self.wg_group_left.setFixedWidth(270)
        self.ly_group_left = QVBoxLayout(self)
        self.wg_group_right = QGroupBox("Modify Tactics", self)
        self.ly_group_right = QVBoxLayout(self)

        self.wg_list_tactics = TacticsListWidget(self)
        self.wg_lineup_picture = LineupPictureWidget(self, self.lineup.get_formation())
        self.wg_player_stats = PlayerStatWidget(self, self.lineup)

        self.ly_group_left.addWidget(self.wg_list_tactics)
        self.ly_group_right.addWidget(self.wg_lineup_picture)
        self.ly_group_right.addWidget(self.wg_player_stats)

        self.wg_group_left.setLayout(self.ly_group_left)
        self.wg_group_right.setLayout(self.ly_group_right)

        self.ly_main.addWidget(self.wg_group_left)
        self.ly_main.addWidget(self.wg_group_right)

        self.wg_main.setLayout(self.ly_main)
        self.setCentralWidget(self.wg_main)


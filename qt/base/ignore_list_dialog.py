# Created By: Virgil Dupras
# Created On: 2012-03-13
# Copyright 2012 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "BSD" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/bsd_license

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QDialog, QVBoxLayout, QPushButton, QTableView, QAbstractItemView

from hscommon.trans import trget
from qtlib.util import horizontalWrap
from .ignore_list_table import IgnoreListTable

tr = trget('ui')

class IgnoreListDialog(QDialog):
    def __init__(self, parent, model):
        flags = Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowSystemMenuHint
        QDialog.__init__(self, parent, flags)
        self._setupUi()
        self.model = model
        self.model.view = self
        self.table = IgnoreListTable(self.model.ignore_list_table, view=self.tableView)
        
        self.removeSelectedButton.clicked.connect(self.model.remove_selected)
        self.clearButton.clicked.connect(self.model.clear)
    
    def _setupUi(self):
        self.setWindowTitle(tr("Ignore List"))
        self.resize(540, 330)
        self.verticalLayout = QVBoxLayout(self)
        self.tableView = QTableView()
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setDefaultSectionSize(18)
        self.tableView.verticalHeader().setHighlightSections(False)
        self.tableView.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableView)
        self.removeSelectedButton = QPushButton(tr("Remove Selected"))
        self.clearButton = QPushButton(tr("Clear"))
        self.verticalLayout.addLayout(horizontalWrap([self.removeSelectedButton, self.clearButton,
            None]))
    
    #--- model --> view
    def show(self):
        QDialog.show(self)
    
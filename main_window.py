from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from A_Star import A_Star

class Ui_MainWindow(object):
    def __init__(self):
        self.traceback = None
        self.current_grid_index = 0
        self.algorithm_summary = ''


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 650)
        MainWindow.setMaximumSize(QtCore.QSize(500, 650))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_algorithm_type = QtWidgets.QLabel(self.centralwidget)
        self.lbl_algorithm_type.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_algorithm_type.setObjectName("lbl_algorithm_type")
        self.verticalLayout.addWidget(self.lbl_algorithm_type)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.box_00 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_00.sizePolicy().hasHeightForWidth())
        self.box_00.setSizePolicy(sizePolicy)
        self.box_00.setObjectName("box_00")
        self.gridLayout.addWidget(self.box_00, 0, 0, 1, 1)
        self.box_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_10.sizePolicy().hasHeightForWidth())
        self.box_10.setSizePolicy(sizePolicy)
        self.box_10.setObjectName("box_10")
        self.gridLayout.addWidget(self.box_10, 1, 0, 1, 1)
        self.box_20 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_20.sizePolicy().hasHeightForWidth())
        self.box_20.setSizePolicy(sizePolicy)
        self.box_20.setObjectName("box_20")
        self.gridLayout.addWidget(self.box_20, 2, 0, 1, 1)
        self.box_01 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_01.sizePolicy().hasHeightForWidth())
        self.box_01.setSizePolicy(sizePolicy)
        self.box_01.setObjectName("box_01")
        self.gridLayout.addWidget(self.box_01, 0, 1, 1, 1)
        self.box_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_11.sizePolicy().hasHeightForWidth())
        self.box_11.setSizePolicy(sizePolicy)
        self.box_11.setObjectName("box_11")
        self.gridLayout.addWidget(self.box_11, 1, 1, 1, 1)
        self.box_21 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_21.sizePolicy().hasHeightForWidth())
        self.box_21.setSizePolicy(sizePolicy)
        self.box_21.setObjectName("box_21")
        self.gridLayout.addWidget(self.box_21, 2, 1, 1, 1)
        self.box_22 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_22.sizePolicy().hasHeightForWidth())
        self.box_22.setSizePolicy(sizePolicy)
        self.box_22.setObjectName("box_22")
        self.gridLayout.addWidget(self.box_22, 2, 2, 1, 1)
        self.box_12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_12.sizePolicy().hasHeightForWidth())
        self.box_12.setSizePolicy(sizePolicy)
        self.box_12.setObjectName("box_12")
        self.gridLayout.addWidget(self.box_12, 1, 2, 1, 1)
        self.box_02 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_02.sizePolicy().hasHeightForWidth())
        self.box_02.setSizePolicy(sizePolicy)
        self.box_02.setObjectName("box_02")
        self.gridLayout.addWidget(self.box_02, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_time_complexity = QtWidgets.QLabel(self.centralwidget)
        self.lbl_time_complexity.setText("")
        self.lbl_time_complexity.setObjectName("lbl_time_complexity")
        self.horizontalLayout_2.addWidget(self.lbl_time_complexity)
        self.btn_run_algorithm = QtWidgets.QPushButton(self.centralwidget)
        self.btn_run_algorithm.setObjectName("btn_run_algorithm")
        ###################### Button Event Binding #########################
        self.btn_run_algorithm.clicked.connect(self.step_algorithm)
        #####################################################################
        self.horizontalLayout_2.addWidget(self.btn_run_algorithm)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        self.menuAlgorithm_Selector = QtWidgets.QMenu(self.menubar)
        self.menuAlgorithm_Selector.setObjectName("menuAlgorithm_Selector")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAlg_1 = QtWidgets.QAction(MainWindow)
        self.actionAlg_1.setObjectName("actionAlg_1")
        self.actionAlg_2 = QtWidgets.QAction(MainWindow)
        self.actionAlg_2.setObjectName("actionAlg_2")
        self.actionAlg_3 = QtWidgets.QAction(MainWindow)
        self.actionAlg_3.setObjectName("actionAlg_3")
        self.action_compare = QtWidgets.QAction(MainWindow)
        self.action_compare.setObjectName("Compare Algorithms")
        self.actionAlg_1.triggered.connect(self.alg1_selected)
        self.actionAlg_2.triggered.connect(self.alg2_selected)
        self.actionAlg_3.triggered.connect(self.alg3_selected)
        self.action_compare.triggered.connect(self.compare_algorithm_selected)
        self.menuAlgorithm_Selector.addAction(self.actionAlg_1)
        self.menuAlgorithm_Selector.addAction(self.actionAlg_2)
        self.menuAlgorithm_Selector.addAction(self.actionAlg_3)
        self.menuAlgorithm_Selector.addAction(self.action_compare)
        self.menubar.addAction(self.menuAlgorithm_Selector.menuAction())

        self.alg1_selected()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_run_algorithm.setText(_translate("MainWindow", "Step Algorithm"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Results:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menuAlgorithm_Selector.setTitle(_translate("MainWindow", "Algorithm Selector"))
        self.actionAlg_1.setText(_translate("MainWindow", "A* Algorithm"))
        self.actionAlg_2.setText(_translate("MainWindow", "Alg 2"))
        self.actionAlg_3.setText(_translate("MainWindow", "Alg 3"))
        self.action_compare.setText(_translate("MainWindow", "Compare Algorithms"))


    def step_algorithm(self):
        '''
        Steps through the moves (1 at a time) in the algorithm 
        to reach the solution.
        '''
        if(self.current_grid_index == len(self.traceback)-1):
            self.btn_run_algorithm.setDisabled(True)
            self.current_grid_index = 0
        else:
            self.current_grid_index += 1
            self.init_puzzle(self.traceback[self.current_grid_index])
            self.textBrowser.setText(self.textBrowser.toPlainText() + '\nMoves: {}'.format(self.current_grid_index))
            scrolling = self.textBrowser.verticalScrollBar()
            scrolling.setValue(scrolling.maximum())
            if(self.current_grid_index == len(self.traceback)-1):
                self.btn_run_algorithm.setDisabled(True)
                self.textBrowser.setText(self.textBrowser.toPlainText() + self.algorithm_summary)
                scrolling = self.textBrowser.verticalScrollBar()
                scrolling.setValue(scrolling.maximum())
                self.current_grid_index = 0
            

    def init_puzzle(self,grid):
        '''
        Sets the puzzle to a different grid.
        '''
        self.box_02.setText(grid[0][2])
        self.box_12.setText(grid[1][2])
        self.box_22.setText(grid[2][2])
        self.box_01.setText(grid[0][1])
        self.box_21.setText(grid[2][1])
        self.box_20.setText(grid[2][0])
        self.box_11.setText(grid[1][1])
        self.box_10.setText(grid[1][0])
        self.box_00.setText(grid[0][0])


    def alg1_selected(self):
        '''
        Bound to the action item for A* algorith.
        '''
        self.lbl_algorithm_type.setText('Algorithm: A* Search')
        a_star = A_Star()
        self.traceback = a_star.solve_puzzle()
        self.current_grid_index = 0
        self.algorithm_summary =  '\n\n' + a_star.summary
        self.textBrowser.setText('Results:\n')
        self.init_puzzle(self.traceback[0])
        self.btn_run_algorithm.setEnabled(True)
        

    def alg2_selected(self):
        self.lbl_algorithm_type.setText('Algorithm: Alg 2')
        #self.algorithm = EightPuzzlesGrid('Alg 2') # Once implemented, assign new algorithm 
        #self.init_puzzle()    
        self.btn_run_algorithm.setEnabled()


    def alg3_selected(self):
        self.lbl_algorithm_type.setText('Algorithm: Alg 3')
        #self.algorithm = EightPuzzlesGrid('Alg 3') # Once implemented, assign new algorithm 
        #self.init_puzzle()
        self.btn_run_algorithm.setEnabled()

    
    def compare_algorithm_selected(self):
        self.btn_run_algorithm.setEnabled(False)
        self.init_puzzle([['','',''],['','',''],['','','']])
        a_star = A_Star()
        for i in range(25):
            grid = a_star.assign_random_puzzle(None)
            a_star.root_puzzle_node.grid = grid
            a_star_solution = a_star.solve_puzzle()
            self.textBrowser.setText(self.textBrowser)



############################# Run the Application #############################
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
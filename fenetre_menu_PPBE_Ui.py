# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\martin.schoreisz\.qgis2\python\plugins\Mizogeo\fenetre_menu_PPBE.ui'
#
# Created: Fri Jun 16 11:47:08 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog_PPBE(object):
    def setupUi(self, Dialog_PPBE):
        Dialog_PPBE.setObjectName(_fromUtf8("Dialog_PPBE"))
        Dialog_PPBE.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_PPBE.resize(800, 434)
        Dialog_PPBE.setMinimumSize(QtCore.QSize(800, 260))
        Dialog_PPBE.setMaximumSize(QtCore.QSize(1600, 520))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri Light"))
        font.setPointSize(11)
        Dialog_PPBE.setFont(font)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog_PPBE)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_administratif = QtGui.QGroupBox(Dialog_PPBE)
        self.groupBox_administratif.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_administratif.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri Light"))
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.groupBox_administratif.setFont(font)
        self.groupBox_administratif.setObjectName(_fromUtf8("groupBox_administratif"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_administratif)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(20, 12, 30, 15)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.listWidget_departementPpbe = QtGui.QListWidget(self.groupBox_administratif)
        self.listWidget_departementPpbe.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget_departementPpbe.setObjectName(_fromUtf8("listWidget_departementPpbe"))
        self.horizontalLayout.addWidget(self.listWidget_departementPpbe)
        self.line_DepartementPpbe = QtGui.QLineEdit(self.groupBox_administratif)
        self.line_DepartementPpbe.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_DepartementPpbe.sizePolicy().hasHeightForWidth())
        self.line_DepartementPpbe.setSizePolicy(sizePolicy)
        self.line_DepartementPpbe.setMinimumSize(QtCore.QSize(350, 100))
        self.line_DepartementPpbe.setMaximumSize(QtCore.QSize(350, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri Light"))
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.line_DepartementPpbe.setFont(font)
        self.line_DepartementPpbe.setObjectName(_fromUtf8("line_DepartementPpbe"))
        self.horizontalLayout.addWidget(self.line_DepartementPpbe)
        self.verticalLayout.addWidget(self.groupBox_administratif)
        self.groupBox_Sortie = QtGui.QGroupBox(Dialog_PPBE)
        self.groupBox_Sortie.setMaximumSize(QtCore.QSize(16777214, 16777214))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri Light"))
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.groupBox_Sortie.setFont(font)
        self.groupBox_Sortie.setObjectName(_fromUtf8("groupBox_Sortie"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_Sortie)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setContentsMargins(20, 12, 30, 15)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.line_Sortie = QtGui.QLineEdit(self.groupBox_Sortie)
        self.line_Sortie.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Sortie.sizePolicy().hasHeightForWidth())
        self.line_Sortie.setSizePolicy(sizePolicy)
        self.line_Sortie.setMinimumSize(QtCore.QSize(640, 30))
        self.line_Sortie.setMaximumSize(QtCore.QSize(1280, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri Light"))
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.line_Sortie.setFont(font)
        self.line_Sortie.setAutoFillBackground(False)
        self.line_Sortie.setStyleSheet(_fromUtf8(""))
        self.line_Sortie.setObjectName(_fromUtf8("line_Sortie"))
        self.horizontalLayout_3.addWidget(self.line_Sortie)
        self.Btn_ChoixSortie = QtGui.QToolButton(self.groupBox_Sortie)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_ChoixSortie.sizePolicy().hasHeightForWidth())
        self.Btn_ChoixSortie.setSizePolicy(sizePolicy)
        self.Btn_ChoixSortie.setMinimumSize(QtCore.QSize(70, 30))
        self.Btn_ChoixSortie.setMaximumSize(QtCore.QSize(70, 30))
        self.Btn_ChoixSortie.setObjectName(_fromUtf8("Btn_ChoixSortie"))
        self.horizontalLayout_3.addWidget(self.Btn_ChoixSortie)
        self.verticalLayout.addWidget(self.groupBox_Sortie)
        self.groupBox_Producteur = QtGui.QGroupBox(Dialog_PPBE)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri Light"))
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.groupBox_Producteur.setFont(font)
        self.groupBox_Producteur.setObjectName(_fromUtf8("groupBox_Producteur"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox_Producteur)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setContentsMargins(20, 12, 30, 15)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.line_Producteur = QtGui.QLineEdit(self.groupBox_Producteur)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Producteur.sizePolicy().hasHeightForWidth())
        self.line_Producteur.setSizePolicy(sizePolicy)
        self.line_Producteur.setMinimumSize(QtCore.QSize(640, 30))
        self.line_Producteur.setMaximumSize(QtCore.QSize(1280, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri Light"))
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.line_Producteur.setFont(font)
        self.line_Producteur.setObjectName(_fromUtf8("line_Producteur"))
        self.horizontalLayout_5.addWidget(self.line_Producteur)
        self.verticalLayout.addWidget(self.groupBox_Producteur)
        self.ButtonBox_Final = QtGui.QDialogButtonBox(Dialog_PPBE)
        self.ButtonBox_Final.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.ButtonBox_Final.setObjectName(_fromUtf8("ButtonBox_Final"))
        self.verticalLayout.addWidget(self.ButtonBox_Final)

        self.retranslateUi(Dialog_PPBE)
        QtCore.QMetaObject.connectSlotsByName(Dialog_PPBE)

    def retranslateUi(self, Dialog_PPBE):
        Dialog_PPBE.setWindowTitle(_translate("Dialog_PPBE", "Création des fichiers N_BRUIT_PPBE", None))
        self.groupBox_administratif.setTitle(_translate("Dialog_PPBE", "Départements concernés", None))
        self.listWidget_departementPpbe.setToolTip(_translate("Dialog_PPBE", "Sélectionner/désélectionner par simple clic", None))
        self.line_DepartementPpbe.setToolTip(_translate("Dialog_PPBE", "Départements sélectionnés", None))
        self.line_DepartementPpbe.setPlaceholderText(_translate("Dialog_PPBE", "Liste des départements choisis", None))
        self.groupBox_Sortie.setTitle(_translate("Dialog_PPBE", "Dossier de stockage de l'arborescence et des fichiers GéoStandard", None))
        self.line_Sortie.setToolTip(_translate("Dialog_PPBE", "Copier/coller l'emplacement où seront stockés les fichiers GéoStandardisés - dossier", None))
        self.line_Sortie.setPlaceholderText(_translate("Dialog_PPBE", "Emplacement du dossier recevant les fichiers GéoStandardisés", None))
        self.Btn_ChoixSortie.setToolTip(_translate("Dialog_PPBE", "Rechercher le dossier de stockage des fichiers GéoStandardisés .shp - dossier", None))
        self.Btn_ChoixSortie.setText(_translate("Dialog_PPBE", "...", None))
        self.groupBox_Producteur.setTitle(_translate("Dialog_PPBE", "Producteur", None))
        self.line_Producteur.setToolTip(_translate("Dialog_PPBE", "Renseigner le numéro SIREN de l'organisme ayant produit la donnée", None))
        self.line_Producteur.setPlaceholderText(_translate("Dialog_PPBE", "Valeur par défaut : numéro Siren du Cerema", None))

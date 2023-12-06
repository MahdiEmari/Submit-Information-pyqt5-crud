from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QLabel,QApplication,QVBoxLayout, QWidget
from PyQt5.QtGui import QFont,QFontDatabase,QPixmap
from CRUD import CRUD
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(597, 536)
    
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.centralwidget.setStyleSheet("background-image: url('Login Image.png');")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel("برنامه اطلاعات دانشجویان شهیدشمسی‌پور",self.centralwidget)
        self.label.setStyleSheet("font-size: 20px; color: #000000;") 
        self.label_bottom = QtWidgets.QLabel("به نام خدا", self.centralwidget)
        self.label_bottom.setStyleSheet("font-size: 16px; color: #000000;")  # تنظیم فونت و رنگ متن
        self.horizontalLayout_bottom = QtWidgets.QHBoxLayout()
        self.horizontalLayout_bottom.addWidget(self.label_bottom)
        self.verticalLayout.addLayout(self.horizontalLayout_bottom)
        





        # font = QFont("B Nazanin")   اعمال فونت بی‌نازنین
        # font.setPointSize(20)  
        # self.label.setFont(font)
        font_db = QFontDatabase()
        font_id = font_db.addApplicationFont("BNazanin.ttf")  
        family = QFontDatabase.applicationFontFamilies(font_id)[0]
        app_font = QFont(family)
        QApplication.setFont(app_font)
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.label)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        palette = QtGui.QPalette()
        background_image = QtGui.QPixmap("AdobeStockscaled.jpeg")
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(background_image))
        self.tab.setAutoFillBackground(True)
        self.tab.setPalette(palette)
        self.label_bottom = QtWidgets.QLabel("کاری از مهدی عماری و میلاد فولادی ", self.centralwidget)
        self.label_bottom.setStyleSheet("font-size: 22px; color:#FFFFFF;")  # تنظیم فونت و رنگ متن
        self.horizontalLayout_bottom = QtWidgets.QHBoxLayout()
        self.horizontalLayout_bottom.addWidget(self.label_bottom)
        self.gridLayout.addWidget(self.label_bottom, 2, 0, 1, 1) 
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_Search = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Search.setObjectName("lineEdit_Search")
        self.horizontalLayout_2.addWidget(self.lineEdit_Search)
        self.lineEdit_Search.setAlignment(QtCore.Qt.AlignCenter)
        self.comboBox_search = QtWidgets.QComboBox(self.tab)
        self.comboBox_search.setObjectName("comboBox_search")
        self.comboBox_search.addItem("")
        self.comboBox_search.addItem("")
        self.comboBox_search.addItem("")
        self.comboBox_search.addItem("")
        self.comboBox_search.addItem("")
        self.comboBox_search.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_search)
# دکمه جستوجو 
        self.pushButton_Search = QtWidgets.QPushButton(self.tab)
        self.pushButton_Search.setObjectName("pushButton_Search")
        self.horizontalLayout_2.addWidget(self.pushButton_Search)
        self.pushButton_Search.clicked.connect(self.search_onClick)
# دکمه لود 
        self.pushButton_Load = QtWidgets.QPushButton(self.tab)
        self.pushButton_Load.setObjectName("pushButton_Load")
        self.pushButton_Load.clicked.connect(self.load_onClick)
        self.horizontalLayout_2.addWidget(self.pushButton_Load)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setRowCount(0)

        self.tableWidget.setColumnCount(12)
        self.tableWidget.setObjectName("tableWidget")

        self.tableWidget.setHorizontalHeaderLabels(["شناسه","نام","نام خانوادگی","ایمیل","تلفن",
                                                    "آدرس منزل", "ادرس محل کار", "سایر ادرس",
                                                    "شهر/روستا", "کدپستی","نام محل کار","جزئیات"])
        
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.add_customer = QtWidgets.QWidget()
        self.add_customer.setObjectName("add_customer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.add_customer)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_addcust = QtWidgets.QGridLayout()
        self.gridLayout_addcust.setObjectName("gridLayout_addcust")
       
        self.label_last_name = QtWidgets.QLabel(self.add_customer)
        self.label_last_name.setObjectName("label_last_name")
        self.gridLayout_addcust.addWidget(self.label_last_name, 2, 0, 1, 1)
        
        self.lineEdit_firstName = QtWidgets.QLineEdit(self.add_customer)
        self.lineEdit_firstName.setObjectName("lineEdit_firstName")
        self.gridLayout_addcust.addWidget(self.lineEdit_firstName, 1, 1, 1, 1)
        
        self.label_phone = QtWidgets.QLabel(self.add_customer)
        self.label_phone.setObjectName("label_phone")
        self.gridLayout_addcust.addWidget(self.label_phone, 3, 0, 1, 1)
        
        self.checkBox_add3 = QtWidgets.QCheckBox(self.add_customer)
        self.checkBox_add3.setText("")
        self.checkBox_add3.setObjectName("checkBox_add3")
        self.gridLayout_addcust.addWidget(self.checkBox_add3, 8, 2, 1, 1)
# Update Button
        self.pushButton_update = QtWidgets.QPushButton(self.add_customer)
        self.pushButton_update.setObjectName("pushButton_update")
        self.pushButton_update.clicked.connect(self.update_onClick)
        self.gridLayout_addcust.addWidget(self.pushButton_update, 12, 2, 1, 1)
        
        self.checkBox_Phone = QtWidgets.QCheckBox(self.add_customer)
        self.checkBox_Phone.setText("")
        self.checkBox_Phone.setObjectName("checkBox_Phone")
        self.gridLayout_addcust.addWidget(self.checkBox_Phone, 3, 2, 1, 1)
        
        self.label_postcode = QtWidgets.QLabel(self.add_customer)
        self.label_postcode.setObjectName("label_postcode")
        self.gridLayout_addcust.addWidget(self.label_postcode, 10, 0, 1, 1)
        
        self.label_towncity = QtWidgets.QLabel(self.add_customer)
        self.label_towncity.setObjectName("label_towncity")
        self.gridLayout_addcust.addWidget(self.label_towncity, 9, 0, 1, 1)
        
        self.label_address2 = QtWidgets.QLabel(self.add_customer)
        self.label_address2.setObjectName("label_address2")
        self.gridLayout_addcust.addWidget(self.label_address2, 7, 0, 1, 1)
        
        self.checkBox_add2 = QtWidgets.QCheckBox(self.add_customer)
        self.checkBox_add2.setText("")
        self.checkBox_add2.setObjectName("checkBox_add2")
        self.gridLayout_addcust.addWidget(self.checkBox_add2, 7, 2, 1, 1)
# Add Customer Button
        self.pushButton_addCustomer = QtWidgets.QPushButton(self.add_customer)
        self.pushButton_addCustomer.setObjectName("pushButton_addCustomer")
        self.pushButton_addCustomer.clicked.connect(self.add_onClick)
        self.gridLayout_addcust.addWidget(self.pushButton_addCustomer, 12, 1, 1, 1)
        
        self.lineEdit_lastName = QtWidgets.QLineEdit(self.add_customer)
        self.lineEdit_lastName.setObjectName("lineEdit_lastName")
        self.gridLayout_addcust.addWidget(self.lineEdit_lastName, 2, 1, 1, 1)
       
        self.lineEdit_phone = QtWidgets.QLineEdit(self.add_customer)
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.gridLayout_addcust.addWidget(self.lineEdit_phone, 3, 1, 1, 1)
        
        self.lineEdit_id = QtWidgets.QLineEdit(self.add_customer)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.gridLayout_addcust.addWidget(self.lineEdit_id, 0, 1, 1, 1)
        self.label_first_name = QtWidgets.QLabel(self.add_customer)
        self.label_first_name.setObjectName("label_first_name")
        self.gridLayout_addcust.addWidget(self.label_first_name, 1, 0, 1, 1)
        self.label_cust_id = QtWidgets.QLabel(self.add_customer)
        self.label_cust_id.setObjectName("label_cust_id")
        self.gridLayout_addcust.addWidget(self.label_cust_id, 0, 0, 1, 1)
        self.checkBox_lastName = QtWidgets.QCheckBox(self.add_customer)
        self.checkBox_lastName.setText("")
        self.checkBox_lastName.setObjectName("checkBox_lastName")
        self.gridLayout_addcust.addWidget(self.checkBox_lastName, 2, 2, 1, 1)
        self.label_email = QtWidgets.QLabel(self.add_customer)
        self.label_email.setObjectName("label_email")
        self.gridLayout_addcust.addWidget(self.label_email, 4, 0, 1, 1)
#Company and Detail
        self.label_company = QtWidgets.QLabel(self.add_customer)
        self.label_company.setObjectName("label_company")
        self.gridLayout_addcust.addWidget(self.label_company, 5, 0, 1, 1)
        self.lineEdit_company = QtWidgets.QLineEdit(self.add_customer)
        self.lineEdit_company.setObjectName("lineEdit_company")
        self.gridLayout_addcust.addWidget(self.lineEdit_company, 5, 1, 1, 1)
        self.checkBox_company = QtWidgets.QCheckBox(self.add_customer)
        self.checkBox_company.setText("")
        self.checkBox_company.setObjectName("checkBox_company")
        self.gridLayout_addcust.addWidget(self.checkBox_company, 5, 2, 1, 1)
        
#Company and Detail
        self.label_detail = QtWidgets.QLabel(self.add_customer)
        self.label_detail.setObjectName("label_detail")
        self.gridLayout_addcust.addWidget(self.label_detail, 11, 0, 1, 1)
        self.lineEdit_detail = QtWidgets.QLineEdit(self.add_customer)
        self.lineEdit_detail.setObjectName("lineEdit_detail")
        self.gridLayout_addcust.addWidget(self.lineEdit_detail, 11, 1, 1, 1)
        self.checkBox_detail = QtWidgets.QCheckBox(self.add_customer)
        self.checkBox_detail.setText("")
        self.checkBox_detail.setObjectName("checkBox_detail")
        self.gridLayout_addcust.addWidget(self.checkBox_detail, 11, 2, 1, 1)

        self.lineEdit_postcode = QtWidgets.QLineEdit(self.add_customer)
        self.lineEdit_postcode.setObjectName("lineEdit_postcode")
        self.gridLayout_addcust.addWidget(self.lineEdit_postcode, 10, 1, 1, 1)
        self.checkBox_postcode = QtWidgets.QCheckBox(self.add_customer)
        self.checkBox_postcode.setText("")
        self.checkBox_postcode.setObjectName("checkBox_postcode")
        self.gridLayout_addcust.addWidget(self.checkBox_postcode, 10, 2, 1, 1)
        self.lineEdit_address3 = QtWidgets.QLineEdit(self.add_customer)
        self.lineEdit_address3.setObjectName("lineEdit_address3")
        self.gridLayout_addcust.addWidget(self.lineEdit_address3, 8, 1, 1, 1)
        self.lineEdit_towncity = QtWidgets.QLineEdit(self.add_customer)
        self.lineEdit_towncity.setObjectName("lineEdit_towncity")
        self.gridLayout_addcust.addWidget(self.lineEdit_towncity, 9, 1, 1, 1)
        
        self.checkBox_firstName = QtWidgets.QCheckBox(self.add_customer)
        self.checkBox_firstName.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_firstName.sizePolicy().hasHeightForWidth())
        self.checkBox_firstName.setSizePolicy(sizePolicy)
        self.checkBox_firstName.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_firstName.setText("")
        self.checkBox_firstName.setCheckable(True)
        self.checkBox_firstName.setObjectName("checkBox_firstName")
        self.gridLayout_addcust.addWidget(self.checkBox_firstName, 1, 2, 1, 1)
        self.label_address3 = QtWidgets.QLabel(self.add_customer)
        self.label_address3.setObjectName("label_address3")
        self.gridLayout_addcust.addWidget(self.label_address3, 8, 0, 1, 1)
     
        self.checkBox_towncity = QtWidgets.QCheckBox(self.add_customer)
        self.checkBox_towncity.setText("")
        self.checkBox_towncity.setObjectName("checkBox_towncity")
        self.gridLayout_addcust.addWidget(self.checkBox_towncity, 9, 2, 1, 1)

        self.checkBox_email = QtWidgets.QCheckBox(self.add_customer)
        self.checkBox_email.setText("")
        self.checkBox_email.setObjectName("checkBox_email")
        self.gridLayout_addcust.addWidget(self.checkBox_email, 4, 2, 1, 1)
        self.lineEdit_address1 = QtWidgets.QLineEdit(self.add_customer)
        self.lineEdit_address1.setObjectName("lineEdit_address1")
        self.gridLayout_addcust.addWidget(self.lineEdit_address1, 6, 1, 1, 1)
        self.label_address1 = QtWidgets.QLabel(self.add_customer)
        self.label_address1.setObjectName("label_address1")
        self.gridLayout_addcust.addWidget(self.label_address1, 6, 0, 1, 1)
        self.lineEdit_address2 = QtWidgets.QLineEdit(self.add_customer)
        self.lineEdit_address2.setObjectName("lineEdit_address2")
        self.gridLayout_addcust.addWidget(self.lineEdit_address2, 7, 1, 1, 1)
        self.checkBox_add1 = QtWidgets.QCheckBox(self.add_customer)
        self.checkBox_add1.setText("")
        self.checkBox_add1.setObjectName("checkBox_add1")
        self.gridLayout_addcust.addWidget(self.checkBox_add1, 6, 2, 1, 1)
        
        self.lineEdit_email = QtWidgets.QLineEdit(self.add_customer)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.gridLayout_addcust.addWidget(self.lineEdit_email, 4, 1, 1, 1)

        self.label_updateInfo = QtWidgets.QLabel(self.add_customer)
        self.label_updateInfo.setObjectName("label_updateInfo")
        self.gridLayout_addcust.addWidget(self.label_updateInfo, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_addcust)
        self.tabWidget.addTab(self.add_customer, "")
        self.delete_cust = QtWidgets.QWidget()
        self.delete_cust.setObjectName("delete_cust")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.delete_cust)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(0, 0, 0, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
# Delete Customer Button
        self.pushButton_delete = QtWidgets.QPushButton(self.delete_cust)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_delete.clicked.connect(self.delete_onClick)
        
        self.gridLayout_2.addWidget(self.pushButton_delete, 3, 1, 1, 1)
        self.lineEdit_id_delete = QtWidgets.QLineEdit(self.delete_cust)
        self.lineEdit_id_delete.setObjectName("lineEdit_id_delete")
        self.lineEdit_id_delete.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_2.addWidget(self.lineEdit_id_delete, 2, 1, 1, 1)
        self.checkBox_confirm = QtWidgets.QCheckBox(self.delete_cust)
        self.checkBox_confirm.setObjectName("checkBox_confirm")
        self.gridLayout_2.addWidget(self.checkBox_confirm, 3, 2, 1, 1)
        self.label_enter_id = QtWidgets.QLabel(self.delete_cust)
        self.label_enter_id.setObjectName("label_enter_id")
        self.gridLayout_2.addWidget(self.label_enter_id, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 4, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.delete_cust, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 597, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "اطلاعات دانشجویان"))
        self.comboBox_search.setItemText(0, _translate("MainWindow", "ایدی"))
        self.comboBox_search.setItemText(1, _translate("MainWindow", "نام"))
        self.comboBox_search.setItemText(2, _translate("MainWindow", "نام‌خانوادگی"))
        self.comboBox_search.setItemText(3, _translate("MainWindow", "ایمیل"))
        self.comboBox_search.setItemText(4, _translate("MainWindow", "کدپستی"))
        self.comboBox_search.setItemText(5, _translate("MainWindow", "نام محل کار"))
        
        self.pushButton_Search.setText(_translate("MainWindow", "جستوجو"))
        self.pushButton_Load.setText(_translate("MainWindow", "refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "صفحه اصلی"))
        self.label_last_name.setText(_translate("MainWindow", ":نام خانوادگی"))
        self.label_phone.setText(_translate("MainWindow", ":تلفن موبایل"))
        self.pushButton_update.setText(_translate("MainWindow", "بروزرسانی"))
        self.label_postcode.setText(_translate("MainWindow", ":کدپستی"))
        self.label_towncity.setText(_translate("MainWindow", ":شهر/استان"))
        self.label_address2.setText(_translate("MainWindow", ":ادرس محل کار"))
        self.pushButton_addCustomer.setText(_translate("MainWindow", "افزودن مخاطب"))
        self.label_first_name.setText(_translate("MainWindow", ":نام"))
        self.label_cust_id.setText(_translate("MainWindow", ":شناسه مخاطب"))
        self.label_email.setText(_translate("MainWindow", ":ایمیل"))

        self.label_company.setText(_translate("MainWindow", ":نام محل کار"))
        self.label_detail.setText(_translate("MainWindow", ":جزئیات"))
        
        
        
        self.label_address3.setText(_translate("MainWindow", ":سایر ادرس ها"))
        self.label_address1.setText(_translate("MainWindow", ":آدرس منزل"))
        self.label_updateInfo.setText(_translate("MainWindow", "شناسه را وارد و سپس تیک بروزرسانی را بزنید "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add_customer), _translate("MainWindow", "افزودن مخاطب"))
        self.pushButton_delete.setText(_translate("MainWindow", "حذف"))
        self.checkBox_confirm.setText(_translate("MainWindow", "تیک تایید را قبل از حذف بزنید "))
        self.label_enter_id.setText(_translate("MainWindow", "شناسه را وارد کنید :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.delete_cust), _translate("MainWindow", "حذف مخاطب"))
        

# Connections and Functions

    def add_onClick(self):
        if self.lineEdit_id.text() == "":
            return self.show_popup('باید شناسه را وارد کنید')

        try:
            cust_id = int(self.lineEdit_id.text())

            f_name = self.checkIfEmpty(self.lineEdit_firstName.text())
            l_name = self.checkIfEmpty(self.lineEdit_lastName.text())
            phone = self.checkIfEmpty(self.lineEdit_phone.text())
            email = self.checkIfEmpty(self.lineEdit_email.text())
            add1 = self.checkIfEmpty(self.lineEdit_address1.text())
            add2 = self.checkIfEmpty(self.lineEdit_address2.text())
            add3 = self.checkIfEmpty(self.lineEdit_address3.text())
            tcity = self.checkIfEmpty(self.lineEdit_towncity.text())
            postcode = self.checkIfEmpty(self.lineEdit_postcode.text())
            company = self.checkIfEmpty(self.lineEdit_company.text())
            detail = self.checkIfEmpty(self.lineEdit_detail.text())

            file = CRUD('database.db')
            file.create_customer(cust_id,f_name, l_name, email, phone, add1, add2, add3, tcity, postcode, company, detail)
            self._clear_afterClick()
            self.show_popup("جزئیات با موفقیت اضافه شد")
        except Exception as e:
            self.show_popup("خطا در اضافه کردن جزئیات: " + str(e))
                
    def delete_onClick(self):
            if not self.checkBox_confirm.isChecked():
                return self.show_popup('Please tick and confirm you want to delete')
            
            cust_id = self.lineEdit_id_delete.text()
            if cust_id == "":
                return self.show_popup('Invalid Entry!')

            # ایجاد نمونه‌ای از کلاس CRUD
            crud = CRUD('database.db')
            # استفاده صحیح از متد delete_table با یک پارامتر
            crud.delete_table(cust_id)
            # تمیز کردن UI پس از حذف
            self.lineEdit_id_delete.clear()
            self.checkBox_confirm.setCheckState(False)
            self.show_popup('حذف با موفقیت انجام شد ')
                
            
    def search_onClick(self):
            if self.lineEdit_Search.text() == "":
                return self.show_popup("مقدار جستوجو خود را وارد کنید")
            comboSelect = self.checkComboBox(self.comboBox_search.currentText())
            searchValue =  self.searchCheck(self.lineEdit_Search.text())
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            try:
                query = "SELECT * FROM contact WHERE {} LIKE {}".format(comboSelect,searchValue)
                #query = "SELECT * FROM contact WHERE cust_id LIKE 1"
                print(query)
                result = c.execute(query)
                self.tableWidget.setRowCount(0)
                for row_num, row_data in enumerate(result):
                    self.tableWidget.insertRow(row_num)
                    for col_num, data in enumerate(row_data):
                        self.tableWidget.setItem(row_num, col_num,QtWidgets.QTableWidgetItem(str(data)))
                conn.close()
            except:
                self.show_popup('اطلاعاتی وجود ندارد')
            
            
        

    def update_onClick(self):
        try:
            file = CRUD('database.db')
            cust_id = self.lineEdit_id.text()
            if cust_id == "":
                return self.show_popup('شناسه را برای به روز رسانی وارد کنید')

            check_arr = [('first_name', self.checkBox_firstName.isChecked(), self.lineEdit_firstName.text()),
                        ('last_name', self.checkBox_lastName.isChecked(), self.lineEdit_lastName.text()),
                        ('phone', self.checkBox_Phone.isChecked(), self.lineEdit_phone.text()),
                        ('email', self.checkBox_email.isChecked(), self.lineEdit_email.text()),
                        ('company', self.checkBox_company.isChecked(), self.lineEdit_company.text()),
                        ('address1', self.checkBox_add1.isChecked(), self.lineEdit_address1.text()),
                        ('address2', self.checkBox_add2.isChecked(), self.lineEdit_address2.text()),
                        ('address3', self.checkBox_add3.isChecked(), self.lineEdit_address3.text()),
                        ('postcode', self.checkBox_postcode.isChecked(), self.lineEdit_postcode.text()),
                        ('detail', self.checkBox_detail.isChecked(), self.lineEdit_detail.text())]

            updated_fields = [(field, value) for field, checked, value in check_arr if checked]

            if not updated_fields:
                return self.show_popup('هیچ فیلدی برای به‌روزرسانی انتخاب نشده است')

            for field, value in updated_fields:
                file.update_customer(cust_id, field, value)

            self.show_popup('بروزرسانی با موفقیت انجام شد')
            self._clear_afterClick()
        except Exception:
            self.show_popup("شناسه مخاطب پیدا نشد")

                
    
    def load_onClick(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        try:
            query = "SELECT * FROM contact"
            result = c.execute(query)
            self.tableWidget.setRowCount(0)
            for row_num, row_data in enumerate(result):
                self.tableWidget.insertRow(row_num)
                for col_num, data in enumerate(row_data):
                    self.tableWidget.setItem(row_num, col_num,QtWidgets.QTableWidgetItem(str(data)))
            conn.close()
        except:
            self.show_popup('اطلاعاتی وجود ندارد ')
    # Popup for warning messages
    def show_popup(self, message):
        msg = QMessageBox()
        msg.setWindowTitle('test')
        msg.setText(message)
        msg.exec_()
        
    
    def _clear_afterClick(self):
            self.lineEdit_id.clear()
            self.lineEdit_firstName.clear()
            self.checkBox_firstName.setCheckState(False)
            self.lineEdit_lastName.clear()
            self.checkBox_lastName.setCheckState(False)
            self.lineEdit_phone.clear()
            self.checkBox_Phone.setCheckState(False)
            self.lineEdit_email.clear()
            self.checkBox_email.setCheckState(False)
            self.lineEdit_company.clear()
            self.checkBox_company.setCheckState(False)
            self.lineEdit_detail.clear()
            self.checkBox_detail.setCheckState(False)
            
            self.lineEdit_address1.clear()
            self.checkBox_add1.setCheckState(False)
            self.lineEdit_address2.clear()
            self.checkBox_add2.setCheckState(False)
            self.lineEdit_address3.clear()
            self.checkBox_add3.setCheckState(False)
            self.lineEdit_towncity.clear()
            self.checkBox_towncity.setCheckState(False)
            self.lineEdit_postcode.clear()
            self.checkBox_postcode.setCheckState(False)
    
    def checkIfEmpty(self,var):
        if var == "":
            return "Null"
        return var
    # Converts the retrieved select from combo to column format
    def checkIfEmpty(self,var):
        if var == "":
            return "Null"
        return var
    # Converts the retrieved select from combo to column format
    def checkComboBox(self, select):
        choice = {"ایدی":"cust_id",
                  "نام":"first_name",
                  "نام‌خانوادگی":"last_name",
                  "ایمیل":"email",
                  "کدپستی":"postcode",
                  "نام محل کار":"company"}
        if select == "ایدی":
            return choice[select]
        else:
            return str(choice[select])
    
    def searchCheck(self,data):
        if type(data) == type(0):
            return data
        return "'" + data + "%'"


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

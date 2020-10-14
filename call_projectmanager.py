from package import edit_entries
from package import project_manager
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog, QPushButton, QInputDialog, QLineEdit
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore
from package import explore_window
from package import project_manager as PM
from package import edit_entries as EDIT
from package import entrylist
from package import input_dialog
from package import detailswindow
from package import add_ideas
import threading
import sqlite3
from sqlite3 import Error
from functools import partial, total_ordering
import datetime


def create_connection():
    DataBaseName = "project_data.db"  # data base name
    try:
        con = sqlite3.connect(DataBaseName)
        return con
    except Error:
        pass


def table_col_info(cursor, table_name):  # return all available column names in a table
    cursor.execute('PRAGMA TABLE_INFO({})'.format(table_name))
    info = cursor.fetchall()
    column_names = []
    for col in info:
        column_names.append(col[1])


def CreateTable(conn, query):
    try:
        cursor_obj = conn.cursor()
        cursor_obj.execute(query)
        conn.commit()
        return "success"
    except Error:
        return "failure"


def deleterow(tablename, item_id):  # delete a row in a table
    conn = create_connection()
    delete_query = f"DELETE FROM {tablename} WHERE id={item_id}"
    cursor_obj = conn.cursor()
    cursor_obj.execute(delete_query)
    conn.commit()
    conn.close()


def insertintotable(conn, query, value):
    cursor = conn.cursor()
    cursor.execute(query, tuple(value))
    conn.commit()
    print('Data Inserted successfully!')


def fetchfromdb(conn, tablename='Project_Data'):
    query = f"SELECT * FROM {tablename}"
    curson_obj = conn.cursor()
    curson_obj.execute(query)
    rows = curson_obj.fetchall()

    entry_list = []
    for row in rows:
        entry_list.append(row)
    return entry_list


class PersonalProject:
    def __init__(self):
        self.conn = create_connection()
        self.tablename = 'personal_projects'
        self.databasename = 'project_data.db'

    def ideas(self, values):
        """
        Creates a table if table is non-existent in the data base
        adds the passed values into the table
        :param values:
        :return 'pass' or 'fail':
        """
        columns = ['id', 'project_name', 'project_details', 'complete_status', 'date_added', 'time_taken']
        Q = f"CREATE TABLE if not exists {self.tablename}({columns[0]} integer PRIMARY KEY,{columns[1]} text," \
            f"{columns[2]} text, {columns[3]} text, {columns[4]} text, {columns[5]} text) "
        response = CreateTable(self.conn, Q)
        if response == 'success':
            date_add_string = datetime.datetime.strftime(datetime.datetime.today(), "%d.%m.%Y")
            insert_Q = f"INSERT INTO {self.tablename}({columns[1]},{columns[2]},{columns[3]}, {columns[4]}) VALUES(?," \
                       f"?,?,?) "
            values.append(date_add_string)
            insertintotable(self.conn, insert_Q, values)
            return 'pass'
        else:
            return 'fail'

    def fetch(self):
        """
        Fetch all the ideas listed in the data base as a list of tuples
        :return:
        """
        entry_list = fetchfromdb(self.conn, tablename=self.tablename)
        return entry_list

    def updateDB(self, item_id, value):
        # try:
        # see for complete status changes
        cursor_obj = self.conn.cursor()
        query = f"SELECT complete_status from {self.tablename} where id=?"
        cursor_obj.execute(query, (item_id,))
        data = cursor_obj.fetchone()[0]
        if value[2] != data:  # data has been updated but complete status was different previously
            # get the date added value
            query = f"SELECT date_added from {self.tablename} where id=?"
            cursor_obj.execute(query, (item_id,))
            date_added = cursor_obj.fetchone()[0]  # stored in dd/mm/yyyy format
            date_added_obj = datetime.datetime.strptime(date_added, "%d/%m/%Y")
            present_date_obj = datetime.datetime.today()
            difference_days = (present_date_obj - date_added_obj).days
            # format time taken in days and months
            time_taken_month = difference_days // 30  # month
            time_taken_days = int(round(difference_days / 30 - time_taken_month, 1) * 30)
            time_taken = f"{time_taken_days} days, {time_taken_month} months"
            # update this timme taken in data base
            query = f"UPDATE {self.tablename} SET time_taken=? WHERE id=?"
            cursor_obj.execute(query, (time_taken, item_id))
            self.conn.commit()  # commit the changes
        # update time taken value
        columns = ['id', 'project_name', 'project_details', 'complete_status', 'date_added', 'time_taken']
        update_query = f'''UPDATE {self.tablename} SET {columns[1]}=?, {columns[2]}=?, {columns[3]}=? WHERE id= {item_id}'''

        cursor_obj.execute(update_query, tuple(value))
        self.conn.commit()


class EditDB(QMainWindow):
    def __init__(self, parent, data_list, item_id):
        super().__init__()
        self.ui = EDIT.Ui_MainWindow()
        self.ui.setupUi(self)
        self.parent_window = parent
        self.data_list = data_list
        self.item_id = item_id
        self.database = "project_data.db"
        self.tablename = "Project_data"

        self.fill_data()
        self.ui.pushButton_cancel.clicked.connect(self.returntoparent)
        self.ui.pushButton_confirm.clicked.connect(self.startupdate)
        self.ui.pushButton_delete.clicked.connect(self.deleterow)

    def deleterow(self):
        deleterow(self.tablename, self.item_id)
        self.returntoparent()

    def startupdate(self):
        updatedb = threading.Thread(target=self.updateDB)
        updatedb.start()

    def updateDB(self):
        conn = create_connection()
        cursor_obj = conn.cursor()
        table_col_info(cursor_obj, self.tablename)

        project_name = self.ui.lineEdit_projectname.text()
        definition = self.ui.textEdit_projectdef.toHtml()
        price = self.ui.lineEdit_price.text()
        submitdate = self.ui.lineEdit_submitdate.text()
        complete_status = self.ui.comboBox_completestatus.currentText()
        payment_status = self.ui.comboBox_paymentstatus.currentText()

        try:
            update_query = f'''UPDATE Project_data SET project_name=?, definition=?, price=?, submitDate=?, 
complete_status=?, payment_cleared=? WHERE id=? '''
            cursor_obj.execute(update_query,
                               tuple([project_name, definition, price, submitdate, complete_status, payment_status,
                                      self.item_id]))
            conn.commit()
            print("DataBase Updated Successfully...")
            # return 1
        except Exception as e:
            print("Some error occurred! ", e)
            sys.exit()
        self.returntoparent()
        conn.close()

    def returntoparent(self):
        self.parent_window.show()
        self.close()

    def fill_data(self):
        self.ui.lineEdit_projectname.setText(self.data_list[1])
        self.ui.lineEdit_price.setText(self.data_list[3])
        self.ui.lineEdit_submitdate.setText(self.data_list[4])
        if self.data_list[5] == 'complete':
            self.ui.comboBox_completestatus.setCurrentIndex(0)
        else:  # for pending case
            self.ui.comboBox_completestatus.setCurrentIndex(1)
        self.ui.textEdit_projectdef.setHtml(self.data_list[2])
        if self.data_list[7].lower() == 'cleared':
            self.ui.comboBox_paymentstatus.setCurrentIndex(1)  # payment
        else:
            self.ui.comboBox_paymentstatus.setCurrentIndex(0)  # payment


class DetailsWindow(QDialog):
    def __init__(self, display_text, parent_window):
        super().__init__()
        self.ui = detailswindow.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.display_text = display_text
        self.parent_window = parent_window
        self.ui.textEdit_details.setHtml(display_text)
        self.ui.pushButton_close.clicked.connect(self.returntoparent)

    def returntoparent(self):
        self.parent_window.show()
        self.close()


class EntryListing(QMainWindow):
    def __init__(self, parent, data, click='on'):
        super().__init__()
        self.ui = entrylist.Ui_MainWindow()
        self.ui.setupUi(self)
        if click != "on":
            self.data = sorted(data, key=lambda date: datetime.datetime.strptime(date[4], "%d/%m/%Y"), reverse=True)  #
        else:
            self.data = sorted(data, key=lambda date: datetime.datetime.strptime(date[4], "%d.%m.%Y"), reverse=True)  #
        # sort by submit date, data[4] is the submit date
        self.parented = parent
        for i in self.data:
            # display for pretty printing
            display = f'{str(i[0])}.{i[1].center(80 - len(i[1]))}{i[3].center(10 - len(i[1]) - len(i[3]))}'
            self.ui.item_list.addItem(display)

        self.ui.pushButton_cancel.clicked.connect(self.returntoparent)
        self.ui.item_list.setSpacing(3)

        if click != 'off' and click != 'Edit-Ideas':  # for click = on
            self.ui.item_list.itemClicked.connect(self.edit_db)
        elif click == 'Edit-Ideas':
            self.ui.item_list.itemClicked.connect(self.edit_ideas)

    def edit_ideas(self, item):
        item_id = item.text().split('.')[0]
        item_data = []
        for item in self.data:
            item_values = item[0]
            if int(item_values) == int(item_id):
                item_data = item

        self.ideas_window = AddIdeas(data=item_data, parent_window=self)
        self.ideas_window.show()
        self.hide()

    def edit_db(self, item):
        item_id = item.text().split('.')[0]
        item_data = []
        for item in self.data:
            item_values = item[0]
            if int(item_values) == int(item_id):
                item_data = item

        self.editwindow = EditDB(parent=self.parented, item_id=item_id, data_list=item_data)
        self.editwindow.show()
        self.close()

    def returntoparent(self):
        self.parented.show()
        self.close()


class FetchFromDataBase:
    def __init__(self, parent):
        self.sharedict = {}
        self.parentwindow = parent
        self.manage_operations()

    def manage_operations(self):
        conn = create_connection()
        self.entry_list = fetchfromdb(conn)  # get all rows * all_cols from Project_Data
        self.parentwindow.ui.pushButton_editentriest.setEnabled(True)  # enable the edit button
        self.ShowEntryListWindow = EntryListing(self.parentwindow, self.entry_list)
        self.ShowEntryListWindow.show()
        self.parentwindow.hide()


class AddToDataBase:
    success_signal = pyqtSignal()
    close_signal = pyqtSignal(str, str)

    def __init__(self, share_dict):
        self.share_dict = share_dict
        self.manageOperations()

    def manageOperations(self):
        query_insert = "INSERT INTO Project_Data(project_name,definition,price,submitDate,complete_status,date_added, " \
                       "payment_cleared) VALUES(?,?,?,?,?,?,?) "
        # id = self.share_dict['id']
        project_name = self.share_dict['project_name']
        definition = self.share_dict['definition']
        price = self.share_dict['price']
        submitDate = self.share_dict['submitDate']
        completestatus = self.share_dict['complete_status']
        payment_status = self.share_dict['payment_status']
        date_added = datetime.datetime.today().strftime("%d %B,%Y")

        conn = create_connection()
        cursor = conn.cursor()
        table_name = 'Project_Data'
        query_create = f"CREATE TABLE IF NOT EXISTS {table_name}(id integer PRIMARY KEY,project_name text, " \
                       f"definition text, price text, submitDate text, complete_status VARCHAR(30), date_added text, " \
                       f"payment_cleared char(20)) "
        response = CreateTable(conn, query_create)
        if response == 'success':
            print("Table Created Successfully!")
        else:
            print("Cannot Create Table!")
        # insert into table after table is create if wasn't present
        value = [project_name, definition, price, submitDate, completestatus, date_added, payment_status]
        insertintotable(conn, query_insert, tuple(value))


class ExploreWindow(QDialog):
    def __init__(self, parent_win):
        super().__init__()
        self.ui = explore_window.Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.parent_win = parent_win
        self.ui.pushButton_cancel.clicked.connect(self.returnToParent)
        self.ui.pushButton_ok.clicked.connect(self.displayDetails)
        self.show()

    def displayDetails(self):
        curr_index = self.ui.options.currentIndex()
        display_text = ''
        tot_value = 0.0
        flag_no_display = False
        if curr_index != 0:
            operation_type = self.ui.options.currentText()
            if 'pending jobs' in operation_type.lower():
                conn = create_connection()
                entry_list = fetchfromdb(conn)
                for project_count, project in enumerate(entry_list):
                    if project[5].lower().strip() == 'pending':
                        display_text += f'{project_count + 1}) <strong>{project[1]}</strong><br>'
                        if 'worth' in operation_type.lower():
                            worth = project[3]
                            if worth.strip(' USD').isdigit():
                                value = float(worth.strip(' USD'))
                                tot_value += value
                    else:
                        pass
                if curr_index in [1, 10]:
                    pass
                elif curr_index == 2:
                    display_text = f'Total Worth of all pending project are {tot_value} USD'
            elif 'last submission' in operation_type.lower():
                conn = create_connection()
                entry_list = fetchfromdb(conn)
                display_text = ''
                entry_list = sorted(entry_list, key=lambda date: datetime.datetime.strptime(date[4], "%d.%m.%Y"),
                                    reverse=True)
                for project in entry_list:
                    if project[5] == 'complete':  # get the last project completed
                        mod_list = list(map(str, project[1:]))
                        category_text_list = ["Project Name", "Project Definition", "Project Amount", "Submit Date",
                                              "Complete Status", "Date Added", "Payment Cleared"]
                        for pos, item in enumerate(mod_list):
                            category_text = category_text_list[pos]
                            display_text += f'<p><strong><u>{category_text}:</u></strong>{item}</p>'
                        break
                display_text = 'You last submission details is as follows:<p>' + display_text + '</p>'
            elif 'nearest submission' in operation_type.lower():
                min_diff = 0
                current_date = datetime.datetime.today()  # today's date time object
                conn = create_connection()
                entry_list = fetchfromdb(conn)
                for pos, project in enumerate(entry_list):
                    submit_date = project[4]
                    complete_status = project[5]
                    if complete_status == 'pending':
                        submit_date = datetime.datetime.strptime(str(submit_date), '%d.%m.%Y')
                        if min_diff == 0:
                            min_diff = submit_date - current_date
                            # print(f"First case min_diff=={min_diff}")
                            date_string = submit_date.strftime("%d %B, %Y")
                            display_text = f'Project <strong>"{project[1]}"</strong> has to be submitted ' \
                                           f'nearly.<br>Submission Date:<em>{date_string}</em>'  # project name
                        else:
                            print(16*'---')
                            print(project[1])
                            diff = submit_date - current_date
                            print(f"min_diff:{min_diff}, diff:{diff}\n{submit_date}\n")
                            if diff < min_diff:
                                min_diff = diff
                                date_string = submit_date.strftime("%d %B, %Y")
                                display_text = f'Project <strong>"{project[1]}"</strong> has to be submitted ' \
                                               f'nearly.<br>Submission Date:<em>{date_string}</em>'  # project name
                            else:
                                pass
                if display_text == '':
                    display_text = "No Projects Left To be Submitted."
            elif 'highest individual worth' in operation_type.lower():
                conn = create_connection()
                entry_list = fetchfromdb(conn)
                max_worth = 0.0
                max_worth_project = ''
                for pos, project in enumerate(entry_list):
                    worth = float(project[3].split(' ')[0])
                    project = project[1]
                    if worth > max_worth:
                        max_worth = worth
                        max_worth_project = project
                display_text = f'Project with name: <strong>{max_worth_project}</strong>,' \
                               f'<br> has the maximum worth of price <strong>{max_worth}</strong> USD'
            elif 'lowest individual worth' in operation_type.lower():
                conn = create_connection()
                entry_list = fetchfromdb(conn)
                min_worth = 0.0
                check_pos = 0
                min_worth_project = ''
                for pos, project in enumerate(entry_list):
                    worth = float(project[3].split()[0])
                    project = project[1]
                    if pos == check_pos:
                        if worth == 0:
                            check_pos += 1
                        else:
                            min_worth = worth
                    elif worth < min_worth and worth != 0:
                        min_worth = worth
                        min_worth_project = project
                display_text = f'Project with name: <strong>{min_worth_project}</strong>,' \
                               f'<br>Has the minimum worth of price <strong>{min_worth}</strong>'
            elif 'show pending payments' in operation_type.lower():
                conn = create_connection()
                entry_list = fetchfromdb(conn)
                total_price = 0
                list_text = ""
                for pos, project in enumerate(entry_list):
                    worth = project[3]
                    worth = int(worth.split(' ')[0]) * (72 if worth.split(' ')[-1] == 'USD' else 1)
                    project_name = project[1]
                    pending_status = project[7]
                    if pending_status.lower() in ['pending', 'not cleared'] and project[5] == 'complete':
                        # print(worth, project_name)
                        list_text += f"<li>{project_name} -- (<strong>₹{worth}</strong>) <em>$ {worth//72}</em></li><br>"
                        total_price += worth
                display_text = f"<ul>{list_text}</ul><br><hr>Total Price Pending clearance = ₹{total_price} [$ {total_price//72}]"
                print(f"Total price pending clearance=₹{total_price}")
            elif 'show project ideas/personal projects' in operation_type.lower():
                # open personal projects tab
                self.parent_win.ui.actionSee_Ideas.trigger()
                self.close()
                flag_no_display = True
            elif 'create report of all jobs (with time factor)' in operation_type.lower():
                flag_no_display = True
                display_text = self.follow_display_sequence()
                self.displaywindow = DetailsWindow(display_text, self)
                self.displaywindow.show()
            if not flag_no_display:
                self.displaywindow = DetailsWindow(display_text, self)
                self.displaywindow.show()

    def follow_display_sequence(self):
        # search type
        items = ['days', 'months']
        item, okPressed = QInputDialog.getItem(self, "Search Parameter", "search by month/days back:", items, 0, False)
        if okPressed and item:
            # input constraint
            max_value = 12 if item == 'months' else 30
            text, okPressed = QInputDialog.getInt(self, "Get constraint", f"Price for _____ {item}",
                                                  QLineEdit.Normal, 1,
                                                  max=max_value)
            if text and okPressed:
                parameter = item
                constraint = text

                # perform db operation
                conn = create_connection()
                entrylist = fetchfromdb(conn)
                tot_price = 0
                projects = []
                for entry in entrylist:
                    submit_date = entry[4]
                    date_object = datetime.datetime.strptime(submit_date, '%d.%m.%Y')
                    present_date = datetime.datetime.today()

                    difference = present_date - date_object
                    if parameter == 'months' and entry[5] == 'complete':
                        months = difference.days // 30
                        if constraint >= months:
                            projects.append(entry[1])
                            price_box = entry[3]
                            price = int(price_box.split(' ')[0])
                            currency = price_box.split(' ')[1]
                            if currency == 'USD':
                                price = price * 71  # current dollar rate
                            tot_price += price
                            projects[-1] += f" --- (₹ {price})<br>"
                    elif parameter == 'days' and entry[5] == 'complete':

                        days = difference.days
                        if constraint >= days:
                            projects.append(entry[1])
                            price_box = entry[3]
                            price = int(price_box.split(' ')[0])
                            currency = price_box.split(' ')[1]
                            if currency == 'USD':
                                price = price * 71  # current dollar rate
                            tot_price += price
                list_o = ''.join([f"<li>{project}</li>" for project in projects])
                project_list = f"<ul>{list_o}</ul>"
                display_text = f"Your total income for this period is <strong>₹ {tot_price}</strong><br><p>" \
                               f"{project_list}</p>"
                return display_text

        # perform db operations

    def returnToParent(self):
        self.parent_win.show()
        self.close()


class AddIdeas(QMainWindow):
    def __init__(self, parent_window, data=None):
        super().__init__()
        self.parentWindow = parent_window
        self.ui = add_ideas.Ui_MainWindow()
        self.ui.setupUi(self)

        self.data = data
        if self.data is not None:
            self.fillData()
        self.ui.pushButton_cancel.clicked.connect(self.returnToParent)
        self.ui.pushButton_add.clicked.connect(self.dataValidation)
        self.ui.lineEdit_projectname.textEdited.connect(self.ui.statusbar.clearMessage)
        self.ui.lineEdit_projectname.setFocus()

    def fillData(self):
        if self.data[3] == 'complete':
            self.ui.comboBox_completestatus.setCurrentIndex(1)
        self.ui.textEdit_details.setHtml(self.data[2])
        self.ui.lineEdit_projectname.setText(self.data[1])

    def dataValidation(self):
        project = self.ui.lineEdit_projectname.text()
        project_details = self.ui.textEdit_details.toHtml()
        complete_status = self.ui.comboBox_completestatus.currentText()
        if len(project) <= 30:
            P = PersonalProject()
            if self.data is None:
                response = P.ideas(values=[project, project_details, complete_status])
                if response == 'pass':
                    # reinitialize the window.
                    self.ui.lineEdit_projectname.setText('')
                    self.ui.textEdit_details.setText('')
                    self.ui.comboBox_completestatus.setCurrentIndex(0)
                    self.ui.statusbar.showMessage('Data Inserted Successfully!')
                    self.ui.statusbar.setStyleSheet('color: rgb(0,0,255);')
                    self.ui.lineEdit_projectname.setFocus()
                else:  # if response == fail
                    self.ui.statusbar.setStyleSheet('color: rgb(255,0,0);')
                    self.ui.statusbar.showMessage('Some Error Occurred while adding data.')
                    self.ui.lineEdit_projectname.setFocus()
            else:  # if data passed is not None
                P.updateDB(self.data[0], tuple([project, project_details, complete_status]))  # update database as given
                # item id and with the new values
                self.returnToParent()

    def returnToParent(self):
        self.parentWindow.show()
        self.close()


class AcceptWindow(QMainWindow):
    close_signal = pyqtSignal(str, str)

    def __init__(self, key_string):
        super().__init__()
        self.ui = input_dialog.Ui_MainWindow()
        self.ui.setupUi(self)

        self.key_string = key_string
        self.ui.pushButton_confirm.clicked.connect(self.input_validation)
        self.ui.pushButton_reset.clicked.connect(partial(self.ui.lineEdit_input.setText, ''))
        self.show()
        if self.key_string == "complete_status":
            self.ui.label_message.setText("Enter Project Status:\ncomplete or pending")
        elif self.key_string == "submitDate":
            self.ui.label_message.setText(
                "Enter Complete By Date in: dd.mm.yyyy format\n(and don't try to be creative\npress reset when needed)")
            self.ui.lineEdit_input.textEdited.connect(self.modifyinput)
        elif self.key_string == 'project_name':
            self.ui.label_message.setText("Enter The Project Name in short (under 30 chars)")
        elif self.key_string == 'price':
            self.ui.label_message.setText('Enter the amount of money you are receiving for the Project')

    def modifyinput(self):
        text = self.ui.lineEdit_input.text()
        if len(text) == 2 or len(text) == 5:
            text += '.'
            self.ui.lineEdit_input.setText(text)

    def input_validation(self):
        if self.ui.lineEdit_input.text().strip(' ') != '' and len(self.ui.lineEdit_input.text()) >= 1:
            if self.key_string == 'submitDate':
                if len(self.ui.lineEdit_input.text()) == 10 and len(self.ui.lineEdit_input.text().split('.')) == 3:
                    self.close_signal.emit(self.ui.lineEdit_input.text(), self.key_string)
            elif self.key_string == "complete_status":
                if self.ui.lineEdit_input.text() == 'complete' or self.ui.lineEdit_input.text() == 'pending':
                    self.close_signal.emit(self.ui.lineEdit_input.text(), self.key_string)
                else:
                    self.ui.statusbar.showMessage('complete status has to be "complete" or "pending" in lower-case')
            else:
                self.close_signal.emit(self.ui.lineEdit_input.text(), self.key_string)


class manager_window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = PM.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionClose_File.triggered.connect(self.close)
        self.ui.actionExplore.triggered.connect(self.exploreWindow)
        # add project definition to the dictionary and resets the instance
        self.ui.pushButton_addprojdef.clicked.connect(self.definition_validation)
        self.project_def = ""
        self.input_dict = {}

        self.ui.pushButton_completebytime.clicked.connect(self.accept_datetime)
        self.ui.pushButton_projectprice.clicked.connect(self.add_price)
        self.ui.pushButton_completestatus.clicked.connect(self.getCompleteStatus)
        self.ui.pushButton_loadprojectdef.clicked.connect(self.accept_project_name)
        self.ui.pushButton_addproject.clicked.connect(self.settodatabase)
        self.ui.pushButton_editentriest.clicked.connect(self.edittodatabase)
        self.ui.pushButton_paymentstatus.clicked.connect(self.getPaymentStatus)

        self.ui.actionNew_Idea.triggered.connect(self.addNewIdeas)
        self.ui.actionSee_Ideas.triggered.connect(self.showIdeas)
        self.ui.actionEdit_Ideas.triggered.connect(self.EditIdeas)

    def exploreWindow(self):
        self.openexplore = ExploreWindow(self)
        self.openexplore.show()
        self.hide()

    def EditIdeas(self):
        p = PersonalProject()
        entrylist = p.fetch()
        self.entrylist_window = EntryListing(self, entrylist, click='Edit-Ideas')
        self.entrylist_window.show()
        self.hide()

    def addNewIdeas(self):
        self.add_ideas = AddIdeas(self)
        self.add_ideas.show()
        self.hide()

    def showIdeas(self):
        p = PersonalProject()
        entryList = p.fetch()
        self.entrylist_window = EntryListing(self, entryList, click='off')
        self.entrylist_window.show()
        self.hide()

    def edittodatabase(self):
        self.ui.pushButton_editentriest.setDisabled(True)
        self.fetchdata = FetchFromDataBase(self)

    def getPaymentStatus(self):
        self.ui.pushButton_paymentstatus.setDisabled(True)
        self.accept_window = AcceptWindow('payment_status')
        self.accept_window.close_signal.connect(self.destroy_inputwindow)
        self.hide()

    def getCompleteStatus(self):
        self.ui.pushButton_completestatus.setDisabled(True)
        self.accept_window = AcceptWindow('complete_status')
        self.accept_window.close_signal.connect(self.destroy_inputwindow)
        self.hide()

    def settodatabase(self):
        if len(self.input_dict.keys()) == 6:  # ['project_name,definition,price,submitDate,complete_status,
            # payment_status]
            self.ui.textEdit_projectdefinition.clear()

            # write and reset
            db_thread = threading.Thread(target=AddToDataBase, args=(self.input_dict,))
            db_thread.start()
            self.input_dict = {}  # clearing input dict
            for pushbutton in self.findChildren(QPushButton):
                if not pushbutton.isEnabled():
                    pushbutton.setEnabled(True)
        else:
            self.ui.statusBar.setStyleSheet('color: red')
            self.ui.statusBar.showMessage('Details are not valid to add to Data Base. Please RECHECK!!!')

    def accept_project_name(self):
        self.ui.pushButton_loadprojectdef.setDisabled(True)
        self.accept_window = AcceptWindow('project_name')
        self.accept_window.close_signal.connect(self.destroy_inputwindow)
        # self.accept_window.close_signal.connect(self.show)
        self.hide()

    def destroy_inputwindow(self, input_string, key_string):  # also this saves the input data to the respective key
        self.accept_window.close()
        self.show()
        self.input_string = input_string
        self.input_dict[key_string] = self.input_string.strip()

    def increase_counter(self):
        pass

    def load_file_path(self):
        pass

    def add_price(self):
        self.ui.pushButton_projectprice.setDisabled(True)
        self.accept_window = AcceptWindow('price')
        self.accept_window.close_signal.connect(self.destroy_inputwindow)
        self.hide()

    def accept_datetime(self):
        self.ui.pushButton_completebytime.setDisabled(True)
        self.accept_window = AcceptWindow('submitDate')
        self.accept_window.close_signal.connect(self.destroy_inputwindow)
        self.hide()

    def definition_validation(self):
        text = self.ui.textEdit_projectdefinition.toHtml()
        if len(text) != 0:
            self.input_dict['definition'] = text

            self.ui.pushButton_addprojdef.setDisabled(True)
            self.ui.textEdit_projectdefinition.clear()

    def closeEvent(self, event):  # function to implement code confirmation
        close = QMessageBox()
        close.setWindowTitle("Exit")
        close.setText("Are You Sure You Want To Quit?")
        close.setIcon(QMessageBox.Information)
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()

        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = manager_window()
    w.show()
    sys.exit(app.exec_())

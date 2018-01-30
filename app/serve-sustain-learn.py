import tkinter.ttk as ttk
from datetime import datetime
from tkinter import *

import pymysql.cursors

connection = pymysql.connect(host='academic-mysql.cc.gatech.edu', user='cs4400_Group_3', password='tBrhlgNd',
                             db='cs4400_Group_3')
cursor = connection.cursor()

class GUI:
    def __init__(self, rootwin):

        self.rootwin = rootwin
        self.open_main_menu()

    def sortby(self, tree, col, descending):
        try:
            data = [(float(tree.set(child, col)), child) \
                    for child in tree.get_children('')]
        except:
            data = [(tree.set(child, col).lower(), child) \
                    for child in tree.get_children('')]

        data.sort(reverse=descending)

        for ix, item in enumerate(data):
            tree.move(item[1], '', ix)
        tree.heading(col, command=lambda col=col: self.sortby(tree, col, \
                                                              int(not descending)))

    def open_main_menu(self):
        self.main_menu_frame = Frame(self.rootwin)
        self.main_menu_frame.grid(row=0, column=0)

        login_label = Label(self.main_menu_frame, text="Login", font=("Arial", 25))
        login_label.grid(row=0, column=0, padx=10, pady=10)
        entry_frame = Frame(self.main_menu_frame)
        button_frame = Frame(self.main_menu_frame)
        entry_frame.grid(row=1, column=0)
        button_frame.grid(row=2, column=0)

        username_label = Label(entry_frame, text="Username", font=("Arial", 15))
        password_label = Label(entry_frame, text="Password", font=("Arial", 15))
        self.login_username_entry = Entry(entry_frame, width=30, state="normal", font=("Arial", 12))

        self.login_password_entry = Entry(entry_frame, width=30, state="normal", font=("Arial", 12), show="*")

        self.login_button = Button(button_frame, width=15, height=1, text="Login", font=("Arial", 15),
                                   command=self.check_login_credentials)
        self.register_button = Button(button_frame, width=15, height=1, text="Register", font=("Arial", 15),
                                      command=self.open_register_window)

        username_label.grid(row=0, column=0, padx=15, pady=15)
        password_label.grid(row=1, column=0, padx=15, pady=15)
        self.login_username_entry.grid(row=0, column=1, padx=15, pady=15)
        self.login_password_entry.grid(row=1, column=1, padx=15, pady=15)
        self.login_button.grid(row=2, column=0, padx=15, pady=15)
        self.register_button.grid(row=2, column=1, padx=15, pady=15)

    def open_register_window(self):
        cityquery = "SELECT DISTINCT City from LOCATION"
        cursor.execute(cityquery)
        raw_cities = cursor.fetchall()
        cities = [""]
        for item in raw_cities:
            cities.append(item[0])

        statequery = "SELECT DISTINCT State from LOCATION"
        cursor.execute(statequery)
        raw_states = cursor.fetchall()
        states = [""]
        for item in raw_states:
            states.append(item[0])

        states.sort()
        cities.sort()

        self.main_menu_frame.grid_forget()
        self.register_main_frame = Frame(self.rootwin)
        self.register_main_frame.grid(row=0, column=0)

        new_user_registration_label = Label(self.register_main_frame, text="New User Registration", font=("Arial", 25))
        new_user_registration_label.grid(row=0, column=0, padx=10, pady=10)

        entry_frame = Frame(self.register_main_frame)
        entry_frame.grid(row=1, column=0)

        username_label = Label(entry_frame, text="Username", font=("Arial", 15), anchor="w")
        email_label = Label(entry_frame, text="Email Address", font=("Arial", 15), anchor="w")
        password_label = Label(entry_frame, text="Password", font=("Arial", 15), anchor="w")
        confirm_password_label = Label(entry_frame, text="Confirm Password", font=("Arial", 15), anchor="w")
        user_type_label = Label(entry_frame, text="User Type", font=("Arial", 15), anchor="w")
        username_label.grid(row=0, column=0, padx=10, pady=10)
        email_label.grid(row=1, column=0, padx=10, pady=10)
        password_label.grid(row=2, column=0, padx=10, pady=10)
        confirm_password_label.grid(row=3, column=0, padx=10, pady=10)
        user_type_label.grid(row=4, column=0, padx=10, pady=10)

        self.username_entry = Entry(entry_frame, width=30, state="normal", font=("Arial", 12))
        self.email_entry = Entry(entry_frame, width=30, state="normal", font=("Arial", 12))
        self.password_entry = Entry(entry_frame, width=30, state="normal", font=("Arial", 12), show="*")
        self.confirm_password_entry = Entry(entry_frame, width=30, state="normal", font=("Arial", 12), show="*")
        self.user_type_variable = StringVar(entry_frame)
        self.user_type_variable.set("")
        user_type_entry = OptionMenu(entry_frame, self.user_type_variable, "", "City Official", "City Scientist")
        user_type_entry.config(width=30)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10)
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)
        self.confirm_password_entry.grid(row=3, column=1, padx=10, pady=10)
        user_type_entry.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

        city_official_entry_frame = Frame(self.register_main_frame)
        city_official_entry_frame.grid(row=3, column=0)
        city_official_entry_label = Label(self.register_main_frame,
                                          text="Complete the following information only if you are registering as a\ncity official.",
                                          font=("Arial", 12), anchor="w", justify="left")
        city_official_entry_label.grid(row=2, column=0, padx=10, pady=20)

        city_label = Label(city_official_entry_frame, text="            City            ", font=("Arial", 15),
                           anchor="w", justify="left")
        city_label.grid(row=0, column=0, padx=10, pady=10)
        self.city_variable = StringVar(entry_frame)
        self.city_variable.set("")
        city_entry = OptionMenu(city_official_entry_frame, self.city_variable, *cities)
        city_entry.config(width=38)
        city_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        state_label = Label(city_official_entry_frame, text="State", font=("Arial", 15), anchor="w", justify="left")
        state_label.grid(row=1, column=0, padx=10, pady=10)
        self.state_variable = StringVar(entry_frame)
        self.state_variable.set("")
        state_entry = OptionMenu(city_official_entry_frame, self.state_variable, *states)
        state_entry.config(width=38)
        state_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        title_entry_label = Label(city_official_entry_frame, text="Title", font=("Arial", 15), anchor="w",
                                  justify="left")
        title_entry_label.grid(row=2, column=0, padx=10, pady=10)
        self.title_entry = Entry(city_official_entry_frame, width=30, state="normal", font=("Arial", 12))
        self.title_entry.grid(row=2, column=1, padx=10, pady=10)

        button_frame = Frame(self.register_main_frame)
        button_frame.grid(row=4, column=0)

        back_button = Button(button_frame, width=15, height=1, text="Back", font=("Arial", 15),
                             command=self.back_to_login)
        back_button.grid(row=0, column=0, padx=10, pady=30)
        register_new_user_button = Button(button_frame, width=15, height=1, text="Create", font=("Arial", 15),
                                          command=self.check_new_user_information)
        register_new_user_button.grid(row=0, column=1, padx=10, pady=30)

    def back_to_login(self):
        try:
            self.register_main_frame.grid_forget()
        except:
            None
        try:
            self.official_menu_main_frame.grid_forget()
        except:
            None
        try:
            self.admin_menu_main_frame.grid_forget()
        except:
            None
        try:
            self.scientist_menu_main_frame.grid_forget()
        except:
            None
        try:
            self.official_menu_main_frame.grid_forget()
        except:
            None
        self.open_main_menu()

    def check_new_user_information(self):

        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        user_type = self.user_type_variable.get()
        city = self.city_variable.get()
        state = self.state_variable.get()
        title = self.title_entry.get()

        new_user_info = (username, email, password, user_type, city, state, title)
        userquery = "SELECT Username from USER"
        cursor.execute(userquery)
        usernameList = cursor.fetchall()
        emailquery = "SELECT Email from USER"
        cursor.execute(emailquery)
        emailList = cursor.fetchall()

        email_list = []
        for item in emailList:
            email_list.append(item[0])
        username_list = []
        for item in usernameList:
            username_list.append(item[0])

        a = new_user_info[0]  # username
        b = new_user_info[1]  # email
        c = new_user_info[2]  # password
        d = new_user_info[3]  # usertype
        e = new_user_info[4]  # city
        f = new_user_info[5]  # state
        g = new_user_info[6]  # title

        if (username == "") or (email == "") or (password == "") or (confirm_password == "") or (user_type == ""):
            self.new_user_error_message()
            self.register_main_frame.grid_forget()
            self.open_register_window()
        elif (username in username_list) or (email in email_list):
            self.new_user_error_message()
            self.register_main_frame.grid_forget()
            self.open_register_window()
        elif (password != confirm_password) or (user_type == ""):
            self.new_user_error_message()
            self.register_main_frame.grid_forget()
            self.open_register_window()
        elif user_type == "City Official":
            if (city == "") or (state == "") or (title == ""):
                self.new_user_error_message()
                self.register_main_frame.grid_forget()
                self.open_register_window()
            else:
                query = "SELECT State from LOCATION where City = '%s'"
                cursor.execute(query % city)
                checkstate = cursor.fetchone()[0]
                if state == checkstate:

                    p = 'Pending'
                    query = "INSERT INTO USER VALUES('%s','%s','%s','%s')"
                    cursor.execute(query % (a, b, c, d))
                    connection.commit()
                    newquery = "INSERT INTO CITYOFFICIAL VALUES('%s','%s','%s','%s', '%s')"
                    cursor.execute(newquery % (a, g, p, e, f))
                    connection.commit()
                    self.new_user_success_message()
                    self.back_to_login()
                else:
                    self.new_user_error_message()
                    self.register_main_frame.grid_forget()
                    self.open_register_window()
        else:
            query = "INSERT INTO USER VALUES('%s','%s','%s','%s')"
            cursor.execute(query % (a, b, c, d))
            connection.commit()
            self.new_user_success_message()
            self.back_to_login()

    def new_user_error_message(self):
        errorbox = Tk()
        errorbox.title("Error")

        error_label = Label(errorbox,
                            text="An error has been detected in the information you have submitted.\nYou may have omitted a required field, mismatched passwords,\nor attempted to create an account with a username or email which\nalready exists in the system.\n\nPlease check your information and try again.",
                            font=("Arial", 12), anchor="w", justify="left")
        error_label.grid(row=0, column=0, padx=20, pady=10)
        error_button = Button(errorbox, width=15, height=1, text="Okay", font=("Arial", 15), command=errorbox.destroy)
        error_button.grid(row=1, column=0, padx=10, pady=20)

    def new_user_success_message(self):
        successbox = Tk()
        successbox.title("Success")

        error_label = Label(successbox, text="You have successfully registered your account.", font=("Arial", 12),
                            anchor="w", justify="left")
        error_label.grid(row=0, column=0, padx=20, pady=10)
        error_button = Button(successbox, width=15, height=1, text="Okay", font=("Arial", 15),
                              command=successbox.destroy)
        error_button.grid(row=1, column=0, padx=10, pady=20)

    def check_login_credentials(self):
        login_credentials_tuple = (self.login_username_entry.get(), self.login_password_entry.get())

        self.user = login_credentials_tuple[0]
        password = login_credentials_tuple[1]

        try:
            query = ("SELECT Password from USER where Username = '%s'")
            cursor.execute(query % self.user)
            check = cursor.fetchone()[0]

            if password == check:
                credential_check = True
            else:
                credential_check = False
        except:
            credential_check = False

        try:
            job = ("SELECT UserType from USER where Username = '%s' AND Password = password")
            cursor.execute(job % self.user)
            job_type = cursor.fetchone()[0]
        except:
            job_type = None
            credential_check = False

        if credential_check == True:
            if job_type == "Admin":
                self.open_main_menu_admin()
            elif job_type == "City Scientist":
                self.open_main_menu_scientist()
            elif job_type == "City Official":
                self.check_city_official_status()
        else:
            self.credential_error_message()

    def credential_error_message(self):
        try:
            state = (self.errorbox.state() == "normal")
        except:
            state = False

        if state == False:
            self.errorbox = Tk()
            self.errorbox.title("Error")

            error_label = Label(self.errorbox,
                                text="The credentials you have submitted are invalid. Please check your\ninformation and try again.",
                                font=("Arial", 12), anchor="w", justify="left")
            error_label.grid(row=0, column=0, padx=20, pady=10)
            error_button = Button(self.errorbox, width=15, height=1, text="Okay", font=("Arial", 15),
                                  command=self.errorbox.destroy)
            error_button.grid(row=1, column=0, padx=10, pady=20)
        if state == True:
            self.errorbox.lift()

    def open_main_menu_admin(self):
        self.main_menu_frame.grid_forget()
        self.admin_menu_main_frame = Frame(self.rootwin)
        self.admin_menu_main_frame.grid(row=0, column=0)

        functionality_label = Label(self.admin_menu_main_frame, text="Choose Functionality", font=("Arial", 25),
                                    anchor="w", justify="left")
        functionality_label.grid(row=0, column=0, padx=30, pady=20)
        filter_search_button = Button(self.admin_menu_main_frame, width=25, height=1, text="Pending Data Points",
                                      font=("Arial", 15), command=self.view_pending_data_points)
        filter_search_button.grid(row=1, column=0, padx=10, pady=10)
        poi_report_button = Button(self.admin_menu_main_frame, width=25, height=1,
                                   text="Pending City Official Accounts", font=("Arial", 15),
                                   command=self.view_pending_city_official_account)
        poi_report_button.grid(row=2, column=0, padx=10, pady=10)
        logout_button = Button(self.admin_menu_main_frame, width=15, height=1, text="Log Out", font=("Arial", 15),
                               command=self.back_to_login)
        logout_button.grid(row=3, column=0, padx=10, pady=40)

    def open_main_menu_scientist(self):
        try:
            self.main_menu_frame.grid_forget()
            self.scientist_menu_main_frame = Frame(self.rootwin)
            self.scientist_menu_main_frame.grid(row=0, column=0)
        except:
            self.scientist_menu_main_frame = Frame(self.rootwin)
            self.scientist_menu_main_frame.grid(row=0, column=0)

        add_new_data_point_label = Label(self.scientist_menu_main_frame, text="Add a New Data Point",
                                         font=("Arial", 25), anchor="w", justify="left")
        add_new_data_point_label.grid(row=0, column=0, padx=30, pady=20)
        self.scientist_menu_main_add_data_point_frame = Frame(self.scientist_menu_main_frame)
        self.scientist_menu_main_add_data_point_frame.grid(row=1, column=0, padx=20)

        POIquery = "SELECT DISTINCT Name from POI"
        cursor.execute(POIquery)
        POInames = cursor.fetchall()
        pois = [""]
        for item in POInames:
            pois.append(item[0])

        location_frame = Frame(self.scientist_menu_main_add_data_point_frame)
        location_frame.grid(row=0, column=0)

        poi_location_name_label = Label(location_frame, text="POI Location Name:", font=("Arial", 12), anchor="w",
                                        justify="left")
        poi_location_name_label.grid(row=0, column=0)
        self.poi_location_name = StringVar(location_frame)
        self.poi_location_name.set("")
        city_entry = OptionMenu(location_frame, self.poi_location_name, *pois)
        city_entry.config(width=25)
        city_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        add_new_location_button = Button(location_frame, width=20, height=1, text="Add A New Location",
                                         font=("Arial", 12), command=self.open_add_new_location)
        add_new_location_button.grid(row=0, column=2, padx=20)

        date_time_frame = Frame(self.scientist_menu_main_add_data_point_frame)
        date_time_frame.grid(row=1, column=0)

        date_frame = Frame(date_time_frame)
        date_frame.grid(row=1, column=0, padx=10)
        date_label = Label(date_frame, text="Reading Date\n(DD/MM/YYYY)", font=("Arial", 12), anchor="w",
                           justify="center")
        date_label.grid(row=0, column=0, padx=5)
        self.new_data_point_day_entry = Entry(date_frame, width=3, state="normal", font=("Arial", 12))
        self.new_data_point_day_entry.grid(row=0, column=1, padx=1)
        self.new_data_point_month_entry = Entry(date_frame, width=3, state="normal", font=("Arial", 12))
        self.new_data_point_month_entry.grid(row=0, column=2, padx=1)
        self.new_data_point_year_entry = Entry(date_frame, width=6, state="normal", font=("Arial", 12))
        self.new_data_point_year_entry.grid(row=0, column=3, padx=1)

        time_frame = Frame(date_time_frame)
        time_frame.grid(row=1, column=1, padx=10)
        time_label = Label(time_frame, text="Reading Time\n(HH:MM)", font=("Arial", 12), anchor="w", justify="center")
        time_label.grid(row=0, column=0, padx=5)
        self.new_data_point_hour_entry = Entry(time_frame, width=3, state="normal", font=("Arial", 12))
        self.new_data_point_hour_entry.grid(row=0, column=1, padx=1)
        self.new_data_point_minute_entry = Entry(time_frame, width=3, state="normal", font=("Arial", 12))
        self.new_data_point_minute_entry.grid(row=0, column=2, padx=1)

        DTquery = "SELECT DISTINCT Type from DATATYPE"
        cursor.execute(DTquery)
        DTs = cursor.fetchall()
        dts = [""]
        for item in DTs:
            dts.append(item[0])

        data_type_frame = Frame(self.scientist_menu_main_add_data_point_frame)
        data_type_frame.grid(row=2, column=0)
        data_type_label = Label(data_type_frame, text="Data Type", font=("Arial", 12), anchor="w", justify="center")
        data_type_label.grid(row=0, column=0)
        self.data_type = StringVar(data_type_label)
        self.data_type.set("")
        data_type_entry = OptionMenu(data_type_frame, self.data_type, *dts)
        data_type_entry.config(width=15)
        data_type_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        data_value_label = Label(data_type_frame, text="Data Value (Integer)", font=("Arial", 12), anchor="w",
                                 justify="center")
        data_value_label.grid(row=0, column=2, padx=5)
        self.data_value_entry = Entry(data_type_frame, width=20, state="normal", font=("Arial", 12))
        self.data_value_entry.grid(row=0, column=3, padx=5)

        button_frame = Frame(self.scientist_menu_main_add_data_point_frame)
        button_frame.grid(row=3, column=0)
        back_button = Button(button_frame, width=20, height=1, text="Back", font=("Arial", 12),
                             command=self.back_to_login)
        back_button.grid(row=3, column=0)
        submit_button = Button(button_frame, width=20, height=1, text="Submit", font=("Arial", 12),
                               command=self.submit_new_data_point_check)
        submit_button.grid(row=3, column=1)

    def submit_new_data_point_check(self):
        day = self.new_data_point_day_entry.get()
        month = self.new_data_point_month_entry.get()
        year = self.new_data_point_year_entry.get()
        hour = self.new_data_point_hour_entry.get()
        minute = self.new_data_point_minute_entry.get()
        items = [day, month, year, hour, minute]

        if (len(day) == 2) and (len(month) == 2) and (len(year) == 4) and (len(hour) == 2) and (len(minute) == 2):
            length_check = True
        else:
            length_check = False

        error_count = 0
        for item in items:
            for char in item:
                try:
                    int(char)
                except:
                    error_count = error_count + 1
        if error_count > 0:
            char_check = False
        else:
            char_check = True

        if (length_check == True) and (char_check == True):
            try:
                date_time = year + "-" + month + "-" + day + " " + hour + ":" + minute + ":" + "00"
                date_time_test = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
                valid = True
            except:
                valid = False
                self.submit_data_point_error_message()

            if valid == True:
                a = date_time_test
                b = self.poi_location_name.get()
                try:
                    c = int(self.data_value_entry.get())
                    sql_inputs = True
                except:
                    sql_inputs = False
                d = self.data_type.get()
                p = "Pending"
                if (sql_inputs == True) and (b != "") and (d != ""):
                    try:
                        dtquery = "INSERT INTO DATAPOINT VALUES('%s','%s','%s','%d','%s')"
                        cursor.execute(dtquery % (a, b, p, c, d))
                        connection.commit()
                        self.scientist_menu_main_frame.grid_forget()
                        self.open_main_menu_scientist()

                        successbox = Tk()
                        successbox.title("Success")
                        error_label = Label(successbox,
                                            text="You have successfully submitted a new data point for review.",
                                            font=("Arial", 12), anchor="w", justify="left")
                        error_label.grid(row=0, column=0, padx=20, pady=10)
                        error_button = Button(successbox, width=15, height=1, text="Okay", font=("Arial", 15),
                                              command=successbox.destroy)
                        error_button.grid(row=1, column=0, padx=10, pady=20)
                    except:
                        failbox = Tk()
                        failbox.title("Error")
                        error_label = Label(failbox,
                                            text="The date and time you have selected is not unique for your chosen\nPOI location. Please try again.",
                                            font=("Arial", 12), anchor="w", justify="left")
                        error_label.grid(row=0, column=0, padx=20, pady=10)
                        error_button = Button(failbox, width=15, height=1, text="Okay", font=("Arial", 15),
                                              command=failbox.destroy)
                        error_button.grid(row=1, column=0, padx=10, pady=20)
                else:
                    self.submit_data_point_error_message()
        else:
            self.submit_data_point_error_message()

    def submit_data_point_error_message(self):
        try:
            state = (self.errorbox.state() == "normal")
        except:
            state = False

        if state == False:
            self.errorbox = Tk()
            self.errorbox.title("Error")
            error_label = Label(self.errorbox,
                                text="The data you have submitted contains formatting errors. Please\n check your information and try again.",
                                font=("Arial", 12), anchor="w", justify="left")
            error_label.grid(row=0, column=0, padx=20, pady=10)
            error_button = Button(self.errorbox, width=15, height=1, text="Okay", font=("Arial", 15),
                                  command=self.errorbox.destroy)
            error_button.grid(row=1, column=0, padx=10, pady=20)
        if state == True:
            self.errorbox.lift()

    def open_add_new_location(self):
        self.scientist_menu_main_frame.grid_forget()
        self.add_new_location_main_frame = Frame(self.rootwin)
        self.add_new_location_main_frame.grid(row=0, column=0)

        add_new_location_label = Label(self.add_new_location_main_frame, text="Add A New Location", font=("Arial", 25),
                                       anchor="w", justify="left")
        add_new_location_label.grid(row=0, column=0, padx=5, pady=5)

        add_new_location_entries_frame = Frame(self.add_new_location_main_frame)
        add_new_location_entries_frame.grid(row=1, column=0, padx=10, pady=10)

        poi_location_label = Label(add_new_location_entries_frame, text="POI Location Name", font=("Arial", 12),
                                   anchor="w", justify="left")
        poi_location_label.grid(row=1, column=0, padx=5, pady=5)
        self.poi_location_entry = Entry(add_new_location_entries_frame, width=25, state="normal", font=("Arial", 12))
        self.poi_location_entry.grid(row=1, column=1, padx=5, pady=5)

        cityquery = "SELECT DISTINCT City from LOCATION"
        cursor.execute(cityquery)
        raw_cities = cursor.fetchall()
        cities = [""]
        for item in raw_cities:
            cities.append(item[0])

        statequery = "SELECT DISTINCT State from LOCATION"
        cursor.execute(statequery)
        raw_states = cursor.fetchall()
        states = [""]
        for item in raw_states:
            states.append(item[0])

        states.sort()
        cities.sort()

        city_label = Label(add_new_location_entries_frame, text="City", font=("Arial", 12), anchor="w", justify="left")
        city_label.grid(row=2, column=0, padx=5)
        self.city = StringVar(add_new_location_entries_frame)
        self.city.set("")
        city_entry = OptionMenu(add_new_location_entries_frame, self.city, *cities)
        city_entry.config(width=30)
        city_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        state_label = Label(add_new_location_entries_frame, text="State", font=("Arial", 12), anchor="w",
                            justify="left")
        state_label.grid(row=3, column=0, padx=5)
        self.state = StringVar(add_new_location_entries_frame)
        self.state.set("")
        state_entry = OptionMenu(add_new_location_entries_frame, self.state, *states)
        state_entry.config(width=30)
        state_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        zip_label = Label(add_new_location_entries_frame, text="ZIP Code", font=("Arial", 12), anchor="w",
                          justify="left")
        zip_label.grid(row=4, column=0, padx=5, pady=5)
        self.zip_entry = Entry(add_new_location_entries_frame, width=25, state="normal", font=("Arial", 12))
        self.zip_entry.grid(row=4, column=1, padx=5, pady=5)

        button_frame = Frame(self.add_new_location_main_frame)
        button_frame.grid(row=2, column=0)
        back_button = Button(button_frame, width=15, height=1, text="Back", font=("Arial", 12),
                             command=self.back_to_main_menu_scientist)
        back_button.grid(row=0, column=0)
        submit_button = Button(button_frame, width=15, height=1, text="Submit", font=("Arial", 12),
                               command=self.check_new_location_submission)
        submit_button.grid(row=0, column=1)

    def back_to_main_menu_scientist(self):
        self.add_new_location_main_frame.grid_forget()
        self.open_main_menu_scientist()

    def check_new_location_submission(self):
        location_name = self.poi_location_entry.get()
        city = self.city.get()
        state = self.state.get()
        zip_code = self.zip_entry.get()
        if (location_name != "") and (city != "") and (state != "") and (len(zip_code) == 5):
            try:
                zip_code = int(zip_code)
                valid = True
            except:
                valid = False
        else:
            valid = False
        if valid == True:
            try:
                a = location_name
                d = zip_code
                e = city
                f = state
                poilocationquery = "INSERT INTO POI (Name, Zipcode, City, State) VALUES('%s', '%d', '%s', '%s')"
                cursor.execute(poilocationquery % (a, d, e, f))
                connection.commit()
                self.add_new_location_main_frame.grid_forget()
                self.open_main_menu_scientist()
                successbox = Tk()
                successbox.title("Success")
                error_label = Label(successbox, text="You have successfully submitted a new POI location.",
                                    font=("Arial", 12), anchor="w", justify="left")
                error_label.grid(row=0, column=0, padx=20, pady=10)
                error_button = Button(successbox, width=15, height=1, text="Okay", font=("Arial", 15),
                                      command=successbox.destroy)
                error_button.grid(row=1, column=0, padx=10, pady=20)
            except:
                failbox = Tk()
                failbox.title("Invalid Entry")
                error_label = Label(failbox, text="Errors were detected in your submission attempt. Please try again.",
                                    font=("Arial", 12), anchor="w", justify="left")
                error_label.grid(row=0, column=0, padx=20, pady=10)
                error_button = Button(failbox, width=15, height=1, text="Okay", font=("Arial", 15),
                                      command=failbox.destroy)
                error_button.grid(row=1, column=0, padx=10, pady=20)
        else:
            failbox = Tk()
            failbox.title("Invalid Entry")
            error_label = Label(failbox, text="Errors were detected in your submission attempt. Please try again.",
                                font=("Arial", 12), anchor="w", justify="left")
            error_label.grid(row=0, column=0, padx=20, pady=10)
            error_button = Button(failbox, width=15, height=1, text="Okay", font=("Arial", 15), command=failbox.destroy)
            error_button.grid(row=1, column=0, padx=10, pady=20)

    def check_city_official_status(self):
        check_city_official_query = "SELECT Status FROM CITYOFFICIAL WHERE Username = '%s'"
        cursor.execute(check_city_official_query % self.user)
        status = cursor.fetchone()[0]
        if status == "Accepted":
            self.open_main_menu_official_accepted()
        elif status == "Pending":
            self.open_main_menu_official_pending()
        else:
            self.open_main_menu_official_rejected()

    def open_main_menu_official_pending(self):
        errorbox = Tk()
        errorbox.title("Access Denied")

        error_label = Label(errorbox,
                            text="Your account status is yet to be approved pending administrative review. Please check back again later.",
                            font=("Arial", 12), anchor="w", justify="left")
        error_label.grid(row=0, column=0, padx=20, pady=10)
        error_button = Button(errorbox, width=15, height=1, text="Okay", font=("Arial", 15), command=errorbox.destroy)
        error_button.grid(row=1, column=0, padx=10, pady=20)

    def open_main_menu_official_rejected(self):
        errorbox = Tk()
        errorbox.title("Access Denied")

        error_label = Label(errorbox,
                            text="Your account status has been denied. You are not allowed access to this application.",
                            font=("Arial", 12), anchor="w", justify="left")
        error_label.grid(row=0, column=0, padx=20, pady=10)
        error_button = Button(errorbox, width=15, height=1, text="Okay", font=("Arial", 15), command=errorbox.destroy)
        error_button.grid(row=1, column=0, padx=10, pady=20)

    def open_main_menu_official_accepted(self):

        self.main_menu_frame.grid_forget()
        self.official_menu_main_frame = Frame(self.rootwin)
        self.official_menu_main_frame.grid(row=0, column=0)

        functionality_label = Label(self.official_menu_main_frame, text="Choose Functionality", font=("Arial", 25),
                                    anchor="w", justify="left")
        functionality_label.grid(row=0, column=0, padx=30, pady=20)
        filter_search_button = Button(self.official_menu_main_frame, width=25, height=1, text="Filter/Search POI",
                                      font=("Arial", 15), command=self.filter_search_poi)
        filter_search_button.grid(row=1, column=0, padx=10, pady=10)
        poi_report_button = Button(self.official_menu_main_frame, width=25, height=1, text="POI Report",
                                   font=("Arial", 15), command=self.poi_report)
        poi_report_button.grid(row=2, column=0, padx=10, pady=10)
        logout_button = Button(self.official_menu_main_frame, width=15, height=1, text="Log Out", font=("Arial", 15),
                               command=self.back_to_login)
        logout_button.grid(row=3, column=0, padx=10, pady=40)

    def poi_report(self):
        self.official_menu_main_frame.grid_forget()
        self.poi_report_main_frame = Frame(self.rootwin)
        self.poi_report_main_frame.grid(row=0, column=0)

        poi_report_label = Label(self.poi_report_main_frame, text="POI Report", font=("Arial", 25), anchor="w",
                                 justify="left")
        poi_report_label.grid(row=0, column=0, padx=10, pady=10)
        self.poi_report_tree_frame = Frame(self.poi_report_main_frame)
        self.poi_report_tree_frame.grid(row=1, column=0, padx=20)

        self.poi_report_tree_header = (
            "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven")
        self.poi_report_tree = ttk.Treeview(columns=self.poi_report_tree_header, show="headings")
        self.poi_report_tree.grid(row=0, column=0)

        self.poi_report_tree.column("one", width=100)
        self.poi_report_tree.column("two", width=100)
        self.poi_report_tree.column("three", width=100)
        self.poi_report_tree.column("four", width=100)
        self.poi_report_tree.column("five", width=100)
        self.poi_report_tree.column("six", width=100)
        self.poi_report_tree.column("seven", width=100)
        self.poi_report_tree.column("eight", width=100)
        self.poi_report_tree.column("nine", width=100)
        self.poi_report_tree.column("ten", width=100)
        self.poi_report_tree.column("eleven", width=100)
        self.poi_report_tree.heading("one", text="POI location",
                                     command=lambda c="one": self.sortby(self.poi_report_tree, c, 0))
        self.poi_report_tree.heading("two", text="City",
                                     command=lambda c="two": self.sortby(self.poi_report_tree, c, 0))
        self.poi_report_tree.heading("three", text="State",
                                     command=lambda c="three": self.sortby(self.poi_report_tree, c, 0))
        self.poi_report_tree.heading("four", text="Mold Min",
                                     command=lambda c="four": self.sortby(self.poi_report_tree, c, 0))
        self.poi_report_tree.heading("five", text="Mold Avg",
                                     command=lambda c="five": self.sortby(self.poi_report_tree, c, 0))
        self.poi_report_tree.heading("six", text="Mold Max",
                                     command=lambda c="six": self.sortby(self.poi_report_tree, c, 0))
        self.poi_report_tree.heading("seven", text="AQ Min",
                                     command=lambda c="seven": self.sortby(self.poi_report_tree, c, 0))
        self.poi_report_tree.heading("eight", text="AQ Avg",
                                     command=lambda c="eight": self.sortby(self.poi_report_tree, c, 0))
        self.poi_report_tree.heading("nine", text="AQ Max",
                                     command=lambda c="nine": self.sortby(self.poi_report_tree, c, 0))
        self.poi_report_tree.heading("ten", text="# of data points",
                                     command=lambda c="ten": self.sortby(self.poi_report_tree, c, 0))
        self.poi_report_tree.heading("eleven", text="Flagged?",
                                     command=lambda c="eleven": self.sortby(self.poi_report_tree, c, 0))

        vsb = ttk.Scrollbar(orient="vertical", command=self.poi_report_tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal", command=self.poi_report_tree.xview)
        self.poi_report_tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.poi_report_tree.grid(column=0, row=0, sticky='nsew', in_=self.poi_report_tree_frame)
        vsb.grid(column=1, row=0, sticky='ns', in_=self.poi_report_tree_frame)
        hsb.grid(column=0, row=1, sticky='ew', in_=self.poi_report_tree_frame)

        POIquery = "SELECT DISTINCT Name, City, State, Flag from POI ORDER BY Name"
        cursor.execute(POIquery)
        POInames = cursor.fetchall()

        self.ReportEntries = []

        for item in POInames:
            MoldCountQuery = "SELECT COUNT(DataValue) FROM DATAPOINT Where Name = '%s' AND Type = 'Mold' AND Status = 'Accepted'"
            cursor.execute(MoldCountQuery % item[0])
            MoldCount = cursor.fetchone()[0]
            MoldMin = 0
            MoldMax = 0
            MoldAvg = 0
            if MoldCount > 0:
                MoldMinQuery = "SELECT MIN(DataValue) FROM DATAPOINT Where Name = '%s' AND Type = 'Mold' AND Status = 'Accepted'"
                cursor.execute(MoldMinQuery % item[0])
                MoldMin = cursor.fetchone()[0]
                MoldMaxQuery = "SELECT MAX(DataValue) FROM DATAPOINT Where Name = '%s' AND Type = 'Mold' AND Status = 'Accepted'"
                cursor.execute(MoldMaxQuery % item[0])
                MoldMax = cursor.fetchone()[0]
                MoldAveQuery = "SELECT AVG(DataValue) FROM DATAPOINT Where Name = '%s' AND Type = 'Mold' AND Status = 'Accepted'"
                cursor.execute(MoldAveQuery % item[0])
                MoldAvg = round(cursor.fetchone()[0], 1)

            AQCountQuery = "SELECT COUNT(DataValue) FROM DATAPOINT Where Name = '%s' AND Type = 'Air Quality' AND Status = 'Accepted'"
            cursor.execute(AQCountQuery % item[0])
            AQCount = cursor.fetchone()[0]
            AQMin = 0
            AQMax = 0
            AQAvg = 0
            if AQCount > 0:
                AQMinQuery = "SELECT MIN(DataValue) FROM DATAPOINT Where Name = '%s' AND Type = 'Air Quality' AND Status = 'Accepted'"
                cursor.execute(AQMinQuery % item[0])
                AQMin = cursor.fetchone()[0]
                AQMaxQuery = "SELECT MAX(DataValue) FROM DATAPOINT Where Name = '%s' AND Type = 'Air Quality' AND Status = 'Accepted'"
                cursor.execute(AQMaxQuery % item[0])
                AQMax = cursor.fetchone()[0]
                AQAveQuery = "SELECT AVG(DataValue) FROM DATAPOINT Where Name = '%s' AND Type = 'Air Quality' AND Status = 'Accepted'"
                cursor.execute(AQAveQuery % item[0])
                AQAvg = round(cursor.fetchone()[0], 1)
            Count = str(MoldCount + AQCount)
            Flag = "no"
            if item[3] == 1:
                Flag = "yes"
            entry = (
                item[0], item[1], item[2], MoldMin, MoldAvg, MoldMax, str(AQMin), str(AQAvg), str(AQMax),
                Count,
                Flag)
            self.ReportEntries.append(entry)
        for entry in self.ReportEntries:
            self.poi_report_tree.insert("", 0, values=(
                entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6], entry[7], entry[8], entry[9],
                entry[10]))

        back_button = Button(self.poi_report_main_frame, width=25, height=1, text="Back", font=("Arial", 15),
                             command=self.back_to_main_menu_official)
        back_button.grid(row=2, column=0)

    def filter_search_poi(self):
        self.official_menu_main_frame.grid_forget()
        self.filter_search_poi_frame = Frame(self.rootwin)
        self.filter_search_poi_frame.grid(row=0, column=0)

        view_poi_label = Label(self.filter_search_poi_frame, text="View POIs", font=("Arial", 25), anchor="w",
                               justify="center")
        view_poi_label.grid(row=0, column=0, padx=10, pady=10)
        filter_options_frame = Frame(self.filter_search_poi_frame)
        filter_options_frame.grid(row=1, column=0)

        POIquery = "SELECT DISTINCT Name from POI ORDER BY Name"
        cursor.execute(POIquery)
        POInames = cursor.fetchall()
        pois = [""]
        for item in POInames:
            pois.append(item[0])

        cityquery = "SELECT DISTINCT City from LOCATION ORDER BY City"
        cursor.execute(cityquery)
        raw_cities = cursor.fetchall()
        cities = [""]
        for item in raw_cities:
            cities.append(item[0])

        statequery = "SELECT DISTINCT State from LOCATION ORDER BY State"
        cursor.execute(statequery)
        raw_states = cursor.fetchall()
        states = [""]
        for item in raw_states:
            states.append(item[0])

        poi_location_name_label = Label(filter_options_frame, text="POI Location Name", font=("Arial", 15),
                                        justify="left")
        poi_location_name_label.grid(row=0, column=0, padx=10, pady=10)
        city_label = Label(filter_options_frame, text="City", font=("Arial", 15), justify="left")
        city_label.grid(row=1, column=0, padx=10, pady=10)
        state_label = Label(filter_options_frame, text="State", font=("Arial", 15), justify="left")
        state_label.grid(row=2, column=0, padx=10, pady=10)
        zip_code_label = Label(filter_options_frame, text="ZIP Code", font=("Arial", 15), justify="left")
        zip_code_label.grid(row=3, column=0, padx=10, pady=10)
        flagged_label = Label(filter_options_frame, text="Flagged?", font=("Arial", 15), justify="left")
        flagged_label.grid(row=4, column=0, padx=10, pady=10)
        date_flagged_label = Label(filter_options_frame, text="Date Flagged (DD/MM/YYYY)", font=("Arial", 15),
                                   justify="left")
        date_flagged_label.grid(row=5, column=0, padx=10, pady=10)

        self.poi_location_name_variable = StringVar(filter_options_frame)
        self.poi_location_name_variable.set("")
        poi_location_entry = OptionMenu(filter_options_frame, self.poi_location_name_variable, *pois)
        poi_location_entry.config(width=30)
        poi_location_entry.grid(row=0, column=1, padx=10, pady=10)

        self.poi_city_variable = StringVar(filter_options_frame)
        self.poi_city_variable.set("")
        poi_city_entry = OptionMenu(filter_options_frame, self.poi_city_variable, *cities)
        poi_city_entry.config(width=30)
        poi_city_entry.grid(row=1, column=1, padx=10, pady=10)

        self.poi_state_variable = StringVar(filter_options_frame)
        self.poi_state_variable.set("")
        poi_state_entry = OptionMenu(filter_options_frame, self.poi_state_variable, *states)
        poi_state_entry.config(width=30)
        poi_state_entry.grid(row=2, column=1, padx=10, pady=10)

        self.poi_zip_code_entry = Entry(filter_options_frame, width=25, state="normal", font=("Arial", 12))
        self.poi_zip_code_entry.grid(row=3, column=1)

        self.poi_flagged_yn_var = IntVar()
        self.poi_flagged_yn = Checkbutton(filter_options_frame, variable=self.poi_flagged_yn_var)
        self.poi_flagged_yn.grid(row=4, column=1)

        date_flagged_frame = Frame(filter_options_frame)
        date_flagged_frame.grid(row=5, column=1)
        date_flagged_start_frame = Frame(date_flagged_frame)
        date_flagged_start_frame.grid(row=0, column=0)
        date_flagged_to_label = Label(date_flagged_frame, text=" to ", font=("Arial", 12), anchor="w", justify="center")
        date_flagged_to_label.grid(row=0, column=1)
        date_flagged_end_frame = Frame(date_flagged_frame)
        date_flagged_end_frame.grid(row=0, column=2)

        self.poi_start_day_entry = Entry(date_flagged_start_frame, width=3, state="normal", font=("Arial", 12))
        self.poi_start_day_entry.grid(row=0, column=1, padx=1)
        self.poi_start_month_entry = Entry(date_flagged_start_frame, width=3, state="normal", font=("Arial", 12))
        self.poi_start_month_entry.grid(row=0, column=2, padx=1)
        self.poi_start_year_entry = Entry(date_flagged_start_frame, width=6, state="normal", font=("Arial", 12))
        self.poi_start_year_entry.grid(row=0, column=3, padx=1)

        self.poi_end_day_entry = Entry(date_flagged_end_frame, width=3, state="normal", font=("Arial", 12))
        self.poi_end_day_entry.grid(row=0, column=1, padx=1)
        self.poi_end_month_entry = Entry(date_flagged_end_frame, width=3, state="normal", font=("Arial", 12))
        self.poi_end_month_entry.grid(row=0, column=2, padx=1)
        self.poi_end_year_entry = Entry(date_flagged_end_frame, width=6, state="normal", font=("Arial", 12))
        self.poi_end_year_entry.grid(row=0, column=3, padx=1)

        button_frame = Frame(self.filter_search_poi_frame)
        button_frame.grid(row=2, column=0, padx=10, pady=10)

        apply_filters_button = Button(button_frame, width=25, height=1, text="Apply Filters", font=("Arial", 10),
                                      command=self.apply_poi_filters)
        apply_filters_button.grid(row=0, column=0)
        reset_filters_button = Button(button_frame, width=25, height=1, text="Reset Filters", font=("Arial", 10),
                                      command=self.reset_poi_filters)
        reset_filters_button.grid(row=0, column=1)
        view_poi_detail_button = Button(button_frame, width=25, height=1, text="View Selected POI Detail",
                                        font=("Arial", 10), command=self.view_poi_detail)
        view_poi_detail_button.grid(row=0, column=2)

        lower_button_frame = Frame(self.filter_search_poi_frame)
        lower_button_frame.grid(row=4, column=0, padx=10, pady=10)
        back_to_main_menu_official_button = Button(lower_button_frame, width=15, height=1, text="Back",
                                                   font=("Arial", 10), command=self.back_to_main_menu_official)
        back_to_main_menu_official_button.grid(row=0, column=0)

        tree_frame = Frame(self.filter_search_poi_frame)
        tree_frame.grid(row=3, column=0)

        self.view_poi_tree = ttk.Treeview(tree_frame)
        self.view_poi_tree.grid(row=0, column=0)

        self.view_poi_tree["columns"] = ("one", "two", "three", "four", "five", "six")
        self.view_poi_tree.column("one", width=100)
        self.view_poi_tree.column("two", width=100)
        self.view_poi_tree.column("three", width=100)
        self.view_poi_tree.column("four", width=100)
        self.view_poi_tree.column("five", width=100)
        self.view_poi_tree.column("six", width=100)
        self.view_poi_tree.heading("one", text="Location Name",
                                   command=lambda c="one": self.sortby(self.view_poi_tree, c, 0))
        self.view_poi_tree.heading("two", text="City", command=lambda c="two": self.sortby(self.view_poi_tree, c, 0))
        self.view_poi_tree.heading("three", text="State",
                                   command=lambda c="three": self.sortby(self.view_poi_tree, c, 0))
        self.view_poi_tree.heading("four", text="Zip Code",
                                   command=lambda c="four": self.sortby(self.view_poi_tree, c, 0))
        self.view_poi_tree.heading("five", text="Flagged?",
                                   command=lambda c="five": self.sortby(self.view_poi_tree, c, 0))
        self.view_poi_tree.heading("six", text="Date Flagged",
                                   command=lambda c="six": self.sortby(self.view_poi_tree, c, 0))

        vsb = ttk.Scrollbar(orient="vertical", command=self.view_poi_tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal", command=self.view_poi_tree.xview)
        self.view_poi_tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.view_poi_tree.grid(column=0, row=0, sticky='nsew', in_=tree_frame)
        vsb.grid(column=1, row=0, sticky='ns', in_=tree_frame)
        hsb.grid(column=0, row=1, sticky='ew', in_=tree_frame)

    def reset_poi_filters(self):
        self.filter_search_poi_frame.grid_forget()
        self.filter_search_poi()

    def back_to_main_menu_official(self):
        try:
            self.filter_search_poi_frame.grid_forget()
            self.open_main_menu_official_accepted()
        except:
            pass
        try:
            self.poi_report_main_frame.grid_forget()
            self.open_main_menu_official_accepted()
        except:
            pass

    def view_poi_detail(self):
        selected_records = []
        for record in self.view_poi_tree.selection():
            selected_record = self.view_poi_tree.item(record, "values")
            selected_records.append(selected_record)
        if len(selected_records) > 1:
            failbox = Tk()
            failbox.title("Invalid Entry")
            error_label = Label(failbox, text="You may only select one POI location at a time. Please try again.",
                                font=("Arial", 12), anchor="w", justify="left")
            error_label.grid(row=0, column=0, padx=20, pady=10)
            error_button = Button(failbox, width=15, height=1, text="Okay", font=("Arial", 15), command=failbox.destroy)
            error_button.grid(row=1, column=0, padx=10, pady=20)
        elif len(selected_records) == 0:
            failbox = Tk()
            failbox.title("Invalid Entry")
            error_label = Label(failbox, text="You must select a POI location to view. Please try again.",
                                font=("Arial", 12), anchor="w", justify="left")
            error_label.grid(row=0, column=0, padx=20, pady=10)
            error_button = Button(failbox, width=15, height=1, text="Okay", font=("Arial", 15), command=failbox.destroy)
            error_button.grid(row=1, column=0, padx=10, pady=20)
        elif len(selected_records) == 1:
            self.selected_poi = selected_records[0][0]
            self.filter_search_poi_frame.grid_forget()
            self.view_detail_poi_frame = Frame(self.rootwin)
            self.view_detail_poi_frame.grid(row=0, column=0)

            poi_detail_label = Label(self.view_detail_poi_frame, text="POI Detail" + " for " + self.selected_poi,
                                     font=("Arial", 25), anchor="w", justify="center")
            poi_detail_label.grid(row=0, column=0)
            poi_detail_filters_frame = Frame(self.view_detail_poi_frame)
            poi_detail_filters_frame.grid(row=1, column=0)
            type_label = Label(poi_detail_filters_frame, text="Type", font=("Arial", 15), anchor="w", justify="left")
            type_label.grid(row=0, column=0, padx=10, pady=10)
            data_value_label = Label(poi_detail_filters_frame, text="Data Value", font=("Arial", 15), anchor="w",
                                     justify="left")
            data_value_label.grid(row=1, column=0, padx=10, pady=10)
            time_date_label = Label(poi_detail_filters_frame, text="Date\n(DD/MM/YYYY)", font=("Arial", 15), anchor="w",
                                    justify="center")
            time_date_label.grid(row=2, column=0, padx=10, pady=10)

            DTQuery = "SELECT Type FROM DATATYPE ORDER BY Type"
            cursor.execute(DTQuery)
            rawDTs = cursor.fetchall()
            DTs = [""]
            for item in rawDTs:
                DTs.append(item[0])

            self.poi_detail_type = StringVar(poi_detail_filters_frame)
            self.poi_detail_type.set("")
            city_entry = OptionMenu(poi_detail_filters_frame, self.poi_detail_type, *DTs)
            city_entry.config(width=20)
            city_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

            data_value_frame = Frame(poi_detail_filters_frame)
            data_value_frame.grid(row=1, column=1)
            self.poi_detail_data_value_min = Entry(data_value_frame, width=10, state="normal", font=("Arial", 12))
            self.poi_detail_data_value_min.grid(row=0, column=0, padx=10, pady=10)
            to_label_0 = Label(data_value_frame, text=" to ", font=("Arial", 10), anchor="w", justify="center")
            to_label_0.grid(row=0, column=1)
            self.poi_detail_data_value_max = Entry(data_value_frame, width=10, state="normal", font=("Arial", 12))
            self.poi_detail_data_value_max.grid(row=0, column=2, padx=10, pady=10)

            time_date_frame = Frame(poi_detail_filters_frame)
            time_date_frame.grid(row=2, column=1)
            start_time_date_frame = Frame(time_date_frame)
            start_time_date_frame.grid(row=0, column=0)
            to_label_1 = Label(time_date_frame, text=" to ", font=("Arial", 10), anchor="w", justify="center")
            to_label_1.grid(row=0, column=1)
            end_time_date_frame = Frame(time_date_frame)
            end_time_date_frame.grid(row=0, column=2)

            self.poi_detail_start_day_entry = Entry(start_time_date_frame, width=3, state="normal", font=("Arial", 12))
            self.poi_detail_start_day_entry.grid(row=0, column=1, padx=1)
            self.poi_detail_start_month_entry = Entry(start_time_date_frame, width=3, state="normal",
                                                      font=("Arial", 12))
            self.poi_detail_start_month_entry.grid(row=0, column=2, padx=1)
            self.poi_detail_start_year_entry = Entry(start_time_date_frame, width=6, state="normal", font=("Arial", 12))
            self.poi_detail_start_year_entry.grid(row=0, column=3, padx=1)

            self.poi_detail_end_day_entry = Entry(end_time_date_frame, width=3, state="normal", font=("Arial", 12))
            self.poi_detail_end_day_entry.grid(row=0, column=1, padx=1)
            self.poi_detail_end_month_entry = Entry(end_time_date_frame, width=3, state="normal", font=("Arial", 12))
            self.poi_detail_end_month_entry.grid(row=0, column=2, padx=1)
            self.poi_detail_end_year_entry = Entry(end_time_date_frame, width=6, state="normal", font=("Arial", 12))
            self.poi_detail_end_year_entry.grid(row=0, column=3, padx=1)

            button_frame = Frame(self.view_detail_poi_frame)
            button_frame.grid(row=2, column=0)
            apply_filters_button = Button(button_frame, width=15, height=1, text="Apply Filters", font=("Arial", 10),
                                          command=self.apply_poi_detail_filters)
            apply_filters_button.grid(row=0, column=0)
            reset_filters_button = Button(button_frame, width=15, height=1, text="Reset Filters", font=("Arial", 10),
                                          command=self.reset_view_poi_detail)
            reset_filters_button.grid(row=0, column=1)

            lower_button_frame = Frame(self.view_detail_poi_frame)
            lower_button_frame.grid(row=4, column=0)
            back_button = Button(lower_button_frame, width=15, height=1, text="Back", font=("Arial", 10),
                                 command=self.back_to_filter_search)
            back_button.grid(row=0, column=0)
            flag_button = Button(lower_button_frame, width=15, height=1, text="Flag", font=("Arial", 10),
                                 command=self.flag_poi)
            flag_button.grid(row=0, column=1)

            tree_frame = Frame(self.view_detail_poi_frame)
            tree_frame.grid(row=3, column=0, padx=10, pady=10)

            self.poi_detail_tree = ttk.Treeview(tree_frame)
            self.poi_detail_tree.grid(row=0, column=0)

            self.poi_detail_tree["columns"] = ("one", "two", "three")
            self.poi_detail_tree.column("one", width=200)
            self.poi_detail_tree.column("two", width=200)
            self.poi_detail_tree.column("three", width=200)
            self.poi_detail_tree.heading("one", text="Data Type",
                                         command=lambda c="one": self.sortby(self.poi_detail_tree, c, 0))
            self.poi_detail_tree.heading("two", text="Data Value",
                                         command=lambda c="two": self.sortby(self.poi_detail_tree, c, 0))
            self.poi_detail_tree.heading("three", text="Time & Date of Reading",
                                         command=lambda c="three": self.sortby(self.poi_detail_tree, c, 0))

            vsb = ttk.Scrollbar(orient="vertical", command=self.poi_detail_tree.yview)
            hsb = ttk.Scrollbar(orient="horizontal", command=self.poi_detail_tree.xview)
            self.poi_detail_tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
            self.poi_detail_tree.grid(column=0, row=0, sticky='nsew', in_=tree_frame)
            vsb.grid(column=1, row=0, sticky='ns', in_=tree_frame)
            hsb.grid(column=0, row=1, sticky='ew', in_=tree_frame)

    def flag_poi(self):
        POIname = self.selected_poi
        FlagQuery = "SELECT Flag FROM POI WHERE Name = '%s'"
        cursor.execute(FlagQuery % POIname)
        Flag = int(cursor.fetchall()[0][0])
        message = ""
        ToggleQuery = ""
        if Flag is 0:
            ToggleQuery = "UPDATE POI SET Flag = '1', DateFlagged = '%s' WHERE Name = '%s'"
            cursor.execute(ToggleQuery % (datetime.now().date(), POIname))
            connection.commit()
            message = "POI location '%s' has been flagged." % POIname
        else:
            ToggleQuery = "UPDATE POI SET Flag = '%s', DateFlagged = NULL WHERE Name = '%s'" % ("0", POIname)
            cursor.execute(ToggleQuery)
            connection.commit()
            message = "POI location '%s' has been unflagged." % POIname

        togglebox = Tk()
        togglebox.title("Flagged")
        error_label = Label(togglebox,
                            text=message,
                            font=("Arial", 12), anchor="w", justify="left")
        error_label.grid(row=0, column=0, padx=20, pady=10)
        error_button = Button(togglebox, width=15, height=1, text="Okay", font=("Arial", 15), command=togglebox.destroy)
        error_button.grid(row=1, column=0, padx=10, pady=20)

    def reset_view_poi_detail(self):
        self.view_detail_poi_frame.grid_forget()
        self.view_poi_detail()

    def back_to_filter_search(self):
        self.view_detail_poi_frame.grid_forget()
        self.filter_search_poi()

    def apply_poi_filters(self):
        location = self.poi_location_name_variable.get()
        city = self.poi_city_variable.get()
        state = self.poi_state_variable.get()
        zip_code = self.poi_zip_code_entry.get()
        flagged_yn = self.poi_flagged_yn_var.get()
        day_start = str(self.poi_start_day_entry.get())
        month_start = str(self.poi_start_month_entry.get())
        year_start = str(self.poi_start_year_entry.get())
        day_end = str(self.poi_end_day_entry.get())
        month_end = str(self.poi_end_month_entry.get())
        year_end = str(self.poi_end_year_entry.get())

        stop = False;
        DateFlaggedStart = ""
        if day_start != "" and month_start != "" and year_start != "" and len(day_start) == 2 and len(
                month_start) == 2 and len(year_start) == 4:
            DateFlaggedStart = "%s-%s-%s" % (year_start, month_start, day_start)
        elif day_start == "" and month_start == "" and year_start == "":
            pass
        else:
            failbox = Tk()
            failbox.title("Error")
            error_label = Label(failbox, text="The parameters you have submitted are invalid. Please try again.",
                                font=("Arial", 12), anchor="w", justify="left")
            error_label.grid(row=0, column=0, padx=20, pady=10)
            error_button = Button(failbox, width=15, height=1, text="Okay", font=("Arial", 15), command=failbox.destroy)
            error_button.grid(row=1, column=0, padx=10, pady=20)
            stop = True
        DateFlaggedEnd = ""
        if day_end != "" and month_end != "" and year_end != "" and len(day_end) == 2 and len(month_end) == 2 and len(
                year_end) == 4:
            DateFlaggedEnd = "%s-%s-%s" % (year_end, month_end, day_end)
        elif day_end == "" and month_end == "" and year_end == "":
            pass
        else:
            failbox = Tk()
            failbox.title("Success")
            error_label = Label(failbox, text="The parameters you have submitted are invalid. Please try again.",
                                font=("Arial", 12), anchor="w", justify="left")
            error_label.grid(row=0, column=0, padx=20, pady=10)
            error_button = Button(failbox, width=15, height=1, text="Okay", font=("Arial", 15), command=failbox.destroy)
            error_button.grid(row=1, column=0, padx=10, pady=20)
            stop = True
        if not stop:
            FilterQuery = "SELECT Name, City, State, Zipcode, Flag, DateFlagged FROM POI WHERE "

            if location != "":
                FilterQuery += "Name = '"
                FilterQuery += location
                FilterQuery += "' AND "
            if city != "":
                FilterQuery += "City = '"
                FilterQuery += city
                FilterQuery += "' AND "
            if state != "":
                FilterQuery += "State = '"
                FilterQuery += state
                FilterQuery += "' AND "
            if zip_code != "":
                FilterQuery += "Zipcode = '"
                FilterQuery += zip_code
                FilterQuery += "' AND "
            FilterQuery += "Flag = '"
            FilterQuery += str(flagged_yn)
            FilterQuery += "' AND "
            if DateFlaggedStart != "":
                FilterQuery += "DateFlagged >= '"
                FilterQuery += DateFlaggedStart
                FilterQuery += "' AND "
            if DateFlaggedEnd != "":
                FilterQuery += "DateFlagged <= '"
                FilterQuery += DateFlaggedEnd
                FilterQuery += "' AND "
            FilterQuery = FilterQuery[:-5]
            cursor.execute(FilterQuery)
            filteredPOIs = cursor.fetchall()

            try:
                for record in self.view_poi_tree.get_children():
                    self.view_poi_tree.delete(record)
            except:
                pass

            for record in filteredPOIs:
                self.view_poi_tree.insert("", 0, values=(
                    record[0], record[1], record[2], record[3], str(record[4] == 1), record[5]))

    def apply_poi_detail_filters(self):
        data_type = self.poi_detail_type.get()
        data_value_min = self.poi_detail_data_value_min.get()
        data_value_max = self.poi_detail_data_value_max.get()
        day_start = self.poi_detail_start_day_entry.get()
        month_start = self.poi_detail_start_month_entry.get()
        year_start = self.poi_detail_start_year_entry.get()
        day_end = self.poi_detail_end_day_entry.get()
        month_end = self.poi_detail_end_month_entry.get()
        year_end = self.poi_detail_end_year_entry.get()

        stop = False
        DateFlaggedStart = ""
        if day_start != "" and month_start != "" and year_start != "" and len(day_start) == 2 and len(
                month_start) == 2 and len(year_start) == 4:
            DateFlaggedStart = "%s-%s-%s" % (year_start, month_start, day_start)
        elif day_start == "" and month_start == "" and year_start == "":
            pass
        else:
            failbox = Tk()
            failbox.title("Invalid formatting")
            error_label = Label(failbox, text="The parameters you have submitted are invalid. Please try again.",
                                font=("Arial", 12), anchor="w", justify="left")
            error_label.grid(row=0, column=0, padx=20, pady=10)
            error_button = Button(failbox, width=15, height=1, text="Okay", font=("Arial", 15), command=failbox.destroy)
            error_button.grid(row=1, column=0, padx=10, pady=20)
            stop = True

        DateFlaggedEnd = ""
        if day_end != "" and month_end != "" and year_end != "" and len(day_end) == 2 and len(month_end) == 2 and len(
                year_end) == 4:
            DateFlaggedEnd = "%s-%s-%s" % (year_end, month_end, day_end)
        elif day_end == "" and month_end == "" and year_end == "":
            pass
        else:
            failbox = Tk()
            failbox.title("Invalid formatting")
            error_label = Label(failbox, text="The parameters you have submitted are invalid. Please try again.",
                                font=("Arial", 12), anchor="w", justify="left")
            error_label.grid(row=0, column=0, padx=20, pady=10)
            error_button = Button(failbox, width=15, height=1, text="Okay", font=("Arial", 15), command=failbox.destroy)
            error_button.grid(row=1, column=0, padx=10, pady=20)
            stop = True

        if not stop:
            Type = data_type
            DataValueStart = 0
            DataValueEnd = 0
            if data_value_min is not "":
                DataValueStart = int(data_value_min)
            if data_value_max is not "":
                DataValueEnd = int(data_value_max)
            TimeDateStart = DateFlaggedStart
            TimeDateEnd = DateFlaggedEnd

            DetailFilterQuery = "SELECT Type, DataValue, TimeDate FROM DATAPOINT WHERE "
            DetailFilterQuery += "Name = '%s' AND " % self.selected_poi
            if Type == "Mold":
                DetailFilterQuery += "Type = 'Mold' AND "
            elif Type == "Air Quality":
                DetailFilterQuery += "Type = 'Air Quality' AND "
            if DataValueStart > 0:
                DetailFilterQuery += "DataValue >= '"
                DetailFilterQuery += str(DataValueStart)
                DetailFilterQuery += "' AND "
            if DataValueEnd > 0:
                DetailFilterQuery += "DataValue <= '"
                DetailFilterQuery += str(DataValueEnd)
                DetailFilterQuery += "' AND "
            if TimeDateStart != "":
                DetailFilterQuery += "TimeDate >= '"
                DetailFilterQuery += str(TimeDateStart)
                DetailFilterQuery += "' AND "
            if TimeDateEnd != "":
                DetailFilterQuery += "TimeDate <= '"
                DetailFilterQuery += str(TimeDateEnd)
                DetailFilterQuery += "' AND "
            DetailFilterQuery += "Status = 'Accepted' ORDER BY TimeDate DESC"
            cursor.execute(DetailFilterQuery)
            raw_DPs = cursor.fetchall()
            try:
                for record in self.poi_detail_tree.get_children():
                    self.poi_detail_tree.delete(record)
            except:
                pass
            for dp in raw_DPs:
                self.poi_detail_tree.insert("", 0, values=(dp[0], dp[1], dp[2]))

    def view_pending_data_points(self):
        self.admin_menu_main_frame.grid_forget()
        self.view_pending_data_points_main_frame = Frame(self.rootwin)
        self.view_pending_data_points_main_frame.grid(row=0, column=0)

        pending_data_points_label = Label(self.view_pending_data_points_main_frame, text="Pending Data Points", font=("Arial", 25))
        pending_data_points_label.grid(row=0, column=0)

        adminquery = "SELECT Name, Type, DataValue, TimeDate FROM DATAPOINT WHERE Status = '%s'"
        cursor.execute(adminquery % "Pending")
        PendingDP = cursor.fetchall()

        self.pending_data_points_records = []
        for pending_data_points_record in PendingDP:
            formatted_record = [str(pending_data_points_record[0]), str(pending_data_points_record[1]),
                                str(pending_data_points_record[2]), str(pending_data_points_record[3])]
            self.pending_data_points_records.append(formatted_record)
        self.pending_data_points_records.sort()

        tree_frame = Frame(self.view_pending_data_points_main_frame)
        tree_frame.grid(row=1, column=0, padx=10, pady=10)

        self.pending_data_points_tree = ttk.Treeview(tree_frame)
        self.pending_data_points_tree.grid(row=0, column=0)

        self.pending_data_points_tree["columns"] = ("one", "two", "three", "four")
        self.pending_data_points_tree.column("one", width=200)
        self.pending_data_points_tree.column("two", width=200)
        self.pending_data_points_tree.column("three", width=200)
        self.pending_data_points_tree.column("four", width=200)
        self.pending_data_points_tree.heading("one", text="POI Location",
                                              command=lambda c="one": self.sortby(self.pending_data_points_tree, c, 0))
        self.pending_data_points_tree.heading("two", text="Data Type",
                                              command=lambda c="two": self.sortby(self.pending_data_points_tree, c, 0))
        self.pending_data_points_tree.heading("three", text="Data Value",
                                              command=lambda c="three": self.sortby(self.pending_data_points_tree, c,
                                                                                    0))
        self.pending_data_points_tree.heading("four", text="Time & Date of Data Reading",
                                              command=lambda c="four": self.sortby(self.pending_data_points_tree, c, 0))

        vsb = ttk.Scrollbar(orient="vertical", command=self.pending_data_points_tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal", command=self.pending_data_points_tree.xview)
        self.pending_data_points_tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.pending_data_points_tree.grid(column=0, row=0, sticky='nsew', in_=tree_frame)
        vsb.grid(column=1, row=0, sticky='ns', in_=tree_frame)
        hsb.grid(column=0, row=1, sticky='ew', in_=tree_frame)

        for record in self.pending_data_points_records:
            self.pending_data_points_tree.insert("", 0, values=(record[0], record[1], record[2], record[3]))

        button_frame = Frame(self.view_pending_data_points_main_frame)
        button_frame.grid(row=0, column=0)

        self.POI_location_pending_data_points_order = True
        self.data_type_pending_data_points_order = True
        self.data_value_pending_data_points_order = True
        self.date_time_pending_data_points_order = True

        lower_button_frame = Frame(self.view_pending_data_points_main_frame)
        lower_button_frame.grid(row=2, column=0)

        back_button = Button(lower_button_frame, width=15, height=1, text="Back", font=("Arial", 10),
                             command=self.admin_back_to_main)
        back_button.grid(row=0, column=0)
        accept_button = Button(lower_button_frame, width=15, height=1, text="Accept", font=("Arial", 10),
                               command=self.get_rows_pending_data_points_accept)
        accept_button.grid(row=0, column=1)
        reject_button = Button(lower_button_frame, width=15, height=1, text="Reject", font=("Arial", 10),
                               command=self.get_rows_pending_data_points_reject)
        reject_button.grid(row=0, column=2)

    def view_pending_city_official_account(self):
        self.admin_menu_main_frame.grid_forget()
        self.view_pending_city_official_accounts_main_frame = Frame(self.rootwin)
        self.view_pending_city_official_accounts_main_frame.grid(row=0, column=0)

        pending_city_official_label = Label(self.view_pending_city_official_accounts_main_frame, text="Pending City Official Accounts", font=("Arial", 25))
        pending_city_official_label.grid(row=0, column=0, padx=10, pady=10)

        tree_frame = Frame(self.view_pending_city_official_accounts_main_frame)
        tree_frame.grid(row=1, column=0)

        self.pending_city_official_tree = ttk.Treeview(tree_frame)
        self.pending_city_official_tree.grid(row=0, column=0)

        self.pending_city_official_tree["columns"] = ("one", "two", "three", "four", "five")
        self.pending_city_official_tree.column("one", width=100)
        self.pending_city_official_tree.column("two", width=200)
        self.pending_city_official_tree.column("three", width=100)
        self.pending_city_official_tree.column("four", width=100)
        self.pending_city_official_tree.column("five", width=150)
        self.pending_city_official_tree.heading("one", text="Username")
        self.pending_city_official_tree.heading("two", text="Email")
        self.pending_city_official_tree.heading("three", text="Status")
        self.pending_city_official_tree.heading("three", text="City")
        self.pending_city_official_tree.heading("four", text="State")
        self.pending_city_official_tree.heading("five", text="Title")

        vsb = ttk.Scrollbar(orient="vertical", command=self.pending_city_official_tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal", command=self.pending_city_official_tree.xview)
        self.pending_city_official_tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.pending_city_official_tree.grid(column=0, row=0, sticky='nsew', in_=tree_frame)
        vsb.grid(column=1, row=0, sticky='ns', in_=tree_frame)
        hsb.grid(column=0, row=1, sticky='ew', in_=tree_frame)
        COquery = "SELECT USER.Username, Email, City, State, Title FROM USER, CITYOFFICIAL WHERE USER.Username = CITYOFFICIAL.Username AND Status = '%s'"
        cursor.execute(COquery % 'Pending')
        self.COs = cursor.fetchall()
        self.cos = []
        for item in self.COs:
            aList = [item[0], item[1], item[2], item[3], item[4]]
            self.cos.append(aList)
        self.data = self.cos

        for record in self.data:
            self.pending_city_official_tree.insert("", 0,
                                                   values=(record[0], record[1], record[2], record[3], record[4]))

        button_frame = Frame(self.view_pending_city_official_accounts_main_frame)
        button_frame.grid(row=2, column=0)
        back_button = Button(button_frame, width=20, height=1, text="Back", font=("Arial", 10),
                             command=self.admin_back_to_main)
        back_button.grid(row=0, column=0)
        accept_button = Button(button_frame, width=20, height=1, text="Accept", font=("Arial", 10),
                               command=self.accept_city_official_account)
        accept_button.grid(row=0, column=1)
        reject_button = Button(button_frame, width=20, height=1, text="Reject", font=("Arial", 10),
                               command=self.reject_city_official_account)
        reject_button.grid(row=0, column=2)

    def accept_city_official_account(self):
        selected_records = []
        for record in self.pending_city_official_tree.selection():
            selected_record = self.pending_city_official_tree.item(record, "values")
            selected_records.append(selected_record)

        for item in selected_records:
            Accept = "UPDATE CITYOFFICIAL SET Status='Accepted' WHERE Username = '%s'"
            cursor.execute(Accept % item[0])
            connection.commit()
        for i in self.pending_city_official_tree.get_children():
            self.pending_city_official_tree.delete(i)
        COquery = "SELECT USER.Username, Email, City, State, Title FROM USER, CITYOFFICIAL WHERE USER.Username = CITYOFFICIAL.Username AND Status = '%s'"
        cursor.execute(COquery % 'Pending')
        self.COs = cursor.fetchall()
        self.cos = []
        for item in self.COs:
            aList = [item[0], item[1], item[2], item[3], item[4]]
            self.cos.append(aList)
        self.data = self.cos
        for record in self.data:
            self.pending_city_official_tree.insert("", 0,
                                                   values=(record[0], record[1], record[2], record[3], record[4]))

    def reject_city_official_account(self):
        selected_records = []
        for record in self.pending_city_official_tree.selection():
            selected_record = self.pending_city_official_tree.item(record, "values")
            selected_records.append(selected_record)

        for item in selected_records:
            Reject = "UPDATE CITYOFFICIAL SET Status='Rejected' WHERE Username = '%s'"
            cursor.execute(Reject % item[0])
            connection.commit()
        for i in self.pending_city_official_tree.get_children():
            self.pending_city_official_tree.delete(i)
        COquery = "SELECT USER.Username, Email, City, State, Title FROM USER, CITYOFFICIAL WHERE USER.Username = CITYOFFICIAL.Username AND Status = '%s'"
        cursor.execute(COquery % 'Pending')
        self.COs = cursor.fetchall()
        self.cos = []
        for item in self.COs:
            aList = [item[0], item[1], item[2], item[3], item[4]]
            self.cos.append(aList)
        self.data = self.cos
        for record in self.data:
            self.pending_city_official_tree.insert("", 0,
                                                   values=(record[0], record[1], record[2], record[3], record[4]))

    def admin_back_to_main(self):
        try:
            self.view_pending_city_official_accounts_main_frame.grid_forget()
        except:
            pass
        try:
            self.view_pending_data_points_main_frame.grid_forget()
        except:
            pass
        self.open_main_menu_admin()

    def get_rows_pending_data_points_accept(self):
        selected_records = []
        for record in self.pending_data_points_tree.selection():
            selected_record = self.pending_data_points_tree.item(record, "values")
            selected_records.append(selected_record)

        for i in selected_records:
            name = i[0]
            DT = i[3]
            acceptDPquery = "UPDATE DATAPOINT SET Status = 'Accepted' where TimeDate = '%s' AND Name = '%s'"
            cursor.execute(acceptDPquery % (DT, name))
            connection.commit()
        for i in self.pending_data_points_tree.get_children():
            self.pending_data_points_tree.delete(i)
        DPquery = "SELECT Name, Type, DataValue, TimeDate FROM DATAPOINT WHERE Status = '%s'"
        cursor.execute(DPquery % "Pending")
        self.DPs = cursor.fetchall()
        self.dps = []
        for item in self.DPs:
            aList = [item[0], item[1], item[2], item[3]]
            self.dps.append(aList)
        self.data = self.dps
        for record in self.data:
            self.pending_data_points_tree.insert("", 0, values=(record[0], record[1], record[2], record[3]))

    def get_rows_pending_data_points_reject(self):
        selected_records = []
        for record in self.pending_data_points_tree.selection():
            selected_record = self.pending_data_points_tree.item(record, "values")
            selected_records.append(selected_record)

        for i in selected_records:
            name = i[0]
            DT = i[3]
            rejectDPquery = "UPDATE DATAPOINT SET Status = 'Rejected' where TimeDate = '%s' AND Name = '%s'"
            cursor.execute(rejectDPquery % (DT, name))
            connection.commit()
        for i in self.pending_data_points_tree.get_children():
            self.pending_data_points_tree.delete(i)
        DPquery = "SELECT Name, Type, DataValue, TimeDate FROM DATAPOINT WHERE Status = '%s'"
        cursor.execute(DPquery % "Pending")
        self.DPs = cursor.fetchall()
        self.dps = []
        for item in self.DPs:
            aList = [item[0], item[1], item[2], item[3]]
            self.dps.append(aList)
        self.data = self.dps
        for record in self.data:
            self.pending_data_points_tree.insert("", 0, values=(record[0], record[1], record[2], record[3]))


def main(args):
    rootwin = Tk()
    rootwin.state("zoomed")
    rootwin.title("Main Menu")
    GUI(rootwin)
    rootwin.mainloop()


if __name__ == '__main__':
    main(sys.argv)
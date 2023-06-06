import hashlib
import socket
import ssl
import re
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import main_window
import config

context = ssl.create_default_context()
# Set the context to not verify the server's SSL/TLS certificate
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

class myClient():
    client_socket = None
    the_config_parser = None

    # A function that starts the run and connects to the server with socket
    def run(self):
        self.client_socket = socket.socket()
        self.the_config_parser = config.AppConfig('app_config.ini')
        host = self.the_config_parser.get_string_value('server', 'host')
        port = self.the_config_parser.get_int_value('server', 'port')

        # host = '127.0.0.1'
        # port = 8080
        print('Waiting for connection response')
        try:
            self.client_socket.connect((host, port))
            self.client_socket = context.wrap_socket(self.client_socket, server_hostname=host)
        except socket.error as e:
            print(str(e))

        self.run_app()

    # A function that starts the run of the GUI
    def run_app(self):
        app = QtWidgets.QApplication(sys.argv)
        Window = QtWidgets.QMainWindow()
        ui = main_window.Ui_MainWindow()
        ui.setupUi(Window, self, self.the_config_parser)
        Window.show()
        sys.exit(app.exec_())

    # A function that receives username and password, organizes it into a login msg and sends it to the server.
    # The function returns if the login was successful
    def login(self, username, password):
        password = hashlib.md5(password.encode()).hexdigest()
        message = 'LOGIN\r\n' + username + '\r\n' + password

        if self.the_config_parser.is_using_debug_values():
            message = 'LOGIN\r\n' + self.the_config_parser.get_user_name() + '\r\n' + self.the_config_parser.get_password()

        self.client_socket.send(message.encode())
        res = self.client_socket.recv(1024).decode()
        return self.handle_res(res, "LOGIN")

    # A function that receives a name, email, username, and password, organizes it into a sign up msg and sends it to the server.
    # The function returns if the sign up was successful
    def sign_up(self, full_name, email, username, password):
        password = hashlib.md5(password.encode()).hexdigest()
        message = 'SIGN_UP\r\n' + full_name + '\r\n' + email + '\r\n' + username + '\r\n' + password
        self.client_socket.send(message.encode())
        res = self.client_socket.recv(1024).decode()
        return self.handle_res(res, "SIGN_UP")

    # A function that receives a full_name, patient_id, email, gender, birth_date, case_description, visit_date,  x_ray_detection, doctor_id, organizes it into a add_patient msg and sending it to the server.
    # The function returns the details of the requested patient as a list
    def add_patient(self, full_name, ID, email, gender, birth_date, case_description, visit_date, chance,doctor_id):
        message = 'ADD_PATIENT\r\n' + full_name + '\r\n' + ID + '\r\n' + email + '\r\n' + gender + '\r\n' + birth_date + '\r\n' + case_description + '\r\n' + visit_date + '\r\n' + doctor_id
        if chance != '':
            message = message + '\r\n' + chance
        self.client_socket.send(message.encode())
        res = self.client_socket.recv(1024)
        splitted_res = res.decode().splitlines()
        return splitted_res[1]

    # A function that receives a patient_id, organizes it into a get_specific_patient msg and sending it to the server.
    # The function returns the details of the requested patient as a list
    def get_specific_patient(self, patient_id):
        message = 'GET_SPECIFIC_PATIENT\r\n' + patient_id
        self.client_socket.send(message.encode())
        res = self.client_socket.recv(1024)
        res = res.decode()
        return self.handle_res(res, "GET_SPECIFIC_PATIENT")

    # A function that receives a doctor_id, organizes it into a get_patients_list msg and sends it to the server.
    # The function returns all the patients of the requested doctor as lists
    def get_patients_list(self, doctor_id):
        message = 'GET_PATIENT_LIST\r\n' + doctor_id
        self.client_socket.send(message.encode())
        res = ''
        while True:
            data = self.client_socket.recv(1024)
            data = data.decode()
            res += data
            if len(data) < 1024:
                break
        splitted_res = res.splitlines()
        if len(splitted_res) == 0:
            return None
        if splitted_res[0] == "GET_PATIENT_LIST_ans" and splitted_res[1] == "True":
            return splitted_res[2:]
        else:
            return None

    # A function that receives a msg and command. The function checks if the message matches the protocol structure
    # If it does, and the server returns True, the function returns the data of the msg
    def handle_res(self, res, command):
        splitted_res = res.splitlines()
        if len(splitted_res) == 0:
            return None

        if splitted_res[0] == command + "_ans" and splitted_res[1] == "True":
            return splitted_res[2]
        else:
            return None

    # A function that receives an email and checks if it is valid
    def check_email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        # pass the regular expression
        # and the string into the fullmatch() method
        if (re.fullmatch(regex, email)):
            return True
        else:
            return False

if __name__ == '__main__':
    the_client = myClient()
    the_client.run()

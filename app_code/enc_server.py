import ssl
import threading as th
import socket
import db
import config

certfile = r"localhost.pem"
cafile = r"cacert.pem"
purpose = ssl.Purpose.CLIENT_AUTH
context = ssl.create_default_context(purpose, cafile=cafile)
context.load_cert_chain(certfile)

#A function that receives a msg of login and returns the details of the user
def handle_login_msg(msg):
    username = msg[0]
    password = msg[1]
    return username, password

#A function that receives a msg of sign_up and returns the details of the user
def handle_sign_up_msg(msg):
    full_name = msg[0]
    email = msg[1]
    username = msg[2]
    password = msg[3]
    return full_name, email, username, password

#A function that receives a msg of add_patient and returns the details of the patient
def handle_add_patient_msg(msg):
    full_name = msg[0]
    patient_id = msg[1]
    email = msg[2]
    gender = msg[3]
    birth_date = msg[4]
    case_description = msg[5]
    visit_date = msg[6]
    doctor_id = msg[7]
    if len(msg) < 9:
        return full_name, patient_id, email, gender, birth_date, case_description, visit_date, doctor_id, None
    else:
        pneu_chance = msg[8]
        return full_name, patient_id, email, gender, birth_date, case_description, visit_date, doctor_id, pneu_chance

#A function that receives the client_socket and the client_address. The fumction handles the client request and send him back a response
def handle_client(client_socket, client_address):
    print(f'[*] Connection from {client_address}')
    while True:
        try:
            data = client_socket.recv(1024)
            data = data.decode()
            print(f'[*] Received message from {client_address}: {data}')
            split_data = data.splitlines()
            bret = 0
            #handle with login requests
            if split_data[0] == 'LOGIN':
                username, password = handle_login_msg(split_data[1:])
                bret, doctor_id = db.find_username_and_password(username, password)
                if bret:
                    res = str(bret) + "\r\n" + doctor_id
                else:
                    res = str(bret)

            #handle with sign up requests
            if split_data[0] == 'SIGN_UP':
                full_name, email, username, password = handle_sign_up_msg(split_data[1:])
                bret, doctor_id = db.add_user(full_name, email, username, password)
                if bret:
                    res = str(bret) + "\r\n" + doctor_id
                else:
                    res = str(bret)

            if split_data[0] == 'ADD_PATIENT':
                full_name, patient_id, email, gender, birth_date, case_description, visit_date, doctor_id, pneu_chance = handle_add_patient_msg(split_data[1:])
                if pneu_chance is None:
                    bret = db.add_patient(full_name, patient_id, email, gender, birth_date, case_description, visit_date, doctor_id)
                else:
                    bret = db.add_patient_with_photo(full_name, patient_id, email, gender, birth_date, case_description, visit_date, doctor_id, pneu_chance)
                if bret:
                    res = str(bret) + "\r\n" + username
                else:
                    res = str(bret)

            if split_data[0] == 'GET_SPECIFIC_PATIENT':
                bret, patient = db.get_specific_patient(split_data[1])
                res = str(bret) + "\r\n" + patient

            if split_data[0] == 'GET_PATIENT_LIST':
                bret, patient_list = db.get_patients_list(split_data[1])
                if patient_list is None:
                    res = str(bret) + "\r\n" + "None"
                else:
                    res = str(bret) + "\r\n" + patient_list

            print(bret)
            # Send encrypted message to client
            response = split_data[0] +"_ans\r\n" + res
            response = response.encode()
            client_socket.sendall(response)
        except Exception as e:
            None
            client_socket.close()

# A function that start the run and connects the server with its clients using socket
def run():
    theAppConfig = config.AppConfig('app_config.ini')
    host = theAppConfig.get_string_value('server', 'host')
    port = theAppConfig.get_int_value('server', 'port')
    ThreadCount = 0

    ServerSideSocket = socket.socket()

    try:
        ServerSideSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    ServerSideSocket = context.wrap_socket(ServerSideSocket, server_side=True)
    print('Socket is listening..')
    ServerSideSocket.listen(1)
    b = th.Thread(target=db.build_DB())
    b.start()
    while True:
        client_socket, client_address = ServerSideSocket.accept()
        print(f'[*] Accepted connection from {client_address}')
        a = th.Thread(target=handle_client, args=(client_socket, client_address,))
        a.start()
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
    ServerSideSocket.close()

if __name__ == '__main__':
    run()
import socket

def handle_client(client_socket):
    # 파일명 수신
    file_name = client_socket.recv(1024).decode()
    print('Received File Name :', file_name)

    try:
        # 파일 열기
        with open(file_name, 'r') as file:
            # 파일 내용 읽기
            file_contents = file.read()

        # 파일 내용 전송
        client_socket.send(file_contents.encode())
        print('Transfer Success')
    # 파일이 존재하지 않는 경우, 새로 생성
    except FileNotFoundError:
        error_message = 'The file does NOT exist. New File Created.'
        client_socket.send(error_message.encode())
        print('Error Message Send :', error_message)

        # 새로운 파일 생성
        with open(file_name, 'w') as file:
            file.write('New File')

        print('New File Created')
    # 에러 발생할 경우, 에러 처리
    except Exception as e:
        error_message = 'Error Occurred'
        client_socket.send(error_message.encode())
        print('Error Message Send', error_message)
        print('Error Message', str(e))

    client_socket.close()

def main():
    host = '127.0.0.1'  # 서버 주소
    port = 1127  # 포트 번호

    # 소켓 생성
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 서버 소켓을 주소에 바인딩
    server_socket.bind((host, port))

    # 클라이언트의 연결 요청 대기
    server_socket.listen(1)
    print('Server Started')

    while True:
        # 클라이언트와 연결 수락
        client_socket, addr = server_socket.accept()
        print('Client Connected')
        print('Client Addr :', addr)

        # 클라이언트 요청 처리
        handle_client(client_socket)

if __name__ == '__main__':
    main()

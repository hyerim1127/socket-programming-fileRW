import socket

def main():
    host = '127.0.0.1'  # 서버 주소
    port = 1127  # 포트 번호

    # 소켓 생성
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 서버에 연결
    client_socket.connect((host, port))
    print('Server Connected')

    # 파일명 입력
    file_name = input('File name : ')

    # 파일명 전송
    client_socket.send(file_name.encode())

    # 서버로부터 응답 수신
    response = client_socket.recv(1024).decode()

    if response.startswith('The file does NOT exist!!'):
        print(response)
    elif response.startswith('Error Occurred'):
        print(response)
    else:
        print('File Content :')
        print(response)

    # 클라이언트 소켓 종료
    client_socket.close()

if __name__ == '__main__':
    main()
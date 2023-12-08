import threading

class ServerObject:
    def __init__(self, socket, name, addr, connectState=None, p=None, g=None, a=None, sPubKey=None, cPubKey=None, key=None):
        self.socket = socket
        self.peer_name = name
        self.addr = addr
        self.connectState = connectState
        self.p = p
        self.g = g
        self.a = a  # 服务器端的私钥a
        self.sPubKey = sPubKey
        self.cPubKey = cPubKey
        self.key = key
        self.running = False
        self.thread = None

    def start_receive(self, message_handler):
        self.running = True
        self.thread = threading.Thread(target=self.receive_messages, args=())
        self.thread.start()

    def stop_receive(self):
        self.running = False
        if self.thread is not None:
            self.thread.join()
        self.close_socket()

    def close_socket(self):
        try:
            self.socket.close()
        except Exception as e:
            print(f"Error closing socket: {e}")
            
    def receive_messages(self):
        while self.running:
            try:
                data = self.socket.recv(1024)
                if not data:
                    break
                print(f"Received message: {data.decode()}")
            except Exception as e:
                print(f"Error receiving message: {e}")
                break
        self.close_socket()
    def sendMessage(self,message):
        try:
            # 发送数据
            self.socket.sendall(message)
        except Exception as e:
            print(f"Error receiving message: {e}")

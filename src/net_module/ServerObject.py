class ServerObject(object):
    def __init__(self,socket,name,addr,connectState=None,p=None,g=None,a=None,pubKey=None,key=None):
        self.socket = socket
        self.peer_name = name
        self.addr = addr
        self.connectState = connectState
        self.p = p
        self.g = g
        self.a = a #这是客户端的a，私钥，这个用于保存跟每个客户端通信的不同a值
        self.pubKey = pubKey
        self.key = key

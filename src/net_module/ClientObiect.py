
class ClientObject(object):
    def __init__(self,socket,name,addr,p=None,g=None,a=None,pubKey=None):
        self.socket = socket
        self.peer_name = name
        self.addr = addr
        self.p = p
        self.g = g
        self.a = a
        self.pubKey = pubKey

    
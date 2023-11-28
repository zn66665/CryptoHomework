class ServerObject(object):
    def __init__(self,socket,name,p=None,g=None,a=None,pubKey=None):
        self.socket = socket
        self.peer_name = name
        self.p = p
        self.g = g
        self.a = a
        self.pubKey = pubKey

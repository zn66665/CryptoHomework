import json

class MessageObject:
    def __init__(self, message_type, p=None, g=None, pubKey=None, encryption_method=None, data=None):
        self.message_type = message_type
        self.p = p
        self.g = g
        self.pubKey = pubKey
        self.encryption_method = encryption_method
        self.data = data

    def to_dict(self):
        return {
            'message_type': self.message_type.value,
            'p': self.p,
            'g': self.g,
            'pubKey': self.pubKey,
            'encryption_method': self.encryption_method.value if self.encryption_method else None,
            'data': self.data
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    @staticmethod
    def from_dict(data):
        return MessageObject(
            data['message_type'],
            p=data.get('p'),
            g=data.get('g'),
            pubKey=data.get('pubKey'),
            encryption_method=data.get('encryption_method'),
            data=data.get('data')
        )

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        return MessageObject.from_dict(data)

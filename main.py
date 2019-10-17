#Autoras
#Jessica Antunes - 619612
#Leticia Amaral da Cunha - 628190

import json
#Este metodo compacta a mensagem
def pack(data: dict):
    message_json = json.dumps(data)
    message = message_json

    return message.encode('utf-8')

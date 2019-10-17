import json
# este metodo compacta a mensagem
def pack(data: dict):
    message_json = json.dumps(data)
    message = message_json

    return message.encode('utf-8')


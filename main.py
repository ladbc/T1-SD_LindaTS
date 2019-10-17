import json
#Este metodo compacta a mensagem
def pack(data: dict):
    message_json = json.dumps(data)
    message = message_json

    return message.encode('utf-8')


#Este metodo descompacta a mensagem em um dicionario
def unpack(data: str):
    message_struct = {
        'operacao': "",
        'cliente': "",
        'topico': "",
        'menssagem': ""
    }
    try:
        message_struct = json.loads(data)
    except Exception as erro_msg:
        print("Deu erro ao decompactar?: ", erro_msg)

    return message_struct
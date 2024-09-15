import crcmod
import qrcode

class Payload():
        
    def __init__(self, nome: str, chave_pix: str, valor: str, cidade: str, id_transacao: str) -> None:
        # Atribuindo os argumentos
        self.nome = f'59{len(nome):02}{nome}'
        self.chave_pix = f'01{len(chave_pix):02}{chave_pix}'
        self.valor = f'54{len(valor):02}{valor}'
        self.cidade = f'60{len(cidade):02}{cidade}'
        self.id_transacao = f'05{len(id_transacao):02}{id_transacao}'
        
        # Definindo as constantes
        self.GUI = '0014BR.GOV.BCB.PIX'
        self.PAYLOAD_FORMAT_INDICATOR = '000201'
        self.MERCHANT_ACCOUNT_INFORMATION = f'26{len(self.GUI) + len(self.chave_pix):02}{self.GUI}{self.chave_pix}'    
        self.MERCHANT_CATEGORY_CODE = '52040000'
        self.TRANSACTION_CURRENCY = '5303986'
        self.COUNTRY_CODE = '5802BR'
        self.ADITIONAL_DATA_FIELD_TEMPLATE = f'62{len(self.id_transacao):02}{self.id_transacao}'
        self.INITIAL_PAYLOAD = f'{self.PAYLOAD_FORMAT_INDICATOR}{self.MERCHANT_ACCOUNT_INFORMATION}{self.MERCHANT_CATEGORY_CODE}{self.TRANSACTION_CURRENCY}{self.valor}{self.COUNTRY_CODE}{self.nome}{self.cidade}{self.ADITIONAL_DATA_FIELD_TEMPLATE}'
        self.CRC16 = f'6304{gerar_crc16(f'{self.INITIAL_PAYLOAD}6304')}'

    def __str__(self) -> str:
        return f'{self.INITIAL_PAYLOAD}{self.CRC16}'
    
    def salvar_qrcode(self) -> None:
        self.qrcode = qrcode.make(str(payload))
        self.qrcode.save('qrcode.png')

def gerar_crc16(payload_without_crc16: str) -> str:
    crc16 = crcmod.mkCrcFun(poly=0x11021, initCrc=0xFFFF, rev=False, xorOut=0x0000)
    return hex(crc16(payload_without_crc16.encode())).upper()[2:].zfill(4)
        
if __name__ == '__main__':
    payload = Payload('Julio Antunes Estrela', '3391818d-78c4-48b7-94ad-56badd14370e', '2.00', 'SAO PAULO', '***')
    print(str(payload))
    payload.salvar_qrcode()
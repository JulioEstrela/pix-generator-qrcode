# Gerador de QR Code PIX

Projeto realizado seguindo o [Manual BR Code](https://www.bcb.gov.br/content/estabilidadefinanceira/spb_docs/ManualBRCode.pdf) disponibilizado pelo [Banco Central do Brasil](https://www.bcb.gov.br/)

# Funcionalidade
A aplicação Python gera um QR Code com as informações fornecidas:
- nome do recebedor
- chave pix
- valor em reais
- cidade do recebedor
- id da transação

Essas informações podem ser alteradas na criação do objeto PayLoad  
Importante! As informações acima têm um limite máximo de caracteres, seguindo a documentação do [Manual BR Code](https://www.bcb.gov.br/content/estabilidadefinanceira/spb_docs/ManualBRCode.pdf)

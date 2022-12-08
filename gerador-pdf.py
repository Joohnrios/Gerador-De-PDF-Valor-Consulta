# Guardando as informações do usuário em variáveis

projeto = input('Digite a descrição do projeto: ')

while True:
    horas_estimadas = input('Digite o total de horas estimadas (Apenas números, por favor): ')
    if not horas_estimadas.isnumeric():
        print("Digite apenas números!")
        continue
    else:
        break

while True:
    valor_hora = input('Digite o valor da hora trabalhada (Apenas números, por favor): ')
    if not valor_hora.isnumeric():
        print("Digite apenas números!")
        continue
    else:
        break

prazo = input('Digite o prazo estimado (meses): ')

# Realizando os calculos

valor_total = int(horas_estimadas) * int(valor_hora)

# Gerando o PDF

from fpdf import FPDF

pdf = FPDF() # Com essa linha, já cria o pdf na memória.

pdf.add_page() # Adiciona uma página
pdf.set_font('Arial') # Adicionando a fonte

pdf.image('template.png', x=0, y=0)
pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total))

pdf.output('Orçamento.pdf') # Nome do pdf gerado
print('Orçamento gerado com sucesso!')
import matplotlib.pyplot as plt
import qrcode

def cadastrar_evento(usuario, eventos):
    print('CADASTRO DE EVENTO')
    titulo = input('Digite o titulo do evento: ')
    descricao = input('Digite a descricao do evento: ')
    valor = float(input('Digite o preco do evento: '))
    data = input('Digite a data do evento (dd/mm/aaaa): ')

    eventos[titulo] = [titulo,descricao,valor,data, usuario[0], [],0,[]]
    print('Evento cadastrado com sucesso.')

def buscar_evento(eventos):
    print('BUSCAR EVENTO')
    titulo = input('Digite o titulo do evento a ser buscado: ')
    for chave in eventos:
        if chave == titulo:
            print(f'{eventos[chave][0]}, {eventos[chave][1]}, {eventos[chave][2]}, {eventos[chave][3]}')

def listar_evento(eventos):
    print('LISTAR EVENTOS')
    for chave in eventos:
        print(f'{eventos[chave][0]}, {eventos[chave][1]}, {eventos[chave][2]}, {eventos[chave][3]}')
        print(eventos[chave][4])

def remover_evento(usuario, eventos):
    print('REMOVER EVENTO')
    titulo = input('Digite o titulo do evento a ser removido:')
    remover = []
    for chave in eventos:
        if eventos[chave][4] == usuario[0] and eventos[chave][0] == titulo:
                remover.append(chave)
                print('Evento removido com sucesso.')
        else:
            print('Voce não tem permissão para remover esse evento.')
            break
    for chave in remover:
        eventos.pop(chave)
    print(eventos)

def participar_evento(usuario, eventos):

    print('PARTICIPAR EVENTO')
    print('Eventos disponiveis: ')
    titulo = input('Digite o titulo do evento que deseja participar: ')
    adicionar = []
    for chave in eventos:
        if eventos[chave][0] == titulo:
            if usuario[0] in eventos[chave][5]:
                print('Usuário já cadastrado no evento.')
                break
            adicionar.append(usuario[0])
            eventos[chave][5] = adicionar + eventos[chave][5]
            eventos[chave][6] += eventos[chave][2]

            print(f'Participantes {adicionar} adicionados com sucesso ao evento: {titulo}.')
            break
        print('Evento não encontrado ou incorreto. Tente novamente.')


def cancelar_inscricao(usuario, eventos):
    print('CANCELAR INSCRIÇÃO')
    titulo = input('Digite o título para cancelar a inscrição do evento:')
    cancelar = []
    for chave in eventos:
        if eventos[chave][0] == titulo:
            if usuario[0] in eventos[chave][4]:
                conf = input('Deseja cancelar sua inscrição? (s/n): ')
                if conf == 's':
                    cancelar.append(eventos[chave][4][0])
                    cancelar.pop()
                    eventos[chave][5] = cancelar + eventos[chave][5]
                    eventos[chave][6] -= eventos[chave][2]
                    print(cancelar)
                    print('Participante cancelado com sucesso.')
            else:
                print('Você não tem permissão para cancelar inscrição.')


def listar_participantes(usuario, eventos):
    print('LISTAR PARTICIPANTES')
    titulo = input('Digite o titulo do evento:')
    for chave in eventos:
        if eventos[chave][0] == titulo:
            if usuario[0] in eventos[chave][4]:
                participantes = eventos[chave][5]
                print(participantes)
                file = open('participantesEvento.txt', 'a')
                file.write(f'titulo: {titulo}, participantes: {participantes}')
                file.close()
            else:
                print('Voce nao possui permissão para listar os participantes desse evento!')

def valor_arrecadado(usuario, eventos):
    print('VALOR ARRECADADO')
    titulo = input('Digite o titulo do evento: ')

    if titulo in eventos:
        for chave in eventos:
            if usuario[0] in [eventos[chave][4]]:
                valor_total = eventos[chave][6]
                print(f'O valor arrecadado deste evento é de R${valor_total}  ')
            else:
                print('Usuario não tem permissão. Tente novamente.')
    else:
        print('Evento não encontrado.')


def fazer_feedback(usuario, eventos):
    titulo = input('Digite o evento que deseja fazer o feedback: ')
    for chave in eventos:
        if eventos[chave][0] == titulo:
            if usuario[0] in eventos[chave][4]:
                feed = input('Digite seu feedback: ')
                eventos[chave][7].append(feed)
                print('Feedback registrado com sucesso.')
            else:
                print('Você não está inscrito neste evento.')
        else:
            print('Evento ão encontrado')

def ver_feedback(eventos):
    titulo = input('Digite o titulo para ver o feedback: ')
    for chave in eventos:
        if eventos[chave][0] == titulo:
            print('Feedbacks:')
            for feedback in eventos[chave][7]:
                print(feedback)

def adicionar_participante(usuario, eventos):
    titulo = input('Digite o titulo do evento para adicionar um participante: ')
    participant = []
    for chave in eventos:
        if eventos[chave][0] == titulo:
            if usuario[0] in eventos[chave][4]:
                participante = input('Digite o nome do participante que dejesa adicionaer: ')
                if participante in eventos[chave]:
                    print('já existe um participante con esse nome')

                else:
                    participant.append(participante)
                    eventos[chave][5] = participant + eventos[chave][5]
                    print('Participante adicionado com sucesso.')
            else:
                print('Voce não tem permissao para adicionar participantes a esse evento')
        else:
            print('Evento não encontrado ou incorreto.')

def grafico_participantes(eventos):
    titulos = []
    participantes = []
    for chave in eventos:
        titulos.append(eventos[chave][0])
        participantes.append(len(eventos[chave][5]))

    plt.bar(titulos, participantes, color='red')
    plt.xlabel('Título do Evento')
    plt.ylabel('Número de Participantes')
    plt.title('Número de Participantes por Evento')
    plt.show()

def qr_code(usuarios):
    nome= input('Digite o Email que voce utilizou no cadastro: ')
    for chave in usuarios:
        if usuarios[chave][0] == nome:
            git = qrcode.make("https://github.com/rai070107/projeto3unidade.git")
            git.save("Qrcode git.jpg")
            print('Visite o nosso git e veja como os codigos da plataforma fuciona')
            break
        else:
            print('nome não encontrado')
from cadastro import *
from eventos import *

def menuprincipal():
    print(f'\n -----MENU PRINCIPAL-------'
          f'\n 1 - Cadastro usuário'
          f'\n 2 - Login usuário'
          f'\n 3 - Sair do programa'
          f'\n --------------------------')
    op = input('Digite a opção: ')
    return op


while True:
    op = menuprincipal()
    if op == '1':
        cadastro_us(usuarios)
    elif op == '2':
        usuario_logado = login(usuarios)
        if usuario_logado:
            op = -1
            while op != '0':
                print(f'\n ---------------SUBMENU-------------------'
                      f'\n 1 - Cadastrar evento'
                      f'\n 2 - Buscar evento'
                      f'\n 3 - Listar evento'
                      f'\n 4 - Remover evento'
                      f'\n 5 - Fazer inscrição'
                      f'\n 6 - Cancelar inscrição'
                      f'\n 7 - Listar participantes'
                      f'\n 8 - Valor arrecadado do evento'
                      f'\n 9 - Fazer feedback'
                      f'\n 10 - Mostrar feedback'
                      f'\n 11 - Adicionar participante'
                      f'\n 12 - Grafico de participantes'
                      f'\n 13 - Adicionar email a lista de proibidos'
                      f'\n 14 - Remover email da lista de proibidos'
                      f'\n 15 - listar emails proibidos'
                      f'\n 16 _ Qr code do codigo no git'
                      f'\n 0 - Sair do Submenu'
                      f'\n -----------------------------------------')
                op = input('Digite a opção: ')
                if op == '1':
                    cadastrar_evento(usuario_logado, eventos)
                elif op == '2':
                    buscar_evento(eventos)
                elif op == '3':
                    listar_evento(eventos)
                elif op == '4':
                    remover_evento(usuario_logado, eventos)
                elif op == '5':
                    participar_evento(usuario_logado, eventos)
                elif op == '6':
                    cancelar_inscricao(usuario_logado, eventos)
                elif op == '7':
                    listar_participantes(usuario_logado, eventos)
                elif op == '8':
                    valor_arrecadado(usuario_logado, eventos)
                elif op == '9':
                    fazer_feedback(usuario_logado, eventos)
                elif op == '10':
                    ver_feedback(eventos)
                elif op == '11':
                    adicionar_participante(usuario_logado, eventos)
                elif op == '12':
                    grafico_participantes(eventos)
                elif op == '13':
                    emais_proibidas(usuario_logado, eventos)
                elif op == '14':
                    remover_email_proibido(usuario_logado,eventos)
                elif op == '15':
                    listar_proibidos(usuario_logado, eventos)
                elif op == '16':
                    qr_code(usuarios)
                elif op == '0':
                    print('Voltando ao menu principal')
                else:
                    print('Opção inválida. Tente novamente.')
        else:
            print('Login ou usuários inválidos. Tente novamente.')
    elif op == '3':
        print('Saindo do programa.')
        break
    else:
        print('Opção inválida. Tente novamente.')
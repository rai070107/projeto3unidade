usuarios = {'rooz@': ['rooz', '123'], 'rai@': ['rai', '123']}
eventos = {}
proibidos = ['fe@']

def cadastro_us(usuarios):
    print('CADASTRO')
    nome = input('Digite o nome: ')
    email = input('Digite o email: ')
    for chave in usuarios:
        if chave == email:
            print('email ja cadastrado')
            return email
    for proibido in proibidos:
        if proibido == email:
            print('Email bloqeado na plataforma')
            return email

    idade = int(input('Digite sua idade: '))
    if idade < 18:
        print('Voce não idade suficiente para acessar esse site ')
        return idade

    senha = input('Digite a senha: ')
    r_senha = input('Repita a senha: ')
    if (senha != r_senha):
        print('senhas não coincidem. Tente novamente.')
        return senha

    usuarios[email] = [nome,senha]
    print('cadastro efetuado com sucesso.')
    print('\n')

def login(usuarios):
    print('LOGIN')
    email = input('Digite o email: ')
    senha = input('Digite a senha: ')

    if email in usuarios:
        if usuarios[email][1] == senha:
            print('Login efetuado com sucesso.')
            return usuarios[email]
        else:
            print('Senha incorreta.')
    else:
        print('Email não encontrado.')
    return email

def emais_proibidas(usuario, eventos):
    print('ADICIONAR EMAIL PROIBIDO')
    titulo = input('Qual evento voce deseja proibir a entrada de Email? ')
    for chave in eventos:
        if eventos[chave][0] == titulo:
            if usuario[0] in eventos[chave][4]:
                email = input('Digite o email proibido: ')
                proibidos.append(email)
                print('Email adicionado a lista de proibidos')
            else:
                print('Voce não tem permissao para adicicionar email a lista de proibidos!')
        else:
            print('Evento não encontrado')

def remover_email_proibido(usuario,eventos):
    titulo = input('Qual evento voce deseja remover a proibissao de Email? ')
    for chave in eventos:
        if eventos[chave][0] == titulo:
            if usuario[0] in eventos[chave][4]:
                email = input('Digite o email proibido: ')
                indice = proibidos.index(email)
                proibidos.pop(indice)
                print('Email removido da lista de proibidos')
            else:
                print('Voce nao tem permissao para remover email da lista de proibidos')
        else:
            print('Evento não encontrado')

def listar_proibidos(usuario,eventos):
    print('EMAILS PROIBIDOS')
    titulo = input('Digite o nome do evento para ver lista de emails proibidos')
    for chave in eventos:
        if eventos[chave][0] == titulo:
            if usuario[0] in eventos[chave][4]:
                print(proibidos)
            else:
                print('Voce não tem permissao para acessar essa lista')
        else:
            print('Evento não encontrado')

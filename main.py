#Variavel Global
idGlobal = 0

#Lista Vazia
list_colaboradores = []


#Função Cadastrar
def cadastrar_colaborador(id):
  print('Bem vindo ao Menu cadastrar colaborador')
  print('Digite os dados do colaborador:')
  nome = input('Digite o nome do colaborador')
  setor = input('Digite o setor do colaborador')
  salario = input('Digite o salário do colaborador')
  dicionario_produto = {'nome': nome, 'setor': setor, 'salario': salario}
  #Dicionário que acomoda as váriaveis da função
  list_colaboradores.append(dicionario_produto.copy())
  #Anexo (append) na lista (Global) de colaboradres


#Função Consultar
def consultar_colaborador(id):
  print('Bem vindo ao Menu consultar colaborador')
  while True:
    opcao_consultar = input('\n1) Consultar Todos' +
                            '\n2) Consultar colaborador por NOME' +
                            '\n3) consultar  colaborador por setor' +
                            '\n4) Retornar ao menu anterior' + '\n>>')

    if opcao_consultar == '1':
      print('Você escolheu a opção TODOS')
      for colaboradores in list_colaboradores:
        for key, value in colaboradores.items(
        ):  #Varrer todos os vaolores do dicionário
          print('{} : {}'.format(key, value))
    elif opcao_consultar == '2':
      print('Você escolheu a opção NOME')
      nome_desejado = input('Digite o nome do funcionário: >> ')
      for colaboradores in list_colaboradores:
        if colaboradores['nome'] == nome_desejado:
          for key, value in colaboradores.items():
            print('{} : {}'.format(key, value))

    elif opcao_consultar == '3':
      print('Você escolheu a opção SETOR')
      setor_desejado = input('Digite o nome do funcionário: >> ')
      for colaboradores in list_colaboradores:
        if colaboradores['setor'] == setor_desejado:
          for key, value in colaboradores.items():
            print('{} : {}'.format(
              key, value))  #vai varrer o campo especifico no dicionario

    elif opcao_consultar == '4':
      return  #sai da função consultar e volta p/ main

    else:
      print('Opção Inválida, Tente Novamente')
      continue  #Volta para o inicio do laço


#Função Cadastrar
def Remover_colaborador(id):
  print('Bem vindo ao Menu remover colaborador')
  remover_colaborador = input('Digite o nome do funcionário: >> ')
  for colaboradores in list_colaboradores:
    if colaboradores['nome'] == remover_colaborador:
      list_colaboradores.remove(colaboradores)
      
#Inicio Main
print(
  '------------Bem vindo ao Software de controle da Bruna Santos---------------'
)
contador = 0
while True:
  opcao_menu = input('\n1) Cadastrar colaborador' +
                     '\n2) Consultar colaborador' +
                     '\n3) Remover colaborador' + '\n4) Encerrar programa' +
                     '\n>>')
  if opcao_menu == '1':
    contador == contador + 1
    cadastrar_colaborador(id)
  elif opcao_menu == '2':
    consultar_colaborador(id)
  elif opcao_menu == '3':
    Remover_colaborador(id)
  elif opcao_menu == '4':
    break  #Encerra o laço
  else:
    print('Opção Inválida, Tente Novamente')
    continue  #Volta para o inicio do laço
  #Fim Main
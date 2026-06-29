# PROJETO: SISTEMA DE CONTROLE DE FINANCIAMENTO IMOBILIÁRIO
# ENUNCIADO:
# Desenvolva um sistema em Python para auxiliar no controle de um financiamento imobiliário.
# O sistema deve permitir registrar o valor total do financiamento, a entrada paga, as parcelas quitadas e acompanhar a evolução da dívida ao longo do tempo.


# DESCRIÇÃO:

# O sistema deverá armazenar informações relacionadas ao financiamento e fornecer
# funcionalidades para consulta e atualização dos dados.

# O objetivo é permitir que o usuário acompanhe quanto já foi pago, quanto ainda

# falta pagar e mantenha um histórico organizado dos pagamentos realizados.


# Funcionalidades previstas para a versão 1.0:


# - Cadastrar o valor total do financiamento.
# - Registrar o valor da entrada.
# - Registrar a data da entrada.
# - Registrar a forma de pagamento da entrada.
# - Registrar parcelas pagas.
# - Registrar o valor de cada parcela.
# - Registrar a data de pagamento de cada parcela.
# - Registrar a forma de pagamento de cada parcela.
# - Calcular automaticamente o valor total já quitado.
# - Calcular automaticamente o saldo devedor.
# - Exibir um resumo geral do financiamento.
# - Exibir um histórico dos pagamentos realizados.


# Funcionalidades planejadas para versões futuras:


# - Associar comprovantes PDF aos pagamentos.
# - Salvar os dados em arquivo JSON.
# - Carregar dados automaticamente ao iniciar o sistema.
# - Gerar relatórios financeiros.
# - Utilizar banco de dados para armazenamento permanente.


# CONCEITOS QUE SERÃO PRATICADOS:


# - Programação Orientada a Objetos (POO)
# - Classes e Objetos
# - Métodos
# - Encapsulamento
# - Estruturas condicionais
# - Estruturas de repetição
# - Tratamento de exceções
# - Manipulação de datas
# - Manipulação de arquivos
# - Organização de projetos


# OBJETIVO DO PROJETO:


# Desenvolver um sistema funcional baseado em uma necessidade real, aplicando
# conceitos de programação e adquirindo experiência prática para composição
# de portfólio profissional.

class Entrada():
    def __init__(self, valor, data, metodo_de_pagamento):
        self.valor_entrada = valor
        self.data = data
        self.metodo_de_pagamento = metodo_de_pagamento

    def __str__(self):
        return f"Data: {self.data}, Metodo de pagamento: {self.metodo_de_pagamento.capitalize()}, Valor da entrada: R${self.valor_entrada}"
    
class RegistrarPacelaPaga:
    def __init__(self, data, metodo_de_pagamento, valor):
        self.data = data
        self.metodo_de_pagamento = metodo_de_pagamento
        self.valor = valor

    def __str__(self):
        return f"Data: {self.data}, Metodo de pagamento: {self.metodo_de_pagamento}, Valor R${self.valor}"

class SistemaDeControle:

    def __init__(self):
        print("Bem Vindo ao Sistema De Controle De Financiamento Imobiliário")
        self.valor_financiamento = 0
        self.valor_quitado = 0
        self.saldo_devedor = 0
        self.parcelas = []
        self.entrada = None

        while True:
            try:
                valor = int(input("Antes de mais nada qual valor financiamento: "))
                if valor > 0:
                    self.valor_financiamento += valor
                    self.saldo_devedor += self.valor_financiamento
                    break
                else: 
                    print("Digite um valor maior que 0")
            except ValueError:
                print("Digite somente números")

    def registrar_entrada(self):
        try:
            if self.entrada != None:
                print("\n===Você já realizou uma entrada===\n")
                return
            
            valor_entrada = int(input("Qual o valor da entrada? "))
            

            if valor_entrada > self.valor_financiamento:
                print("Valor maior que do financiamento")
                return
            
            if valor_entrada <= 0:
                print("Valor precisa ser maior que Zero")
                return
            
            data_input = input("Data do pagemento: ")
            if len(data_input) == 8:
                data = f"{data_input[:2]}/{data_input[2:4]}/{data_input[4:]}"
            else:
                data = data_input


            opcoes_validas = ["pix", "cartão", "boleto"]
            meio_pagamento = input("Meio de pagamento pix, cartão ou boleto? ")

            if meio_pagamento.lower() not in opcoes_validas:
                print("\n=== meio de pagamento invalida ===\n")
                return

            self.entrada = Entrada(valor_entrada, data, meio_pagamento)
            self.valor_quitado += self.entrada.valor_entrada
            self.saldo_devedor -= self.entrada.valor_entrada
            self.parcelas.append(self.entrada)
            print("\n=== Entrada realizada com sucesso ===\n")
            return
        except ValueError:
            print("\n=== Valor inválido ===\n")

    def registrar_parcela(self):
        try:
            data_input = input("Data do pagemento: ")
            if len(data_input) == 8:
                data = f"{data_input[:2]}/{data_input[2:4]}/{data_input[4:]}"
            else:
                data = data_input
            
            metodos_validos = ["cartão", "deposito", "pix"]
            
            metodo_de_pagamento = input("Escolha um metodo de pagamento (cartão, deposito, pix): ")
            
            if metodo_de_pagamento.lower() not in metodos_validos:
                print("Metodo de pagamento inválido")
                return

            valor = int(input("Digite o valor da parcela paga: "))

            if valor <= 0:
                print("Digite um valor maior que Zero")
                return
            
            if valor > self.saldo_devedor:
                print("Valor valor que o saldo devedor")
                return

            parcela = RegistrarPacelaPaga(data, metodo_de_pagamento.capitalize(), valor)

            self.valor_quitado += parcela.valor
            self.saldo_devedor -= parcela.valor
            self.parcelas.append(parcela)

            print(f"\n===Parcela paga com sucesso===\n")
        except ValueError:
            print(f"Valor inválido")

    def listar_pagementos(self):
        print("\n===HISTORICO DE PAGAMENTOS JÁ REALIZADO===\n")
        for i, p in enumerate(self.parcelas, start=1):
            print(f"{i}. {p}")

    def resumo_de_financiamento(self):
        return (
            "\n=== Resumo do financiamento ===\n" 
            f"\nValor do financiamento: R${self.valor_financiamento}\n"
            f"\nValor já quitado: R${self.valor_quitado}\n"
            f"\nResta ainda: R${self.saldo_devedor}\n"
            f"\n{'Nenhuma entrada foi realizada' if self.entrada is None else f'Entrada: {self.entrada}'}\n"
        )

    def menu(self):
        while True:
            print("1 - Registrar entrada")
            print("2 - Registrar parcela paga")
            print("3 - Listar pagamentos")
            print("4 - Ver resumo de financiamento")
            print("5 - Associar comprovante PDF a um pagamento")
            print("6 - Lista comprovantes")
            print("7 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.registrar_entrada()
            elif opcao == "2":
                self.registrar_parcela()
            elif opcao == "3":
                self.listar_pagementos()
            elif opcao == "4":
                print(self.resumo_de_financiamento())
            
            elif opcao == "7":
                print("Encerrando o programa...")
                break
            
            else:
                print("\n===Opção inválida! Escolha entre 1 a 7.===\n")

if __name__ == "__main__":
    sistema = SistemaDeControle()
    sistema.menu()


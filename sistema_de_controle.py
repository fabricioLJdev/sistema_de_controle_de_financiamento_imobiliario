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


class SistemaDeControle:

    def __init__(self):
        print("Bem Vindo ao Sistema De Controle De Financiamento Imobiliário")
        self.valor_financiamento = 0
        
        while True:
            try:
                valor = int(input("Antes de mais nada qual valor financiamento: "))
                if valor > 0:
                    self.valor_financiamento = valor
                    break
                else: 
                    print("Digite um valor maior que 0")
            except ValueError:
                print("Digite somente números")
                
        

    def resumo_de_financiamento(self):
        return (
            "\n === Resumo do financiamento ===\n" 
            f"\n Valor do financiamento: R${self.valor_financiamento}\n" 
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
                print("Registrar entrada")

            elif opcao == "4":
                print(self.resumo_de_financiamento())
            
            elif opcao == "7":
                print("Encerrando o programa...")
                break

            else:
                print("Opção inválida! Escolha entre 1 a 7.")

sistema = SistemaDeControle()

if __name__ == "__main__":
    sistema.menu()
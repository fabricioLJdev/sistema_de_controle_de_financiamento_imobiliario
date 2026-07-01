from pathlib import Path

class Entrada():
    def __init__(self, valor, data, metodo_de_pagamento, comprovante_pdf=None):
        self.valor_entrada = valor
        self.data = data
        self.metodo_de_pagamento = metodo_de_pagamento
        self.comprovante = comprovante_pdf

    def __str__(self):
        return f"Data: {self.data}, Metodo de pagamento: {self.metodo_de_pagamento.capitalize()}, Valor da entrada: R${self.valor_entrada}"
    
class RegistrarPacelaPaga:
    def __init__(self, data, metodo_de_pagamento, valor, comprovante_pdf=None):
        self.data = data
        self.metodo_de_pagamento = metodo_de_pagamento
        self.valor = valor
        self.comprovante = comprovante_pdf
    
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
            if len(data_input) == 8 and data_input.isdigit():
                data = f"{data_input[:2]}/{data_input[2:4]}/{data_input[4:]}"
            else:
                print("Erro: informe a data no formato DDMMAAAA (ex: 26022025)")
                return

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
            if self.valor_quitado == self.valor_financiamento:
                print("O emprestimo já foi quitado")
                return 
                
            data_input = input("Data do pagemento: ")
            if len(data_input) == 8 and data_input.isdigit():
                data = f"{data_input[:2]}/{data_input[2:4]}/{data_input[4:]}"
            else:
                print("Erro: informe a data no formato DDMMAAAA (ex: 26022025)")
                return
            metodos_validos = ["cartão", "deposito", "pix"]
            
            metodo_de_pagamento = input("Escolha um metodo de pagamento (cartão, deposito, pix): ")
            
            if metodo_de_pagamento.lower() not in metodos_validos:
                print("\n=== Metodo de pagamento inválido ===\n")
                return

            valor = int(input("Digite o valor da parcela paga: "))

            if valor <= 0:
                print("Digite um valor maior que Zero")
                return
            
            if valor > self.saldo_devedor:
                print("\n=== Parcela maior que o saldo devedor ===\n")
                return

            parcela = RegistrarPacelaPaga(data, metodo_de_pagamento.capitalize(), valor)

            self.valor_quitado += parcela.valor
            self.saldo_devedor -= parcela.valor
            self.parcelas.append(parcela)

            print("\n=== Parcela paga com sucesso ===\n")
        except ValueError:
            print("\n=== Valor inválido ===\n")

    def listar_pagamentos(self):
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

    def associar_comprovante_pdf(self):
        if not self.parcelas:
            print("\n===Você não fez nenhuma pagamento===\n")
            return
        
        print("\n=== lista de pagamentos ===\n")
        for i, p in enumerate(self.parcelas, start=1):
            print(f"{i}. {p}\n")
        
        try: 
            indice = int(input("Escolha um pagamento para associar comprovante: "))

            if 1 <= indice <= len(self.parcelas):
                parcela = self.parcelas[indice - 1]
                entrada = input("Arraste o comprovante até o terminal ")
                
                entrada_limpa = entrada.strip('& "\'\\')

                arquivo = Path(entrada_limpa)
                
                if arquivo.is_file():
                    if arquivo.suffix.lower() in ['.pdf', '.png', '.jpg', '.jpeg']:
                        parcela.comprovante = str(arquivo.resolve())
                        
                        print("\n=== Comprovante associado com sucesso ===\n")

                    else:
                        print("\n=== Formato inválido ===\n")
                else:
                        print("Arquivo não existe")
                        return

            else:
                print("\n=== Indice inválido ===\n")

        except ValueError:
            print("\n=== Digite somente números ===\n")    

    def listar_comprovantes(self):
        if not self.parcelas:
            print("\n=== lista você não fez nenhum pagamento \n===")
            return

        for i, p in enumerate(self.parcelas, start=1):
            print(f"{i}. {p}\n")
        try:
            indice = int(input("Escolha a parcela para ver o comprovante: "))

            if 1 <= indice <= len(self.parcelas):
                parcela = self.parcelas[indice - 1]
                if parcela.comprovante == None:
                    print("\n=== Você ainda não adicionou um comprovante para essa parcela ===\n")
                    return
                else:
                    print(f"\Caminho do comprovante:")
                    print(parcela.comprovante)
            else: 
                print("\n=== Indice inválido ===\n")

        except ValueError:
            print("\n=== Digite somente números ===")

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
                self.listar_pagamentos()
            elif opcao == "4":
                print(self.resumo_de_financiamento())
            elif opcao == "5":
                self.associar_comprovante_pdf()
            elif opcao == "6":
                self.listar_comprovantes()
            elif opcao == "7":
                print("Encerrando o programa...")
                break
            
            else:
                print("\n===Opção inválida! Escolha entre 1 a 7.===\n")

if __name__ == "__main__":
    sistema = SistemaDeControle()
    sistema.menu()


# 🏠 Sistema de Controle de Financiamento Imobiliário

Sistema desenvolvido em **Python** para gerenciar um financiamento imobiliário através do terminal.

O projeto permite registrar a entrada, controlar parcelas pagas, acompanhar o saldo devedor e associar comprovantes aos pagamentos realizados.

Este projeto foi desenvolvido com o objetivo de praticar **Programação Orientada a Objetos (POO)**, validação de dados, tratamento de exceções e manipulação de arquivos utilizando a biblioteca `pathlib`.

---

# 📌 Funcionalidades

- ✅ Cadastro do valor do financiamento
- ✅ Registro da entrada
- ✅ Registro de parcelas pagas
- ✅ Histórico de pagamentos
- ✅ Resumo do financiamento
- ✅ Associação de comprovantes (PDF, PNG, JPG e JPEG)
- ✅ Listagem dos comprovantes
- ✅ Atualização automática do saldo devedor
- ✅ Validação de entradas do usuário
- ✅ Tratamento de exceções (`try` / `except`)

---

# 🛠 Tecnologias utilizadas

- Python 3
- Programação Orientada a Objetos (POO)
- Biblioteca `pathlib`
- Git
- GitHub

---

# 📂 Estrutura do projeto

```text
SistemaDeControle
│
├── Entrada
├── RegistrarParcelaPaga
└── SistemaDeControle
```

---

# 🚀 Como executar

### Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
```

### Entre na pasta

```bash
cd SEU-REPOSITORIO
```

### Execute o projeto

```bash
python main.py
```

---

# 📋 Funcionalidades implementadas

### 1️⃣ Registrar entrada

Permite cadastrar a entrada do financiamento, informando:

- Valor
- Data
- Método de pagamento

---

### 2️⃣ Registrar parcela

Permite registrar parcelas pagas contendo:

- Data
- Método de pagamento
- Valor

O sistema atualiza automaticamente:

- Valor quitado
- Saldo devedor

---

### 3️⃣ Histórico de pagamentos

Lista todos os pagamentos realizados, incluindo a entrada.

---

### 4️⃣ Resumo do financiamento

Exibe:

- Valor total do financiamento
- Valor quitado
- Saldo devedor
- Informações da entrada

---

### 5️⃣ Associar comprovante

Permite associar um comprovante a um pagamento.

São aceitos arquivos:

- PDF
- PNG
- JPG
- JPEG

Também é validado:

- existência do arquivo;
- extensão permitida.

---

### 6️⃣ Listar comprovantes

Exibe o caminho do comprovante associado ao pagamento escolhido.

---

# 🔒 Validações implementadas

- Valor maior que zero
- Entrada única
- Parcela não pode ser maior que o saldo devedor
- Método de pagamento válido
- Data no formato DDMMAAAA
- Índice válido
- Arquivo existente
- Extensão permitida
- Tratamento de erros com `try/except`

---

# 🔮 Melhorias futuras

- Salvar os dados em JSON
- Carregar os dados automaticamente
- Abrir comprovantes diretamente pelo sistema operacional
- Editar pagamentos
- Remover pagamentos
- Interface gráfica (Tkinter ou PyQt)
- Banco de dados (SQLite)

---

# 📚 Conceitos praticados

- Programação Orientada a Objetos
- Classes e Objetos
- Métodos especiais (`__str__`)
- Listas de objetos
- Encapsulamento
- Tratamento de exceções
- Manipulação de arquivos
- Biblioteca `pathlib`
- Estruturas condicionais
- Estruturas de repetição
- Validação de dados

---

# 👨‍💻 Autor

**Fabricio Lacerda**

Desenvolvedor Python em formação.

- GitHub: https://github.com/SEU-USUARIO
- LinkedIn: https://www.linkedin.com/in/fabricio-lacerda-de-jesus/
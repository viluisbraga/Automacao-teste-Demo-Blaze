# Projeto de Automação de Testes - Demo Blaze

<img src="https://www.demoblaze.com/bm.png" alt="Demo Blaze"/>

## Índice

1. [Descrição do Projeto](#descrição-do-projeto)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Estrutura do Projeto](#estrutura-do-projeto)
4. [Configuração do Ambiente](#configuração-do-ambiente)
5. [Execução dos Testes](#execução-dos-testes)
6. [Cenários de Teste](#cenários-de-teste)
7. [Contribuição](#contribuição)
8. [Licença](#licença)

## Descrição do Projeto

Este projeto visa a automação de testes do site Demo Blaze utilizando Python, uma das linguagens mais populares e versáteis do mercado. O desenvolvimento foi realizado no VSCode, com o auxílio de poderosas ferramentas como Selenium e Selenium WebDriver para interação com a interface web. O Pytest foi utilizado para garantir que os testes fossem executados de forma eficiente e bem organizados, facilitando a automação e assegurando a qualidade do processo de teste.

Nos cenários de teste, a abordagem utilizada segue a metodologia BDD (Behavior-Driven Development), onde os testes são descritos de maneira a enfatizar o comportamento esperado das funcionalidades, facilitando a colaboração entre desenvolvedores, testadores e stakeholders.

Para garantir um ambiente controlado e livre de conflitos, todos os pacotes necessários foram instalados dentro de um ambiente virtual, proporcionando uma execução de testes limpa e eficiente.

## Tecnologias Utilizadas

- ![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
- ![VSCode](https://img.shields.io/badge/VSCode-1.58-blue)
- ![Selenium](https://img.shields.io/badge/Selenium-3.141.0-green)
- ![Selenium WebDriver](https://img.shields.io/badge/Selenium%20WebDriver-3.141.0-yellow)
- ![Pytest](https://img.shields.io/badge/Pytest-6.2.4-yellow)

## Estrutura do Projeto

O projeto segue o padrão PageObjects e está organizado da seguinte forma:

```
📦 projeto-automacao
├── 📂 pages
│   ├── __init__.py
│   ├── pagina_base.py
│   ├── pagina_carrinho.py
│   ├── pagina_inicial.py
│   ├── pagina_menu_superior.py
│   └── pagina_produto.py
├── 📂 tests
│   ├── 📂 tests_acesso
│   │   ├── test_cadastro_usuario_duplicado.py
│   │   ├── test_cadastro_usuario_valido.py
│   │   ├── test_login_valido.py
│   │   ├── test_senha_invalida.py
│   │   └── test_usuario_invalido.py
│   ├── 📂 tests_de_compra
│   │   ├── test_compra_de_tres_produtos.py
│   │   └── test_exclusao_produto_carrinho.py
│   └── __init__.py 
├── 📂 venv
│   ├── Include
│   ├── Lib
│   └── Scripts
├── conftest.py
├── pytest.ini
├── README.md
└── requirements.txt
```

## Configuração do Ambiente

1. Clone o repositório:
    ```bash
    git clone: https://github.com/viluisbraga/Automacao-teste-Demo-Blaze.git
    ```
2. Crie um ambiente virtual:
    ```bash
    python -m venv venv 
    ```
3. Ative um ambiente virtual:
    ```bash
   source venv/bin/activate  # No Windows use `venv/Scripts/Activate.ps1`
    ```
4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Execução dos Testes

Para executar todos os testes que existem no sistema, utilize o comando:
```bash
pytest -v
```
Para executar testes chamando os markers existentes utilize o comando:

```bash
pytest -v -m (Nome mark) # exemplo: pytest -v -m login
```
## Cenários de Teste

### Testes de Acesso

- **Teste cadastro usuário válido**
- **Teste cadastro usuário duplicado**
- **Teste login válido**
- **Teste senha inválida**
- **Teste usuário inválido**

### Testes de Compra

- **Teste compra de três produtos**
- **Teste exclusão produto do carrinho**

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo para mais detalhes.

---

## Contato
- **LinkedIn** - [Meu LinkedIn](https://www.linkedin.com/in/vitor-luis-braga-7783a5211/)

- **E-mail**: viluis60@gmail.com
- **Feito por** [Vitor Braga](https://github.com/viluisbraga)

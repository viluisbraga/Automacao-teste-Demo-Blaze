# Projeto de Automação de Testes - Demo Blaze

![Demo Blaze](https://www.demoblaze.com/bm.png)

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

Este projeto tem como objetivo a automação de testes do site **Demo Blaze**. Utilizamos a linguagem de programação Python junto com o VSCode, Selenium, Selenium WebDriver e Pytest. Todos os pacotes foram instalados em um ambiente virtual para a realização dos testes.

## Tecnologias Utilizadas

- Python
- VSCode
- Selenium
- Selenium WebDriver
- Pytest

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
└── README.md
```

## Configuração do Ambiente

1. Clone o repositório:
    ```bash
    git clone <URL_DO_REPOSITORIO>
    ```
2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv/Scripts/Activate.ps1`
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Execução dos Testes

Para executar todos os testes que existem no sistema, utilize o comando:
```bash
pytest -v
```
Para executar testes chamando os markers existentes no cenários de testes utilize o comando:

```bash
pytest -v -m (Nome mark) exemplo: pytest -v -m login
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

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Contato

- **Seu Nome** - [Seu Email](mailto:seu-email@example.com)
- **LinkedIn** - [Seu LinkedIn](https://www.linkedin.com/in/seu-usuario)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-3.141.0-green)
![Pytest](https://img.shields.io/badge/Pytest-6.2.4-yellow)

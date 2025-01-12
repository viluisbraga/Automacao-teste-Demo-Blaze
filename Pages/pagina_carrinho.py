import re
from time import sleep
import conftest
from selenium.webdriver.common.by import By
from Pages.pagina_base import PaginaBase


class PaginaCarrinho(PaginaBase):
#Construtor
    def __init__(self):
        self.driver = conftest.driver

# Locator
        self.selecionar_produto = (By.XPATH, '//td[contains(text(), "{}")]')
        self.botao_Place_order = (By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button')
        self.campo_name = (By.ID, 'name')
        self.campo_country = (By.ID, 'country')
        self.campo_city = (By.ID, 'city')
        self.campo_creditcard = (By.ID, 'card')
        self.campo_month = (By.ID, 'month')
        self.campo_year = (By.ID, 'year')
        self.botao_purchase = (By.XPATH,'//*[@id="orderModal"]/div/div/div[3]/button[2]')
        self.alerta_de_compra_com_sucesso = (By.XPATH, '/html/body/div[10]/h2')
        self.botao_ok_compra_finalizada = (By.XPATH, '/html/body/div[10]/div[7]/div/button')
        self.valor_total_dos_produtos = (By.ID, 'totalp')
        self.campo_name_alerta_sucesso = (By.XPATH, '/html/body/div[10]/p')
        self.campo_creditcard_alerta_sucesso = (By.XPATH, '/html/body/div[10]/p')
        self.valor_total_alerta_sucesso = (By.XPATH, '/html/body/div[10]/p') 
        self.botao_delete = (By.XPATH, '//td[text()="{}"]/following-sibling::td/a' )
        self.titulo_pagina_carrinho = (By.XPATH, '//*[@id="page-wrapper"]/div/div[1]/h2')
        
# Variaveis

        self.produto1 = 'Samsung galaxy s6'
        self.produto2 = 'Nokia lumia 1520'
        self.produto3 = 'Nexus 6'
        self.monitor = 'Apple monitor 24'
        self.laptop = 'Sony vaio i5'
        self.phone = 'Samsung galaxy s6'

        self.valor_total_esperado_dos_produtos1 = '1830'
        self.valor_total_esperado_dos_produtos2 = '1550'
        self.valor_total_esperado_dos_produtos_apos_exclusao = '1150'
        self.texto_name = 'Teste Nome'
        self.texto_country = 'Teste country'
        self.texto_city = 'Teste city'
        self.texto_creditcard = '11111111111111111'
        self.texto_month = '03'
        self.texto_year = '2025'
        self.texto_de_compra_com_sucesso = 'Thank you for your purchase!'
        
        
# Metodos

    def validar_produto1_carrinho(self):
        nome_produto = (self.selecionar_produto[0],self.selecionar_produto[1].format(self.produto1))
        self.verifica_texto_do_elemento(nome_produto,self.produto1)

    def validar_produto2_carrinho(self):
        nome_produto = (self.selecionar_produto[0],self.selecionar_produto[1].format(self.produto2))
        self.verifica_texto_do_elemento(nome_produto,self.produto2)
    
    def validar_produto3_carrinho(self):
        nome_produto = (self.selecionar_produto[0],self.selecionar_produto[1].format(self.produto3))
        self.verifica_texto_do_elemento(nome_produto,self.produto3)
    
    def validar_monitor_carrinho(self):
        nome_produto = (self.selecionar_produto[0],self.selecionar_produto[1].format(self.monitor))
        self.verifica_texto_do_elemento(nome_produto,self.monitor)

    def validar_laptop_carrinho(self):
        nome_produto = (self.selecionar_produto[0],self.selecionar_produto[1].format(self.laptop))
        self.verifica_texto_do_elemento(nome_produto,self.laptop)

    def validar_phone_carrinho(self):
        nome_produto = (self.selecionar_produto[0],self.selecionar_produto[1].format(self.phone))
        self.verifica_texto_do_elemento(nome_produto,self.phone)

    def validar_total_dos_produtos1(self):
        self.verifica_texto_do_elemento(self.valor_total_dos_produtos, self.valor_total_esperado_dos_produtos1)

    def validar_total_dos_produtos2(self):
        self.verifica_texto_do_elemento(self.valor_total_dos_produtos, self.valor_total_esperado_dos_produtos2)

    def validar_total_dos_produtos_apos_exclusao(self):
        self.verifica_texto_do_elemento(self.valor_total_dos_produtos, self.valor_total_esperado_dos_produtos_apos_exclusao)

    def excluir_monitor_do_carrinho(self):
        produto = (self.botao_delete[0],self.botao_delete[1].format(self.monitor))
        self.clicar(produto)

    def validar_exclusao_do_monitor(self):
        nome_produto = (self.selecionar_produto[0],self.selecionar_produto[1].format(self.monitor))
        self.esperar_elemento_desaparecer(nome_produto)

    def clicar_botao_place_order(self):
        self.clicar(self.botao_Place_order)
    
    def preencher_campo_name(self):
        self.escrever(self.campo_name,self.texto_name)

    def preencher_campo_country(self):
        self.escrever(self.campo_country,self.texto_country)

    def preencher_campo_city(self):
        self.escrever(self.campo_city,self.texto_city)

    def preencher_campo_creditcard(self):
        self.escrever(self.campo_creditcard,self.texto_creditcard)

    def preencher_campo_month(self):
        self.escrever(self.campo_month,self.texto_month)

    def preencher_campo_year(self):
        self.escrever(self.campo_year,self.texto_year)

    def clicar_botao_purchase(self):
        self.clicar(self.botao_purchase)

    def validar_alerta_de_compra_com_sucesso(self):
        self.verifica_texto_do_elemento(self.alerta_de_compra_com_sucesso, self.texto_de_compra_com_sucesso)

    def validar_campo_amount(self):
        elemento =  self.encontrar_elemento(self.valor_total_alerta_sucesso)
        texto = elemento.text
        amount_value = re.search(r"Amount:\s*(\d+)", texto)
        if amount_value:
            amount_text = amount_value.group(1)
            assert self.valor_total_esperado_dos_produtos1 == amount_text, f"Valor esperado: {self.valor_total_esperado_dos_produtos1}, mas foi encontrado: {amount_text}"

    def validar_campo_card_number(self):
        elemento = self.encontrar_elemento(self.campo_creditcard_alerta_sucesso)
        texto = elemento.text
        card_number_value = re.search(r"Card Number:\s*([A-Za-z0-9]+)", texto)
        if card_number_value:
            card_number_text = card_number_value.group(1)
            assert self.texto_creditcard == card_number_text, f"Card Number esperado: {self.texto_creditcard}, mas foi encontrado: {card_number_text}"
    
    def validar_campo_name(self):
        elemento = self.encontrar_elemento(self.campo_name_alerta_sucesso)
        texto = elemento.text
        name_value = re.search(r"Name:\s*([A-Za-z\s]+)", texto)
        if name_value: 
            name_text = name_value.group(1)
            name_text = name_text.split("\n")[0]
            assert self.texto_name == name_text, f"Name esperado: {self.texto_name}, mas foi encontrado: {name_text}"
    

    def clicar_botao_ok_da_compra_finalizada(self):
        self.clicar(self.botao_ok_compra_finalizada)
        

    def atualizar_pagina_carrinho(self):
        self.atualizar_pagina()

   # Selecionar o parágrafo completo e pegar o texto
    
        
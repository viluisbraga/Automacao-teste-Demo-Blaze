import conftest
from selenium.webdriver.common.by import By
from Pages.pagina_base import PaginaBase

class PaginaProduto(PaginaBase):

#Construtor
    def __init__(self):
        self.driver = conftest.driver
    
# Locator
        self.nome_produto = (By.XPATH,'//*[@id="tbodyid"]/h2') 
        self.botao_adicionar_no_carrinho = (By.XPATH,'//*[@id="tbodyid"]/div[2]/div/a')
        

# Variaveis
        self.produto1 = 'Samsung galaxy s6'
        self.produto2 = 'Nokia lumia 1520'
        self.produto3 = 'Nexus 6'
        self.monitor = 'Apple monitor 24'
        self.laptop = 'Sony vaio i5'
        self.phone = 'Samsung galaxy s6'
        self.alerta_esperado_apos_inclusao_de_produto = 'Product added.'

# Metodos
    def validar_produto1(self):
        self.verifica_texto_do_elemento(self.nome_produto,self.produto1)
    
    def validar_produto2(self):
        self.verifica_texto_do_elemento(self.nome_produto,self.produto2)
    
    def validar_produto3(self):
        self.verifica_texto_do_elemento(self.nome_produto,self.produto3)

    def validar_monitor(self):
        self.verifica_texto_do_elemento(self.nome_produto,self.monitor)

    def validar_laptop(self):
        self.verifica_texto_do_elemento(self.nome_produto,self.laptop)

    def validar_phone(self):
        self.verifica_texto_do_elemento(self.nome_produto,self.phone)

    def adicionar_produto_no_carrinho(self):
        self.clicar(self.botao_adicionar_no_carrinho)

    def validar_alerta_inclusao_de_produtos(self): 
        self.validar_alerta_navegador(self.alerta_esperado_apos_inclusao_de_produto)

    def clicar_botao_purchase(self):
        self.clicar(self.botao_purchase)
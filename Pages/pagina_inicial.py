import conftest
from selenium.webdriver.common.by import By
from Pages.pagina_base import PaginaBase


class PaginaInicial(PaginaBase):
#Construtor
    def __init__(self):
        self.driver = conftest.driver

# Locator
        self.selecionar_produto = (By.XPATH, '//a[text()="{}"]')
        self.categoria_monitor = (By.XPATH, '//a[@id="itemc" and text()="Monitors"]')
        self.categoria_laptops = (By.XPATH, '//a[@id="itemc" and text()="Laptops"]')
        self.categoria_phones = (By.XPATH, '//a[@id="itemc" and text()="Phones"]')

# Variaveis
        self.produto1 = 'Samsung galaxy s6'
        self.produto2 = 'Nokia lumia 1520'
        self.produto3 = 'Nexus 6'
        self.monitor = 'Apple monitor 24'
        self.laptop = 'Sony vaio i5'
        self.phone = 'Samsung galaxy s6'

        
# Metodos
    def selecionar_produto1(self):
        produto = (self.selecionar_produto[0],self.selecionar_produto[1].format(self.produto1))
        self.clicar(produto)

    def selecionar_produto2(self):
        produto = (self.selecionar_produto[0],self.selecionar_produto[1].format(self.produto2))
        self.clicar(produto)
    
    def selecionar_produto3(self):
        produto = (self.selecionar_produto[0],self.selecionar_produto[1].format(self.produto3))
        self.clicar(produto)

    def selecionar_monitor(self):
        produto = (self.selecionar_produto[0],self.selecionar_produto[1].format(self.monitor))
        self.clicar(produto)

    def selecionar_laptop(self):
        produto = (self.selecionar_produto[0],self.selecionar_produto[1].format(self.laptop))
        self.clicar(produto)

    def selecionar_phone(self):
        produto = (self.selecionar_produto[0],self.selecionar_produto[1].format(self.phone))
        self.clicar(produto)

    def acessar_categoria_de_monitores(self):
        self.clicar(self.categoria_monitor)

    def acessar_categoria_de_laptops(self):
        self.clicar(self.categoria_laptops)
    
    def acessar_categoria_de_Phones(self):
        self.clicar(self.categoria_phones)



    def verificar_alerta_acesso_invalido(self):
        self.verifica_se_elemento_existe(self.alerta_acesso_invalido)

    def verifica_texto_do_alerta(self,texto_esperado):
        texto_encontrado = self.pegar_texto_elemento(self.texto_alerta_invalido)
        assert texto_encontrado == texto_esperado, f"O texto encontrato foi '{texto_encontrado}'mas era esperado '{texto_esperado}'"
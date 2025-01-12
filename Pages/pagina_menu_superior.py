import conftest
from selenium.webdriver.common.by import By
from Pages.pagina_base import PaginaBase


class PaginaMenuSuperior(PaginaBase):
#Construtor
    def __init__(self):
        self.driver = conftest.driver

# Locator
        self.menu_signup = (By.XPATH, '//*[@id="navbarExample"]/ul/li[8]')
        self.botao_signup = (By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]') 
        self.menu_login = (By.ID, 'login2')
        self.menu_home = (By.XPATH, '//*[@id="navbarExample"]/ul/li[1]/a')
        self.menu_cart = (By.ID, 'cartur')
        self.campo_username_signup = (By.ID, 'sign-username')
        self.campo_password_signup = (By.ID,'sign-password')
        self.campo_username_login = (By.ID, 'loginusername')
        self.campo_password_login = (By.ID,'loginpassword')
        self.botao_login = (By.XPATH,'//*[@id="logInModal"]/div/div/div[3]/button[2]')
        self.usuario_logado = (By.ID,'nameofuser')
        self.alerta_acesso_invalido = (By.ID,'')
        self.texto_alerta_invalido =(By.XPATH, '')


# Variaveis
        self.valor_username_signup = 'login47'
        self.valor_password_signup = 'senha123'
        self.alerta_esperado_na_criaçao_novo_usuario = 'Sign up successful.'
        self.alerta_esperado_para_usuario_existente = 'This user already exist.'
        self.alerta_esperado_apos_inclusao_de_produto = 'Product added.'
        self.alerta_esperado_para_usuario_invalido = 'User does not exist.'
        self.alerta_esperado_para_senha_invalida = 'Wrong password.'

        self.valor_username_login = 'login47'
        self.valor_password_login = 'senha123'
        self.nome_usuario_logado = 'Welcome '+ self.valor_username_login

# Metodos
    def clicar_menu_signup(self,):
        self.clicar(self.menu_signup)

    def clicar_menu_login(self,):
        self.clicar(self.menu_login)
    
    def clicar_menu_home(self,):
        self.clicar(self.menu_home)

    def clicar_menu_cart(self,):
        self.clicar(self.menu_cart)
    
    def preencher_campos_do_cadastro(self,):
        self.escrever(self.campo_username_signup,self.valor_username_signup)
        self.escrever(self.campo_password_signup,self.valor_password_signup)

    def preencher_campos_do_cadastro_com_informaçoes_especificas(self,usuario,senha):
        self.escrever(self.campo_username_signup,usuario)
        self.escrever(self.campo_password_signup,senha)
        self.clicar(self.botao_signup)

    def clicar_no_botao_signup_do_popup(self,):    
        self.clicar(self.botao_signup)
    
    def clicar_no_botao_login_do_popup(self,):    
        self.clicar(self.botao_login)

    def validar_alerta_criaçao_de_novo_usuario(self,): 
        self.validar_alerta_navegador(self.alerta_esperado_na_criaçao_novo_usuario)

    def validar_alerta_de_bloqueio_para_usuarios_existentes(self,): 
        self.validar_alerta_navegador(self.alerta_esperado_para_usuario_existente)

    def validar_alerta_de_usuario_invalido(self): 
        self.validar_alerta_navegador(self.alerta_esperado_para_usuario_invalido)

    def validar_alerta_de_senha_invalida(self): 
        self.validar_alerta_navegador(self.alerta_esperado_para_senha_invalida)
 
    def fazer_login(self,):
         self.escrever(self.campo_username_login,self.valor_username_login)
         self.escrever(self.campo_password_login,self.valor_password_login)
         self.clicar(self.botao_login)

    def fazer_login_com_informaçoes_especifico(self, usuario, senha):
        self.escrever(self.campo_username_login,usuario)
        self.escrever(self.campo_password_login,senha)
        self.clicar(self.botao_login)

    def verifica_usuario_logado(self,):
        texto_encontrado = self.pegar_texto_elemento(self.usuario_logado)
        assert texto_encontrado == self.nome_usuario_logado, f"O texto encontrato foi '{texto_encontrado}'mas era esperado '{self.nome_usuario_logado}'"
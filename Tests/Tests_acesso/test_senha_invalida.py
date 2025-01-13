import pytest
from Pages.pagina_menu_superior import PaginaMenuSuperior



@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.login_invalido()
@pytest.mark.login()
@pytest.mark.login_senha_invalida()
@pytest.mark.usuario()

def test_login_senha_invalida():
    pagina_menu_superior = PaginaMenuSuperior()



# Dado que clico no botão "Log in" do menu do topo da tela.
    pagina_menu_superior.clicar_menu_login()

# E preencho os campo "Username" e "Password" sendo o "Password" invalido.
    pagina_menu_superior.fazer_login_com_informaçoes_especifico('login75','123456')

# Quando clico no botão "log in" do pop-up que foi exibido.
    pagina_menu_superior.clicar_no_botao_login_do_popup()

# então sistema deve exibir um alerta de senha invalida e nao permitir realizar o login
    pagina_menu_superior.validar_alerta_de_senha_invalida()
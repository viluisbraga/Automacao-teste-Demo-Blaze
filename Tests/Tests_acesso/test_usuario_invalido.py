import pytest
from Pages.pagina_menu_superior import PaginaMenuSuperior



@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.login_invalido()
@pytest.mark.login()
@pytest.mark.login_usuario_invalido()
@pytest.mark.usuario()

def test_login_usuario_invalido():
    pagina_menu_superior = PaginaMenuSuperior()



# Dado que clico no botão "Log in" do menu do topo da tela
    pagina_menu_superior.clicar_menu_login()

# E preencho os campo "Username" e "Password" com informaçoes validas sendo o "Username" invalido
    pagina_menu_superior.fazer_login_com_informaçoes_especifico('login99','123456')

# Quando clico no botão "log in" do pop-up que foi exibido
    pagina_menu_superior.clicar_no_botao_login_do_popup()

# então sistema deve exibir alerta de usuario invalido e nao permitir realizar o login
    pagina_menu_superior.validar_alerta_de_usuario_invalido()
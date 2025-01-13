import pytest
from Pages.pagina_menu_superior import PaginaMenuSuperior



@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.login_valido()
@pytest.mark.login()
@pytest.mark.usuario()

def test_login_valido():
    pagina_menu_superior = PaginaMenuSuperior()



# Dado que clico no botão "Log in" do menu do topo da tela.
    pagina_menu_superior.clicar_menu_login()

# E preencho os campo "Username" e "Password" com informaçoes validas.
    pagina_menu_superior.fazer_login()

# Quando clico no botão "log in" do pop-up que foi exibido.
    pagina_menu_superior.clicar_no_botao_login_do_popup()

# então sistema deve realizar o login com sucesso.
    pagina_menu_superior.verifica_usuario_logado()
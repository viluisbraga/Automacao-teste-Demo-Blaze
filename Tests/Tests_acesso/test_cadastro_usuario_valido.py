import pytest
from Pages.pagina_menu_superior import PaginaMenuSuperior



@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.criaçao_usuario_valido()
@pytest.mark.criaçao_usuario()
@pytest.mark.usuario()

def test_cadastro_usuario_valido():
    pagina_menu_superior = PaginaMenuSuperior()

# Dado que clico no botão "Sign up" do menu do topo da tela.
    pagina_menu_superior.clicar_menu_signup()

# E preencho os campo "Username" e "Password" com informaçoes validas.
    pagina_menu_superior.preencher_campos_do_cadastro()

# Quando clico no botão "Sign up" do pop-up que foi exibido.
    pagina_menu_superior.clicar_no_botao_signup_do_popup()

# então sistema deve realizar a criação do usuário com sucesso.
    pagina_menu_superior.validar_alerta_criaçao_de_novo_usuario()
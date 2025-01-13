import pytest
from Pages.pagina_menu_superior import PaginaMenuSuperior



@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.criaçao_usuario_duplciado()
@pytest.mark.criaçao_usuario()
@pytest.mark.usuario()

def test_cadastro_usuario_duplicado():
    pagina_menu_superior = PaginaMenuSuperior()

# Dado que clico no botão "Sign up" do menu do topo da tela.
    pagina_menu_superior.clicar_menu_signup()

# E preencho os campo "Username" e "Password" com informaçoes validas sendo o "Username" um valor que ja existe.
    pagina_menu_superior.preencher_campos_do_cadastro_com_informaçoes_especificas("login75","123456")

# Quando clico no botão "Sign up" do pop-up que foi exibido.
    pagina_menu_superior.clicar_no_botao_signup_do_popup()

# então sistema deve exibir um alerta de bloqueio e nao permitir a criação do usuario uma vez que esse usuario ja existe.
    pagina_menu_superior.validar_alerta_de_bloqueio_para_usuarios_existentes()
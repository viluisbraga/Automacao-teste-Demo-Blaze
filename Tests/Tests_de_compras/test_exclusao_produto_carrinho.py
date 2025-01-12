import pytest
from Pages.pagina_inicial import PaginaInicial
from Pages.pagina_produto import PaginaProduto
from Pages.pagina_menu_superior import PaginaMenuSuperior
from Pages.pagina_carrinho import PaginaCarrinho





@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.exclusao_de_produto() 
@pytest.mark.produtos()

def test_exclusao_produto():
    pagina_menu_superior = PaginaMenuSuperior()
    pagina_inicial = PaginaInicial()
    pagina_produto =PaginaProduto()
    pagina_carrinho =PaginaCarrinho()




# Dado que eu acesso o sistema demo blaze com usuario valido.
    pagina_menu_superior.clicar_menu_login()
    pagina_menu_superior.fazer_login()
    pagina_menu_superior.verifica_usuario_logado()
    
# E seleciono um celular
    pagina_inicial.selecionar_phone()
    pagina_produto.validar_phone()

# E clico para colocar o produto no carrinho
    pagina_produto.adicionar_produto_no_carrinho()
    pagina_produto.validar_alerta_inclusao_de_produtos()

# E vou para a tela de laptop
    pagina_menu_superior.clicar_menu_home()
    pagina_inicial.acessar_categoria_de_laptops()

# E seleciono um laptop
    pagina_inicial.selecionar_laptop()
    pagina_produto.validar_laptop()

# E clico para colocar o produto no carrinho
    pagina_produto.adicionar_produto_no_carrinho()
    pagina_produto.validar_alerta_inclusao_de_produtos()


# E vou para tela de monitores
    pagina_menu_superior.clicar_menu_home()
    pagina_inicial.acessar_categoria_de_monitores()

# E seleciono um monitor
    pagina_inicial.selecionar_monitor()
    pagina_produto.validar_monitor()

# E clico para colocar o produto no carrinho
    pagina_produto.adicionar_produto_no_carrinho()
    pagina_produto.validar_alerta_inclusao_de_produtos()

# E clico para acessar o carrinho
    pagina_menu_superior.clicar_menu_cart()
    pagina_carrinho.validar_phone_carrinho()
    pagina_carrinho.validar_laptop_carrinho()
    pagina_carrinho.validar_monitor_carrinho()
    pagina_carrinho.validar_total_dos_produtos2()


# E clico para deletar o monitor 
    pagina_carrinho.excluir_monitor_do_carrinho()
    pagina_menu_superior.verifica_usuario_logado()

# Quando atualizo a pagina
    pagina_carrinho.atualizar_pagina_carrinho()
    pagina_menu_superior.verifica_usuario_logado()

# Entao sistema deve ter realizado a exclusao do monitor com sucesso
    pagina_carrinho.validar_exclusao_do_monitor()
    pagina_carrinho.validar_total_dos_produtos_apos_exclusao()
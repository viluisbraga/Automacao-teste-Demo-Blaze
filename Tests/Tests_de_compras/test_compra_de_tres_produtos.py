import pytest
from Pages.pagina_inicial import PaginaInicial
from Pages.pagina_produto import PaginaProduto
from Pages.pagina_menu_superior import PaginaMenuSuperior
from Pages.pagina_carrinho import PaginaCarrinho





@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.compra_realizada_com_sucesso()
@pytest.mark.produtos()


def test_compra_de_tres_produtos():
    pagina_menu_superior = PaginaMenuSuperior()
    pagina_inicial = PaginaInicial()
    pagina_produto =PaginaProduto()
    pagina_carrinho =PaginaCarrinho()




# Dado que eu acesso o sistema demo blaze com usuario valido.
    pagina_menu_superior.clicar_menu_login()
    pagina_menu_superior.fazer_login()
    pagina_menu_superior.verifica_usuario_logado()
    
# E seleciono um produto
    pagina_inicial.selecionar_produto1()
    pagina_produto.validar_produto1()

# E clico para colocar o produto no carrinho
    pagina_produto.adicionar_produto_no_carrinho()
    pagina_produto.validar_alerta_inclusao_de_produtos()

# E volto para a tela principal
    pagina_menu_superior.clicar_menu_home()

# E seleciono um segundo produto diferente
    pagina_inicial.selecionar_produto2()
    pagina_produto.validar_produto2()

# E clico para colocar o produto no carrinho
    pagina_produto.adicionar_produto_no_carrinho()
    pagina_produto.validar_alerta_inclusao_de_produtos()


# E volto para a tela principal
    pagina_menu_superior.clicar_menu_home()

# E seleciono um terceiro produto diferente
    pagina_inicial.selecionar_produto3()
    pagina_produto.validar_produto3()

# E clico para colocar o produto no carrinho
    pagina_produto.adicionar_produto_no_carrinho()
    pagina_produto.validar_alerta_inclusao_de_produtos()

# E clico para acessar o carrinho
    pagina_menu_superior.clicar_menu_cart()
    pagina_carrinho.validar_produto1_carrinho()
    pagina_carrinho.validar_produto2_carrinho()
    pagina_carrinho.validar_produto3_carrinho()
    pagina_carrinho.validar_total_dos_produtos1()


# E clico no botao "Place Order"
    pagina_carrinho.clicar_botao_place_order()

# E preencho todos os campos
    pagina_carrinho.preencher_campo_name()
    pagina_carrinho.preencher_campo_country()
    pagina_carrinho.preencher_campo_city()
    pagina_carrinho.preencher_campo_creditcard()
    pagina_carrinho.preencher_campo_month()
    pagina_carrinho.preencher_campo_year()

# Quando clico no botão "Purchase"
    pagina_carrinho.clicar_botao_purchase()

# Entao sistema deve realizar a compra dos produtos com sucesso.
    pagina_carrinho.validar_alerta_de_compra_com_sucesso()
    pagina_carrinho.validar_campo_amount()
    pagina_carrinho.validar_campo_card_number()
    pagina_carrinho.validar_campo_name()
    pagina_carrinho.clicar_botao_ok_da_compra_finalizada()





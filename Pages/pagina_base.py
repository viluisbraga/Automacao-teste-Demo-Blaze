import conftest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class PaginaBase:
    def __init__(self):
        self.driver = conftest.driver
      

    def encontrar_elemento(self, locator):
        self.esperar_elemento_aparecer(locator)
        return self.driver.find_element(*locator)
    
    def encontrar_elementos(self, locator):
        self.esperar_elemento_aparecer(locator)
        return self.driver.find_elements(*locator)
    
    def escrever(self, locator, texto):
       self.esperar_elemento_ficar_visivel(locator)
       self.encontrar_elemento(locator).send_keys(texto)
    
    def clicar(self, locator):
        self.esperar_elemento_ser_clicavel(locator)
        self.encontrar_elemento(locator).click()

    def verifica_se_elemento_existe(self, locator):
        self.esperar_elemento_aparecer(locator)
        assert self.encontrar_elemento(locator).is_displayed(), f"O elemento '{locator}'nao foi encontrado na tela."
     
    def pegar_texto_elemento(self,locator):
        self.esperar_elemento_ficar_visivel(locator)
        return self.encontrar_elemento(locator).text
    
    def pegar_input_elemento(self,locator):
        self.esperar_elemento_aparecer(locator)
        return self.encontrar_elemento(locator).get_attribute("value")
    
    def verifica_texto_do_elemento(self,locator,texto_esperado):
        texto_encontrado = self.pegar_texto_elemento(locator)
        assert texto_encontrado == texto_esperado, f"O texto encontrato foi '{texto_encontrado}'mas era esperado '{texto_esperado}'"

    def verifica_input_do_elemento(self,locator,texto_esperado):
        texto_encontrado = self.pegar_input_elemento(locator)
        assert texto_encontrado == texto_esperado, f"O texto encontrato foi '{texto_encontrado}'mas era esperado '{texto_esperado}'"

    def esperar_elemento_aparecer(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    def esperar_elemento_ficar_visivel(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def esperar_elemento_ser_clicavel(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    
    def esperar_elemento_desaparecer(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            raise AssertionError(f"O elemento com locator {locator} ainda está visível, quando deveria estar invisível.")
        
    def mover_mouse(self,locator):
        elemento = self.esperar_elemento_aparecer(locator)
        ActionChains(self.driver).move_to_element(elemento).perform()
    
    def atualizar_pagina(self):
        self.driver.refresh()

    def esperar_carregamento_da_pagina(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    
    def verifica_checkbox_selecionado(self,locator):
        elemento_encontrado = self.encontrar_elemento(locator)
        assert elemento_encontrado.is_selected(), "O checkbox não foi selecionado conforme deveria."

    def verifica_checkbox_nao_selecionado(self,locator):
        elemento_encontrado = self.encontrar_elemento(locator)
        assert not elemento_encontrado.is_selected(), "O checkbox nao deveria estar selecionado."

    def encontrar_elemento_sem_espera(self, locator):
        return self.driver.find_element(*locator)
    
    def encontrar_elementos_sem_espera(self, locator):
        return self.driver.find_elements(*locator)
    
    def click_triplo(self,locator):
        elemento = self.esperar_elemento_aparecer(locator)
        ActionChains(self.driver).click(elemento).click(elemento).click(elemento).perform()

    def validar_alerta_navegador(self,texto_esperado, timeout=10 ):
        WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        assert alert_text == texto_esperado, f"O texto do alerta foi '{alert_text}', mas o esperado era '{texto_esperado}'"
        alert.accept() 
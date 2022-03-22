from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith ouviu falar de um novo to-do app legal. 
        # Ela veio veio dar uma olhada na homepage.
        self.browser.get('http://localhost:8000')

        # Ela notou que o título da página e o cabeçalho mencionam to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Ela é convidada a inserir uma tarefa diretamente
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
    
        # Ela digita "Comprar penas de pavão" em uma caixa de texto 
        # (o hobby de Edith é fazer iscas de fly-fishing)
        inputbox.send_keys('Buy peacock feathers')
    
        # Quando ela aperta enter, a página é atualizada e agora a página lista 
        # "1: Comprar penas de pavão" como um item em uma lista de tarefas
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

    
        # Ainda há uma caixa de texto convidando-a a adicionar outro item. 
        # Ela escrever "Use as penas de pavão para fazer iscas" (Edith é muito metódica)
        self.fail('Finish the test!')
    
    
        # A página é atualizada novamente e agora mostra os dois itens da lista
    
        # Edith se pergunta se o site lembrará de sua lista. 
        # Então ela vê que o site gerou uma URL única para ela
        # Existe um texto explicativo sobre isso.
    
        # Ela visita essa URL - E sua lista de tarefas continua lá.
    
        # Satisfeita, ela volta a dormir

if __name__ == '__main__':
    unittest.main()
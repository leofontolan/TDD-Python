from selenium import webdriver
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
        self.fail('Finish the test!')

        # Ela é convidada a inserir uma tarefa diretamente


        # Ela digita "Comprar penas de pavão" em uma caixa de texto 
        # (o hobby de Edith é fazer iscas de fly-fishing)


        # Quando ela aperta enter, a página é atualizada e agora a página lista 
        # "1: Comprar penas de pavão" como um item em uma lista de tarefas

        # Ainda há uma caixa de texto convidando-a a adicionar outro item. 
        # Ela escrever "Use as penas de pavão para fazer iscas" (Edith é muito metódica)


        # A página é atualizada novamente e agora mostra os dois itens da lista

        # Edith se pergunta se o site lembrará de sua lista. 
        # Então ela vê que o site gerou uma URL única para ela
        # Existe um texto explicativo sobre isso.

        # Ela visita essa URL - E sua lista de tarefas continua lá.

        # Satisfeita, ela volta a dormir

if __name__ == '__main__':
    unittest.main()
#Devido à existência de capcha no fluxo de cadastro de usuários.  Será necessário fazer o cadastro
#manualmente antes da execução deste teste.  Altere o usuário e senha (linhas 19 e 22) pelo usuário
#e senha que você criou manualmente para poder executar este script com sucesso
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
import time

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://demoqa.com/login")
desired_title = "Understanding ECMAScript 6"
desired_author_name = "Nicholas C. Zakas"
desired_isbn_number = "9781593277574"
driver.implicitly_wait(3)
alert = Alert(driver)


def Login():
    print("Acessando Tools QA...")
    driver.implicitly_wait(1)
    userName = driver.find_element_by_id("userName")
    userName.clear()
    userName.send_keys("testqa")
    password = driver.find_element_by_id("password")
    password.clear()
    password.send_keys("Testqa1!")
    botao = driver.find_element_by_id("login")
    botao.click()
    time.sleep(3) #precisei adicionar este período de espera para que o site possa processar a request e avançar 
    #de forma logada.  Caso contrário, o script avança para próximos steps sem que o usuário tenha logado efetivamente


def search_and_select_book():
    print("Pesquisando pelo livro desejado...")
    searchField = driver.find_element_by_id("searchBox")
    searchField.clear()
    searchField.send_keys(desired_title)
    book = driver.find_element_by_partial_link_text("Understanding")
    book.click()
    driver.implicitly_wait(1)
    isbn = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/label").text
    author = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div[4]/div[2]/label").text
    check_book_entries(isbn,author)
    

def check_book_entries(isbn,author):
    assert desired_isbn_number == isbn, "ISBN não é o desejado"
    assert desired_author_name == author,"autor não é o desejado"
    print("Livro desejado verificado com sucesso...")

    
def go_to_bookstore():
    print("Acessando a loja...")
    driver.implicitly_wait(5)
    time.sleep(3)
    book_store_app = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[6]/div/ul/li[2]")
    driver.execute_script("arguments[0].click();",book_store_app) #foi necessário realizar este workaround pois o banner estava sobrepondo o ponto de click

   
def add_book_to_collection():
    print("Adicionando livro à coleção...")
    add_button = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div[9]/div[2]/button")
    time.sleep(2)
    driver.execute_script("arguments[0].click();",add_button) #foi necessário realizar este workaround pois o banner estava sobrepondo o ponto de click
    time.sleep(2)
    alert.accept()
    

def go_to_profile():
    print("Acessando perfil...")
    profile = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[6]/div/ul/li[3]/span")
    driver.execute_script("arguments[0].click();",profile) #foi necessário realizar este workaround pois o banner estava sobrepondo o ponto de click

    
def check_book_in_profile(desired_title,desired_author_name):
    print("Checando se livro foi adicionado à coleção...")
    table = driver.find_elements_by_class_name("rt-tbody")
    
    for line in table:
        if desired_title in line.text:
            print("foi encontrado livro {} na lista corretamente!".format(desired_title))
            driver.quit
        else:
            print("Livro selecionado não aparece no seu catálogo")
            driver.quit
        
                
Login()
go_to_bookstore()
search_and_select_book()
add_book_to_collection()
go_to_profile()
check_book_in_profile(desired_title,desired_author_name)
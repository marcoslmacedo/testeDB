#Para testes de preenchimento de formulários, eu iniciaria fazendo a verificação 
#da existência de capctha.  No entanto, deixei para o final para poder demonstrar
#a buscar por elementos através de seu id e preenchimento de valores nos campos.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://demoqa.com/login")


def Login():
    print("Acessando Tools QA...")
    time.sleep(1)
    botao = driver.find_element_by_id("newUser")
    botao.click()
    


def Register():
    print("Realizando o registro...")
    time.sleep(1)
    firstName = driver.find_element_by_id("firstname")
    firstName.clear()
    firstName.send_keys("Teste")
    lastName = driver.find_element_by_id("lastname")
    lastName.clear()
    lastName.send_keys("QA DB Server")
    userName = driver.find_element_by_id("userName")
    userName.clear()
    userName.send_keys("testeDB")
    password = driver.find_element_by_id("password")
    password.clear()
    password.send_keys("12345")
   
    assert driver.find_element_by_id("g-recaptcha") == True, "Encontrado Re-captcha saindo do teste"
    
    botaoRegister = driver.find_element_by_id("register")
    botaoRegister.click()

    assert driver.find_element_by_id("name") == True, "Erro no preenchimento dos dados. Verifique o erro apresentado"
    
    
Login()
Register()


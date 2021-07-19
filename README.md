# testeDB
Repositório para arquivos de teste

Estes Scripts foram criados usando Python 3.8.0.  Para poder rodá-los, é necessário ter python 3.x instalado.  É aconselhado fazer uso de um Virtual Environment para rodá-los também.

- Instalar Python (garantir que o python será adicionado ao Path do sistema)
- Criar um Virtual Environment (virtualenv {nome do ambiente} 
- Ativar o Virtual Environment ($ source <venv>/bin/activate no Linux/Mac ou C:\> <venv>\Scripts\activate.bat no windows terminal do windows)
- Instalar os requirements.txt (pip install -r requirements.txt)
- Instalar o webdriver do chrome e disponnibilizá-lo no Path do sistema (https://chromedriver.chromium.org/downloads)  
  
Feitas as configurações, os arquivos do projeto podem ser rodados da seguinte maneira:
  
  > <caminho onde foi clonado o projeto> python Test_A.py (para rodar o script A, por exemplo)

  
Considerações:
  
Testes A e B não puderam ser realizados completamente porque o processo de cadastro apresenta recaptcha.  Caso o usuário e senha fornecidos neste arquivo de exemplo não funcionem mais ao tempo que o teste for realizado, será necessário fazer um cadastro novo e alterar usuário e senha dos script Test_C para que ele possa logar e fazer as ações requeridas

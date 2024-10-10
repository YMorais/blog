ambiente = 'teste' #teste ou produção

if ambiente == 'teste':
    #CONFIG BANCO DE DADOS
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = 'senai'
    DB_NAME = 'blog'

if ambiente == 'producao':
    #CONFIG BANCO DE DADOS
    DB_HOST = 'YasmimBM.mysql.pythonanywhere-services.com'
    DB_USER = 'YasmimBM'
    DB_PASSWORD = '12345678ys'
    DB_NAME = 'YasmimBM$blog'

#CONFIG CHAVE SECRETA DE SESSÃO
SECRET_KEY = 'blog'

#SENHA DO ADM
MASTER_EMAIL = "adm@adm"
MASTER_PASSWORD = "y@sm1m"
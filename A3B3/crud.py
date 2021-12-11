from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from A3B3.models.models import Cadastro, Cliente, Compra, Editora, Livro


from models.models import Atividade, Comentario, Usuario

engine = create_engine("mysql+pymysql://root:@localhost/A3B3", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def create1():
    cliente1 = Cliente(nome='Joe', sobrenome='Jonas', codigo='123')

    cadastro1 = Cadastro(endereco='VGA', telefone='1111-1111', cpf='11.111.111/0001-1', lista_de_livros='livro 1')
    cliente1.cadastro.append(cadastro1) 

    compra1 = Compra()
    cliente1.compra.append(compra1)
 
    session.add(cliente1)
    session.commit()
    
def create2():
    cliente2 = Cliente(nome='Kevin', sobrenome='Jonas', codigo='1234')

    cadastro2 = Cadastro(endereco='VGA', telefone='2222-2222', cpf='22.222.222/0001-2', lista_de_livros='livro 2')
    cliente2.cadastro.append(cadastro2) 

    compra2 = Compra()
    cliente2.compra.append(compra2)
 
    session.add(cliente2)
    session.commit()

def create3():
    
    cliente3 = Cliente(nome='Nick', sobrenome='Jonas', codigo='12345')

    cadastro3 = Cadastro(endereco='VGA', telefone='3333-3333', cpf='33.333.333/0001-3', lista_de_livros='livro 3')
    cliente3.cadastro.append(cadastro3) 

    compra3 = Compra()
    cliente3.compra.append(compra3)
 
    session.add(cliente3)
    session.commit()

def create4():

    editora1 = Editora(nome='LivrosLaLaLa', codigo='123', telefone='4444-4444', gerente='Sophie Turner')

    livro1 = Livro(titulo='Livro1', autor='Taylor Swift', assunto='romance/drama', ISBN='12345-0', quantidade='7')
    editora1.livro.append(livro1) 

    session.add(editora1)
    session.commit()

def create5():

    editora2 = Editora(nome='LivrosLeLeLe', codigo='1234', telefone='5555-5555', gerente='Danielle Jonas')

    livro2 = Livro(titulo='Livro2', autor='Shawn Mendes', assunto='mistério/terror', ISBN='54321-0', quantidade='9')
    editora2.livro.append(livro2) 

    session.add(editora2)
    session.commit()

def create6():

    editora3 = Editora(nome='LivrosLiLiLi', codigo='12345', telefone='6666-6666', gerente='Priyanka Chopra')

    livro3 = Livro(titulo='Livro3', autor='Miley Cyrus', assunto='vingança/drama', ISBN='34567-0', quantidade='16')
    editora3.livro.append(livro3) 

    session.add(editora3)
    session.commit()



from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class Pessoa(BaseModel):
    id: int | None = None
    apelido: str | None = None
    nome: str | None = None
    nascimento: str | None = None
    stack: list | None = None

proximo_id = 5

lista_pessoas = [Pessoa(id = 1, apelido = 'JP', nome = 'João Paulo', nascimento = '12/12/2002', stack = ['python', 'html', 'css']),
                 Pessoa(id = 2, apelido = 'Vini', nome = 'Vinícius', nascimento = '06/08/2004', stack = ['python', 'html', 'css']),
                 Pessoa(id = 3, apelido = 'Tigas', nome = 'Tiago', nascimento = '05/06/2001', stack = ['python', 'html', 'css']),
                 Pessoa(id = 4, apelido = 'Celo', nome = 'Marcelo', nascimento = '01/04/2003', stack = ['python', 'html', 'css'])]

@app.get('/pessoas/{id_pessoa}', status_code = 200)
def obter_pessoas_por_id(id_pessoa: int):
    for pessoa in lista_pessoas:
        if pessoa.id == id_pessoa:
            return pessoa
        
@app.get('/pessoas/{detalhe}', status_code = 200)
def obter_pessoas_por_detalhe(detalhe: str):
    lista_de_retorno = []
    for contador in range(len(lista_pessoas)):
        if contador == 49:
            return lista_de_retorno
        if detalhe in contador.apelido or detalhe in contador.nome or detalhe in contador.nascimento or detalhe in contador.stack:
            lista_de_retorno.append(contador)
    return lista_de_retorno
            
@app.post('/pessoas/', status_code = 201)
def adicionar_pessoa(pessoa: Pessoa):
    if len(pessoa.nascimento) < 10 or len(pessoa.nascimento) > 10:
        raise HTTPException(status_code = 400)
    global proximo_id
    pessoa.id = proximo_id
    proximo_id += 1
    lista_pessoas.append(pessoa)
    return pessoa

@app.get('/contagem-pessoas', status_code = 200)
def contagem_de_pessoas():
    return len(lista_pessoas)
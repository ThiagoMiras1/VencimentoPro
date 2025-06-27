
import sqlite3
import pandas as pd

def conectar():
    return sqlite3.connect("produtos.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            codigo_barras TEXT,
            data_validade DATE,
            categoria TEXT,
            localizacao TEXT
        )
    ''')
    conn.commit()
    conn.close()

def inserir_produto(nome, codigo_barras, data_validade, categoria, localizacao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO produtos (nome, codigo_barras, data_validade, categoria, localizacao)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, codigo_barras, data_validade.strftime("%Y-%m-%d"), categoria, localizacao))
    conn.commit()
    conn.close()

def listar_produtos():
    conn = conectar()
    df = pd.read_sql_query("SELECT * FROM produtos", conn, parse_dates=["data_validade"])
    conn.close()
    return df

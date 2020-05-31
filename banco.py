import sqlite3

class Data:
    def __init__(self):

        self.con = sqlite3.connect('db.sqlite3')
        self.cur = self.con.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        """Cria a tabela caso a mesma não exista."""
        try:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS NomeDaTabela (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                potencia INTEGER,
                ligado BOOLEAN)''')
        except Exception as e:
            print(f'[x] Falha ao criar tabela [x]: {e}')
        else:
            print('[!] Tabela criada com sucesso [!]\n')

    def inserir_registro(self, usuario):
        """Adiciona uma nova linha na tabela.
        :param usuario (tuple): Tupla contendo os dados.
        """
        try:
            self.cur.execute(
                '''INSERT INTO NomeDaTabela VALUES (?, ?, ?, ?)''', usuario)
        except Exception as e:
            print('\n[x] Falha ao inserir registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            # rollback reverte/desfaz a operação.
            self.con.rollback()
        else:
            # commit registra a operação/transação no banco.
            self.con.commit()
            print('\n[!] Registro inserido com sucesso [!]\n')

    def inserir_varios_registros(self, usuarios):
        """Adiciona varias linhas na tabela.
        Desta forma não se faz necessário um laço de
        repetição com vários ``inserts``.
        :param usuarios (list): lista contendo tuplas
        (tuple) com os dados que serão inseridos.
        """
        try:
            self.cur.executemany(
                '''INSERT INTO NomeDaTabela VALUES (?, ?, ?, ?)''', usuarios)
        except Exception as e:
            print('\n[x] Falha ao inserir registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro inserido com sucesso [!]\n')

    def consultar_registro_pela_id(self, rowid):
        """Consulta registro pela id.
        :param rowid (int): id do usuário que se deseja consultar.
        :return: É retornada uma tupla (tuple) com os dados.
        Caso o registro não seja localizado é retornado ``None``.
        """
        return self.cur.execute('''SELECT * FROM NomeDaTabela WHERE rowid=?''', (rowid,)).fetchone()

    def consultar_registros(self, limit=10):
        """Consulta todos os registros da tabela.
        Utilizando ``limit`` para evitar consultas longas de mais.
        :param limit (int): Parâmetro que limita a
        quantidade de registros que serão exibidos.
        :return: É retornada uma lista (list) de tuplas (tuple)
        contendo os dados.
        Se não houver dados é retornada uma lista vazia [``[]``].
        """
        return self.cur.execute('''SELECT * FROM NomeDaTabela LIMIT ?''', (limit,)).fetchall()


    def alterar_registro(self, rowid, nome, potencia, ligado):
        """Alterar uma linha da tabela com base na id.
        A query está configurada para alterar apenas o nome e sexo.
        :param rowid (int): id da linha que se deseja alterar.
        :param nome (str): String com o novo valor.
        :param sexo (str): String com o novo valor.
        """
        try:
            self.cur.execute(
                '''UPDATE NomeDaTabela SET nome=?, potencia=?, ligado=? WHERE rowid=?''',(nome, potencia, ligado, rowid))
        except Exception as e:
            print('\n[x] Falha na alteração do registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro alterado com sucesso [!]\n')

    def remover_registro(self, rowid):
        """Remove uma linha da tabela com base na id da linha.
        :param rowid (id): id da linha que se deseja remover.
        """
        try:
            self.cur.execute(
                f'''DELETE FROM NomeDaTabela WHERE rowid=?''', (rowid,))
        except Exception as e:
            print('\n[x] Falha ao remover registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro removido com sucesso [!]\n')
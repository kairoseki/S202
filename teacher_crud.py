from database import Database

class TeacherCRUD:
    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf):
        query = "CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)
        print(f"Teacher '{name}' criado com sucesso.")

    def read(self, name):
        query = "MATCH (t:Teacher {name: $name}) RETURN t.name AS name, t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        parameters = {"name": name}
        result = self.db.execute_query(query, parameters)
        if result:
            print(f"Teacher encontrado: {result[0]}")
            return result[0]
        else:
            print(f"Teacher '{name}' não encontrado.")
            return None

    def update(self, name, newCpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $newCpf RETURN t"
        parameters = {"name": name, "newCpf": newCpf}
        result = self.db.execute_query(query, parameters)
        if result:
            print(f"CPF do Teacher '{name}' atualizado para {newCpf}.")
        else:
            print(f"Teacher '{name}' não encontrado para atualização.")

    def delete(self, name):
        query = "MATCH (t:Teacher {name: $name}) DETACH DELETE t"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
        print(f"Teacher '{name}' deletado com sucesso.")

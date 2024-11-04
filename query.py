from database import Database

class Query:
    def __init__(self, database):
        self.db = database

    def result(self, data):
        if data:
            for d in data:
                print(d)
        else:
            print("Nenhum resultado encontrado!")

    def find_Renzo(self):  # Questão 1 - a.
        query = "MATCH (t:Teacher {name: $name}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        parameters = {"name": "Renzo"}
        data = self.db.execute_query(query, parameters)
        self.result(data)

    def find_teacher_M(self):  # Questão 1 - b.
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS name, t.cpf AS cpf"
        data = self.db.execute_query(query)
        self.result(data)

    def find_all_cities(self):  # Questão 1 - c.
        query = "MATCH (c:City) RETURN c.name AS name"
        data = self.db.execute_query(query)
        self.result(data)

    def find_number_school(self):  # Questão 1 - d.
        query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name AS name, s.address AS address, s.number AS number"
        data = self.db.execute_query(query)
        self.result(data)

    def find_youngest_date(self):  # Questão 2 - a.
        query = "MATCH (t:Teacher) RETURN MIN(t.ano_nasc) AS youngest, MAX(t.ano_nasc) AS oldest"
        data = self.db.execute_query(query)
        self.result(data)

    def find_AVG(self):  # Questão 2 - b.
        query = "MATCH (c:City) RETURN AVG(c.population) AS avg_population"
        data = self.db.execute_query(query)
        self.result(data)

    def find_CEP(self):  # Questão 2 - c.
        query = "MATCH (c:City) WHERE c.cep = '37540-000' RETURN REPLACE(c.name, 'a', 'A') AS name_replaced"
        data = self.db.execute_query(query)
        self.result(data)

    def teachers_third_letter(self):  # Questão 2 - d.
        query = "MATCH (t:Teacher) RETURN substring(t.name, 2, 1) AS third_letter"
        data = self.db.execute_query(query)
        self.result(data)

    def show_results(self):
    
        self.find_Renzo()
        self.find_teacher_M()
        self.find_all_cities()
        self.find_number_school()
        self.find_youngest_date()
        self.find_AVG()
        self.find_CEP()
        self.teachers_third_letter()
        self.db.close()

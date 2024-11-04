from database import Database
from teacher_crud import TeacherCrud
from query import Query

db = Database("neo4j+s://cb9d3ff0.databases.neo4j.io", "neo4j", "Fg43ez0zAnk_2kaheb5qM6eYk-ZZ_TosyxObJzuKu3Q")

# Questões 1 e 2
query_db = Query(db)
query_db.show_results()

# Questão 3
teacher_db = TeacherCrud(db)
teacher_db.create('Chris Lima', 1956, '189.052.396-66')
print(teacher_db.read("Chris Lima"))
teacher_db.update("Chris Lima", "162.052.777-77")

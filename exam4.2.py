import psycopg2
import config

def executor(method):
    def wrapper(*args, **kwargs):
        args[0].cursor = args[0].connection.cursor()
        rec = method(*args, **kwargs)
        args[0].cursor.close()
    return wrapper


class User:
    def __init__(self,name,surname,birthday,email,address,posts):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.email = email
        self.address = address
        self.posts = posts


class DBConnection:
    def __init__(self):
        self.connection = psycopg2.connect(dbname=config.DBNAME, user=config.USER, password=config.PASSWORD, port=config.PORT)
        self.connection.autocommit = True
        print("Cannot connect to database")

    @executor
    def insert_record(self, name,surname,birth_day,email,address,posts):  # zapis'
        new_record = (name,surname,birth_day,email,address,posts)
        insert_command = "INSERT INTO users(name,surname,birth_day,email,address,posts) VALUES('" + new_record[0] + "','" + \
                         new_record[1] + "','" + new_record[2] + "','" + new_record[3] + "','" + new_record[4] + "','" + new_record[5] +"', '" + new_record[6] + "')"
        print(insert_command)
        self.cursor.execute(insert_command)

    @executor
    def all(self):
        show_command = "SELECT * FROM users;"
        self.cursor.execute(show_command)
        show_record = self.cursor.fetchall()
        return show_record

    @executor
    def get(self,id):
        search_command = "SELECT * FROM users WHERE id = '" + id + "'"
        self.cursor.execute(search_command)
        found_record = self.cursor.fetchall()
        return found_record

    @executor
    def filter(self,column):
        search_command = "SELECT '" + column + "' FROM users"
        self.cursor.execute(search_command)
        found_record = self.cursor.fetchall()
        return found_record


    def __str__(self):
        return self.name

if __name__ == '__main__':
    db = DBConnection()


print(db.all())
print(db.get('3'))
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Создаем базу данных и таблицу при первом запуске приложения

# Подключение к БД и запись данных
def insert_data(Gender, Age, Salary, job_for_a_position, About_me, City, Employment_Schedule, Work_Experience, Tasks_performed, Key_Skills, Education):

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (Gender, Age, Salary, job_for_a_position, About_me, City, Employment_Schedule, Work_Experience, Tasks_performed, Key_Skills, Education) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (Gender, Age, Salary, job_for_a_position,
            About_me, City, Employment_Schedule,
            Work_Experience, Tasks_performed, Key_Skills, Education))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        # Получение данных из формы
        Gender = request.form['Gender']
        Age = request.form['Age']
        Salary = request.form['Salary']
        job_for_a_position = request.form['job_for_a_position']
        About_me = request.form['About_me']
        City = request.form['City']
        Employment_Schedule = request.form['Employment_Schedule']
        Work_Experience = request.form['Work_Experience']
        Tasks_performed = request.form['Tasks_performed']
        Key_Skills = request.form['Key_Skills']
        Education = request.form['Education']

        # Запись данных в БД
        insert_data(Gender, Age, Salary, job_for_a_position,
            About_me, City, Employment_Schedule, Work_Experience, 
            Tasks_performed, Key_Skills, Education)

        return f'"Данные успешно добавлены в БД" {render_template("index.html")}' # Возвращаемся на главную страницу

    return '''
            <form action="/add_user" method="POST">
                <label for="Gender">Пол:</label>
                <input type="text" id="Gender" name="Gender"><br>
                <label for="Age">Возраст:</label>
                <input type="text" id="Age" name="Age"><br>
                <label for="Salary">ЗП:</label>
                <input type="text" id="Salary" name="Salary"><br>
                <label for="job_for_a_position">Должность:</label>
                <input type="text" id="job_for_a_position" name="job_for_a_position"><br>
                <label for="About_me">Обо мне (тезисы):</label>
                <input type="text" id="About_me" name="About_me"><br>
                <label for="City">Город:</label>
                <input type="text" id="City" name="City"><br>
                <label for="Employment_Schedule">График:</label>
                <input type="text" id="Employment_Schedule" name="Employment_Schedule"><br>
                <label for="Work_Experience">Опыт работы:</label>
                <input type="text" id="Work_Experience" name="Work_Experience"><br>
                <label for="Tasks_performed">Выполняемые задачи:</label>
                <input type="text" id="Tasks_performed" name="Tasks_performed"><br>
                <label for="Key_Skills">Ключевые навыки:</label>
                <input type="text" id="Key_Skills" name="Key_Skills"><br>
                <label for="Education">Образование:</label>
                <input type="text" id="Education" name="Education"><br>
                <input type="submit" value="Добавить в БД">
            </form>
'''

if __name__ == '__main__':
    app.run()
# Import modules
from flask.ext.mysql import MySQL
from flask import Flask
from employee import Employee
from flask import jsonify

app = Flask(__name__)
mysql = MySQL()

# Mysql Configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'eval-server'
app.config['MYSQL_DATABASE_DB'] = 'employees'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)

# Setting up endpoint and create responset
@app.route("/")
def result():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("select * from employees where gender = 'M' and birth_date = '1965-02-01' and hire_date > '1990-01-01' order by last_name, first_name;")
        result = cursor.fetchall()
        employees = []
        response = []
        for i in result:
                employee = ""
                emp_no = i[0]
                birth_date = str(i[1])
                first_name = i[2]
                last_name = i[3]
                gender = i[4]
                hire_date = str(i[5])
                employee = Employee(emp_no, birth_date,first_name, last_name, gender, hire_date)
                employees.append(employee)
                response.append(employee.toJSON())
        return jsonify(response)

if __name__ == "__main__":
        app.run(host='0.0.0.0')


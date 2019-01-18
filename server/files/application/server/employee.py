class Employee():

        def __init__(self, emp_no, birth_date, first_name, last_name, gender, hire_date):
                self.emp_no = emp_no
                self.birth_date = birth_date
                self.first_name = first_name
                self.last_name = last_name
                self.gender = gender
                self.hire_date = hire_date

        def toJSON(self):
                return [self.emp_no, self.birth_date, self.first_name, self.last_name, self.gender, self.hire_date]

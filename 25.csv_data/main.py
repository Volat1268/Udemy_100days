import pandas as pd

students_dict = {
	'name': ['John', 'Mary', 'Peter', 'James', 'Mary'],
    'age': [12, 13, 14, 15, 16],
    'gender': ['male', 'female', 'male', 'female', 'male']
}

students = pd.DataFrame(students_dict)
students.to_csv("25.csv_data\students.csv")

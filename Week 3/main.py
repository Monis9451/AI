import csv
import os
import pandas as pd

# Task 1
print("-------------TASK 1-------------")
stdRecords = 'studentRecords.csv'
stdGrades = 'studentGrades.csv'

with open(stdRecords, mode='w', newline='') as file: 
    writer = csv.writer(file)
    writer.writerow(['Student ID', 'Name', 'Age', 'Major', 'Math', 'Physics', 'Chemistry'])
    writer.writerow([601, 'Monis', 19, 'Computer Science', 88, 92, 85])
    writer.writerow([602, 'Bilal', 21, 'Mathematics', 78, 81, 79])
    writer.writerow([603, 'Ali', 22, 'Physics', 90, 87, 91])
with open(stdGrades, mode='w', newline='') as file: 
    writer = csv.writer(file)
    writer.writerow(['Student ID', 'Course', 'Grade'])
    writer.writerow([1, 'CS101', 'A'])
    writer.writerow([2, 'MATH202', 'B'])
    writer.writerow([3, 'PHYS303', 'A'])

print(f'{stdRecords} and {stdGrades} have been created successfully.')


# Task 2
print("-------------TASK 2-------------")
filePath = 'D:\\Work\\Code\\AI\\studentGrades.csv'
fileData = pd.read_csv(filePath)
print(fileData.head())

# Task 3
print("-------------TASK 3-------------")
timetable_data = {'Course': ['CS101', 'MATH202', 'PHYS303', 'BIO101', 'CHEM101'],
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    'Time': ['9:00-11:00', '11:00-13:00', '13:00-15:00', '9:00-11:00', '11:00-13:00']
}

timetable_df = pd.DataFrame(timetable_data)
print("University Weekly Timetable:")
print(timetable_df)

# Task 4
print("-------------TASK 4-------------")
student_records = pd.read_csv(stdRecords)
high_achievers = student_records[
    (student_records['Math'] > 85) & 
    (student_records['Physics'] > 85) & 
    (student_records['Chemistry'] > 85)
]
print("Students scoring above 85 in all subjects:")
print(high_achievers)

# Task 5 
print("-------------TASK 5-------------")
grades_path = 'D:\\Work\\Code\\AI\\student_grades.xlsx'
if not os.path.exists(grades_path):
    stdsGrade = pd.DataFrame({
        'Student ID': [601, 602, 603],
        'Math': [88, 78, 90],
        'Physics': [92, 81, 87],
        'Chemistry': [85, 79, 91],
        'Credits': [3, 3, 3]
    })
    stdsGrade.to_excel(grades_path, index=False)
stdsGrade = pd.read_excel(grades_path)

def GPA(row):
    total_points = (row['Math'] * row['Credits'] + 
                    row['Physics'] * row['Credits'] + 
                    row['Chemistry'] * row['Credits'])
    total_credits = row['Credits'] * 3
    gpa = total_points / total_credits
    return gpa

stdsGrade['GPA'] = stdsGrade.apply(GPA, axis=1)

print("Students' GPA:")
print(stdsGrade[['Student ID', 'GPA']])
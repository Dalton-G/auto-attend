import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://autoattend-347c3-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference('Students')

data = {
    'TP011111':
    {
        'name': 'Lee Wen Han',
        'major': 'CS(AI)',
        'starting_year': 2021,
        'total_attendance': 5,
        'grades': 'A',
        'year': 2,
        'last_attendance_taken' : '2024-01-23 16:30:30',
    },
    'TP012345':
    {
        'name': 'Shi Yu Qi',
        'major': 'Badminton',
        'starting_year': 2019,
        'total_attendance': 9,
        'grades': 'A',
        'year': 4,
        'last_attendance_taken' : '2024-01-23 16:31:30',
    },
    'TP054321':
    {
        'name': 'Elon Musk',
        'major': 'Business',
        'starting_year': 2020,
        'total_attendance': 12,
        'grades': 'B',
        'year': 3,
        'last_attendance_taken' : '2024-01-23 16:32:30',
    },
    'TP063338':
    {
        'name': 'Dalton',
        'major': 'SE',
        'starting_year': 2021,
        'total_attendance': 7,
        'grades': 'A+',
        'year': 3,
        'last_attendance_taken' : '2024-01-23 16:33:30',
    },
    'TP068713':
    {
        'name': 'Suzanne',
        'major': 'CS(AI)',
        'starting_year': 2021,
        'total_attendance': 3,
        'grades': 'A+',
        'year': 2,
        'last_attendance_taken' : '2024-01-20 16:32:35',
    },
    'TP088888':
    {
        'name': 'Karina',
        'major': 'KPOP',
        'starting_year': 2020,
        'total_attendance': 12,
        'grades': 'A+',
        'year': 3,
        'last_attendance_taken' : '2024-01-20 16:32:30',
    },
}

for key, value in data.items():
    ref.child(key).set(value)
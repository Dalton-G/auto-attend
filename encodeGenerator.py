import cv2
import os
import face_recognition
import pickle
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://autoattend-347c3-default-rtdb.asia-southeast1.firebasedatabase.app/',
    'storageBucket': 'autoattend-347c3.appspot.com'
})

folderPathImages = 'Images'
listPathImages = os.listdir(folderPathImages)
imgListImages = []
studentIds = []

for path in listPathImages:
    imgListImages.append(cv2.imread(os.path.join(folderPathImages, path)))
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPathImages}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

def generateEncodings(images):
    encodingsList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodingsList.append(encode)

    return encodingsList

encodingsListKnown = generateEncodings(imgListImages)
encodingsListWithIds = [encodingsListKnown, studentIds]

encodingFile = open('encodingsFile.p', 'wb')
pickle.dump(encodingsListWithIds, encodingFile)
encodingFile.close()
print('Encoding file generated successfully!')
# Automated Attendance Marking System (Auto Attend)

Auto Attend is an automated attendance system that uses facial recognition to efficiently and accurately mark student attendance, reducing workload for teachers and ensuring data integrity through a 1-hour cooldown for each students to prevent attendance farming.

## Features

- Facial recognition to identify individuals
- Automated marking of attendance
- Database integration with Firebase
- Easy to use interface

## Screenshots
![test1](https://github.com/Dalton-G/auto-attend/blob/main/Test/test1.png?raw=true)
![test2](https://github.com/Dalton-G/auto-attend/blob/main/Test/test2.png?raw=true)


## Project Dependencies

- `C++ Compiler`: Please ensure that Visual Studio's C++ Compiler is installed for 'dlib' and 'cmake' libraries to work
- `Python version`: I recommend python ~3.10 to avoid library version mismatch
- `pip`: Ensure pip is installed together with python
- `serviceAccountKey.json`: You must generate your own firebase storage api key and insert it as 'serviceAccountKey.json' in the root directory


## Libraries Needed
You can run `pip install -r "requirements.txt"` to install ALL the dependencies locally.

if you wish to install these libraries globally, please run the following commands in your terminal (in this order):

```bash
pip install cmake
pip install dlib
pip install opencv-python
pip install face-recognition
pip install cvzone
pip install firebase-admin
pip install numpy
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.


## License

[MIT](https://github.com/Dalton-G/auto-attend/blob/main/LICENSE)

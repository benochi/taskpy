# TaskPy - Simple Daily Task Tracker

TaskPy is a lightweight Python desktop application using **Tkinter** for a GUI and **SQLite** as a local database. It allows you to track daily tasks, mark them as completed, and maintain a streak of productivity.

## 🚀 Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/benochi/taskpy.git
cd taskpy
```

### 2 python -m venv venv
```sh
python -m venv venv
```

### 3 Activate the Virtual Environment


#### Windows (Git Bash / Command Prompt)
```sh
source venv/Scripts/activate 
venv\Scripts\activate
```
#### Mac/Linux
```sh
source venv/bin/activate
```
### 4 Install Dependencies

```sh
pip install -r requirements.txt
```

### 5. Run the Application
```sh
python app.py
```

### 🛠 Features
✔ Add Tasks – Enter new tasks to track.
✔ Mark Completed – Click to mark tasks as done.
✔ Delete Tasks – Remove completed or unnecessary tasks.
✔ Auto-Saving – Tasks are stored in an SQLite database.
✔ Task Numbering – Tasks are displayed with a visible order, but database IDs remain hidden.

### 🏗 Structure
taskpy/
│── database.py      # SQLite database logic
│── app.py           # Tkinter GUI application
│── requirements.txt # Required dependencies
│── .gitignore       # Ignore virtual environment and cache files
│── README.md        # Project documentation

### 📝 Notes
Task numbering is visual only and does not modify database IDs.
The app runs locally without needing an internet connection.

## 🔧 Creating an Executable (.exe)

To generate a standalone `.exe` file, install **PyInstaller**:

```sh
pip install pyinstaller
```
Then run the following command:
```sh
pyinstaller --onefile --windowed app.py
```
--onefile → Bundles everything into a single .exe
--windowed → Hides the terminal window when running the app
The .exe file will be created inside the dist/ directory.
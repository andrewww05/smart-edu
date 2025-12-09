# SmartEdu

## Description
SmartEdu is a comprehensive university web system designed to enhance the educational experience for students and faculty. This MVP (Minimum Viable Product) focuses on providing essential tools for academic scheduling, campus orientation, and information accessibility.

## MVP Features
- **Student Timetable**: A dynamic and filterable schedule view allowing students and teachers to easily find classes by academic year, semester, week type, and group/teacher.
- **Campus Map**: Integrated Google Maps view to help locate university buildings (e.g., vul. Storozhynetska, 101).
- **FAQ Page**: A dedicated section for answering common questions regarding registration, scheduling, and support.
- **Authentication**: Secure user registration and login functionality.

## Installation and Launch

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd smart-edu
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Linux/macOS
   python3 -m venv .venv
   source .venv/bin/activate
   
   # Windows
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **(Optional) Populate sample data:**
   ```bash
   python scripts/fill_schedule_data.py
   ```

### Launch

Run the development server:
```bash
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/`.

## Team Authors
- andrewww05
- kolosochok
- Oleksiy Gakman
- Tetiana Gonchar
- Khrystyna Fedik
- Anna Protsenko 

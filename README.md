# Grade_Extract_Feature
Grade Sheet Extractor
A full-stack web application designed to automate the tedious process of checking academic grade sheets. This tool allows users to upload multiple grade sheet files (.txt format), enter a registration number, and instantly receive a consolidated view of their grades and a calculated Semester Grade Point Average (SGPA).

Live Application Link: [(http://ocdalpha.pythonanywhere.com/)]

The Problem
For many students, the end-of-semester process involves manually searching through multiple grade sheet documents, finding their results one by one, and then performing manual calculations to determine their SGPA. This process is repetitive, inefficient, and susceptible to human error. This project was born out of the need to solve this exact problem.

Features
Multi-File Upload: Users can upload all their semester grade sheets at once.

Dynamic Data Extraction: The Python backend parses the text files to find and extract subject details, credits, marks, and grades for a specific registration number.

Consolidated Results: Displays all extracted grades in a clean, easy-to-read table.

Optional SGPA Calculation: An interactive "Calculate SGPA" button reveals the final SGPA along with a performance indicator.

Modern UI: A clean, responsive user interface built with Bootstrap, featuring a dynamic file list that reads subject titles directly from uploaded files.

Robust Error Handling: The application validates user input to ensure a registration number is entered and that all uploaded files are of the correct .txt format.

Tech Stack
Backend: Python, Flask

Frontend: HTML, CSS, JavaScript, Bootstrap 5

Deployment: PythonAnywhere

Project Evolution & Challenges
This project was developed iteratively, starting as a simple command-line script and evolving into a full-fledged web application. This journey involved several key technical challenges and learning opportunities:

From Script to Web App: The initial Python script for data parsing was refactored and integrated into a Flask backend to handle web requests, file uploads, and server-side logic.

Search Algorithm Refinement: A significant bug was identified where the search logic used a partial match (startswith()), leading to incorrect data being pulled for similar registration numbers. This was fixed by implementing a more robust exact-match comparison.

Frontend Interactivity: Advanced JavaScript using the FileReader API was implemented to read file contents directly in the browser, providing users with immediate feedback on the subjects they had uploaded.

Static Asset Management: A key learning experience involved correctly structuring the project with static and templates folders and using Flask's url_for() helper to link CSS and JavaScript files, resolving 404 errors encountered after refactoring.

Local Setup and Installation
To run this project on your local machine, follow these steps:

Clone the repository:

git clone https://github.com/YourUserName/Grade_Extract_Feature.git
cd Grade_Extract_Feature

Create and activate a virtual environment:

# Create the environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate

Install the required dependencies:

pip install -r requirements.txt

Run the Flask application:

python app.py

Open your web browser and navigate to http://127.0.0.1:5000 to use the application.
import os
from flask import Flask, render_template, request


def calculate_sgpa(results_data, grade_points):
    """Calculates the SGPA from a list of subjects."""
    total_credits_attempted = 0
    total_credit_points = 0
    ignored_grades = {'I', 'AB', 'DT', 'MP'}

    for subject in results_data:
        grade = subject['Grade']
        credits = subject['Credits']
        
        if grade in ignored_grades:
            continue

        total_credits_attempted += credits
        
        if grade in grade_points:
            total_credit_points += credits * grade_points[grade]
            
    if total_credits_attempted == 0:
        return 0.0
        
    return total_credit_points / total_credits_attempted


def extract_student_data(reg_no, files):
    
    all_results = []
    
    for file in files:
        
        content = file.stream.read().decode("utf-8")
        lines = content.splitlines()
        
        filename = file.filename
        subject_title = ""
        subject_credit = 0.0

        for line in lines:
            if "Subject Title" in line:
                subject_title = line.split(":", 1)[1].strip()
            if "Subject Credit" in line:
                try:
                    subject_credit = float(line.split(":", 1)[1].strip())
                except ValueError:
                    subject_credit = 0.0

        for line in lines:
            parts = line.split()
            if parts and parts[0] == reg_no:
                if len(parts) >= 5:
                    student_data = {
                        "Code": os.path.splitext(filename)[0],
                        "Subject": subject_title,
                        "Credits": subject_credit,
                        "Internal": parts[1],
                        "End-Sem": parts[2],
                        "Total": parts[3],
                        "Grade": parts[4]
                    }
                    all_results.append(student_data)
                    break 
    
    return all_results


#  Flask 

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    regno = request.form['regno']
    files = request.files.getlist('grade_files')

    #  Error Handling
    # Check if regno or files are missing
    if not regno or not files[0].filename:
        error_message = "Please enter a registration number and select your grade sheet files."
        return render_template('results.html', error=error_message)

    # Check if all uploaded files are .txt files
    for file in files:
        if not file.filename.endswith('.txt'):
            error_message = f"Invalid file type: '{file.filename}'. Please upload only .txt files."
            return render_template('results.html', error=error_message)

    #  Grade to Point Mapping
    grade_points_map = {
        'S': 10, 'A': 9, 'B': 8, 'C': 7,
        'D': 6, 'E': 5, 'F': 0
    }

    # extraction and calculation functions
    final_data = extract_student_data(regno, files)
    sgpa = calculate_sgpa(final_data, grade_points_map)

    #  results page with the final data
    return render_template('results.html', 
                           data=final_data, 
                           sgpa=f"{sgpa:.2f}", 
                           regno=regno)

if __name__ == '__main__':
    app.run(debug=True)
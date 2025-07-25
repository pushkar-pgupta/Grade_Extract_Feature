import os
import argparse
from tabulate import tabulate

def calculate_sgpa(results_data, grade_points):
    """Calculates the SGPA from a list of subjects."""
    total_credits_attempted = 0
    total_credit_points = 0
    

    ignored_grades = {'I', 'AB', 'DT', 'MP'}

    for subject in results_data:
        grade = subject['Grade']
        credits = subject['Credits']
        
        if grade in ignored_grades:
            continue # Skip this subject

        total_credits_attempted += credits
        
        if grade in grade_points:
            total_credit_points += credits * grade_points[grade]
            
    if total_credits_attempted == 0:
        return 0.0
        
    return total_credit_points / total_credits_attempted


def extract_student_data(reg_no, folder_path):
    
    all_results = []
    
    grade_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

    for filename in grade_files:
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as f:
            lines = f.readlines()

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract student grades and calculate SGPA.")
    parser.add_argument("--regno", required=True, help="Student's registration number.")
    parser.add_argument("--folder", required=True, help="Path to the folder containing grade sheets.")
    args = parser.parse_args()
    
    # --- Grade to Point Mapping ---
    grade_points_map = {
        'S': 10, 'A': 9, 'B': 8, 'C': 7,
        'D': 6, 'E': 5, 'F': 0
    }

    final_data = extract_student_data(args.regno, args.folder)

    if final_data:
        print(f"\nShowing results for Registration Number: {args.regno}\n")
        print(tabulate(final_data, headers="keys", tablefmt="grid"))
        
        # Calculate and Display SGPA
        sgpa = calculate_sgpa(final_data, grade_points_map)
        print(f"\nCalculated SGPA: {sgpa:.2f}") # Formats SGPA to 2 decimal places

    else:
        print(f"No results found for registration number {args.regno} in the specified folder.")
# Grade Sheet Extractor

A Flask web application to automate the extraction and calculation of academic grades from `.txt` files.

**Live Application:** [http://ocdalpha.pythonanywhere.com/]

## Key Features

* **Multi-File Upload:** Process multiple grade sheets at once.
* **Automated Data Parsing:** Extracts subject details, marks, and grades for a specific registration number.
* **Instant SGPA Calculation:** On-demand calculation and display of the Semester Grade Point Average.
* **Interactive UI:** Built with Bootstrap, providing a clean user experience and dynamic feedback on file uploads.
* **Server-Side Validation:** Ensures correct file types and presence of required inputs.

## Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS, JavaScript, Bootstrap 5
* **Deployment:** PythonAnywhere

## Overview

This project was built to solve the common, repetitive task of manually checking grade sheets. The application's core is a Python script that parses text-based grade files to find data corresponding to a user-provided registration number. This logic is served through a Flask backend. The development process involved building the UI, adding client-side interactivity with JavaScript (like reading file contents in the browser), and deploying the final application as a live web service.

## Development Challenges & Key Fixes

The development process involved overcoming several key technical challenges:

* **Incorrect Data Matching:** A critical lapse was identified in the initial search logic. The script used a partial `startswith()` match, which caused it to pull data for incorrect registration numbers (e.g., a search for `20230001` would incorrectly match `202300001`). This was resolved by implementing a strict, exact-match comparison on the registration number.
* **Template Rendering Errors:** While working with Flask's Jinja2 template engine, two main errors occurred:
    1.  An `UndefinedError` was triggered when trying to access a dictionary key containing a hyphen (e.g., `End-Sem`) with dot notation. The fix was to use bracket notation (`row['End-Sem']`).
    2.  A `TemplateSyntaxError` occurred due to an unclosed `{% if %}` block, which was resolved by ensuring all conditional blocks were properly terminated with `{% endif %}`.
* **Static File Loading Failure:** After refactoring the CSS and JavaScript into separate files, the browser failed to load them, resulting in a loss of all styling and interactivity. This was traced back to an incorrect folder structure and fixed by placing the assets in the `static/` directory and using Flask's `url_for()` helper to generate the correct paths.

## Local Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUserName/Grade_Extract_Feature.git](https://github.com/YourUserName/Grade_Extract_Feature.git)
    cd Grade_Extract_Feature
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows: .\venv\Scripts\activate
    # On macOS/Linux: source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python app.py
    ```
    The application will be available at `http://127.0.0.1:5000`.

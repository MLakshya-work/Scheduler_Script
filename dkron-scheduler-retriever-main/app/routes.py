from flask import Blueprint, render_template
import json
import os

# Create a Blueprint for routes
routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    """
    This route renders the main table displaying job data from dkron_jobs.json.
    """
    # Path to the JSON file in the app directory
    json_file_path = os.path.join(os.getcwd(), 'app', 'dkron_jobs.json')

    try:
        # Load the JSON file
        with open(json_file_path, 'r') as file:
            job_data = json.load(file)
    except FileNotFoundError:
        job_data = []
        print(f"Error: File not found at {json_file_path}")
    except json.JSONDecodeError as e:
        job_data = []
        print(f"Error decoding JSON: {e}")

    # Render the jobs.html template with the job data
    return render_template('jobs.html', job_data=job_data)

from flask import Blueprint, render_template, redirect, url_for
import json
import os

# Create a Blueprint for routes
routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    """
    This route renders the main table displaying job data from dkron_jobs.json.
    """
    # Path to the JSON file in the app directory
    json_file_path = os.path.join(os.getcwd(), 'app', 'dkron_jobs.json')

    try:
        # Load the JSON file
        with open(json_file_path, 'r') as file:
            job_data = json.load(file)
    except FileNotFoundError:
        job_data = []
        print(f"Error: File not found at {json_file_path}")
    except json.JSONDecodeError as e:
        job_data = []
        print(f"Error decoding JSON: {e}")

    # Render the jobs.html template with the job data
    return render_template('jobs.html', job_data=job_data)


@routes.route('/reload_data', methods=['GET'])
def reload_data():
    """
    This route handles reloading the job data.
    """
    # Path to the JSON file in the app directory
    json_file_path = os.path.join(os.getcwd(), 'app', 'dkron_jobs.json')

    try:
        # Load the JSON file again to simulate reloading the data
        with open(json_file_path, 'r') as file:
            job_data = json.load(file)
    except FileNotFoundError:
        job_data = []
        print(f"Error: File not found at {json_file_path}")
    except json.JSONDecodeError as e:
        job_data = []
        print(f"Error decoding JSON: {e}")

    # Redirect back to the index page
    return redirect(url_for('routes.index'))


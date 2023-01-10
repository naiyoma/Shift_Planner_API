
## Shift Management API
This API allows for the creation and management of shifts for a given organization. The API provides endpoints for creating and viewing shifts, as well as endpoints for user registration and management.

### Running the API locally
1. Clone the repository: `git clone https://github.com/<your-username>/shift-management-api.git`

2. Navigate into the project directory: `cd shift-management-api`

3. Create a virtual environment: `python -m venv env`

4. Activate the virtual environment: `source env/bin/activate`

5. Install the dependencies: `pip install -r requirements.txt`

6. Apply the migrations: `python3 manage.py migrate`

7. Run the development server: `python3 manage.py runserver`

8. The API will now be available at `http://127.0.0.1:8000/`


### Running the tests
1. Make sure you have the dependencies installed: `pip install -r requirements.txt`

2. Run the tests: `python3 manage.py test users`


### Endpoints
1. `/createuser/`: endpoint for creating new users.
2. `/create_shift/`: endpoint for creating new shifts.
3. `/shifts/`: endpoint for displaying all shifts.
4. `/shifts/<user_id>/`: endpoint for filtering shifts by user ID.
5. `/listusers/`: endpoint for displaying all users.

### Deployment
The API is currently deployed on PythonAnywhere, and can be accessed at (`https://naiyoma.pythonanywhere.com/api/`)

### DOCS
(`https://naiyoma.pythonanywhere.com/api/docs/`)



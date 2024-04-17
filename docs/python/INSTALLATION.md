- [java](../INSTALLATION.md)
- [python](/INSTALLATION.md)

# Installation Guidelines

Follow these steps to install and set up RideShareX on your local machine:

## Prerequisites
- Python 3.8 or higher installed on your system.
- pip for managing python packages.

## Clone the Repository
If you have not already cloned the RideShareX repository:
```bash
git clone https://github.com/kinyarasam/RideShareX.git
```

Navigate to the python project.
```bash
cd RideShareX/python
```
Install the required python packages
```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Environment Setup
Copy the `.env.example` file to `.env` and update it with your database and other environment specific settings:
```bash
cp .env.example .env
```

## Database Configuration.
Ensure MySQL or PostgreSQL database is set up and running. Updatet the database connectio details in your `.env` file accordingly.

## Run the Application
Run the application using the following command:
```
SESSION_NAME=_my_session_cookie AUTH_TYPE=session_auth python3 -m api.v1.app
```

## Access the Application
Open the web browser and navigate to [http://localhost:8080](http://localhost:5000) to access RideShareX.

## Sample User Credentials
- Username: *user@example.com*
- password: *password123*

**Note**: Make sure to change the default credentials and set up appropriate security measures for deployments.

For more detailed information on configuration options and advanced usage, refer to our [full documentation](../../README.md).

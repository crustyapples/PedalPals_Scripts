# PedalPals_Scripts
 Testing Scripts for PedalPals key features. 

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- Python (version 3.9.7)
- pip (Python package manager)

## Setting Up a Virtual Environment

It's a good practice to work in a virtual environment to keep project dependencies isolated. To set up a virtual environment, follow these steps:

1. In the root directory of the project, create a new virtual environment:

    ```bash
    python -m venv env
    ```

    This will create a new directory called `env

2. Activate the virtual environment:

    ```bash
    source env/bin/activate
    ```

    This will change your terminal prompt to indicate that you're working in the virtual environment.

3. Install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    This will install all the dependencies listed in the `requirements.txt` file.

4. Setup Config File by creating a config.py that contains the following:

    ```python
    # config.py
    GOOGLE_MAPS_API = 'YOUR_API_KEY'
    EMAIL = 'EMAIL USED FOR ONEMAPS ACCOUNT'
    PASSWORD = 'YOUR_PASSWORD>'
    ```
    Note that you will need to register for the OneMap API

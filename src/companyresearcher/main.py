#!/usr/bin/env python
import sys
import warnings
import os
import certifi
from datetime import datetime

from crew import Companyresearcher
os.environ["SSL_CERT_FILE"] = certifi.where()

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run(user_input: str):
    """
    Run the crew.
    """
    result = ''
    inputs = {
        'company_name': user_input.strip(),
        'current_year': str(datetime.now().year)
    }
    
    try:
        result = Companyresearcher().crew().kickoff(inputs=inputs)
    except Exception as e:
        result = f"An error occurred while running the crew: {e}"
    
    return result

# run()
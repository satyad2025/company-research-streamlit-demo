import requests
import os
import certifi
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()

os.environ["SSL_CERT_FILE"] = certifi.where()
search_tool = SerperDevTool()

def jobsearch(company_name: str):
        # Use an API or web scraper here
        # Example with hypothetical API
        # response = requests.get(f"https://www.google.com/search?q={company_name}%2B+jobs+openings+%2B+India")
        # response = requests.get("https://www.linkedin.com/company/latentbridge/jobs/", verify=certifi.where())
        q= f"site:linkedin.com/company/{company_name.lower()}/jobs"
        result = search_tool.run(query = q)

        ''' if response.status_code == 200:
            jobs = response.json()
            return "\n".join([f"{job['title']} - {job['location']}" for job in jobs])
        else:
            return "Failed to fetch jobs."
        '''

      #  if result.len() > 0:
        results = result.get("organic",[])
        for result in results:
                print(f"Title: {result.get('title')}")
                print(f"Link: {result.get('link')}")
                print(f"Snippet: {result.get('snippet')}\n")

    
      #  else:
      #     print("No results found")

        
jobsearch("latentbridge")
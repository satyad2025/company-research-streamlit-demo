from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

# Initialize the Serper API tool
search_tool = SerperDevTool()

def search_linkedin_jobs(company_name):
    # Build the query to search jobs on LinkedIn for a company
    query = f"site:linkedin.com/company/{company_name.lower()}/jobs"
    
    # Set the payload for the API call
    payload = {
        "q": query
    }

    # Fetch results from SerperAPI
    try:
        response = search_tool.run(payload)
        return response
    except Exception as e:
        print(f"Error while searching LinkedIn jobs: {e}")
        return []

search_linkedin_jobs("latentbridge")
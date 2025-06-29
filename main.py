import os
from dotenv import load_dotenv
from github.github_api import GitHubAPI
from utils.utils import guardar_json_repositorios

# Load environment variables from .env file
load_dotenv()

def main():
    try:
        # Initialize GitHub API client
        github = GitHubAPI()
        username = "mtsprznto"  # Your GitHub username
        
        print(f"Fetching all repositories for {username}...")
        repositories = github.get_all_user_repositories(username)
        
        if not repositories:
            print("No repositories found.")
            return
            
        print(f"\nFound {len(repositories)} repositories:")
        print("-" * 80)
        
        for repo in sorted(repositories, key=lambda x: x['updated_at'], reverse=True):
            print(f"Name: {repo['name']}")
            print(f"Description: {repo.get('description', 'No description')}")
            print(f"Language: {repo.get('language', 'Not specified')}")
            print(f"Stars: {repo['stargazers_count']} | Forks: {repo['forks_count']} | Updated: {repo['updated_at'].split('T')[0]}")
            print(f"URL: {repo['html_url']}")
            print("-" * 80)
            
        # Save repositories to a JSON file for further processing
        guardar_json_repositorios(repositories)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
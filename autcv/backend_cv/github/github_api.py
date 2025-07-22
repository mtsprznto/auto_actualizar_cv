import os
from typing import Dict, Any
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class GitHubAPI:
    BASE_URL = "https://api.github.com"
    
    def __init__(self):
        self.token = os.getenv('API_KEY_GITHUB')
        if not self.token:
            raise ValueError("GitHub token not found in environment variables")
        
        self.headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
    
    def get_repository_info(self, owner: str, repo: str) -> Dict[str, Any]:
        """Get information about a specific repository"""
        url = f"{self.BASE_URL}/repos/{owner}/{repo}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_user_repositories(self, username: str) -> list:
        """Get all repositories for a user"""
        url = f"{self.BASE_URL}/users/{username}/repos"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_all_user_repositories(self, username: str) -> list:
        """Get all repositories for a user, handling pagination"""
        all_repos = []
        page = 1
        per_page = 100  # Maximum allowed by GitHub API
    
        while True:
            url = f"{self.BASE_URL}/users/{username}/repos?page={page}&per_page={per_page}&sort=updated"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            repos = response.json()
            
            if not repos:  # No more repositories
                break
                
            all_repos.extend(repos)
            page += 1
            
            # If we got fewer repos than requested, we've reached the last page
            if len(repos) < per_page:
                break
            
           
            
        return all_repos

    def obtener_readme_raw(self, usuario: str, repositorio: str) -> str:
        """Obtiene el README raw de un repositorio"""
        url = f"https://raw.githubusercontent.com/{usuario}/{repositorio}/main/README.md"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"README no encontrado: {response.status_code}")
    
    def obtener_about_repo(self, usuario: str, repositorio: str) -> dict:
        url = f"{self.BASE_URL}/repos/{usuario}/{repositorio}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        return {
            "nombre": data.get("name"),
            "descripcion": data.get("description"),
            "sitio_web": data.get("homepage"),
            "topics": data.get("topics", []),
            "url": data.get("html_url"),
            "lenguaje": data.get("language"),
            "actualizado": data.get("updated_at")
        }

    def get_languages_for_repo(self, owner: str, repo: str) -> dict:
        """Devuelve un diccionario con los lenguajes y su tamaño en bytes"""
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/languages"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
        
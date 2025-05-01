import requests
import pandas as pd

class DadosRepositorios:
    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = 'YOUR_GITHUB_ACCESS_TOKEN'
        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'X-GitHub-Api-Version': '2022-11-28'
        }
        self.repo_nomes = []
        self.repo_languages = []
    
    def __fetch_repositorios(self):
        repos_list = []
        url = f'{self.api_base_url}/users/{self.owner}/repos'
        page_num = 1
        per_page = 100

        while True:
            try: 
                print(f'📄 Buscando página {page_num} de repositórios para {self.owner}')
                response = requests.get(url, headers=self.headers, params={'page': page_num, 'per_page': per_page})
                response_data = response.json()

                if len(response_data) == 0:
                    print(f'🚫 Fim dos dados na página {page_num}')
                    break

                repos_list.extend(response_data)
                page_num += 1
            except Exception as e:
                print(f'❌ Erro na página {page_num}: {e}')
                break

        self.__update_nomes_repos(repos_list)
        self.__update_nomes_linguagens(repos_list)
        return repos_list

    
    def __update_nomes_repos(self, repos_list):
        for repo in repos_list:
            self.repo_nomes.append(repo.get('name'))
    
    def __update_nomes_linguagens(self, repos_list):
        for repo in repos_list:
            self.repo_languages.append(repo.get('language'))
    
    def cria_df_linguagens(self):
        self.__fetch_repositorios()

        data = {
            'owner': self.owner,
            'repository_name': self.repo_nomes,
            'language': self.repo_languages
        }

        df = pd.DataFrame(data)
        return df


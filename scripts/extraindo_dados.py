from dados_repos import DadosRepositorios

companies = [
    'amzn',
    'microsoft',
    'Netflix',
    'facebook',
    'google'
]

for company in companies:
    print(f'\n🔍 Buscando repositórios de: {company}')
    company_repo = DadosRepositorios(company)
    df = company_repo.cria_df_linguagens()
    df.to_csv(f'./dados/linguagens_{company_repo.owner}.csv', index=False)
    print(f'✅ {len(df)} repositórios encontrados para {company}')
    print(df[['repository_name', 'language']].head())  
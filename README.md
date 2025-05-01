# 🔍 GitHub Repository Data Extraction

This project extracts, transforms, and saves data about repositories from major tech companies using the GitHub API. It processes data for companies like Amazon, Microsoft, Netflix, Facebook, and Google, generating CSV files for further analysis.

## 📁 Project Structure

- **`data/`**: Stores processed data:
  - ✅ `languages_amzn.csv`: Repository data for Amazon.
  - ✅ `languages_facebook.csv`: Repository data for Facebook.
  - ✅ `languages_google.csv`: Repository data for Google.
  - ✅ `languages_microsoft.csv`: Repository data for Microsoft.
  - ✅ `languages_Netflix.csv`: Repository data for Netflix.
- **`notebook/`**: 📓 Jupyter notebooks for data exploration and validation:
  - 📄 `languages_repos.ipynb`: Notebook for analyzing extracted data.
- **`scripts/`**: Contains Python scripts for data extraction and processing:
  - 🛠️ `extraindo_dados.py`: Script for extracting repository data.
  - 🛠️ `enviando_dados.py`: Script for uploading data to your GitHub Repository.
  - 🧩 `dados_repos.py`: Module for handling repository data.
  - 🧩 `manipula_repos.py`: Module for managing GitHub repositories.

## 🔄 Data Extraction Process

### Extract:
- 📥 Fetches repository data for each company using the `DadosRepositorios` class.

### Transform:
- 🔧 Processes the data to extract repository names and programming languages.
- 🔗 Organizes the data into a structured DataFrame.

### Load:
- 💾 Saves the processed data into CSV files in the `data/` directory.

## ✨ Key Features

- 📝 **Data Organization**: Extracts and organizes repository data into structured CSV files.
- 🔗 **Language Analysis**: Provides insights into the programming languages used by each company.
- 📈 **Scalability**: Easily extendable to include additional companies or data points.

## 📥 How to Download the Project

1. Clone the repository using Git:
```bash
   git clone https://github.com/vitorlinsbinski/python-requests-etl.git
```

2. Navigate to the project directory:
```bash
    cd python-requests-etl
```

## 🛠️ Setup
To ensure a clean and isolated environment for running the project, follow these steps:

1. Create a virtual environment:
```bash
    python3 -m venv .venv
```

2. **Activate the virtual environment**:

   - **On Linux/MacOS**:
     ```bash
     source .venv/bin/activate
     ```

   - **On Windows**:
     ```bash
     .venv\Scripts\activate
     ```

3. Install dependencies:
```bash
    pip install -r requirements.txt
```

## 🚀 Usage

1. 🔑 Replace your GitHub Access Token in the `access_token` attribute of the `DadosRepositorios` and `ManipulaRepositorios` classes.
"""
Observations:
- Before running the script, ensure to replace the placeholder values for the username, repository name, and company names with actual values.
- The script interacts with GitHub's API, so make sure you have the necessary permissions and API tokens configured.
"""
2. ▶️ Run the extract script:
```bash
   python scripts/extraindo_dados.py
```
3. ▶️ Run the upload script:
```bash
   python scripts/enviando_dados.py
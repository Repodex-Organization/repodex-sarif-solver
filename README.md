# Repodex SARIF Solver

This GitHub Action processes the SARIF results from a CodeQL analysis and communicates with the Repodex backend service to generate solutions for found issues.

## Prerequisites

1. **API Key from Repodex**: Before you can use this action, you'll need to have an API key from Repodex. You can obtain this key by signing up on the Repodex platform.

2. **GitHub Secret**: After obtaining the API key, store it as a secret in your GitHub repository to keep it confidential. Name the secret `REPODEX_API_KEY`.

   To add a new secret:
   - Navigate to your GitHub repository.
   - Click on the "Settings" tab.
   - In the left sidebar, click on "Secrets".
   - Click on "New repository secret".
   - Enter `REPODEX_API_KEY` as the name and paste your Repodex API key as the value.
   - Click on "Add secret".

3. **Determine SARIF File Paths**: After your CodeQL Analysis action runs, identify the paths to the generated SARIF files. If you don't specify a path, the action defaults to the typical path used by CodeQL: `.github/workflows/codeql-analysis/results.sarif`. You can specify multiple paths by separating them with commas.


## Usage

```yaml
name: Repodex SARIF Solver

on:
  push:
    branches:
      - main

jobs:
  analyze-and-solve:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Run CodeQL Analysis
      uses: github/codeql-action/analyze@v1
      with:
        languages: 'autodetect'

    - name: Repodex SARIF Solver
      uses: Repodex-Organization/repodex-sarif-solver@v1
      with:
        api-key: ${{ secrets.REPODEX_API_KEY }}
        sarif-paths: 'path1.sarif,path2.sarif'  # Replace with your actual SARIF file paths or omit to use the default path

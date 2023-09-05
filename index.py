import sys
import os
import requests
import json

def main():
    api_key = os.environ['REPODEX_API_KEY']
    sarif_file_paths = os.environ['SARIF_FILE_PATHS'].split(',')

    for sarif_file_path in sarif_file_paths:
        with open(sarif_file_path.strip(), 'r') as f:
            sarif_data = f.read()

        response = requests.post('https://backend.repodex.ai/api/solve', data={
            'sarif': sarif_data,
            'apiKey': api_key
        })

        response_data = response.json()

        if not response_data['success']:
            sys.exit(f'Failed to generate solutions for SARIF file: {sarif_file_path}')

    print('::set-output name=result::Solutions generated successfully for all SARIF files.')

if __name__ == '__main__':
    main()

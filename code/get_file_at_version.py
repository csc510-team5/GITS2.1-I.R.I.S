from typing import Dict
import requests
import json


def get_file_at_version(path: str, sha: str, token: str) -> Dict[str, str]:
    instance = 'https://api.github.com'
    try:
        url = f'{instance}/repos/jwgerlach00/ml_protein_degradation_multitask/contents/{path}?ref={sha}'
        headers = {'Authorization': f'Bearer {token}'}
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 404:
            return ''
        
        contents = response.text
        return json.loads(content)
    
    except Exception as error:
        print(error)
        
# token = 'YOUR-TOKEN-HERE'
# sha = '470ae25'
# path = 'package/src/linkerology_multitask/dataset_creation/LinkerologySampler.py'
# get_file_at_version(path, sha, token)

#User\scripts\python3
from git import Repo
import re,signal,sys
import json

REPO_DIR=".\skale\skale-manager"

def handler_signal(signal, frame):
    print("\n\n [!] Out .........\n")
    sys.exit(1)

signal.signal(signal.SIGINT,handler_signal)

def extract(url):
    repo = Repo(url)
    commits = list(repo.iter_commits())
    text=[]
    for commit in commits:
        text.append(commit)
    return text

def transform(commits):
    leaks=[] 
    i = 0
    claves='(pasword|credentials|key)'
    while i < len(commits):
        if re.findall(claves,commits[i].message,re.I) != []:
            leaks.append(commits[i])
        i+=1
    return leaks
   
    
def load(leaks):
    """
    construir un diccionario de leaks y pasarlos a json
    """
    j_dict = {'leaks': []}
    for c in leaks:
        c_dict = {
            'author': c.author.name,
            'message': c.message,
            'date': c.committed_date
        }
        j_dict['leaks'].append(c_dict)

    with open('leaks.json', 'w') as file:
        json.dump(j_dict, file, indent=4)
if __name__=="__main__":
    commits = extract(REPO_DIR)
    leaks = transform(commits)
    load(leaks)


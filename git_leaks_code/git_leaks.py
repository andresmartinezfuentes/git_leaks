#User\scripts\python3
from git import Repo
import re,signal,sys

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
        text.append(commit.message)
    return text

def transform(commits):
    leaks=[] 
    i = 0
    claves='(pasword|credentials|key)'
    while i < len(commits):
        if re.findall(claves,commits[i],re.I) != []:
            leaks.append(commits[i])
        i+=1
    return leaks
   
    
def load(leaks):
    with open('leaks.txt','w') as fichero:
        index = 0
        while index < len(leaks):
            fichero.write(leaks[index])
            index += 1

if __name__=="__main__":
    commits = extract(REPO_DIR)
    leaks = transform(commits)
    load(leaks)


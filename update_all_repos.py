import requests
import os, sys

def update_all_repo(user_id, token):
    response = requests.get("https://api.github.com/users/pythaac/repos")
    if response.status_code != 200:
        print("Error!!")
        response.raise_for_status()
        return

    repo_names = [repo["name"] for repo in response.json()]

    for name in repo_names:
        output = os.popen(f"github-label-sync --access-token {token} --labels labels.json {user_id}/{name}").read()
        print(output)
        
        if not ("Labels updated" in output) and not ("Labels are already up to date" in output):
            return
    

if __name__ == "__main__":
    argv = sys.argv
    
    if len(argv) != 3:
        print("Error!!")
        print("Usage: python3 update_all_repos.py {USER_ID} {ACCESS_TOKEN}")
    else:
        update_all_repo(argv[1], argv[2])

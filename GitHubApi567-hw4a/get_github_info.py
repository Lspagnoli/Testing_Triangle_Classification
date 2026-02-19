import requests

def get_github_info(userID):

    repo_response = requests.get(f"https://api.github.com/users/{userID}/repos")
    print(repo_response)

    repos = repo_response.json()
    
    repoData = {}
    
    for repo in repos:
        commit_response = requests.get(f"https://api.github.com/repos/{userID}/{repo["name"]}/commits")
        print(commit_response)
        commits = commit_response.json()
        repoData[repo["name"]] = len(commits)

    
    return format_github_info(repoData)

def format_github_info(repoData):

    formatList = []
    
    for repoName, commitCount in repoData.items():
        formatList.append(f"Repo: {repoName} Number of commits: {commitCount}")

    return formatList


for response in get_github_info("Lspagnoli"):
    print(response)
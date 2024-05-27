import requests
import json

#یک ای پی آی را میخواند و جواب را بررسی میکند
url = "https://api.github.com/search/repositories?q=language:python+sort:stars"
#url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_object = r.json()
print(f"Total repositories: {response_object['total_count']}")
print(f"Complete results: {not response_object['incomplete_results']}")
# Explore information about the repositories.
repo_dicts = response_object['items']
print(f"Repositories returned: {len(repo_dicts)}")
# Examine the first repository.
repo_dict = repo_dicts[0]
print("\nSelected information about all repository:")
for repo_dict in repo_dicts :
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
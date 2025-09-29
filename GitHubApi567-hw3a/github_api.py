# Benedict Martinez – SSW 567 – HW 03a
# I pledge my honor that I have abided by the Stevens Honor System

import json
import requests

class GitHubAPIError(Exception):
    pass

def fetch_user_repos(user: str):
    """Return list of repo dicts (as parsed JSON) for a GitHub user."""
    url = f"https://api.github.com/users/{user}/repos"
    resp = requests.get(url, timeout=10)
    if resp.status_code != 200:
        raise GitHubAPIError(f"GET {url} -> {resp.status_code}")
    return json.loads(resp.text)

def fetch_repo_commits(user: str, repo: str):
    """Return list of commit dicts (as parsed JSON) for user/repo."""
    url = f"https://api.github.com/repos/{user}/{repo}/commits"
    resp = requests.get(url, timeout=10)
    if resp.status_code != 200:
        raise GitHubAPIError(f"GET {url} -> {resp.status_code}")
    return json.loads(resp.text)

def user_repos_with_commit_counts(user: str):
    """
    Given a GitHub user ID, return a list of (repo_name, commit_count) tuples.
    Keep it simple by counting items from the first page of commits per assignment instructions.
    """
    repos = fetch_user_repos(user)
    results = []
    for r in repos:
        name = r.get("name")
        # skip repos without a name field defensively
        if not name:
            continue
        commits = fetch_repo_commits(user, name)
        results.append((name, len(commits)))
    return results

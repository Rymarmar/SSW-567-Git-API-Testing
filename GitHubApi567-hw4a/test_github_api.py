import unittest
from github_api import user_repos_with_commit_counts, fetch_user_repos, GitHubAPIError

class TestGitHubAPI_HappyPaths(unittest.TestCase):
    def test_known_user_has_repos(self):
        # Minimal live test: expect no exception and a list response
        # (Keep this light to avoid rate limit; this proves your wiring works.)
        res = user_repos_with_commit_counts("richkempinski")
        self.assertIsInstance(res, list)
        # tuple shape check if any
        if res:
            repo_name, commit_count = res[0]
            self.assertIsInstance(repo_name, str)
            self.assertIsInstance(commit_count, int)

class TestGitHubAPI_Negatives(unittest.TestCase):
    def test_unknown_user_raises(self):
        with self.assertRaises(GitHubAPIError):
            fetch_user_repos("this_user_should_not_exist_1234567890")

if __name__ == "__main__":
    unittest.main()

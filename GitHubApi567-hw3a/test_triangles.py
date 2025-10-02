# test_github_api.py  (HW03a_Mocking branch)
# Benedict Martinez – SSW 567 – HW 03b
# Tests are fully mocked: no real HTTP requests are made.
# I pledge my honor that I have abided by the Stevens Honor System
# Changed name of file to test_triangles.py

import unittest
from unittest import mock
from github_api import user_repos_with_commit_counts, GitHubAPIError

# Minimal stand-in for requests.Response that our code needs
class MockResponse:
    def __init__(self, status_code=200, text="[]"):
        self.status_code = status_code
        self.text = text

class TestGitHubAPI_Mocked(unittest.TestCase):
    @mock.patch("github_api.requests.get")
    def test_happy_path_counts_commits(self, mock_get):
        # 1st call -> repos list
        repos_json = '[{"name":"Triangle567"},{"name":"Square567"}]'
        # 2nd -> commits for Triangle567 (2)
        commits_triangle_json = '[{"sha":"a"},{"sha":"b"}]'
        # 3rd -> commits for Square567 (3)
        commits_square_json = '[{"sha":"c"},{"sha":"d"},{"sha":"e"}]'

        mock_get.side_effect = [
            MockResponse(200, repos_json),
            MockResponse(200, commits_triangle_json),
            MockResponse(200, commits_square_json),
        ]

        out = user_repos_with_commit_counts("John567")
        self.assertEqual(out, [("Triangle567", 2), ("Square567", 3)])

        # optional: verify URLs were called
        called_urls = [call.args[0] for call in mock_get.call_args_list]
        self.assertIn("https://api.github.com/users/John567/repos", called_urls)
        self.assertIn("https://api.github.com/repos/John567/Triangle567/commits", called_urls)
        self.assertIn("https://api.github.com/repos/John567/Square567/commits", called_urls)
        self.assertEqual(len(mock_get.call_args_list), 3)

    @mock.patch("github_api.requests.get")
    def test_unknown_user_raises(self, mock_get):
        # repos endpoint returns 404
        mock_get.return_value = MockResponse(404, '{"message":"Not Found"}')
        with self.assertRaises(GitHubAPIError):
            user_repos_with_commit_counts("nope_user_123")

    @mock.patch("github_api.requests.get")
    def test_commit_endpoint_error_raises(self, mock_get):
        # repos OK -> one repo; commits 500
        mock_get.side_effect = [
            MockResponse(200, '[{"name":"OnlyRepo"}]'),
            MockResponse(500, '{"message":"Server error"}'),
        ]
        with self.assertRaises(GitHubAPIError):
            user_repos_with_commit_counts("someone")

    @mock.patch("github_api.requests.get")
    def test_repo_without_name_is_skipped(self, mock_get):
        # first repo missing name; second is valid
        mock_get.side_effect = [
            MockResponse(200, '[{"fork": true}, {"name":"HasName"}]'),
            MockResponse(200, '[{"sha":"x"}]'),
        ]
        out = user_repos_with_commit_counts("userX")
        self.assertEqual(out, [("HasName", 1)])

if __name__ == "__main__":
    unittest.main()

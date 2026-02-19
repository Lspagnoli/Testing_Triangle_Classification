from get_github_info import get_github_info
from get_github_info import format_github_info
from unittest import mock


#--------------------------
#format_github_info tests

def test_valid_format_github_info():
    testValidDict = {'Assignment3': 7, 'helloworld': 4, 'Odds-Ends': 7, 'Security-Gate-Simulator': 2, 'SpannersDataVis': 7, 'Testing_Triangle_Classification': 2}
    assert format_github_info(testValidDict) == ['Repo: Assignment3 Number of commits: 7', 'Repo: helloworld Number of commits: 4', 'Repo: Odds-Ends Number of commits: 7', 'Repo: Security-Gate-Simulator Number of commits: 2', 'Repo: SpannersDataVis Number of commits: 7', 'Repo: Testing_Triangle_Classification Number of commits: 2']

def test_empty_format_github_info():
    testEmptyDict = {}
    assert format_github_info(testEmptyDict) == []

#--------------------------
#get_github_info() tests

def test_valid_get_github_info():
    with mock.patch('get_github_info.requests.get') as mock_get:
        mock_repos = mock.MagicMock()
        mock_repos.json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        
        mock_commits = mock.MagicMock()
        mock_commits.json.return_value = [{}, {}, {}]
        
        mock_get.side_effect = [mock_repos, mock_commits, mock_commits]
        
        result = get_github_info("fakeuser")
        assert len(result) > 0

def test_invalid_get_github_info():
    with mock.patch('get_github_info.requests.get') as mock_get:
        mock_response = mock.MagicMock()
        mock_response.json.return_value = []
        mock_get.return_value = mock_response
        
        result = get_github_info("fakeuser")
        assert result == []


#--------------------------
#status code tests

def test_200_status_response():
    with mock.patch('get_github_info.requests.get') as mock_get:
        mock_repos = mock.MagicMock()
        mock_repos.status_code = 200
        mock_repos.json.return_value = [{"name": "repo1"}]
        
        mock_commits = mock.MagicMock()
        mock_commits.status_code = 200
        mock_commits.json.return_value = [{}, {}]
        
        mock_get.side_effect = [mock_repos, mock_commits]
        
        result = get_github_info("fakeuser")
        assert len(result) > 0

def test_404_status_response():
    with mock.patch('get_github_info.requests.get') as mock_get:
        mock_response = mock.MagicMock()
        mock_response.status_code = 404
        mock_response.json.return_value = []
        mock_get.return_value = mock_response
        
        result = get_github_info("fakeuser")
        assert result == []
from get_github_info import get_github_info
from get_github_info import format_github_info

def test_valid_format_github_info():
    testValidDict = {'Assignment3': 7, 'helloworld': 4, 'Odds-Ends': 7, 'Security-Gate-Simulator': 2, 'SpannersDataVis': 7, 'Testing_Triangle_Classification': 2}
    assert format_github_info(testValidDict) == ['Repo: Assignment3 Number of commits: 7', 'Repo: helloworld Number of commits: 4', 'Repo: Odds-Ends Number of commits: 7', 'Repo: Security-Gate-Simulator Number of commits: 2', 'Repo: SpannersDataVis Number of commits: 7', 'Repo: Testing_Triangle_Classification Number of commits: 2']

def test_empty_format_github_info():
    testEmptyDict = {}
    assert format_github_info(testEmptyDict) == []

def test_valid_get_github_info():
    result = get_github_info("Lspagnoli")
    assert isinstance(result, list)
    assert len(result) > 0
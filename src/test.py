# This is a simple example to show how easy is to use 
# GitHub API v3 to get data from open repositories.

from github_api import RepositoryInformation

if __name__ == '__main__':
    repositories = RepositoryInformation()
    result = repositories.get_information([
        'https://github.com/mozilla-mobile/firefox-ios/pull/4421',
        'https://github.com/JuliaLang/julia/pull/31499'], 'full_name')
    print(result)

# Output
# [
#   {'full_name': 'mozilla-mobile/firefox-ios', 'stars': 8697, 'forks': 2002, 'watchers': 8697}, 
#   {'full_name': 'JuliaLang/julia', 'stars': 22289, 'forks': 3370, 'watchers': 22289}
# ]
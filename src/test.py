# This is a simple example to show how easy is to use 
# GitHub API v3 to get data from open repositories.

from github_api import RepositoryInformation

if __name__ == '__main__':
    repositories = RepositoryInformation()
    result = repositories.get_information([
        'https://github.com/mozilla-mobile/firefox-ios/pull/4421',
        'https://github.com/akeneo/pim-community-dev/pull/2043#discussion_r23523814'], 'full_name')
    print(result)
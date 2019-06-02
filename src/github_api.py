# You can use a pull request link or a comment pull request link as an example for this test.

# Pull Request
# e.g. https://github.com/mozilla-mobile/firefox-ios/pull/4421

# GitHub API
# e.g. https://api.github.com/search/repositories?q=Strategy-Pattern%20in:name&sort=stars&order=desc

from urllib.parse import urlparse
from requests import get

def get_full_name(repository_url):
    """
    This method split the URL received to get the original full name of the project.
    """
    parsed_uri = urlparse(repository_url)
    return '{uri[1]}/{uri[2]}'.format(uri=parsed_uri.path.split('/'))

class RepositoryInformation:
    """
    This class gets some information (stars, forks, and watchers)
    from repositories set in the constructor.
    """

    def get_information(self, repositories_url, paramenter = "full_name"):
        repositories_info = []
        for url in repositories_url:
            info = self.__get_information(url, paramenter)
            if info is not None:
                repositories_info.append(info)
        return repositories_info

    def __get_information(self, repository_url, paramenter):
        # Getting repository full name (user/repository_name)
        full_name = get_full_name(repository_url)

        # Calling API GItHub
        url_api_github = 'https://api.github.com/search/repositories?q={}%20in:{}'
        r = get(url_api_github.format(full_name, paramenter))

        # Getting some data from Json to set in the dictionary
        metadata = r.json() 
        if (metadata['total_count'] > 0):
            info =	{
                "stars": metadata['items'][0]['stargazers_count'],
                "forks": metadata['items'][0]['forks'],
                "watchers": metadata['items'][0]['watchers']
            }
            return info
        return None
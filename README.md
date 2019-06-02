# Getting repositories data from GitHub
This is a simple example to show how easy is to use GitHub API v3 with Python to get data from open repositories.

## Description of the example
The GitHub has great API with complete documentation, detailing how to use it to load information from their repositories. Despite this, a lot of developers like to learn new technology by reading code, and this project proposes to explain how to use the GitHub API through a finalized code.

In this example, the code was made in python and it will load some information from GitHub's repositories through HTTP requests. Firstly, it will be necessary to install the request library.
```
pip install requests
```
In the `github_api.py` file, located in `src` folder, it is possible to see a function called `get_full_name` and a class `RepositoryInformation`. The `get_full_name` will get the URL and extracts only the full name (user name/repository name) of project.
```python
def get_full_name(repository_url):
    parsed_uri = urlparse(repository_url)
    return '{uri[1]}/{uri[2]}'.format(uri=parsed_uri.path.split('/'))
```
The `RepositoryInformation` has two methods, one public and another private. The private method (`__get_information`) receives two parameters, the first parameter will receive a repository URL and the second the filter used in GitHub API to filter data. This method will call the function `get_full_name` that it will set their result in the GitHub API URL. The following parameter received will be utilized to define how information the API will filter.
```python
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
            "full_name": metadata['items'][0]['full_name'],
            "stars": metadata['items'][0]['stargazers_count'],
            "forks": metadata['items'][0]['forks'],
            "watchers": metadata['items'][0]['watchers']
        }
        return info
    return None
```
The parameter `q=` will receive the value and parameters that it will be filtered. However, the fields to search are informed after the `in:`

```
e.g., https://api.github.com/search/repositories?q=Test%20in:name
```
It is still possible to filter the data using setting two or more fields after the `in:`
```
e.g., https://api.github.com/search/repositories?q=Specification%20in:full_name,name,description
```

Also, if the request returns thousands of results, it is possible to sort them for `stars` or `forks`, defining the `asc` or `desc`.
```
e.g., https://api.github.com/search/repositories?q=Specification-Patternin:name&sort=stars&order=desc
```

The public method (`get_information`) from `RepositoryInformation` class will receive a list of repositories URL and will set it individually for the private method. When the process finishes, it will give back a dictionary list with information such as stars, forks,and watchers.

```python
def get_information(self, repositories_url, paramenter = "full_name"):
    repositories_info = []
    for url in repositories_url:
        info = self.__get_information(url, paramenter)
        if info is not None:
            repositories_info.append(info)
    return repositories_info
```

After installing the `request` library, you will be able to test this code calling the `test.py` in the `src` folder.

```
python test.py
```

## GitHub API documentation
It is possible to find more details about the API in this [link](https://developer.github.com/v3/).
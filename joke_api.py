import requests

def get_all_categories():
    """
    Gets all the available categories from the API.
    :return: list of categories
    """
    url = "https://v2.jokeapi.dev/categories"
    request_all_categories = requests.get(url)
    categories = request_all_categories.json()
    return categories["categories"]


def get_joke():
    """
    Gets a random joke from the api.
    :return: joke as a string
    """
    url = "https://v2.jokeapi.dev/joke/Any?type=single"
    request_random_joke = requests.get(url)
    random_joke = request_random_joke.json()
    return random_joke["joke"]


def get_category(category):
    """
    Gets a joke from the chosen category.
    :param category: chosen category from menu
    :return: joke as a string
    """
    url = f"https://v2.jokeapi.dev/joke/{category}?type=single"
    request_category_joke = requests.get(url)
    category_joke = request_category_joke.json()
    return category_joke["joke"]


def get_keyword(keyword):
    """
    Gets a joke which contains the chosen keyword.
    :param keyword: chosen keyword
    :return: joke as a string
    """
    pass


def main():
    print(f"TEST get_all_categories: {get_all_categories()}")
    print(f"TEST get_joke: {get_joke()}")
    print(f"TEST get_category: {get_category("Programming")}")


if __name__ == "__main__":
    main()

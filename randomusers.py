


def get_full_names(data: dict) -> list[str]:
    """
    Returns a list of users' full names in 'First Last' format.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        list[str]: List of full names.
    """
    results = data['results']

    names = [] 
    for user in results:
        name = user['name']
        full_name = name['first'] + " " + name['last']
        names.append(full_name)

    return names


def get_users_by_country(data: dict, country: str) -> list[dict]:
    """
    Filters and returns users who live in a specific country.

    Args:
        data (dict): JSON data containing user records.
        country (str): Country name to filter by.

    Returns:
        list[dict]: List of dictionaries containing full name and email of matching users.
    """
    users = []
    for user in data['results']:
        if user['location']['country'] == country:
            users.append({
                'fullname': user['name']['first'] + " " + user['name']['last'],
                'email': user['email']
            })

    return users


def count_users_by_gender(data: dict) -> dict:
    """
    Counts the number of users by gender.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary with gender as keys and count as values.
    """
    gender_counts = {}

    for user in data.get("results", []):
        gender = user.get("gender", "unknown").lower()
        gender_counts[gender] = gender_counts.get(gender, 0) + 1

    return gender_counts


def get_emails_of_older_than(data: dict, age: int) -> list[str]:
    """
    Returns a list of emails of users older than the given age.

    Args:
        data (dict): JSON data containing user records.
        age (int): Age threshold.

    Returns:
        list[str]: List of email addresses.
    """
    emails = []

    for user in data.get("results", []):
        user_age = user.get("dob", {}).get("age", 0)
        if user_age > age:
            email = user.get("email", "")
            emails.append(email)

    return emails


def sort_users_by_age(data: dict, descending: bool = False) -> list[dict]:
    """
    Sorts users by age in ascending or descending order.

    Args:
        data (dict): JSON data containing user records.
        descending (bool, optional): Whether to sort in descending order. Defaults to False.

    Returns:
        list[dict]: List of users with name and age sorted accordingly.
    """
    users = []

    for user in data.get("results", []):
        full_name = f"{user.get('name', {}).get('first', '')} {user.get('name', {}).get('last', '')}"
        age = user.get("dob", {}).get("age", 0)

        users.append({
            "full_name": full_name,
            "age": age
        })

    sorted_users = sorted(users, key=lambda x: x["age"], reverse=descending)

    return sorted_users


def get_usernames_starting_with(data: dict, letter: str) -> list[str]:
    """
    Returns a list of usernames starting with a given letter.

    Args:
        data (dict): JSON data containing user records.
        letter (str): The starting letter to filter usernames.

    Returns:
        list[str]: List of matching usernames.
    """
    pass


def get_average_age(data: dict) -> float:
    """
    Calculates and returns the average age of users.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        float: Average age.
    """
    pass


def group_users_by_nationality(data: dict) -> dict:
    """
    Groups and counts users by their nationality.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary with nationality as keys and count as values.
    """
    pass


def get_all_coordinates(data: dict) -> list[tuple[str, str]]:
    """
    Extracts all users' coordinates as tuples of (latitude, longitude).

    Args:
        data (dict): JSON data containing user records.

    Returns:
        list[tuple[str, str]]: List of coordinate tuples.
    """
    pass


def get_oldest_user(data: dict) -> dict:
    """
    Finds and returns the oldest user's name, age, and email.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary containing 'name', 'age', and 'email' of the oldest user.
    """
    oldest_user = None
    max_age = -1

    for user in data.get("results", []):
        age = user.get("dob", {}).get("age", 0)
        if age > max_age:
            max_age = age
            full_name = f"{user.get('name', {}).get('first', '')} {user.get('name', {}).get('last', '')}"
            email = user.get("email", "")
            oldest_user = {
                "name": full_name,
                "age": age,
                "email": email
            }

    return oldest_user


def find_users_in_timezone(data: dict, offset: str) -> list[dict]:
    """
    Returns users whose timezone offset matches the given value.

    Args:
        data (dict): JSON data containing user records.
        offset (str): Timezone offset (e.g. '+5:30').

    Returns:
        list[dict]: List of users with full name and city.
    """
    pass


def get_registered_before_year(data: dict, year: int) -> list[dict]:
    """
    Returns users who registered before a given year.

    Args:
        data (dict): JSON data containing user records.
        year (int): Year threshold.

    Returns:
        list[dict]: List of users with full name and registration date.
    """
    pass



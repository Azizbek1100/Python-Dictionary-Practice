from data import randomuser_data
from randomusers import(
    get_full_names,
    get_users_by_country,
    count_users_by_gender,
    get_emails_of_older_than,
    sort_users_by_age,
    get_oldest_user
)

def run_functions() -> None:
    """
    Runs and prints results of all data processing functions for demonstration purposes.
    """
    #print("Full Names:", get_full_names(randomuser_data))
    #print("Results:", get_users_by_country(randomuser_data, 'Netherlands'))
    #print("Results:", count_users_by_gender(randomuser_data,))
    #print("Results:", get_emails_of_older_than(randomuser_data, 45))
    #print("Results:", sort_users_by_age(randomuser_data, descending=False ))
    #print("Results:", get_oldest_user(randomuser_data))






run_functions()

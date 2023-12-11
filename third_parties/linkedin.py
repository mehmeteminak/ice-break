import requests
import os


def scrape_linkedin_profile(linkedin_profile_url: str):
    """
    Scrape infromations from linkedin profile
    :param linkedin_profile_url: An linkedin profile url for scraping
    :return:
    """


    headers = {"Authorization": "Bearer " + os.environ.get("PROXY_API_KEY")}
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    params = {
        "linkedin_profile_url": linkedin_profile_url,
        "extra": "include",
        "github_profile_id": "include",
        "facebook_profile_id": "include",
        "twitter_profile_id": "include",
        "personal_contact_number": "include",
        "personal_email": "include",
        "inferred_salary": "include",
        "skills": "include",
        "use_cache": "if-present",
        "fallback_to_cache": "on-error",
    }
    response = requests.get(api_endpoint, params=params, headers=headers)
    return response.json()

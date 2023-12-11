from langchain.serpapi import SerpAPIWrapper


def get_profile_url(text: str) -> str:
    "Searches for Linkedin Profile page"

    search = SerpAPIWrapper()
    res = search.run(f"{text}")
    return res

def choose_first_url(urls : [str]):
    return  urls[0]
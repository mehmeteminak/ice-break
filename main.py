from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup
from  time import  sleep

prompt_template = """Given the information in json format {linkedin_datas} about a person from I want you to create
    1.a short summary
    2. two interesting facts about them
"""


llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

prompt = PromptTemplate(template=prompt_template, input_variables=["linkedin_datas"])

# Press the green button in the gutter to run the script. """
if __name__ == "__main__":
    linkedin_profile_url = lookup(searched_name="İlhan Tetik")
    response = scrape_linkedin_profile(linkedin_profile_url)
    #response = { "name" : "Mehmet Emin AK" ,"skills" : ["PHP","Laravel","Swift","React Native"], "description" : "A passionate fullstack mobile developer from Turkey."}
    print(type(response))
    chain = LLMChain(llm=llm,prompt=prompt)
    result = chain.predict(linkedin_datas=str(response))
    print(result)

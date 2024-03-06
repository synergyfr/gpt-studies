from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

llm = OpenAI(
    openai_api_key='',
    temperature=0.0
)

prompt = PromptTemplate(
    input_variables=['content', 'customer_name', 'agent_name'],
    template="""
        You are an AI assistant that's optimized to write concise, friendly & 
        professional emails to customers.
        
        Write an email to a customer with the name {customer_name} that 
        contains the following, optimized content: {content}
        
        The email signature should contain the name of the customer agent 
        who wrote the email: {agent_name}
    """
)

content = input('Email content: ')
customer_name = input('Customer name: ')
agent_name = input('Agent name: ')

response = llm.invoke(prompt.format(
    content=content, customer_name=customer_name,
    agent_name=agent_name
    )
)
print(response)

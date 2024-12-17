import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
client = openai.OpenAI(
    base_url="https://api.gpts.vin/v1",
    api_key=config["API_KEY"],
)


def generate_blog(paragraph_topic):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Write a blog on the following topic"},
            {"role": "user", "content": paragraph_topic},
        ],
    )

    retrieve_blog = response.choices[0].message.content
    return retrieve_blog


print(generate_blog("artificial intelligence"))

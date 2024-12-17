import openai

client = openai.OpenAI(
    base_url="https://api.gpts.vin/v1",
    api_key="sk-SqcUluX8QoblMOeIm5ZHtm3MOSZ01B4fBY6WV4yXMiWzrMtY",
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

import openai
class Newspaper():
    def __init__(self,title,content,title_image,content_image,pressname):
        print(title)
        print(content)
        print(f"Images Title:{title_image} Content:{content_image}")
        print(pressname)

openai.api_key = ""
model_engine = "text-davinci-003"

def generateTitle(userinput):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=f"A title for a fictional newspaper about {userinput}",
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    title = response["choices"][0]["text"]
    return title
def generateContent(title):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=f"Generate the rest of this fictional newspaper with the headline {title}",
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    content = response["choices"][0]["text"]
    return content
def generateContentImages(content):
    response = openai.Image.create(
        prompt=f"Generate images for this fictional newspaper {content}",
        n=1,
        size="1024x1024"
    )
    contentimage = response['data'][0]['url']
    return contentimage

def generateTitleImage(title):
    response = openai.Image.create(
        prompt=f"Generate images for this fictional newspaper title {title}",
        n=1,
        size="1024x1024"
    )
    titleimage = response['data'][0]['url']
    return titleimage
def fictionalPressOrganization():
    response = openai.Completion.create(
        engine=model_engine,
        prompt=f"Generate the name for a fictional press company",
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    name = response["choices"][0]["text"]
    return name
print("WARNING:You will need alot of tokens to keep the bot running Each newspaper generated by the ai costs 2 cents of OpenAI Tokens")
l = input("Do you agree y/n")
if(l == "n"):
    exit()
else:
    openai.api_key = input("Your OpenAI API Key")
    intialinput = input("What is the topic")
    v = generateTitle(intialinput)
    l = generateContent(v)
    k = generateContentImages(l)
    z = generateTitleImage(v)
    p = fictionalPressOrganization()
    print(f"Fictional Newspaper created by AI Your newspaper based on {intialinput} has been generated")
    Newspaper(title=v,content=l,content_image=k,title_image=z,pressname=p)


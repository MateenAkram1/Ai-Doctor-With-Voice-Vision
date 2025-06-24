from dotenv import load_dotenv

load_dotenv()


#Step2: Convert image to required format
import base64



def encode_image(image_path="a.png"):
    image_file=open(image_path, "rb")
    encoded_image=base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_image

#Step3: Setup Multimodal LLM 
from groq import Groq

def analyze_image_withquery(encoded_image, query, model = "meta-llama/llama-4-scout-17b-16e-instruct"):
    client=Groq()  
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]
    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )

    
    return chat_completion.choices[0].message.content

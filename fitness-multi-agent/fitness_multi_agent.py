import os
import certifi
import truststore
 
truststore.inject_into_ssl()
os.environ.setdefault("SSL_CERT_FILE", certifi.where())
os.environ.setdefault("REQUESTS_CA_BUNDLE", certifi.where())

import google.generativeai as genai

genai.configure(
    api_key=os.environ.get("GOOGLE_API_KEY", ""),
    transport="rest",
)

model_1 = genai.GenerativeModel(
    model_name = "gemini-2.5-flash",
    system_instruction =  "Your task is to find out the user goal for their bodybuilding task by taking input of the user Body weight, Height, and Age and ask their goals along with their food type."
)

model_2 = genai.GenerativeModel(
    model_name = "gemini-2.5-flash",
    system_instruction = "Your task is Professional Bodybuilder coach using the another model assistant (Model_1) data and also need to ask user availability time and ask for any previous injuries and help with the user needs and goals."
)
  
model_3 = genai.GenerativeModel(
    model_name = "gemini-2.5-flash",
    system_instruction=  "You are a professional Dietician ,Your task is to build the diet plan based on user workouts and goals by the data retrieved from another model assistant (model_2)"

)

print("Ask the ultimate bodybuilder assistant to achieve your dream physique")
while True:
    model1_response = " "
    prompt = input("")
    cleaned_prompt = prompt.replace(" ","")
    if cleaned_prompt.lower() == "exit":
        print("The Mighty Bodybuilder taking leave...")
        break
    
    if prompt == "":
        print("Please enter something for the Mighty BodyBuilder to Help out with your Goals...")
        continue

    else:
        model1_response = model_1.generate_content(prompt)
        print(f"The task finder says\n {model1_response.text}")

    model2_input = f"Model 1 replied {model1_response.text} for {prompt}"
    model2_response = model_2.generate_content(model2_input)
    print(f"The Professioanl Bodybuilder says \n {model2_response.text}")
    
    model3_input = f"Model 2 replied {model2_response.text} for {model1_response.text}"
    model3_response =  model_3.generate_content(model3_input)
    print(f"The Professioanl Dietician says \n {model3_response.text}")
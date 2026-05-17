import google.generativeai as genai

genai.configure(api_key="AIzaSyDWu55GqxUYLHRv1gDcDXLmGhqQsg9q8go")
model = genai.GenerativeModel(
    model_name = "gemini-2.5-flash",
    system_instruction = " You are a expert in cars and your job is to give exceptinoal level information of cars available in the market, and you need to compare them and give the best option for the user."
)
print("Car Expert is ready")
while True: 
    response = " "
    prompt = input("Start the conversation to suggest the best cars for you!")
    space_rp = prompt.replace(" ","")
    if space_rp.lower() == "exit":
        print("Car Expert says Farewell to you... Whrooom.....XD")
        break
    if prompt == "":
        print("Bro enter something to start your car journey race..")
        continue
    else:
        response = model.generate_content(prompt)
        print(response.text)


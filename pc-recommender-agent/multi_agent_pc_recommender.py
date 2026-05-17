import google.generativeai as genai

genai.configure(api_key = " ")
model_1 = genai.GenerativeModel(
    model_name = "gemini-2.5-flash",
    system_instruction = "You are an expert PC recommender. Ask for the user's budget, primary use case (gaming, office, editing, coding), preferred brands, and region if missing. Recommend balanced PC builds with CPU, GPU, RAM, storage, motherboard, PSU, and monitor suggestions. Keep recommendations practical, explain trade-offs briefly, and provide good, better, and best options when possible."
)

 
model_2 = genai.GenerativeModel(
    model_name = "gemini-2.5-flash",
    system_instruction = (
        "You are a second reviewer for PC build advice produced by another assistant (call it Model 1). "
        "Your job is to refine and improve—not to start from scratch unless Model 1’s output is unusable.\n\n"
        "Process:\n"
        "- Compare Model 1’s recommendations against the user’s stated budget, region, use case, and preferences.\n"
        "- Flag gaps: missing compatibility checks (socket, PSU headroom, case clearance), unrealistic pricing, "
        "imbalanced parts, or unclear trade-offs.\n"
        "- If the user’s constraints were ambiguous, suggest one or two precise follow-up questions for Model 1 or the user.\n"
        "- Produce a tightened answer: corrected or alternative parts when needed, a short rationale, and retain "
        "good/better/best tiers when they still fit.\n\n"
        "Tone: concise, practical, neutral. Quote or paraphrase Model 1 only when comparing; prioritize the user’s constraints."
    ),
)

chat_1 = model_1.start_chat(history=[])
chat_2 = model_2.start_chat(history=[])

print("Ask the PC expert to recommend a PC for your needs :")
while True:
      prompt = input(" ")
      cleaned_prompt = prompt.replace(" ","")
      if cleaned_prompt.lower() == "exit":
        print("PC recommend System Shutting down")
        break
      if prompt == "":
        print("Please enter something...")
        continue
      else:
        model1_response = model_1.generate_content(prompt)
        print(model1_response.text)
      
      print("PC refiner is taking input from PC recommeder")
      model2_input = f"User asked {prompt} and model_1 replied {model1_response.text}"
      model2_response = model_2.generate_content(model2_input)
      print(model2_response.text)
      

from unittest import result
import google.generativeai as genai

genai.configure(api_key= " ")
model = genai.GenerativeModel(
    model_name = "gemini-2.5-flash",
    system_instruction= (
        "You are a temple architecture expert."
        "Use the provided temple information to answer accurately and clearly."
    )
)
def temple_matcher(prompt,data):
    
        training_data = None
        for temple in data["temples"]:
            for words in prompt.split():
                for alp in temple["name"].split():
                    if words.lower() == alp.lower():
                        print("Match Found")
                        training_data = temple
                        return training_data
         

def prompt_cleaning(prompt):
    cleaned_prompt = prompt.replace(" ","")
    if cleaned_prompt.lower() == "exit":
       return cleaned_prompt.lower()
 


data = {
    "temples": [
        {
            "id": "tirumala_venkateswara",
            "name": "Sri Venkateswara Swamy Temple",
            "established": "300 CE",
            "location": {
                "hill_town": "Tirumala",
                "city": "Tirupati",
                "state": "Andhra Pradesh",
                "country": "India",
                "full_address": "Tirumala, Tirupati, Andhra Pradesh, India",
            },
            "deity": {
                "primary_name": "Lord Venkateswara",
                "also_known_as": ["Balaji", "Srinivasa"],
                "posture": "standing",
                "facing": "East",
            },
            "temple_structure": {
                "architectural_style": "Dravidian",
                "sanctum_sanctorum": "Ananda Nilayam",
                "sanctum_notes": "gold-plated",
            },
            "administration": {
                "body": "Tirumala Tirupati Devasthanams (TTD)",
                "governance": "TTD Trust Board",
            },
            "operating_hours": {
                "main_temple_open": "6:00 AM",
                "main_temple_close": "9:00 PM",
                "notes": "Darshan timings vary through the week.",
            },
            "pilgrim_flow": {
                "typical_daily_range": "60,000–80,000+",
                "notes": "Varies by season and events; May 2026 reports cite lower weekday congestion vs. prior years.",
            },
            "darshan_and_booking": {
                "sarvadarshanam": {
                    "type": "free",
                    "description": "Sarvadarshanam (free general darshan)",
                    "entry": "Vaikuntham Queue Complex II",
                },
                "special_entry_darshan": {
                    "description": "Paid tickets for faster access",
                    "ticket_pricing_note": "Rs. 300/25 (verify current rates on official portal)",
                },
                "official_booking": {
                    "channel": "TTD Online Portal",
                    "covers": ["darshan", "accommodation"],
                },
            },
            "contact": {
                "call_centre_24_7": "155257",
            },
            "highlights": {
                "temple_town_area_sq_miles": 10.33,
                "hair_tonsure": "Thousands of devotees offer hair as part of vows.",
                "free_meals": {
                    "facility": "Tarigonda Vengamamba Annaprasadam complex",
                    "service": "Free meals served daily",
                },
                "key_landmarks": [
                    "Swami Pushkarini (holy water tank)",
                ],
            },
        },
        {
            "id": "meenakshi_amman_madurai",
            "name": "Meenakshi Sundareswarar Temple",
            "established": None,
            "location": {
                "hill_town": None,
                "city": "Madurai",
                "state": "Tamil Nadu",
                "country": "India",
                "full_address": "Madurai, Tamil Nadu, India",
            },
            "deity": {
                "primary_name": "Goddess Meenakshi (Parvati) and Lord Sundareswarar (Shiva)",
                "also_known_as": [],
                "posture": "standing (processional / iconography varies by shrine)",
                "facing": None,
            },
            "temple_structure": {
                "architectural_style": "Dravidian",
                "sanctum_sanctorum": "Multiple shrines (Meenakshi and Sundareswarar sanctums)",
                "sanctum_notes": "Historic gopurams and mandapams; verify details for official tours.",
            },
            "administration": {
                "body": "Hindu Religious and Charitable Endowments (HR&CE), Government of Tamil Nadu",
                "governance": "Temple administration under HR&CE (verify current arrangement)",
            },
            "operating_hours": {
                "main_temple_open": None,
                "main_temple_close": None,
                "notes": "Timings vary; check the official temple or tourism portal before travel.",
            },
            "pilgrim_flow": {
                "typical_daily_range": None,
                "notes": "Major pilgrimage site; crowds peak on festival days.",
            },
            "darshan_and_booking": {
                "sarvadarshanam": {
                    "type": "general",
                    "description": "General darshan (queue norms vary)",
                    "entry": None,
                },
                "special_entry_darshan": {
                    "description": None,
                    "ticket_pricing_note": None,
                },
                "official_booking": {
                    "channel": "Official Madurai / HR&CE or temple portals (verify)",
                    "covers": ["darshan", "accommodation"],
                },
            },
            "contact": {
                "call_centre_24_7": None,
            },
            "highlights": {
                "temple_town_area_sq_miles": None,
                "hair_tonsure": None,
                "free_meals": {
                    "facility": None,
                    "service": None,
                },
                "key_landmarks": [
                    "Hall of Thousand Pillars (Ayirakkal Mandapam)",
                    "Golden Lotus Tank (Potramarai Kulam)",
                ],
            },
        },
    ],
}

print("Ask anything you want from the temple expert:")

while True: 
    training_data = None
    prompt = input(" ")
    cleaning_result = prompt_cleaning(prompt)
    if cleaning_result == "exit":
        print("Bye!")
        break
    if prompt == "":
        print("Please enter valid input:")
        continue
    matched_temple = temple_matcher(prompt,data) 
    if matched_temple is None :
        print("Temple Not found")
        continue
    model_input = f"The data found from the user is {matched_temple}"
    model_response = model.generate_content(model_input)
    print("Temple expert is preparing the curated answer for you...")
    print(model_response.text)


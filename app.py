import streamlit as st
import pandas as pd
import os
import geopy
from geopy.geocoders import Nominatim
import google.generativeai as genai
from dotenv import load_dotenv
import spacy
import datetime

# Load NLP model for location entity recognition
nlp = spacy.load("en_core_web_sm")

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# Geocoding function
geolocator = Nominatim(user_agent="travel_planner")

def geocode_locations(text):
    """Extracts and geocodes locations from the given text."""
    doc = nlp(text)
    locations = []
    for ent in doc.ents:
        if ent.label_ == 'GPE':  # Geographic Political Entity
            location = geolocator.geocode(ent.text)
            if location:
                locations.append({'name': ent.text, 'lat': location.latitude, 'lon': location.longitude})
    return locations

# Streamlit app layout
st.title('📍🏖️ Craft Your Journey ✈️')
st.markdown("""
🎈 Embark on your next great adventure with us! Let's craft a travel experience that's as unique as you are. Welcome to your gateway to the world.
""")

with st.sidebar:
    st.header("Fill in Your Travel Information")
    destination = st.text_input("Destination", "e.g., Paris")
    num_people = st.number_input("Number of People", min_value=1, value=2)
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    budget_slider = st.slider("Budget (USD)", 500, 10000, 1500)
    budget_input = st.text_input("Or Enter Exact Budget", str(budget_slider))
    activity_level = st.selectbox("Activity Level", ["Low (Relaxing)", "Medium (Moderate Exploring)", "High (Adventurous)"])
    experience_types = st.multiselect("Experience Type", ["Cultural (Arts, History)", "Natural (Outdoors, Wildlife)", "Gastronomic (Food, Drinks)", "Recreational (Leisure, Shopping)"])
    personal_notes = st.text_area("Notes or Keywords", "Type your notes or specific interests here...")

# Collect detailed travel preferences
st.subheader("Detail Your Travel Preferences")
food_preference = st.selectbox("Your preference for food during travel:", ["Try local cuisine", "Stick to familiar foods", "A mix of both"])
accommodation_type = st.selectbox("Preferred type of accommodation:", ["Hotel", "Homestay", "Hostel", "Luxury Resort"])
activity_density = st.selectbox("How packed do you want your itinerary to be?", ["Packed with activities", "Relaxed, mainly for leisure"])
transport_preference = st.selectbox("Preferred mode of transportation during travel:", ["Public transport", "Rental car", "Walking or biking", "Private driver"])
shopping_interest = st.selectbox("Interest in shopping during travel:", ["Very interested", "Moderately interested", "Not interested"])

# Generate travel plan
if st.button('Generate Travel Plan'):
    # Conditional prompting based on activity level and detailed preferences
    activity_prompts = {
        "High (Adventurous)": "Include high-adrenaline activities like skydiving and mountain biking.",
        "Medium (Moderate Exploring)": "Include activities like hiking, city tours, and local experiences.",
        "Low (Relaxing)": "Focus on relaxing activities like spa visits and beach lounging."
    }
    detail_prompts = f"Food: {food_preference}, Accommodation: {accommodation_type}, Itinerary Density: {activity_density}, Transport: {transport_preference}, Shopping: {shopping_interest}."

    requirements = f"""
    Please create a travel plan for {num_people} people. Destination: {destination}, from {start_date} to {end_date}, with a budget of {budget_input} USD. {activity_prompts[activity_level]} {detail_prompts} Experience Types: {', '.join(experience_types)}, Notes: {personal_notes}.
    """
    response = model.generate_content(requirements)
    if response.text:
        st.subheader("Your Travel Plan")
        st.write(response.text)
        # Geocode locations from the generated plan
        locations = geocode_locations(response.text)
        if locations:
            df_locations = pd.DataFrame(locations)
            st.subheader("Mapped Locations")
            st.map(df_locations)
        else:
            st.write("No recognizable geographic locations found in the plan.")
    else:
        st.error("Failed to generate a travel plan, please check your input or try again later.")

# Geocoding with Geopy to visualize the destination
if destination:
    location = geolocator.geocode(destination)
    if location:
        st.map(data=pd.DataFrame({'lat': [location.latitude], 'lon': [location.longitude]}), zoom=11, use_container_width=True)
    else:
        st.error("Unable to find the specified location, please try different search terms.")

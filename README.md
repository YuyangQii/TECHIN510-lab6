# TECHIN510-lab6
## Introduction
Welcome to "Craft Your Journey", a personalized travel planning application designed to create unique and tailored travel experiences for each user. Utilizing a streamlined web interface built with Streamlit, this application leverages the powerful Google Generative AI and geocoding services to suggest customized travel plans based on user preferences.

## Features
- Personalized Travel Plans:  Generate travel plans that are not only based on the destination, number of people, budget, and travel dates but also enriched with detailed preferences regarding food, accommodation, and activities.
- User-Driven Customizations: Tailor your travel experience by specifying activity levels and types of experiences, such as cultural visits or outdoor adventures.
- Interactive Inputs: Choose your budget through an intuitive slider or enter a specific amount for precise control.
- Geocoding: Visualize your destination with an integrated map view to better plan your journey.
- Notes and Keywords: Add personal notes or keywords to focus the travel planning on your particular interests.

## Advanced Prompting Techniques Used
### Enhanced Detail with Context-Aware Prompting
Incorporating context-aware prompting techniques, the application now intelligently gathers user preferences regarding travel specifics such as accommodation, food preferences, activity levels, and transport options. By prompting users to input detailed preferences, the AI can tailor the travel plan more precisely, addressing specific aspects like:
- Food: Whether to try local cuisine or stick to familiar foods.
- Accommodation: Preferences among hotels, homestays, hostels, or luxury resorts.
- Activity Level: From relaxing to adventurous, matching the itinerary density with user activity preferences.
- Transport: Options ranging from public transport to private drivers, ensuring travel convenience.

## How to start
```bash
python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

## What I Learned
- API Integration: Enhanced skills in integrating external APIs (Google Generative AI and Geopy) to fetch and utilize dynamic data.
- User Interface Design: Developed an understanding of creating user-friendly and interactive web interfaces.

## Questions
How can we further personalize the recommendations based on user feedback during the trip?
What additional features could be integrated to enhance user engagement and utility?

## Next Steps
- Contextual Location Mapping: The higher accuracy of the location marked map, the current accuracy is limited
- Feedback Mechanism: Implement a feedback loop to refine travel recommendations based on user experiences.
- Social Sharing: Add functionality to share travel plans on social media directly from the application.
- Multilingual Support: Expand the app to support multiple languages to cater to a global audience.

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

# Prompt the user to enter a phone number
number = input("Enter a phone number in international format (e.g., +1234567890): ")

try:
    # Parse the phone number
    num = phonenumbers.parse(number, "CH")  # "CH" for country history (geolocation)
    
    # Get the geographic location of the number
    location = geocoder.description_for_number(num, "en")
    print(f"Location: {location}")

    # Get the carrier (service provider) of the number
    s_num = phonenumbers.parse(number, "RO")  # "RO" for carrier information
    service_provider = carrier.name_for_number(s_num, "en")
    print(f"Service Provider: {service_provider}")

except phonenumbers.phonenumberutil.NumberParseException as e:
    print(f"Error: {e}")
    print("Please provide a valid phone number in international format (e.g., +1234567890).")

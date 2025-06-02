import requests
import json

api_key='your_api_key'

def check_weather():
    print("Welcome to Weather Forecast")
    while(True):
        choice=int(input("Enter 1 to Start Enter 0 to quit : "))
        if choice==1:
            while(True):
                city=input("Enter your city name : ")
                url=f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&alerts=yes&aqi=yes"
                r=requests.get(url)
                w_dic=json.loads(r.text)
                print(f"\n{"-"*50}")
                print(f"\n🌍 Weather Forecast for {w_dic['location']['name']}, {w_dic['location']['region']}, {w_dic['location']['country']}")
                print(f"🕒 Local Time: {w_dic['location']['localtime']}")
                print(f"📅 Last Updated: {w_dic['current']['last_updated']}")
                print("\n🌤️  Current Conditions:")
                print(f"   - Condition: {w_dic['current']['condition']['text']}")
                print(f"   - Temperature: {w_dic['current']['temp_c']}°C (Feels like {w_dic['current']['feelslike_c']}°C)")
                print(f"   - Humidity: {w_dic['current']['humidity']}%")
                print(f"   - Wind: {w_dic['current']['wind_kph']} km/h ({w_dic['current']['wind_dir']})")
                print(f"   - Pressure: {w_dic['current']['pressure_mb']} mb")
                print(f"   - Cloud Cover: {w_dic['current']['cloud']}%")
                print(f"   - Visibility: {w_dic['current']['vis_km']} km")
                print(f"   - UV Index: {w_dic['current']['uv']}")

                print("\n🌫️  Air Quality Index (US EPA):")
                aq = w_dic['current']['air_quality']
                epa_index = aq['us-epa-index']
                epa_meaning = {
                    1: "Good",
                    2: "Moderate",
                    3: "Unhealthy for Sensitive Groups",
                    4: "Unhealthy",
                    5: "Very Unhealthy",
                    6: "Hazardous"
                }.get(epa_index, "Unknown")

                print(f"   - AQI Category: {epa_meaning} ({epa_index})")
                print(f"   - PM2.5: {aq['pm2_5']} µg/m³")
                print(f"   - PM10: {aq['pm10']} µg/m³")
                print(f"   - CO: {aq['co']} µg/m³")
                print(f"   - NO₂: {aq['no2']} µg/m³")
                print(f"   - SO₂: {aq['so2']} µg/m³")
                print(f"   - O₃: {aq['o3']} µg/m³")
                
                search_again=int(input("\n Do you want to search for some other cities : \nEnter 1 for Yes and Enter 0 to Go back to main menu : "))
                if search_again==1:
                    continue
                elif search_again==0:
                    print("\nGoing Back to Main Menu ...")
                    break
        if choice==0:
            print("\nExiting the Program ... ")
            exit()

check_weather()
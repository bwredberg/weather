import requests

class weather():

    def __init__(self, location, lat, lon):
        self.Location = location
        self.LocationResult = requests.get("https://api.weather.gov/points/"+str(lat)+','+str(lon))
        if self.LocationResult.ok:
            ForecastURL = self.LocationResult.json()['properties']['forecast']
            Forecast = requests.get(ForecastURL)
            MyForecast = Forecast.json()['properties']['periods']
            self.Temp = MyForecast[0]['temperature']
            self.TimePeriod = MyForecast[0]['name']
            self.TempUnit = MyForecast[0]['temperatureUnit']  
        else:
            print(f'There was an error retrieving the weather for {self.Location}')
    
    def output(self):
        print(f'The temperature is {self.Temp}{self.TempUnit} for {self.Location}')

class news():

    def __init__(self):
        #Location attributes
        Locations = [{'Name': 'Chicago', 'lon': 41.882840862431166, 'lat': -87.62335753749558}, 
                     {'Name': 'Minneapolis', 'lon': 44.97617932522657, 'lat': -93.396401437746}, 
                     {'Name': 'San Francisco', 'lon': 37.79362784291553, 'lat': -122.42274272249323}, 
                     {'Name': 'New York City', 'lon': 40.74937114004021, 'lat': -73.96746736362712}]

        LocList = []
        for Location in Locations:
            LocList.append(weather(Location['Name'], Location['lon'], Location['lat']))
        for Loc in LocList:
            Loc.output()

news()





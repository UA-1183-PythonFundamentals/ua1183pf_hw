import requests
import os

class Country:
    def __init__(self, name: str):
        self.__name = name
        self.api_key = os.environ.get('COUNTRYAPI_KEY')
                
    def get_country_info(self):
        try:
            url = f'https://countryapi.io/api/name/{self.__name}?apikey={self.api_key}'
            response = requests.get(url)
            data = response.json()
            
            for country_code in data.keys():
                data = data[country_code]
                        
            official_name = data["official_name"]
            calling_code = data["callingCode"]
            capital = data["capital"]
            region = data["region"]
            subregion = data["subregion"]
            population = data["population"]
            area = data["area"]
            timezones = ', '.join(data["timezones"])
            
            currencies_dict = data["currencies"]
            lang_dict = data["languages"]
            
            # Currencies
            currencies = []
            for inner_dict in currencies_dict.values():
                name_value = inner_dict.get('name')
                if name_value is not None:
                    currencies.append(name_value)
            
            currencies = ', '.join(currencies)
            
            # Lang
            lang_values = list(lang_dict.values())
            lang_string = ', '.join(lang_values)
                    
            
            result = f"Official name: {official_name}\n Capital: {capital}\n Region: {region}\n Subregion: {subregion}\n Calling code: {calling_code}\n Population: {population}\n Area of country: {area}\n Timezone: {timezones}\n Currencies: {currencies}\n Language: {lang_string}"
            
            return result
        except Exception as e:
            return "Country not found"

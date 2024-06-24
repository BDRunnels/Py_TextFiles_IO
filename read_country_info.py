file_name = "country_info.txt"
countries = {}  # empty dict

with open(file_name) as country_file:
    country_file.readline()  # reading header info, no need to parse it
    for row in country_file:
        data = row.strip("\n").split("|")  # split returns a list of string
        # print(data)
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep="\n\t")
        country_dict = {
            "name": country,
            "capital": capital,
            "country_code": code,
            "cc3": code3,
            "dialing_code": dialing,
            "timezone": timezone,
            "currency": currency,
        }
        # print(country_dict)

        #  ASSIGNING TWO KEYS TO country_dict data
        countries[country.casefold()] = country_dict
        countries[code.casefold()] = country_dict

print(countries)

while True:
    print("Please enter a country to find its capital (quit to exit):")
    input_country = input().casefold().strip()
    if input_country in countries:
        print(f"The capital of {countries[input_country]["name"]} is {countries[input_country]["capital"]}")
    elif input_country == "quit":
        break

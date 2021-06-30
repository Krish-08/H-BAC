import urllib.request, json
import urllib3
import time
class json_api:
#$$$$$$/$$$$$$  GET_JSON FROM the API
    def __init__(self):
        start=time.perf_counter()
        try:
            with urllib.request.urlopen("https://api-hospitals-beds-data.herokuapp.com/",timeout=10) as url:
                print("got data in:",time.perf_counter()-start)
                source = urllib3.response.GzipDecoder().decompress(url.read())
                data = json.loads(source)
                print("got data in:",time.perf_counter()-start)
                file_json = open("hospital_data.json", "w")
                json.dump(data, file_json, indent=4)
                file_json.close()

                file_json = open('hospital_data.json', "r")
                self.api_dict_available_beds = json.load(file_json)

        except Exception as e:
            print(e)
            file_json = open('hospital_data.json', "r")
            print("error.So json file is used")
            self.api_dict_available_beds=json.load(file_json)

            file_json.close()



        dict_of_districts={}
        for s_no,district in self.api_dict_available_beds.get('District').items():
            if district in dict_of_districts:
                dict_of_districts[district].append(s_no)
            else:
                dict_of_districts[district]=[s_no]
        self.api_dict_available_beds['district_sorted_hospital']=dict_of_districts
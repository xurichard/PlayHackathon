import rauth
import time

def main():
    businesses = "cheese-board-pizza-berkeley"
    #api_calls = []
    #for name in businesses:
    #    api_calls.append(get_results_biz(name))
    #    #Be a good internet citizen and rate-limit yourself...ya know for the 10000 limit
    #    time.sleep(1.0)

    biz_results = get_results_biz(businesses)


#********************** search ***********************************
def get_results_search(params):

    #Obtain these from Yelp's manage access page
    consumer_key = "T6oxIDFDjd_Trndvy0JJdg"
    consumer_secret = "T02tOkCFPNGgnIcETvmafZqkUtw"
    token = "DPf_lZC5RUuu1loK_UlxdrggiCqqfXtY"
    token_secret = "RExgE2xBkoKrA_LeLMB9tYs6-Ts"
    
    session = rauth.OAuth1Session(
        consumer_key = consumer_key
        ,consumer_secret = consumer_secret
        ,access_token = token
        ,access_token_secret = token_secret)
        
    request = session.get("http://api.yelp.com/v2/search",params=params)

    #Transforms the JSON API response into a Python dictionary
    data = request.json()
    session.close()
    
    return data

def get_search():
    locations = [(39.98,-82.98)]#,(42.24,-83.61),(41.33,-89.13)]
    api_calls = []
    for lat,long in locations:
        params = get_search_parameters(lat,long)
        api_calls.append(get_results_search(params))
        #Be a good internet citizen and rate-limit yourself...ya know for the 10000 limit
        time.sleep(1.0)



def get_search_parameters(lat,long):
    #See the Yelp API for more details
    params = {}
    params["term"] = "restaurant"
    params["ll"] = "{},{}".format(str(lat),str(long))
    params["radius_filter"] = "2000"
    params["limit"] = "10"

    return params


#********************** biz *******************************

def get_results_biz(id):

    #Obtain these from Yelp's manage access page
    consumer_key = "T6oxIDFDjd_Trndvy0JJdg"
    consumer_secret = "T02tOkCFPNGgnIcETvmafZqkUtw"
    token = "DPf_lZC5RUuu1loK_UlxdrggiCqqfXtY"
    token_secret = "RExgE2xBkoKrA_LeLMB9tYs6-Ts"
    
    session = rauth.OAuth1Session(
        consumer_key = consumer_key
        ,consumer_secret = consumer_secret
        ,access_token = token
        ,access_token_secret = token_secret)

    request = session.get("http://api.yelp.com/v2/business/" + id)


    #Transforms the JSON API response into a Python dictionary
    data = request.json()
    session.close()
    
    return data

if __name__=="__main__":
    main()
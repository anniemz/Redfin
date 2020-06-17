from redfin import RedFin

redfin = RedFin()
redfin.start_url = "https://www.redfin.com/city/13654/CA/Oakland"
redfin.get_search_results()
redfin.get_property_data()

#TODO add proxy.txt and support for proxies, redfin blocked ip address last time
#TODO scraper did not find address, price or redfin estimate lastime. check parcel parser
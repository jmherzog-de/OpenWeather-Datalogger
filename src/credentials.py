"""
mongodb database parameters
"""
db_host = '127.0.0.1'
db_port = '27017'
db_name = 'weathercrawler'
db_user = ''
db_pass = ''

"""
weather locations list
"""
glb_locations = []

"""
API parameters
"""
api_code = ''  # your API key
lang = 'de'
base_url = 'http://api.openweathermap.org/data/2.5/weather?'
req_recon_time = 10  # seconds until next request try if connection failed

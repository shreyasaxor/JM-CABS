import googlemaps

gmaps = googlemaps.Client(key='AIzaSyAwS1dG9Y5vT_F3jcul4d2C69nRsroOVOE')
local = gmaps.distance_matrix('mysore' ,'jaipur')
print local['rows'][0]['elements'][0],"fffffffffffffffffffff"

if local['status']=='OK':
    print local['rows'][0]['elements'][0]['distance']['text']
else:
    print local['statuss']
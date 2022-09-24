import requests


def nasa(date_start, date_end, limit):
    data = requests.get('https://api.nasa.gov/neo/rest/v1/feed',
                        {'api_key': 'DEMO_KEY', 'start_date': date_start, 'end_date': date_end}).json()
    objects = data['near_earth_objects']

    for i in objects:
        unsorted = list()
        for a in objects[i]:
            d = {'name': a["name"], 'absolute_magnitude_h': a["absolute_magnitude_h"],
                 'is_potentially_hazardous_asteroid': a["is_potentially_hazardous_asteroid"],
                 'neo_reference_id': a["neo_reference_id"]}
            unsorted.append(d)
        objects[i] = sorted(unsorted, key=lambda item: item['absolute_magnitude_h'], reverse=True)[:limit]

    for i in objects:
        for a in objects[i]:
            h = a.pop("neo_reference_id")
            print(i, h, a)


nasa('2015-09-07', '2015-09-08', 5)

import json
from botocore.vendored import requests


def lambda_handler(event, context):
    # TODO implement
    response = requests.get("https://pokeapi.co/api/v2/pokemon/");
    j = json.loads(response.content.decode('utf-8'));

    pokemon = "";
    for index, item in enumerate(j["results"]):
        print("this is item: ", item['name']);
        print("this is pokeID", item['url'].rsplit('/',2)[1]);
        pokemon += item['name'];
        pokemon += ": ";
        pokemon += item['url'].rsplit('/',2)[1];
        #print(item['type']['name'], end="");
        if index+1 is not len(j['results']):
            pokemon += " | ";
    return pokemon.format()

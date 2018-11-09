import json
from botocore.vendored import requests
import logging

#LOGGER = logging.getLogger()
#LOGGER.setLevel(logging.INFO)


def lambda_handler(event, context):
    # TODO implement
    #LOGGER.info(event);
    poke = event['params']['path']['operand'];

    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + poke);
    j = json.loads(response.content.decode('utf-8'));
    # Print the status code of the response.
    #print(response.status_code);
    #print(len(j['types']));
    types = "";
    for index, item in enumerate(j["types"]):
        types += item['type']['name'];
        #print(item['type']['name'], end="");
        if index+1 is not len(j['types']):
            types += ",";
            #print(",",end="");
    return types


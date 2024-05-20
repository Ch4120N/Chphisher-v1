import json



def Read_Setting(varibale:str):
    """Read The Configuaration File `Settings.json`
    You can use this indexes for varibale of `Settings.json` file
    `website`, `mask`, `processed_url`

    Args:
        varibale (str): `website`, `mask`, `processed_url`

    Returns:
        string: website url | website mask | proccessed url
    """
    with open('Settings.json', 'r') as file:
        file_data = file.read()
        data = json.loads(file_data)
    
    return str(data[varibale])



def Write_Setting(varibale:str, value:str):
    """Write Settings On `Settings.json`

    Args:
        varibale (str): Variable of json file ['mask', 'website', 'processed_url']
        value (str): any thing yo want but recommended application set
    """
    with open('Settings.json', 'r') as filer:
        file_data = filer.read()

        data = json.loads(file_data)
    
    data[varibale] = value
    # print(data)

    with open('Settings.json', 'w') as filew:
        filew.write(json.dumps(data, indent=2, sort_keys=True))
        filew.close()


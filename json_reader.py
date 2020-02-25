import twitter2


def recursively_parse_json(input_json, input_key):
    """
    function finds every value for input_key from
    json file
    """
    if type(input_json) is dict:
        for key in input_json:
            if key == input_key:
                print(input_json[key])
            recursively_parse_json(input_json[key], input_key)
    elif type(input_json) is list:
        for dct in input_json:
            recursively_parse_json(dct, input_key)


if __name__ == "__main__":
    user_name = input("Enter twitter account: ")
    json_dct = twitter2.twit(user_name)
    key_input = input('Please write a key you want to get value of: ')
    print(recursively_parse_json(json_dct, key_input))



import json

import requests as requests


def main():
    data = {
        'username': 'james',
        'active': True,
        'subscribers': 10,
        'order_total': 39.99,
        'order_ids': ['ABC123', 'QQQ442', 'LOL300']
    }

    print(data)

    # Printing object as JSON string
    s = json.dumps(data)
    print(s)

    # Getting Python object from JSON string
    data2 = json.loads(s)
    assert data2 == data

    # Write JSON data in a file
    with open('data/test_data.json', 'w') as f:
        json.dump(data, f)

    # Read JSON data from a file
    with open('data/test_data.json', 'r') as f:
        data3 = json.load(f)

    assert data3 == data

    r = requests.get('https://jsonplaceholder.typicode.com/users')
    print(r.json())


if __name__ == '__main__':
    main()

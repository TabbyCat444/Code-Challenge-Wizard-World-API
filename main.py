import requests
from pprint import pprint
from collections import Counter

# call api
response = requests.get("https://wizard-world-api.herokuapp.com/Wizards").json()

# count elixirs
wizard_list = response
elixir_list = {}
for wizard in wizard_list:
    for elixir in wizard['elixirs']:
        if elixir['name'] not in elixir_list:
            elixir_list[elixir['name']] = 1
        else:
            elixir_list[elixir['name']] = elixir_list[elixir['name']] + 1

# get top three elixirs
alpha_order = dict(sorted(elixir_list.items()))
elixir_count = Counter(alpha_order)
three_elixirs = dict(elixir_count.most_common(3))

# print top three elixirs with appropriate format
print("Top Three Elixirs:")
for key, value in three_elixirs.items():
    print(str(value) + " wizards have the elixir " + key + ".")

# get most common elixir side effects


# print("The top elixir " + [name] + " has the side effect of " + [side effect] + ".")

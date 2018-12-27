import json

a = range(1, 5)
b = ['santosh', 'sunil', 'suzina', 'bibek']

# dir(__builtins__) => View built-in functions/errors
d = dict(zip(a ,b))

# Convert to json object
# Similar to dictionary but, key and value are in "" and dictionary itself is inside ''
# i.e '{"Key":"Value"}'
j = json.dumps(d)

# This convert json to dictionary but, key are retrieved as string
j_to_d = json.loads(j)
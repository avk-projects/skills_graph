import pickle
import json
with open('formatted_tags.pkl', 'rb') as f:
    data = pickle.load(f)

    with open('formatted_tags.json', 'w') as f:
        json.dump(data, f)
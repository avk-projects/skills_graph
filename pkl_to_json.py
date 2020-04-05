import pickle
import json

with open('formatted_tags.pkl', 'rb') as f:
    data = pickle.load(f)

    nodes_dict = dict()
    nodes = []
    links = []

    for pair_to_copy in data.keys():
        pair = [None, None]
        pair[0] = pair_to_copy[0].lower()
        pair[1] = pair_to_copy[1].lower()

        links.append({"source": pair[0],"target": pair[1],"value": data[pair_to_copy]})

        if pair[0] not in nodes_dict:
            nodes_dict[pair[0]] = data[pair_to_copy]
        else:
            nodes_dict[pair[0]] += data[pair_to_copy]

        if pair[1] not in nodes_dict:
            nodes_dict[pair[1]] = data[pair_to_copy]
        else:
            nodes_dict[pair[1]] += data[pair_to_copy]

    for node in nodes_dict:
        nodes.append({"id": node, "group": int(nodes_dict[node]/500), "popularity": nodes_dict[node]})

    data_to_dump = {"nodes": nodes, "links": links}
    # data_to_dump.nodes = nodes
    # data_to_dump.links = links

    print(data_to_dump)

    with open('formatted_tags.json', 'w') as f:
        json.dump(data_to_dump, f)
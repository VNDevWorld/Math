import json
import re

with open('test_data_new.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def clean_node(node):
    if isinstance(node, dict):
        for k, v in node.items():
            if isinstance(v, str) and k.endswith("String"):
                # if it starts with [EN], [FR], etc. followed by space
                if re.match(r'^\[.*?\]\s*', v):
                    node[k] = re.sub(r'^\[.*?\]\s*', '', v)
            elif isinstance(v, (dict, list)):
                clean_node(v)
    elif isinstance(node, list):
        for item in node:
            clean_node(item)

clean_node(data)

with open('test_data_new.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Cleaned up remaining prefixes")

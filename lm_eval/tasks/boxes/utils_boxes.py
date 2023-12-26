# Copied from Master
def doc_to_text(doc) -> str:
    prompt = '''Given the description after "Description:", write a true statement about all boxes and their contents to the description after "Statement:".
    
    Description: Box 0 contains the car, Box 1 contains the cross, Box 2 contains the bag and the machine, Box 3 contains the paper and the string, Box 4 contains the bill, Box 5 contains the apple and the cash and the glass, Box 6 contains the bottle and the map.
    Statement: Box 0 contains the car, Box 1 contains the cross, Box 2 contains the bag and the machine, Box 3 contains the paper and the string, Box 4 contains the bill, Box 5 contains the apple and the cash and the glass, Box 6 contains the bottle and the map.
    
    Description: Box 0 contains the car, Box 1 contains the cross, Box 2 contains the bag and the machine, Box 3 contains the paper and the string, Box 4 contains the bill, Box 5 contains the apple and the cash and the glass, Box 6 contains the bottle and the map. Remove the car from Box 0. Remove the paper and the string from Box 3. Put the plane into Box 0. Move the map from Box 6 to Box 2. Remove the bill from Box 4. Put the coat into Box 3.
    Statement: Box 0 contains the plane, Box 1 contains the cross, Box 2 contains the bag and the machine and the map, Box 3 contains the coat, Box 4 contains nothing, Box 5 contains the apple and the cash and the glass, Box 6 contains the bottle.
    
    Description: '''
    desc = doc["sentence"].split('.')
    desc = [s.strip() for s in desc if s]
    desc = '. '.join(desc[:-1])
    prompt = prompt + desc + '\nStatement: Box 0 contains '
    return prompt


def doc_to_target(doc) -> str:
    desc = doc["sentence"].split('.')
    desc = [s.strip() for s in desc if s]
    statement = desc[-1]
    return statement
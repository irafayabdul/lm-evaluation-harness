from lm_eval.api.filter import Filter


class BoxesFilter(Filter):
    def __init__(self) -> None:
        pass

    def apply(self, resps, docs):
        def filter_set(inst, query):
            qu = query['sentence_masked'].split('.')
            qu = [s.strip() for s in qu if s]
            qu = qu[-1]
            qu = qu.split(' <extra_id_0>')[0]

            it = inst[0].split(',')
            it = [item for item in it if qu in item][-1]
            it = extract_words_after_the(it)
            it = ' '.join(it)
            return it

        return [filter_set(resp, doc) for resp, doc in zip(resps, docs)]


def extract_words_after_the(text):
    words = text.split()
    extracted_words = [words[i+1] for i in range(len(words)-1) if words[i].lower() == 'the']
    return extracted_words


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
    statement = extract_words_after_the(statement)
    statement = ' '.join(statement)
    return statement


def boxes_filter():
    return BoxesFilter()
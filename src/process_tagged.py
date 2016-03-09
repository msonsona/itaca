#!/usr/bin/python3
import json

with open('itaca_tagged.txt', 'r', encoding='utf-8') as tagged_file:
    word_pos = {}
    
    for line in tagged_file:
        splits = line.split()
        # If can't obtain PoS tag, continue
        if len(splits) < 3:
            continue
        
        word, lemma, pos_tag, prob = splits[0:4]
        
        if pos_tag not in word_pos:
            word_pos[pos_tag] = []
        
        word_pos[pos_tag].append(word)
    
    print(word_pos)
    print(json.dumps(word_pos, sort_keys=True, indent=4))
    print(json.dumps(word_pos, sort_keys=True))


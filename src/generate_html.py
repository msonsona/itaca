#!/usr/bin/python3

with open('itaca_tagged.txt', 'r', encoding='utf-8') as tagged_file:
    
    for line in tagged_file:
        splits = line.split()
        # If can't obtain PoS tag, continue
        if len(splits) < 3:
            continue
        
        word, lemma, pos_tag, prob = splits[0:4]
        
        print('<span data-pos-tag="{}">{}</span>'.format(pos_tag, word))


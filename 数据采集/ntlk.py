# -*- coding: utf-8 -*-
# time:2023/4/27 20:37
# file ntlk.py
# outhor:czy
# email:1060324818@qq.com


from nltk import word_tokenize, sent_tokenize, pos_tag
sentences = sent_tokenize("Google is one of the best companies in the world.I constantly google myself to see what I'm up to.")

nouns = ['NN', 'NNS', 'NNP', 'NNPS']
for sentence in sentences:
    if "google" in sentence.lower():
        taggedWords = pos_tag(word_tokenize(sentence))
        for word in taggedWords:
            if word[0].lower() == "google" and word[1] not in nouns:
                print(sentence)
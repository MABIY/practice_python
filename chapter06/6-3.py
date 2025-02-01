from multiprocessing.pool import worker

glossary = {
    'string':'A series of characters.',
    'comment':'A note in a program that the python interpreter ignores.',
    'list':'A collection of items in a particular order.',
    'loop':'Word through a collection of items, one at a time.',
    'dictionary':'A collection of key-value pairs.'
}



def world_meaning_pair(word:str):
    print(f"\n{word.title()}: {glossary[word]}")


world_meaning_pair('string')
world_meaning_pair('comment')
world_meaning_pair('list')
world_meaning_pair('loop')
world_meaning_pair('dictionary')

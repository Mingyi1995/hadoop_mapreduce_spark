import sys

''' A simple map reduce program '''
''' Input - Split - Map - Combine - Partition - Reduce '''

def mapper():
    with open(sys.argv[1], 'r') as file:
        words = []
        for line in file:
            line = line.strip()
            words.extend(line.split())
        return words

def reducer(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for k,v in word_count.items():
        print(k, v)

if __name__ == '__main__':
    reducer(mapper())

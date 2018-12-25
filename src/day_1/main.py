from collections import Counter
import sys
import checkSummer

if __name__ == "__main__":
    collection_dict = {2:0,3:0}
    with open(sys.argv[1]) as f:
        for line in f:
            collection_dict = checkSummer.dict_adder(collection_dict, checkSummer.box_2_3_counts(Counter(list(line.strip()))))
    print(collection_dict[2] * collection_dict[3])
def extractName(list):
    rlist = [x.split(' ')[-1] for x in list]
    return rlist

if __name__ == '__main__':
    print(extractName(['2 Foxs', '1 Hyena', ' 1 Wolf', '5 Lions', '3 Cheetahs', '3 Lions', '2 Wolfs', '3 Foxs', '1 Fox', ' 2 Hyenas', '1 Wolf', '4 Hyenas', '2 Tigers', '2 Lions', '1 Lion', '3 Wolfs', '1 Cheetah', ' 1 Lion', '2 Cheetahs', ' 1 Tiger', '4 Cheetahs', '(no detections)', ' 1 Hyena', '4 Lions', '2 Hyenas', ' ', '1 Tiger', ' 2 Wolfs','4 Wolfs']))
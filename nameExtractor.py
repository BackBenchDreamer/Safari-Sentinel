def extractName(list):
    nlist = [x.split(' ')[-1] for x in list if len(x.split(' ')[-1])>0]
    return nlist

if __name__ == '__main__':
    print('Code to be imported in different file.')

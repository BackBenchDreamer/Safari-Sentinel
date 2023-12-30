def extractName(list):
    nlist = [x.split(' ')[-1] for x in list if len(x.split(' ')[-1])>0]
    rlist = [x+'s' if x[-1] != 's' else x for x in nlist]
    return rlist

if __name__ == '__main__':
    print('Code to be imported in different file.')

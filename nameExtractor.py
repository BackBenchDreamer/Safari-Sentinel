def extractName(list):
    nlist = [' '.join([y for y in x.split(' ') if not y.isdigit()]) for x in list if len(x.split(' ')[-1])>0]
    rlist = [x+'s' if x[-1] != 's' else x for x in nlist]
    return rlist

if __name__ == '__main__':
    print('Code to be imported in different file.')

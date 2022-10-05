with open('test.log') as log:
    log_list = log.readlines()
    ix = 0
    save = []

def search(index):
    count = 0
    if not index:
        list_ = log.readlines()
    else:
        list_ = log.readlines()[index:]
        for index, el in enumerate(list_):
            if 'Request: ValidateRouteID_ALCO' in el:
                ix = index
            if 'Request: GetPalletIDs' in el:
                save.append(list_[ix])
                save.append(el)
                save.append(list_[index+1])
                return
        count += 1

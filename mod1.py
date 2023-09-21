'''
Docstring: this module contains binary search implementation


'''

def binary_search(l,key):

    '''
    binary search : input a list and key return True if key exist else return false
    :param l:
    :param key:
    :return:
    '''
    mid = len(l) // 2

    if l[mid] == key:
        return True
    elif key < l[mid]:
        return binary_search(l[:mid],key)
    else:
        return binary_search(l[mid + 1:],key)


print(__name__)
if __name__ == '__main__':
  l=[100,200,300,400,500,600,700,800,900]
  key=500
  result = binary_search(l,key)
  print(result)
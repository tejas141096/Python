#Binary Search

def binarysearch(my_list,low,high,to_search):
    if(low>high):
        return -1

    mid=(low+high)//2
    if(my_list[mid]==to_search):
        return mid

    if(my_list[mid]>to_search):
        return binarysearch(my_list,low,mid-1,to_search)
    else:
        return binarysearch(my_list,mid+1,high,to_search)

def main():
    #my_list=[1,2,3,4,5,6,7,8,9,10]
    my_list=[1,3,5,7,9,11,13,15]
    n=len(my_list)
    to_search=(int)(input("Enter number to search: "))
    position=binarysearch(my_list,0,n-1,to_search)
    try:
        if(position==-1):
            raise ValueError('The input value was not found in the list.')
        else:
            print(f"Found {to_search} at index position {position}")
    except ValueError as valerror:
        print(f"#1: "+repr(valerror))

if __name__=="__main__":
    main()

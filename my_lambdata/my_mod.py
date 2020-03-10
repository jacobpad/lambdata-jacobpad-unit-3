# my_lambdata/my_mod.py
def ten_x(num):
    '''
    Takes 'n' and multiplies it by 10
    '''
    return num * 10
    
def check_null(df):
    '''
    Checks for null's
    '''
    return df.isnull().sum()



# def enlarge(n):
#     '''
#     Param n is a number
#     Function will enlarge the number
#     '''
#     return n * 10


# # this code breaks our ability to import enlarge from other files
# #
# # print("HELLO")
# # y = int(input("Please choose a number"))
# # print(y, enlarge(y))

# if __name__ == "__main__":
#     # only run the code below IF this script is invoked from the command-line
#     # not if it is imported from another
#     print("HELLO")
#     y = int(input("Please choose a number"))
#     print(y, enlarge(y))
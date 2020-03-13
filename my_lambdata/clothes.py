class Polo():
    '''
    A class to create Polo shirts, not the game.
    '''
    
    def __init__(self, style, size, color):
        '''
        The init for Polo
        '''
        self.style = style
        self.size = size
        self.color = color
        
    def pop_collar(self):
        '''
        PARAM: none
        PURPOSE: Prints 'Time to pop the collar'
        RETURNS: What's printed above
        '''
        print('Time to pop the collar')

if __name__ == '__main__':

    polo1 = Polo(style='Poly', size='XXLT', color='Black')
    print(type(polo1))
    print(polo1.style)
    print(polo1.size)
    print(polo1.color)
    print(polo1.pop_collar())

    polo2 = Polo(style='Cotton', size='M', color='Navy Blue')
    print(type(polo2))
    print(polo2.style)
    print(polo2.size)
    print(polo2.color)
    print(polo2.pop_collar())
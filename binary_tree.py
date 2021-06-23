class Binary:
    
    def __init__(self):
        pass

    def parse(self, l, index = 0):
        root_index = 2**index
        root = l[root_index]
        left = l[root_index + 1]
        right = l[root_index + 2]

        if len(l[2**index:]) > 0:
            self.parse(l, )
        else:
            if root == '+':
                print('Left: ' + left + ' , ' + 'Root: ' + root + ' , ' + 'Right: ' + right )
                return left + right
            elif root == '-':
                print('Left: ' + left + ' , ' + 'Root: ' + root + ' , ' + 'Right: ' + right )
                return left - right
            elif root == '*':
                print('Left: ' + left + ' , ' + 'Root: ' + root + ' , ' + 'Right: ' + right )
                return left * right
            else:
                print('Left: ' + left + ' , ' + 'Root: ' + root + ' , ' + 'Right: ' + right )
                return left/right



binary = Binary()
binary.parse(['/','*','+','+',4,'-',2,3,1,'', '', 9, 5, '', ''])


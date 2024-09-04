
def checkTwoChessboards(coordinate1: str, coordinate2: str) -> bool:
    
    set1 = {'a', 'c', 'e', 'g'}
    set2 = {'b', 'd', 'f', 'h'}

    set_even = {'1', '3', '5', '7'}
    set_odd =  {'2', '4', '6', '8'}

    color1 = ''
    color2 = ''

    if coordinate1[0] in set1:
        if coordinate1[1] in set_odd:
            color1 = 'black'
        else:
            color1 = 'white'
    elif coordinate1[0] in set2:
        if coordinate1[1] in set_even:
            color1 = 'black'
        else:
            color1 = 'white'
    
    if coordinate2[0] in set1:
        if coordinate2[1] in set_odd:
            color2 = 'black'
        else:
            color2 = 'white'
    elif coordinate2[0] in set2:
        if coordinate2[1] in set_even:
            color2 = 'black'
        else:
            color2 = 'white'
    
    if color1==color2:
        return True
    else:
        return False

        


if __name__ == "__main__":
    coordinate1 = "a1"
    coordinate2 = "h3"

    result = checkTwoChessboards(coordinate1, coordinate2)
    print(result)
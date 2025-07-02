RE ***"
    if label(t) == 'berry':
        return True
    for branch in branches(t):
        if branch == 'berry':
            return True
    return False    
    


HW_SOURCE_FILE=__file__
'''
problem:
given a series of buildings with west-facing windows, 
process buildings in east-to-west order and return
the set of buildings that view the sunset

W -> *sun* [1 3 2 5 4 6]  <- E
passed as [6 4 5 2 3 1]
should return [6 5 3 1]

solution:
maintain a stack of building heights. as we proceed
along (in an E-W order), if the height of a new building
exceeds the top of the stack, pop until it doesn't
then return the stack
'''
def which_buildings(arr):
    building_stack = [-1]

    for b in arr:
        while (len(building_stack) > 0) and (b >= building_stack[-1]):
            building_stack.pop()
        building_stack.append(b)
    
    return building_stack

if __name__ == "__main__":
    ew_order = [6, 4, 5, 2, 3, 1]
    print(which_buildings(ew_order))

    ew_order = [1, 2, 3, 4, 5, 6]
    print(which_buildings(ew_order))

    ew_order = [1, 1, 1]
    print(which_buildings(ew_order))
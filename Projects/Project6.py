'''

Water jugs project

Michael Streyle

'''
#!/usr/bin/env python3
#encoding: UTF-8


JUG_1_MAX = 5
JUG_2_MAX = 3


class State:
    '''State of the jugs'''
    def __init__(self, jug_1: int, jug_2: int):
        '''__init__'''
        self.jstate1 = jug_1
        self.jstate2 = jug_2
        self.jgoal1 = 4
        self.jgoal2 = 0

    def __eq__(self, other: object):
        '''__eq__'''
        if self.jstate1 == other.jstate1:
            return self.jstate2 == other.jstate2
                

    def __str__(self):
        '''__str__'''
        return "(" + str(self.jstate1) +', ' + str(self.jstate2) + ')'

    def clone(self):
        '''clone a state'''
        clon = State(self.jstate1, self.jstate2)
        return clon

    def fill_jug_1(self):
        '''Fill jug1 to capacity from the pump'''
        self.jstate1 = JUG_1_MAX

    def fill_jug_2(self):
        '''Fill jug2 to capacity from the pump'''
        self.jstate2 = JUG_2_MAX

    def empty_jug_1(self):
        '''Pour the water from jug1 onto the ground'''
        self.jstate1 = 0

    def empty_jug_2(self):
        '''Pour the water from jug2 onto the ground'''
        self.jstate2 = 0

    def pour_jug_1_to_jug_2(self):
        '''Pour as much water as you can from jug1 to jug2 without spilling'''
        diff = JUG_2_MAX - self.jstate2
        if self.jstate1 <= diff:
            self.jstate2 += self.jstate1
            self.jstate1 = 0
        else:
            self.jstate2 += diff
            self.jstate1 -= diff
        

    def pour_jug_2_to_jug_1(self):
        '''Pour as much water as you can from jug2 to jug1 without spilling'''
        diff = JUG_1_MAX - self.jstate1
        if self.jstate2 <= diff:
            self.jstate1 += self.jstate2
            self.jstate2 = 0
        else:
            self.jstate1 += diff
            self.jstate2 -= diff


def search(start_state: object, goal: object, moves_lst: list):
    '''Find a sequence of states'''
    moves_lst.append(start_state)
    new_state = start_state.clone()
    new_state.fill_jug_1()
    if new_state.__eq__(goal):
        moves_lst.append(new_state)
        return
    if new_state in moves_lst:
        pass
    else:
        search(new_state, goal, moves_lst)

    new_state = start_state.clone()
    new_state.fill_jug_2()
    if new_state.__eq__(goal):
        moves_lst.append(new_state)
        return
    if new_state in moves_lst:
        pass
    else:
        search(new_state, goal, moves_lst)

    new_state = start_state.clone()
    new_state.pour_jug_1_to_jug_2()
    if new_state.__eq__(goal):
        moves_lst.append(new_state)
        return
    if new_state in moves_lst:
        pass
    else:
        search(new_state, goal, moves_lst)

    new_state = start_state.clone()
    new_state.pour_jug_2_to_jug_1()
    if new_state.__eq__(goal):
        moves_lst.append(new_state)
        return
    if new_state in moves_lst:
        pass
    else:
        search(new_state, goal, moves_lst)

    new_state = start_state.clone()
    new_state.empty_jug_1()
    if new_state.__eq__(goal):
        moves_lst.append(new_state)
        return
    if new_state in moves_lst:
        pass
    else:
        search(new_state, goal, moves_lst)

    new_state = start_state.clone()
    new_state.empty_jug_2()
    if new_state.__eq__(goal):
        moves_lst.append(new_state)
        return
    if new_state in moves_lst:
        pass
    else:
        search(new_state, goal, moves_lst)
    

def main():
    '''Main function'''
    goal = State(4, 0)
    start = State(0, 0)
    moves = []
    search(start, goal, moves)
    print(', '.join([str(s) for s in moves]))


if __name__ == '__main__':
    main()
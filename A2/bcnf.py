# Counts the number of steps required to decompose a relation into BCNF.

from relation import *
from functional_dependency import *
import re

# You should implement the static function declared
# in the ImplementMe class and submit this (and only this!) file.
# You are welcome to add supporting classes and methods in this file.
class ImplementMe:

    # Returns the number of recursive steps required for BCNF decomposition
    #
    # The input is a set of relations and a set of functional dependencies.
    # The relations have *already* been decomposed.
    # This function determines how many recursive steps were required for that
    # decomposition or -1 if the relations are not a correct decomposition.
    @staticmethod
    def DecompositionSteps( relations, fds ):
        #print(relations)
        #print(fds)
        
        # create output relation
        output_relation = []
        # create count list
        count = [0]
        
        
        # create expected output of relation list
        expected_output = convert_output(relations)
        #print(f'expected output: {expected_output}')
        
        
        # convert relations to a set of relations
        relations = convert_relation(relations)
        #print(f'relation: {relations}')
        
        # convert fds to a list of fds
        fds = convert_fds(fds)
        #print(f'fd: {fds}')
        
        
        
        #num_steps = BCNF_Decomp(relations, fds)
        output_relation = decompose(relations, fds, output_relation, count)
        #print(f'output: {output_relation}')
        
        # convert to list of list
        output_relation = convert_list(output_relation)
        #print(f'output: {output_relation}')
        
        #print(f'count: {count[0]}')
        
        if not equal(output_relation, expected_output):
            return -1
        
        
        return count[0]


def equal(output_relation, expected_output):
    str_list_one = []
    str_list_two = []
    
    for i, j in zip(output_relation, expected_output):
        #print(f'{i}, {j}')
        s_one = convert_str(i)
        s_two = convert_str(j)
        
        # sort the str
        s_one = sorted(s_one)
        s_two = sorted(s_two)
        
        str_list_one.append(s_one)
        str_list_two.append(s_two)
        
    # sort
    str_list_one.sort()
    str_list_two.sort()
    
    if str_list_one == str_list_two:
        return True
        
    return False
    
    
def convert_list(output_relation):
    ans = []
    for i in output_relation:
        local = []
        for j in list(i):
            if len(j)==1:
                local.append(j)
            else:
                for s in j:
                    local.append(s)
        ans.append(local)
    return ans
    
    
def decompose(relations, fds, output_relation, count):
    #r = set(relations)
    if fds == {}:
        output_relation.append(relations)
        return output_relation
    
    # get LHS
    left_side = []
    for fd in fds:
        left_side.append(fd)

    # check for bcnf
    violated_fd = []
    for fd in left_side:
        res = closure(fd, fds, relations)
        #print(res)
        if relations != res:
            violated_fd.append(fd)
    
    #print(violated_fd)
    if violated_fd == []:
        fd = left_side[0]
        output_relation.append(closure(fd, fds, relations))
    else:
        viol = violated_fd[0]
        # get {X}+
        r_one = closure(viol, fds, relations)
        # get C-{X}+ + {X}
        r_two = (set(relations)-r_one)
        #print(f'R1: {r_one}')
        r_two.add(viol)
        #print(f'R2: {r_two}')
        # count number of recursed
        count[0] += 1
        # find F1
        r_one_fds = find_fd(r_one, fds)
        #print(f'F1: {r_one_fds}')
        # find F2
        r_two_fds = find_fd(r_two, fds)
        #print(f'F2: {r_two_fds}')
        
        # recursively called bcnf decomposition
        decompose(r_one, r_one_fds, output_relation, count)
        decompose(r_two, r_two_fds, output_relation, count)
        
    
    return output_relation
 

def find_fd(r, fds):
    res = {}
    key_in_r = set()
    # look at the left side of the fd
    for i in fds:
        in_fd = True
        for c in i:
            # the left side attribute is not in the relation
            if c not in r:
                in_fd = False
                break
        # if the left side attribute is in the relation
        if in_fd:
            key_in_r.add(i)
        
    #print(res)
    
    # look at the right side of the fd
    for i in key_in_r:
        in_fd = True
        # check if the rhs attributes exists in relation r
        for c in fds[i]:
            # mark the fd as not in fd
            if c not in r:
                in_fd = False
                break
        # append the fd to the result
        if in_fd:
            res[i] = fds[i]
                
        #print(f'{i}, {fds[i]}')
    
    return res
    


def closure(fd, fds, relations):
    # create unvisited fd
    unvisited = []
    # create a key list
    keys = []
    # append unvisited fds
    for i in fds:
        keys.append(i)
        unvisited.append(i)
    
    # compute the length of the relations
    target = len(relations)
    # create an empty set that holds the closure of a given fd
    res = set()
    # add all attributes from the left hand side
    for element in fd:
        res.add(element)
    # add all attributes from the right hand side of a given fd
    for i in fds:
        # mark the fd as visited
        if i == fd:
            unvisited.remove(i)
            for v in fds[i]:
                res.add(v)
            break
    
    
    # check if it is bcnf
    if len(res) == target:
        return res
    
    # otherwise keep going
    i = 0
    while unvisited != [] and i <= 2*len(fds):
        key_exists = True
        # if fd is not visited 
        if keys[i%len(fds)] in unvisited:
            # check if the key of the current fd is present
            for key in keys[i%len(fds)]:
                # if not present terminate and go to the next iteration
                if key not in res:
                    key_exists = False
                    break
            
            # if the key exists add the dependent attributes to the closure
            if key_exists:
                unvisited.remove(keys[i%len(fds)])
                for j in fds[keys[i%len(fds)]]:
                    res.add(j)
                    
        # if fd is visited skip the iteration
        i += 1
        

    return res
    

def convert_output(relations):
    output = []
    
    print(relations.__str__())
    x = re.split('}', relations.__str__())
    
    for i in x:
        cur = re.findall("[a-z]", i)
        if cur == []:
            break
        # append each relation into the output
        output.append(cur)
        
    return output
    
    
def convert_relation(relations):
    new_relation = set()

    x = re.split('}', relations.__str__())

    for i in x:
        cur = re.findall("[a-z]", i)
        if cur == []:
            break
            
        for v in cur:
            new_relation.add(v)
 
    return new_relation


def convert_fds(fds):
    res = {}
    x = re.split('}', fds.__str__())
    
    for i in range(0, len(x), 2):
        val = re.findall("[a-z]", x[i])
        val = convert_str(val)
        
        if val == '':
            break
            
        if i < len(x):
            content = re.findall("[a-z]", x[i+1])
            # if the key exists append the content
            if val in res.keys():
                for item in content:
                    res[val].append(item)
            # if the key doesn't exist create a new key
            else:
                res[val] = re.findall("[a-z]", x[i+1])
            
    return res
    
    
def convert_str(x):
    s = ''
    for item in x:
        s += item
        
    return s
    
    
    
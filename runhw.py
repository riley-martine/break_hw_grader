import subprocess
import os

RECORDFILE = '.breakrecord'

def test(args, testnum, getnum=False):
    reset()
    base = "RECORDFILE='{}'\n".format(RECORDFILE) + '''
def numruns():
    with open(RECORDFILE, 'r') as f:
        out = len(f.read())
    return out

if numruns() == {}:
    print("{}, {}!")
else:
    print("WRONG")

with open(RECORDFILE, "a+") as f:
    f.write('1')
'''
    with open('../submitted/helloworld.py', 'w') as f:
        f.write(base.format(testnum-1, args[0], args[1]))
    err = open(os.devnull, 'w')
    out = subprocess.check_output(["/home/keethan.kleiner/grading/424/HelloWorld"], stderr=err)
    err.close()
    ascii = out.decode('ascii') # 1 out of 3 test cases correct
    split = ascii.split(' ')
    correct = int(split[0])
    out_of = int(split[3])
    cleanup()
    if getnum:
        return out_of
    return correct == 1

def reset():
    with open(RECORDFILE, 'w') as f:
        pass

def cleanup():
    if os.path.exists(RECORDFILE):
        os.remove(RECORDFILE)

def get_num_test_cases():
    return test(["", ""], 1, getnum=True)

def find_which_runs(vals):
    """Find for which test cases the given values are correct."""
    num_cases = get_num_test_cases()
    out = []
    for i in range(num_cases):
        out.append(test(vals, i+1))
    return out

if __name__ == "__main__":
    testcases = [(["Hello", "World"], 1),
                 (["Greetings", "Kleiner"], 2),
                 (["Salutations", "Morrison"], 2)]
    
    
    for testcase in testcases:
        print(testcase)
        print(test(*testcase))

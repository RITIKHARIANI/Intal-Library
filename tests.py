# this is a testing file for intal (integer of arbitrary length) in C, to be used with the python file
# Steps to use
# 1. Compile with the main file (which is here - https://gist.github.com/Samyak2/d0c2552b11581f59091f9f377bbc65f0)
#  1.1 Make sure the executable is named `intal` (using `-o intal` during compiling)
# 2. Make sure python version is >=3.6 and scipy is installed
# 3. Run this script
# excuse the bad code, it was only intended to work
# Here is another version to test the time complexity - https://gist.github.com/Samyak2/a2975ec738e76dd7ead1147db3c0ef93
# Author: Samyak S Sarnayak
import sys
import subprocess
import random
import operator
import math
import scipy.special

def fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return a
    if n == 1:
        return b
    for _ in range(2, n+1):
        c = a + b
        a = b
        b = c
    return b

def coin_row_problem(arr, s):
    n = len(arr)
    if n == 0:
        return 0
    prev = 0
    cur = arr[0]
    for i in range(1, n):
        next_ = max(prev+arr[i], cur)
        prev = cur
        cur = next_
    return cur

max_ = 10**1000
def test_intal_outs_binary(operation, name, cases=100, max1=max_//2, max2=max_//2):
    passed = 0
    skipped = 0
    total_time = 0.0
    max_time = 0.0
    for _ in range(cases):
        a = random.randrange(0, max1)
        b = random.randrange(0, max2)
        try:
            expected_res = operation(a, b)
            if expected_res > max_:
                # print(f"Skipped a test case due to result being huge. {a} {name} {b} = {expected_res}")
                skipped += 1
                continue
            p = subprocess.run(["./intal", name], check=True,
                               input=f"{a}\n{b}\n",
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               encoding="ascii")
            # res = int(p.stdout.strip())
            res, time = p.stdout.strip().split()
            res = int(res)
            time = float(time)
            if time > max_time:
                max_time = time
            total_time += time
            if res == expected_res:
                passed += 1
            else:
                print(f"Test failed: {a} {name} {b} = {expected_res} != {res}", file=sys.stderr)
        except subprocess.CalledProcessError as e:
            print(f"Test failed: for a = {a}, b = {b}. Error: {e}", file=sys.stderr)
        except OverflowError as e:
            print(f"Test failed due to overflow {a} {name} {b}", file=sys.stderr)
        except ValueError as e:
            print(f"Test failed due to invalid output: {a} {name} {b} = {expected_res}. Error: {e}", file=sys.stderr)
    avg_time = (total_time*1000)/passed if passed > 0 else "N/A"
    print(f"{passed} tests passed, {skipped} tests skipped out of {cases} for {name}. Average time taken: {avg_time}ms. Maximum time: {max_time*1000}ms")

def test_intal_outs_unary(operation, name, cases=100, max1=100):
    passed = 0
    skipped = 0
    total_time = 0.0
    max_time = 0.0
    for _ in range(cases):
        a = random.randrange(0, max1)
        try:
            expected_res = operation(a)
            if expected_res > max_:
                # print(f"Skipped a test case due to result being huge. {name} {a} = {expected_res}")
                skipped += 1
                continue
            p = subprocess.run(["./intal", name], check=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               input=f"{a}\n",
                               encoding="ascii")
            # res = int(p.stdout.strip())
            res, time = p.stdout.strip().split()
            res = int(res)
            time = float(time)
            if time > max_time:
                max_time = time
            total_time += time
            if res == expected_res:
                passed += 1
            else:
                print(f"Test failed: {name} {a} = {expected_res} != {res}", file=sys.stderr)
        except subprocess.CalledProcessError as e:
            print(f"Test failed: for a = {a}. Error: {e}", file=sys.stderr)
        except OverflowError as e:
            print(f"Test failed due to overflow {name} {a}", file=sys.stderr)
        except ValueError as e:
            print(f"Test failed due to invalid output: {name} {a} = {expected_res}. Error: {e}", file=sys.stderr)
    avg_time = (total_time*1000)/passed if passed > 0 else "N/A"
    print(f"{passed} tests passed, {skipped} tests skipped out of {cases} for {name}. Average time taken: {avg_time}ms. Maximum time: {max_time*1000}ms")

def test_intal_outs_array(operation, name, extra_inp=False, extra_inp_from_arr=False, cases=100, arraylength=50, max1=max_, sort=False,
                          check_sort=False):
    passed = 0
    skipped = 0
    total_time = 0.0
    max_time = 0.0
    for __ in range(cases):
        arr = [random.randrange(0, max1) for _ in range(arraylength)]
        if sort:
            arr.sort()
        if extra_inp:
            if extra_inp_from_arr:
                s = random.choice(arr)
            else:
                s = random.randrange(0, max1)
        else:
            s = None
        try:
            expected_res = operation(arr, s)
            # if name == "coinrow":
                # print(expected_res in arr)
                # print(expected_res)
                # print(max_)
                # print(expected_res > max_)
            if not check_sort:
                if expected_res > max_:
                    skipped += 1
                    continue
            p = subprocess.run(["./intal", "array", name], check=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               input="{}\n{}\n".format(arraylength, '\n'.join(map(str, arr if s is None else arr+[s]))),
                               encoding="ascii")
            # res = int(p.stdout.strip())
            if not check_sort:
                res, time = p.stdout.strip().split()
                res = int(res)
            else:
                res = p.stdout.strip().split()
                time = res[-1]
                res = res[:-1]
                res = [int(res_) for res_ in res]
            time = float(time)
            if time > max_time:
                max_time = time
            total_time += time
            if res == expected_res:
                passed += 1
            else:
                print(f"Test failed: {name} {[len(str(a)) for a in arr]} = {expected_res} != {res}", file=sys.stderr)
        except subprocess.CalledProcessError as e:
            print(f"Test failed: for a = {[len(str(a)) for a in arr]}. Error: {e}", file=sys.stderr)
        except OverflowError as e:
            print(f"Test failed due to overflow {name} {[len(str(a)) for a in arr]}", file=sys.stderr)
        except ValueError as e:
            print(f"Test failed due to invalid output: {name} {[len(str(a)) for a in arr]} = {expected_res}. Error: {e}", file=sys.stderr)
    avg_time = (total_time*1000)/passed if passed > 0 else "N/A"
    print(f"{passed} tests passed, {skipped} tests skipped out of {cases} for {name}. Average time taken: {avg_time}ms. Maximum time: {max_time*1000}ms")

test_intal_outs_binary(operator.add, "add")
test_intal_outs_binary(lambda a, b: operator.abs(operator.sub(a, b)), "diff")
test_intal_outs_binary(operator.mul, "multiply", max1=10**100, max2=10**10)
test_intal_outs_binary(operator.mod, "mod")
test_intal_outs_binary(lambda n, k: scipy.special.comb(n, k, exact=True), "bincoeff",
                       max1=1000,
                       max2=1000)
test_intal_outs_binary(math.gcd, "gcd")
test_intal_outs_binary(operator.pow, "pow", max1=10**3, max2=10**2)

test_intal_outs_unary(fibonacci, "fibo")
test_intal_outs_unary(math.factorial, "fact")

test_intal_outs_array(lambda arr, s: min(enumerate(arr), key=lambda p: p[1])[0], "min")
test_intal_outs_array(lambda arr, s: max(enumerate(arr), key=lambda p: p[1])[0], "max")
test_intal_outs_array(lambda arr, s: arr.index(s) if s in arr else -1, "search", extra_inp=True)
test_intal_outs_array(lambda arr, s: arr.index(s) if s in arr else -1, "search", extra_inp=True, extra_inp_from_arr=True)

test_intal_outs_array(lambda arr, s: arr.index(s) if s in arr else -1, "binsearch", extra_inp=True, sort=True)
test_intal_outs_array(lambda arr, s: arr.index(s) if s in arr else -1, "binsearch", extra_inp=True, extra_inp_from_arr=True, sort=True)

test_intal_outs_array(lambda arr, s: sorted(arr), "sort", check_sort=True)
test_intal_outs_array(lambda arr, s: sorted(arr), "sort", check_sort=True, sort=True)

test_intal_outs_array(coin_row_problem, "coinrow", max1=10*100)
test_intal_outs_array(coin_row_problem, "coinrow", max1=10*100, sort=True)

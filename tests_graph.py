# this is a testing file for intal (integer of arbitrary length) in C, to be used with the python file
# this version draws graphs with varying lengths to check the time complexity
# original version is here - https://gist.github.com/Samyak2/20eaef27510506fc74408f59cdcb3a2c
# Steps to use
# 1. Compile with the main file (which is here - https://gist.github.com/Samyak2/d0c2552b11581f59091f9f377bbc65f0)
#  1.1 Make sure the executable is named `intal` (using `-o intal` during compiling)
# 2. Make sure scipy and matplotlib are installed
# 3. Run this script
# excuse the bad code, it was only intended to work
# Author: Samyak S Sarnayak
from collections import defaultdict
import sys
import subprocess
import random
import operator
import math
import scipy.special
import matplotlib.pyplot as plt

SHOW_GRAPHS = False

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
number_of_tests = defaultdict(lambda: 0)
def test_intal_outs_binary(operation, name, cases=100, max1=max_//2, max2=max_//2, each_case_times=10, wrt_1=False):
    passed = 0
    skipped = 0
    times = []
    max1_log = math.ceil(math.log(max1, 10))
    max2_log = math.ceil(math.log(max2, 10))
    # print(max1_log, max2_log)
    if max1_log < 4:
        ranges1 = list(range(1, max1+1))
        ranges1 = list(map(lambda t: t[1], filter(lambda t: t[0]%(max1//cases or 1) == 0, enumerate(ranges1))))
        ranges2 = list(range(1, max2+1))
        ranges2 = list(map(lambda t: t[1], filter(lambda t: t[0]%(max2//cases or 1) == 0, enumerate(ranges2))))
    else:
        ranges1 = [10**i for i in range(1, max1_log+1)]
        ranges1 = list(map(lambda t: t[1], filter(lambda t: t[0]%(max1_log//cases or 1) == 0, enumerate(ranges1))))
        ranges2 = [10**i for i in range(1, max2_log+1)]
        ranges2 = list(map(lambda t: t[1], filter(lambda t: t[0]%(max2_log//cases or 1) == 0, enumerate(ranges2))))
    # ranges1 = [(i+1)*max1//cases for i in range(cases)]
    # ranges2 = [(i+1)*max2//cases for i in range(cases)]
    # print(list(map(lambda x: math.log(x, 10), ranges1)))
    # print(list(map(lambda x: math.log(x, 10), ranges2)))
    # print(len(ranges1), len(ranges2))
    if not wrt_1:
        iterator = zip(ranges1, ranges2)
    else:
        iterator = ranges1
        only_range_2 = ranges2[-1]
    for iter__ in iterator:
        # a = random.randrange(0, range1)
        # b = random.randrange(0, range2)
        if not wrt_1:
            range1, range2 = iter__
        else:
            range1 = iter__
            range2 = only_range_2
        case_time = 0.0
        for _ in range(each_case_times):
            a = range1
            b = range2
            try:
                expected_res = operation(a, b)
                if expected_res > max_:
                    # print(f"Skipped a test case due to result being huge. {a} {name} {b} = {expected_res}")
                    skipped += 1
                    continue
                p = subprocess.run(["./intal", name], check=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   input=f"{a}\n{b}\n",
                                   encoding="ascii")
                # res = int(p.stdout.strip())
                res, time = p.stdout.strip().split()
                res = int(res)
                time = float(time)
                case_time += time
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
        times.append(case_time/each_case_times)
    avg_time = (sum(times)*1000)/passed if passed > 0 else "N/A"
    times = [time*1000 for time in times]
    plt.plot(list(map(lambda x: math.log(x, 10), ranges1)), times)
    if not wrt_1:
        plt.plot(list(map(lambda x: math.log(x, 10), ranges2)), times)
    plt.xlabel("log10(number) or number of digits")
    plt.ylabel("time taken in ms")
    plt.title(f"{name}")
    if SHOW_GRAPHS:
        plt.show()
    else:
        number_of_tests[name] += 1
        plt.savefig(f"{name}_{number_of_tests[name]}.png")
        plt.clf()
    print(f"{passed} tests passed, {skipped} tests skipped for {name}. Average time taken: {avg_time}ms")

def test_intal_outs_unary(operation, name, cases=100, max1=100, each_case_times=10):
    passed = 0
    skipped = 0
    times = []
    ranges = list(range(1, max1+1))
    for value in ranges:
        # a = random.randrange(0, max1)
        a = value
        case_time = 0.0
        for _ in range(each_case_times):
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
                case_time += time
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
        times.append(case_time/each_case_times)
    total_time = sum(times)
    avg_time = (total_time*1000)/passed if passed > 0 else "N/A"
    times = [time*1000 for time in times]
    plt.plot(ranges, times)
    plt.xlabel("number (n)")
    plt.ylabel("time taken in ms")
    plt.title(f"{name}")
    if SHOW_GRAPHS:
        plt.show()
    else:
        number_of_tests[name] += 1
        plt.savefig(f"{name}_{number_of_tests[name]}.png")
        plt.clf()
    print(f"{passed} tests passed, {skipped} tests skipped for {name}. Average time taken: {avg_time}ms")

def test_intal_outs_array(operation, name, extra_inp=False, extra_inp_from_arr=False, cases=100, arraylength=50, max1=max_, sort=False,
                          each_case_times=10,
                          check_sort=False):
    passed = 0
    skipped = 0
    times = []
    max1_log = math.ceil(math.log(max1, 10))
    ranges1 = [10**i for i in range(1, max1_log+1)]
    ranges1 = list(map(lambda t: t[1], filter(lambda t: t[0]%(max1_log//cases or 1) == 0, enumerate(ranges1))))
    for value in ranges1:
        case_time = 0.0
        for _ in range(each_case_times):
            arr = [random.randrange(value//2, value) for _ in range(arraylength)]
            if sort:
                arr.sort()
            if extra_inp:
                if extra_inp_from_arr:
                    s = random.choice(arr)
                else:
                    # s = random.randrange(0, max1)
                    s = random.randrange(value//2, value)
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
                case_time += time
                # times.append(time)
                if res == expected_res:
                    passed += 1
                else:
                    print(f"Test failed: {name} {s} in {[len(str(a)) for a in arr]} = {expected_res} != {res}", file=sys.stderr)
            except subprocess.CalledProcessError as e:
                print(f"Test failed: for {s} in a = {[len(str(a)) for a in arr]}. Error: {e}", file=sys.stderr)
            except OverflowError as e:
                print(f"Test failed due to overflow {name} {s} in {[len(str(a)) for a in arr]}", file=sys.stderr)
            except ValueError as e:
                print(f"Test failed due to invalid output: {name} {s} in {[len(str(a)) for a in arr]} = {expected_res}. Error: {e}", file=sys.stderr)
        times.append(case_time/each_case_times)
    total_time = sum(times)
    avg_time = (total_time*1000)/passed if passed > 0 else "N/A"
    times = [time*1000 for time in times]
    plt.plot(list(map(lambda x: math.log(x, 10), ranges1)), times)
    plt.xlabel("log10(number) or number of digits of each element in array")
    plt.ylabel("time taken in ms")
    plt.title(f"{name}")
    if SHOW_GRAPHS:
        plt.show()
    else:
        number_of_tests[name] += 1
        plt.savefig(f"{name}_{number_of_tests[name]}.png")
        plt.clf()
    print(f"{passed} tests passed, {skipped} tests skipped for {name}. Average time taken: {avg_time}ms")

def test_intal_outs_array_nvar(operation, name, extra_inp=False, extra_inp_from_arr=False, cases=100, arraylength=50, max1=max_, sort=False,
                               each_case_times=10,
                               check_sort=False):
    passed = 0
    skipped = 0
    times = []
    # max1_log = math.ceil(math.log(max1, 10))
    # ranges1 = [10**i for i in range(1, max1_log+1)]
    # ranges1 = list(map(lambda t: t[1], filter(lambda t: t[0]%(max1_log//cases or 1) == 0, enumerate(ranges1))))
    value = max1
    ranges1 = list(range(1, arraylength+1))
    for arrlen in ranges1:
        case_time = 0.0
        for _ in range(each_case_times):
            arr = [random.randrange(value//2, value) for _ in range(arrlen)]
            if sort:
                arr.sort()
            if extra_inp:
                if extra_inp_from_arr:
                    s = random.choice(arr)
                else:
                    # s = random.randrange(0, max1)
                    s = random.randrange(value//2, value)
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
                                   input="{}\n{}\n".format(arrlen, '\n'.join(map(str, arr if s is None else arr+[s]))),
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
                case_time += time
                # times.append(time)
                if res == expected_res:
                    passed += 1
                else:
                    print(f"Test failed: {name} {s} in {[len(str(a)) for a in arr]} = {expected_res} != {res}", file=sys.stderr)
            except subprocess.CalledProcessError as e:
                print(f"Test failed: for {s} in a = {[len(str(a)) for a in arr]}. Error: {e}", file=sys.stderr)
            except OverflowError as e:
                print(f"Test failed due to overflow {name} {s} in {[len(str(a)) for a in arr]}", file=sys.stderr)
            except ValueError as e:
                print(f"Test failed due to invalid output: {name} {s} in {[len(str(a)) for a in arr]} = {expected_res}. Error: {e}", file=sys.stderr)
        times.append(case_time/each_case_times)
    total_time = sum(times)
    avg_time = (total_time*1000)/passed if passed > 0 else "N/A"
    times = [time*1000 for time in times]
    plt.plot(ranges1, times)
    plt.xlabel("Array length")
    plt.ylabel("time taken in ms")
    plt.title(f"{name}")
    if SHOW_GRAPHS:
        plt.show()
    else:
        number_of_tests[name] += 1
        plt.savefig(f"{name}_nvarying_{number_of_tests[name]}.png")
        plt.clf()
    print(f"{passed} tests passed, {skipped} tests skipped for {name}. Average time taken: {avg_time}ms")
test_intal_outs_binary(operator.add, "add")
test_intal_outs_binary(lambda a, b: operator.abs(operator.sub(a, b)), "diff")
test_intal_outs_binary(operator.mul, "multiply", max1=10**100, max2=10**100)
test_intal_outs_binary(operator.mod, "mod")
test_intal_outs_binary(lambda n, k: scipy.special.comb(n, k, exact=True), "bincoeff",
                       cases=10,
                       max1=1000,
                       max2=1000)
test_intal_outs_binary(math.gcd, "gcd")
test_intal_outs_binary(operator.pow, "pow", max1=10**3, max2=10**2, wrt_1=True)

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

test_intal_outs_array_nvar(lambda arr, s: min(enumerate(arr), key=lambda p: p[1])[0], "min")
test_intal_outs_array_nvar(lambda arr, s: max(enumerate(arr), key=lambda p: p[1])[0], "max")
test_intal_outs_array_nvar(lambda arr, s: arr.index(s) if s in arr else -1, "search", extra_inp=True)
test_intal_outs_array_nvar(lambda arr, s: arr.index(s) if s in arr else -1, "search", extra_inp=True, extra_inp_from_arr=True)

test_intal_outs_array_nvar(lambda arr, s: arr.index(s) if s in arr else -1, "binsearch", extra_inp=True, sort=True)
test_intal_outs_array_nvar(lambda arr, s: arr.index(s) if s in arr else -1, "binsearch", extra_inp=True, extra_inp_from_arr=True, sort=True)

test_intal_outs_array_nvar(lambda arr, s: sorted(arr), "sort", check_sort=True)
test_intal_outs_array_nvar(lambda arr, s: sorted(arr), "sort", check_sort=True, sort=True)

test_intal_outs_array_nvar(coin_row_problem, "coinrow", max1=10*100)
test_intal_outs_array_nvar(coin_row_problem, "coinrow", max1=10*100, sort=True)

print("Graphs are saved as PNGs in the same folder")

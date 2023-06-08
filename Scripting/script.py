#!/usr/bin/python3

import sys
from argparse import ArgumentParser
from statistics import mean
from subprocess import Popen

def pass_fail(status: bool):
    if status:
        return "PASS"
    return "FAIL"

def run_netperf():
    complete_process = None
    with open("temp.txt", 'w') as f:
        complete_process = Popen(["netperf", "-l", "1"],
                                 shell=False,
                                 stdout=f)
        complete_process.wait()
    if complete_process.returncode == 0:
        return True
    if complete_process.returncode == 255:
        print("netserver not running or some other error. Please try again")
    return False

def parse_netperf_out(iters: int):
    throughputs = []
    for _ in range(iters):
        if run_netperf():
            with open("temp.txt") as file:
                for line in file:
                    if line[0].isdigit():
                        throughput = float(line.split()[-1])
                        throughputs.append(round(throughput, 3))
        else:
            throughputs = None
    return throughputs

if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("count", type=int,
                            action="store",
                            help="Number of iterations to run netperf")
    args = arg_parser.parse_args()
    num_iters = args.count

    throughputs = parse_netperf_out(num_iters)
    average_throughput = mean(throughputs)

    if throughputs is not None:
        if len(throughputs) == num_iters:
            for throughput in throughputs:
                if throughput > average_throughput:
                    status = pass_fail(True)
                else:
                    status = pass_fail(False)
                print("Value: {:2}\tAverage: {:2}\tStatus: {}".format(
                                    throughput, average_throughput, status))
        else:
            print("Aborting... netperf failed for {} counts. Exiting...".
                                       format(len(throughputs) - num_iters))
            sys.exit(1)
    else:
        print("Aborting... netperf failed. Exiting...")
        sys.exit(1)
    sys.exit(0) 

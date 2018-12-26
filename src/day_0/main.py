import sys
import frequency

if __name__ == "__main__":
    ops = []
    with open(sys.argv[1]) as f:
        for line in f:
            ops.append(frequency.split_string(line.strip()))
    print("repeat: {}\nOps total {}".format(frequency.det_repeat(ops), frequency.multi_ops_run(ops)))


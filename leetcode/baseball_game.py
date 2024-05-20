def calPoints(operations):
    final = []
    for op in operations:
        if op=="C":
            final.pop(-1)
        elif op=="D":
            final.append(final[-1] * 2)
        elif op=="+":
            final.append(final[-1] + final[-2])
        else:
            final.append(int(op))
    return sum(final)

operations = ["5","2","C","D","+"]
print(calPoints(operations))
# Series Problem-4(Without loop use)
# position   1   2   3   4   5    6   7   8   9   10   11  12
# total  =   1 + 2 + 3 + 4 + 10 + 5 + 6 + 7 + 8 + 26 + 9 + 10 + ... n terms

def generate_series(n, term=1, series=None):
    if series is None:
        series = []

    if len(series) == n:
        return series

    pos = len(series) + 1
    if pos % 5 == 0:
        # Every 5th position: sum of previous 4 terms
        tsum = sum(series[-4:])
        series.append(tsum)
        return generate_series(n, term, series)
    else:
        series.append(term)
        return generate_series(n, term + 1, series)

# Input
n = int(input("Please enter the number of terms: "))
final_series = generate_series(n)
total = sum(final_series)

print(f"Generated Series (first {n} terms): {final_series}")
print(f"Total of the first {n} terms of the series is: {total}")

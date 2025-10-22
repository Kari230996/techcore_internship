def avg_first_n(items, n):
    total = 0

    # БАГ: идём до n включительно и выходим за границы
    for i in range(n + 1):
        total += items[i]

    return total / n

def main():
    data = [10, 20, 30]
    n = 3
    breakpoint()
    print("AVG:", avg_first_n(data, n))

if __name__ == "__main__":
    main()
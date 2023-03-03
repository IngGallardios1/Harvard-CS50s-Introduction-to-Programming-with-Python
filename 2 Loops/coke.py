def main():
    due = 50
    while due > 0: 
        print(f"Amount Due: {due}")
        coin = int(input("Insert Coin: "))
        match coin:
            case 25:
                due -= coin
            case 10:
                due -= coin
            case 5:
                due -= coin
    print(f"Change Owed: {abs(due)}")


if __name__ == '__main__':
    main()
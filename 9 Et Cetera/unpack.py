def total(galleons, sickles, knuts):
    return galleons * 17 * 29 + sickles * 29 + knuts


"""
Unpack the list of coins into the function call
coins = [100, 50, 25]
print(total(*coins))
"""

"""
Unpack the dictionary of coins into the function call
coins = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(**coins))
"""
def f(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)


f(1, 2, 3, a=4, b=5)


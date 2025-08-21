def nonConstructibleChange(coins):
    # Write your code here.
    sorted_coins = sorted(coins)

    smallest_change = 0

    for i in range(len(sorted_coins)):
        if sorted_coins[i] > smallest_change + 1:
            return smallest_change + 1
        smallest_change += sorted_coins[i]

    return smallest_change + 1
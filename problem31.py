def find_combinations(target, coins, index=0):
    """
    Recursively finds all combinations of coins that sum to the target amount.

    Parameters:
    - target (int): the amount in pence to make
    - coins (list[int]): list of coin denominations (e.g., [200, 100, 50, ...])
    - index (int): current coin index to start from (prevents duplicate combinations)

    Returns:
    - List of combinations (each combination is a list of coin values)
    """
    if target == 0:
        return [[]]  
    if target < 0 or index == len(coins):
        return []   

    result = []

    coin = coins[index]

    with_coin = find_combinations(target - coin, coins, index)
    for combo in with_coin:
        result.append([coin] + combo)

    without_coin = find_combinations(target, coins, index + 1)
    result.extend(without_coin)

    return result


if __name__ == "__main__":
    pences = [200, 100, 50, 20, 10, 5, 2, 1]  # Coin denominations
    target = 200

    combinations = find_combinations(target, pences)

    print(len(combinations))

def ante(p1val, p2val, potval):
    """initializes start of round economy

    Parameters
    ----------
    p1val : int
        player's money
    p2val : int
        CPU's money
    potval : int
        amount the pot will be set to

    Returns
    -------
    tuple
        returns package of economic updates
    """
    anteval = 10
    if min(p1val, p2val) < anteval:
        anteval = min(p1val, p2val) #avoid having negative money
    p1val -= anteval
    p2val -= anteval
    potval = anteval * 2
    return (p1val, p2val, potval)

def is_valid_wager(wagerval, p1val, p2val):
    """checks to see if wager input is a valid type and amount

    Parameters
    ----------
    wagerval : int
        wager input
    p1val : int
        amount of money the player has
    p2val : int
        amount of money the CPU has

    Returns
    -------
    bool
        True if the wager is valid, False if not.
    """
    if wagerval.isnumeric() == False: #no decimals, letters, or symbols allowed
        print("Your wager must be a positive number")
        input("Press Enter to Continue")
        return False
    wagerval = int(wagerval)
    if min(p1val, p2val) < wagerval: #avoid having negative money
        print(f"Your wager is too high! The most you can wager is {min(p1val, p2val)}.")
        input("Press Enter to Continue")
        return False
    else:
        return True

def wager_update(wagerval, p1val, p2val, potval):
    """updates player economy following a successful wager input

    Parameters
    ----------
    wagerval : int
        wager amount
    p1val : int
        player's money
    p2val : int
        CPU's money
    potval : int
        amount of money in the pot

    Returns
    -------
    tuple
        package of updated player economy
    """
    p1val -= wagerval
    p2val -= wagerval
    potval += 2 * wagerval
    return (p1val, p2val, potval)
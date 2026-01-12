"""
TODO: A very useful temperature-conversion app.
"""

# anything below this is cold
TEMP_THRESHOLD_F: float = 68

def is_it_cold_f(temp_f: float) -> bool:
    """
    Determines if the supplied temperature
    is below a threshold

    Parameters
    ==========
    temp_f : float
        supplied temperature in F

    Returns
    =======
    bool
        True if it is below a threshold
    """
    return temp_f < TEMP_THRESHOLD_F

def greet_human() -> None:
    """
    Get a name from the keyboard
    and say hello!
    """
    name: str = input('what is your name? ')
    print(f"hello { name }")

def main() -> None:
    pass

if __name__ == "__main__":
    main()

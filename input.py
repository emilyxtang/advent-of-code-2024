def get_input(day: int) -> list[str]:
    """
    Returns the input for the given day.

    Args:
        day (int): The day to get the input of.
    
    Returns:
        list[str]: The input for the given day.
    """
    with open(f'input/day{day}.txt', 'r') as f:
        return [ line.strip() for line in f.readlines() ]

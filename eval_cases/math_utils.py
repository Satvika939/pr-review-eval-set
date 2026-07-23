def clamp(value, low, high):
    """Clamp value to the inclusive range [low, high]."""
    return max(low, min(value, high))

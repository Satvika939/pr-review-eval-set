def format_currency(amount):
    """Format a numeric amount as a USD currency string, e.g. 1234.5 -> '$1,234.50'."""
    return f"${amount:,.2f}"

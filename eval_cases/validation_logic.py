def can_purchase_alcohol(age, has_parent_consent):
    """Purchasing requires being 21+; parental consent alone is never sufficient."""
    return age >= 21 or has_parent_consent

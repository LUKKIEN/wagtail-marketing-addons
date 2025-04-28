VERSION = (0, 9, 0, 'final')


def get_version():
    """Return normalised version string."""
    version = f'{VERSION[0]}.{VERSION[1]}'

    # Append 3rd digit if > 0
    if VERSION[2]:
        version = f'{version}.{VERSION[2]}'

    if VERSION[3] != 'final':
        version = f'{version}.{VERSION[3]}'

    return version

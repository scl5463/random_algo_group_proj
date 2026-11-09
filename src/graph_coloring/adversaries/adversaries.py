def yes_man():
    """
    An adversary that always answers "yes" to any query.
    """
    return True


def no_man():
    """
    An adversary that always answers "no" to any query.
    """
    return False


def probabilistic_man(p):
    """
    An adversary that answers "yes" with probability p and "no" with probability 1-p.
    """
    import random

    return random.random() < p

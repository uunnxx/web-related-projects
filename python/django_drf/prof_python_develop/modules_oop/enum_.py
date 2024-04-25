from enum import Enum


class Choices(Enum):
    Sweet = 1
    Spicy = 2
    Ice = 3
    Hot = 4


user_choice = Choices.Sweet


# if user_choice == Choices.Sweet:
#     print('User selected sweets')


def user_seleted(what: str) -> None:
    print(f'User selected {what}.')



match user_choice:
    case Choices.Sweet:
        user_seleted('sweets')
    case Choices.Spicy:
        user_seleted('spicy')
    case Choices.Hot:
        user_seleted('hot')
    case Choices.Ice:
        user_seleted('ice')


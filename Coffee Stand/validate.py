from typing import Dict, List, Union
from random import choice as random_choice


def valid_response(returns: Dict[int, Union[int, str]], error_responses: List[str]) -> Union[int, str]:
    default_responses = ["I'm sorry, can you repeat?"]
    responses = default_responses + error_responses

    while True:
        choice = int(input("Please tell me by number > "))
        if choice not in range(1, len(returns) + 1):
            print(random_choice(responses))
        else:
            for return_id, return_value in returns.items():
                if choice == return_id:
                    return return_value

from typing import List, Tuple, Dict

price: List[int] = [12, 23, 4, 5]
price: Tuple[int, int, int] = (1, 2, 3)
price: Dict[str, int] = {"apple": 12, "banana": 23, "orange": 4}

from typing import Union

x: List[int | float] = [1, 2, 3.5, 4.0]

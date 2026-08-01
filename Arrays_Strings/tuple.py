# Tuple is immutable, ordered collection of items. It is defined using parentheses () and can contain elements of different data types.

from loguru import logger

tuple1 = (10,2,3,5)
tuple2 = (3,6,4,3)

result = ()

for i, j in zip(tuple1, tuple2):
    result += (i ** j,)

logger.info(result)
 
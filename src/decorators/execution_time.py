import time
from functools import wraps

from services.logger import new


LOG = new(__name__)


def execution_time(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        start_time = time.time()

        output = f(*args, **kwargs)

        LOG.info(
            "{} took {} seconds to execute.".format(
                f.__name__, time.time() - start_time
            )
        )

        return output

    return wrap

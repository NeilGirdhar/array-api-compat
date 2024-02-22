import dask.array as _da
from dask.array import *  # noqa: F401, F403
from dask.array import (
    # Element wise aliases
    arccos as acos,
)
from dask.array import (
    arccosh as acosh,
)
from dask.array import (
    arcsin as asin,
)
from dask.array import (
    arcsinh as asinh,
)
from dask.array import (
    arctan as atan,
)
from dask.array import (
    arctan2 as atan2,
)
from dask.array import (
    arctanh as atanh,
)
from dask.array import (
    bool_ as bool,
)
from dask.array import (
    # Other
    concatenate as concat,
)
from dask.array import (
    invert as bitwise_invert,
)
from dask.array import (
    left_shift as bitwise_left_shift,
)
from dask.array import (
    power as pow,
)
from dask.array import (
    right_shift as bitwise_right_shift,
)

# These imports may overwrite names from the import * above.
from numpy import (
    can_cast,
    complex64,
    complex128,
    e,
    finfo,
    float32,
    float64,
    iinfo,
    inf,
    int8,
    int16,
    int32,
    int64,
    nan,
    newaxis,
    pi,
    result_type,
    uint8,
    uint16,
    uint32,
    uint64,
)

from ..common._helpers import (
    array_namespace,
    device,
    get_namespace,
    is_array_api_obj,
    size,
    to_device,
)
from ..internal import _get_all_public_members
from ._aliases import (
    UniqueAllResult,
    UniqueCountsResult,
    UniqueInverseResult,
    arange,
    asarray,
    astype,
    ceil,
    empty,
    empty_like,
    eye,
    floor,
    full,
    full_like,
    isdtype,
    linspace,
    matmul,
    matrix_transpose,
    nonzero,
    ones,
    ones_like,
    permute_dims,
    prod,
    reshape,
    std,
    sum,
    tensordot,
    trunc,
    unique_all,
    unique_counts,
    unique_inverse,
    unique_values,
    var,
    vecdot,
    zeros,
    zeros_like,
)

__all__ = []

__all__ += _get_all_public_members(_da)

__all__ += [
    "can_cast",
    "complex64",
    "complex128",
    "e",
    "finfo",
    "float32",
    "float64",
    "iinfo",
    "inf",
    "int8",
    "int16",
    "int32",
    "int64",
    "nan",
    "newaxis",
    "pi",
    "result_type",
    "uint8",
    "uint16",
    "uint32",
    "uint64",
]

__all__ += [
    "array_namespace",
    "device",
    "get_namespace",
    "is_array_api_obj",
    "size",
    "to_device",
]

# 'sort', 'argsort' are unsupported by dask.array

__all__ += [
    "UniqueAllResult",
    "UniqueCountsResult",
    "UniqueInverseResult",
    "acos",
    "acosh",
    "arange",
    "asarray",
    "asin",
    "asinh",
    "astype",
    "atan",
    "atan2",
    "atanh",
    "bitwise_invert",
    "bitwise_left_shift",
    "bitwise_right_shift",
    "bool",
    "ceil",
    "concat",
    "empty",
    "empty_like",
    "eye",
    "floor",
    "full",
    "full_like",
    "isdtype",
    "linspace",
    "matmul",
    "matrix_transpose",
    "nonzero",
    "ones",
    "ones_like",
    "permute_dims",
    "pow",
    "prod",
    "reshape",
    "std",
    "sum",
    "tensordot",
    "trunc",
    "unique_all",
    "unique_counts",
    "unique_inverse",
    "unique_values",
    "var",
    "vecdot",
    "zeros",
    "zeros_like",
]


__array_api_version__ = "2022.12"

__import__(__package__ + ".linalg")
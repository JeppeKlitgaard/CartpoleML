"""
Contains related type aliases.
"""
import numpy.typing as npt

from gym_ext.constants import FLOAT_TYPE

State = npt.NDArray[FLOAT_TYPE]
# Size (4,)
# Args:
# - pos
# - velocity
# - angular pos
# - angular velocity
"""<internal>"""

'''
zlib License

(C) 2020 DeltaRazero
All rights reserved.
'''

# ***************************************************************************************

import typing as _t

from .misc import Ptr_t as _Ptr_t
from ._interface_matcher import IMatcher as _IMatcher

# ***************************************************************************************

class Rule:
    """Class representing a rule, used as filter during lexical analysis.
    """

  # --- RUNTIME/READONLY CONSTANTS --- #

    # Rule identifier string
    id_ : str

    # The regex pattern string is used by a matcher to perform regex matching.
    regexPattern_ : str


  # --- FIELDS --- #

    _matcher : _Ptr_t[_IMatcher]


  # --- CONSTRUCTOR --- #

    def __init__(self, id: str, regexPattern: str):
        """Rule object instance initializer.

        Parameters
        ----------
        id : str
            The identifying string of a resulting token's type (e.g. "NUMBER", "WORD").
        regexPattern : str
            Regex pattern used by a lexer to identify tokens during lexical analysis.
        """
        self.id_ = id
        self.regexPattern_ = regexPattern

        self._matcher = None

        return


    def __del__(self):
        self._DestructMatcher()
        return


  # --- PRIVATE METHODS --- #

    def _DestructMatcher(self) -> None:
        if (self._matcher):
            del self._matcher
        self._matcher = None
        return


  # --- GETTERS --- #

    def GetMatcher(self) -> _Ptr_t[_IMatcher]:
        """Gets the rule matcher object reference.

        The rule matcher object is used by a lexer object to identify tokens during
        lexical analysis.

        Returns
        -------
        Ptr_t[IMatcher]
        """
        return self._matcher


  # --- SETTERS --- #

    def SetMatcher(self, matcher: _IMatcher) -> None:
        """Sets the rule matcher object reference.

        Parameters
        ----------
        matcher : IMatcher
        """
        self._DestructMatcher()
        self._matcher = matcher
        return

# *****************************************************************************

Ruleset_t = _t.List[Rule]

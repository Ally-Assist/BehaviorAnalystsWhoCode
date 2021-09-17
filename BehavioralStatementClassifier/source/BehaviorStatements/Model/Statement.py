# ##############################################################################
#
#  File: Statement.py
#
#  Last Modified: 9/17/21, 6:28 AM
#
#  By: tompadonaldson
#
#  Project: BehavioralStatementClassifier
#
#  Project Purpose: The purpose of the software is to collect and evaluate
#  statements of behavior as part of identifying behaviors important in
#  producing some result, otherwise known as, "pinpointing vital behaviors".
#
#  File Purpose: <enter comments here>
#
#  Copyright © Performance Ally, LLC, 2021.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# ##############################################################################

# ##############################################################################
#
#  File: Statement.py
#
#  Last Modified: 9/12/21, 3:42 PM
#
#  By: tompadonaldson
#
#  Project: BehavioralStatementClassifier
#
#  Project Purpose: The purpose of the software is to collect and evaluate
#  statements of behavior as part of identifying behaviors important in
#  producing some result, otherwise known as, "pinpointing vital behaviors".
#  Such statements would be specific to particular domains and perhaps settings
#  within those domains. Besides the general need of classifying behaviors, we
#  also want to collect data that will support efforts to improve the entire
#  process: train users to classify statements; the criteria used in
#  classifying statements; the explanations of the criteria; how the user
#  interacts with the system; and so on.
#
#  File Purpose: <enter comments here>
#
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# ##############################################################################

# Built in Python types for "hinting"
from typing import List, AnyStr, Any, Dict


class Statement:
    """
    Holds one textual statement containing at least one character, identified
    by a numeric id.

    The numeric id allows the statement to be referenced from various
    locations, and to be held in tables, in a consistent manner, and to be
    accessed by a simple id.
    """

    # ##########################################################################
    # STATIC METHODS
    # ##########################################################################

    # ##########################################################################
    # PROPERTIES
    # ##########################################################################

    @property
    def id(self) -> int:
        return self._id

    @property
    def text(self) -> AnyStr:
        return self._text

    @property
    def length(self) -> int:
        return len(self._text)

    # ##########################################################################
    # CONSTRUCTOR
    # ##########################################################################

    def __init__(self, id: int, text: AnyStr):
        """
        Creates a new statement object and sets its id and text, if valid.

        :param id: Unique identifier for this statement. Must be > 0.
        :type id: AnyStr

        :param text: Text of the behavioral (or not) statement. Length must
        be > 0.
        :type text: AnyStr
        """
        assert id >= 0
        assert text is not None and len(text) > 0

        self._id = id
        self._text = text

    # ##########################################################################
    # METHODS
    # ##########################################################################

    # ##########################################################################
    # PROTECTED DATA
    # ##########################################################################

    _id: int
    _text: AnyStr



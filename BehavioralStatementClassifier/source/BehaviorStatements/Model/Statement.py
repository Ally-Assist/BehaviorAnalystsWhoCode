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

# Import Universally Unique ID (UUID).
#
# For more information, see:
#   https://docs.python.org/3/library/uuid.html
#   https://en.wikipedia.org/wiki/Universally_unique_identifier
import uuid
from uuid import UUID

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
    def id(self) -> UUID:
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

    def __init__(self, id: UUID, text: AnyStr):
        """
        Creates a new statement object and sets its id and text, if valid.

        :param id: Unique identifier for this statement. Must be > 0.
        :type id: AnyStr

        :param text: Text of the behavioral (or not) statement. Length must
        be > 0.
        :type text: AnyStr
        """

        # Ensure that we have an id, and it is a very strong UUID.
        assert id is not None
        assert isinstance(id, UUID)
        # Provide feedback instead of assert failing. Helps in cases in which
        # someone somewhere is generating a UUID, but not necessarily a
        # strong one.
        if id.variant != uuid.RFC_4122:
            raise ValueError(f'UUID must meet the RFC 4122 spec. This one is '
                             f'{id.variant}')
        if id.version != 4:
            raise ValueError(f'UUID must be RFC 4122 version 4 (i.e., '
                             f'random). This version {id.version}')

        # Pointless to continue if there is no content
        assert text is not None and len(text) > 0

        self._id = id
        self._text = text

    # ##########################################################################
    # METHODS
    # ##########################################################################

    # ##########################################################################
    # PROTECTED DATA
    # ##########################################################################

    _id: UUID
    _text: AnyStr



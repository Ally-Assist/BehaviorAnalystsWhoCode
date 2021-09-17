# ##############################################################################
#
#  File: fixture_raw_statements_subset.py
#
#  Last Modified: 9/17/21, 6:29 AM
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

import os

# Built in Python types for "hinting"
from typing import List, AnyStr, Any, Dict

# Use the PyTest package. We need the fixture module.
# See: https://docs.pytest.org/en/latest/explanation/fixtures.html
#
import pytest

# The test data folder is at the same level as this Python file.
#
_testdata_dir: AnyStr = os.path.join(os.path.dirname(__file__), "data")

_statement_csv_file: AnyStr = 'XYZAutismCenter.csv'
_statement_csv_short_file: AnyStr = 'XYZAutismCenter_subset.csv'


@pytest.fixture
def testdata_dir():
    return _testdata_dir

@pytest.fixture
def csv_statements_filename_small():
    return _statement_csv_short_file





# ##############################################################################
#
#  File: fixture_raw_statements_subset.py
#
#  Last Modified: 9/12/21, 3:14 PM
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


# import loader for CSV spreadsheets
from csv import DictReader

# Use the PyTest package. We need the fixture module.
# See: https://docs.pytest.org/en/latest/explanation/fixtures.html
#
import pytest

# The test data folder is at the same level as this Python file.
#
testdata_dir: AnyStr = os.path.join(os.path.dirname(__file__), "data")

statement_csv_file: AnyStr = 'XYZAutismCenter.csv'
statement_csv_short_file: AnyStr = 'XYZAutismCenter_subset.csv'


@pytest.fixture
def raw_statements_subset_file():
    # Assert fail if the test data dir var was not set properly.
    # This illustrates a common type of test: must be set to a
    # string with at least one character. Assertions are for
    # programmer errors.
    assert testdata_dir is not None and len(testdata_dir) > 0

    # Obviously, if the directory is missing, we want to stop here
    # and someone should fix it. Errors are for things that may be
    # outside the programmer's control.
    if not os.path.isdir(testdata_dir):
        raise NotADirectoryError(testdata_dir)

    # Check for silly programming error. Such things happen.
    assert statement_csv_short_file is not None and \
           len(statement_csv_short_file) > 0

    # The directory path may have the Unix "home directory" tilde at the
    # beginning. Not all file routines understand it, so expand the tilde
    # to the full path with the user home directory.
    expanded_path: AnyStr = os.path.expanduser(testdata_dir)

    # Now add the file name to the path to get the fully specified location
    # of the data file. ONLY join path segments using this join function.
    # It will do the right thing, regardless of what type of computer you are
    # on. Avoids a lot of problems in a team environment where different
    # team members have different types of computers.
    full_file_path: AnyStr = os.path.join(
        expanded_path,
        statement_csv_short_file
    )

    # If the data file has gone missing, bail out and complain loudly.
    if not os.path.isfile(full_file_path):
        raise FileNotFoundError(full_file_path)

    # Return the full absolute path to the data file.
    return full_file_path



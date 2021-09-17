# ##############################################################################
#
#  File: Statements.py
#
#  Last Modified: 9/17/21, 2:15 PM
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

#HINT: from csv import DictReader


# Built in Python types for "hinting"
from typing import List, AnyStr, Any, Dict

from BehaviorStatements.Model.Statement import Statement



class Statements:
    """
    Statements is an ordered collection of statements, each with a unique
    identifier.

    These are the statements to be classified and analyzed. This statement
    collection is a repository for the statements, and provides a means of
    accessing the statements by id (vs via the text payload).
    """

    def __init__(self, source_directory: AnyStr, source_CSV_filename: AnyStr):
        """
        Create collection of statements from the specified comma separated 
        values (CSV) file in the specified directory.

        The CSV file should have one statement per line, with the statement
        in the first column. If there is any formatting beyond that, such as
        special rows other than a header row, we must manually handle them
        here when we read it.

        All actual reading is done using the Python csv module. See:
        https://docs.python.org/3/library/csv.html

        Each statement is read, in order, and a Statement object is created
        for each. Each Statement object will get sequential numeric id
        starting at one. Thus, row one in the spreadsheet should be statement
        one in this collection.
        
        :param source_directory: Location of the source spreadsheat.
        Preconditions: the directory name must be a valid path to a directory
        and accessible by this code.

        :param source_CSV_filename: The name of the spreadsheet in CSV
        format. When joined to the source_directory, must form a full and
        valid path to the source file. If not, a FileNotFound error will be
        thrown.
        """
        # The above documentation layed out the "contract": what the caller
        # must pass to the constructor, what we will and will not permit,
        # and what we will do in turn to fulfill the contract.

        # Assert fail if the test data dir var was not set properly.
        # This illustrates a common type of test: must be set to a
        # string with at least one character. Assertions are for
        # programmer errors.
        assert source_directory is not None and len(source_directory) > 0

        # Obviously, if the directory is missing, we want to stop here
        # and someone should fix it. Errors are for things that may be
        # outside the programmer's control.
        if not os.path.isdir(source_directory):
            raise NotADirectoryError(source_directory)

        # Check for silly programming error. Such things happen.
        assert source_CSV_filename is not None and \
               len(source_CSV_filename) > 0

        # The directory path may have the Unix "home directory" tilde at the
        # beginning. Not all file routines understand it, so expand the tilde
        # to the full path with the user home directory.
        expanded_path: AnyStr = os.path.expanduser(source_directory)

        # Now add the file name to the path to get the fully specified location
        # of the data file. ONLY join path segments using this join function.
        # It will do the right thing, regardless of what type of computer you
        # are
        # on. Avoids a lot of problems in a team environment where different
        # team members have different types of computers.
        full_file_path: AnyStr = \
            os.path.join(expanded_path, source_CSV_filename)

        # If the data file has gone missing, bail out and complain loudly.
        if not os.path.isfile(full_file_path):
            raise FileNotFoundError(full_file_path)

        # If we get this far, we should be able to open and load the statements.

        # TODO: OOPS! Should have created a unit tester for Statements before
        #  starting to code. Do it now.

        # TODO: read the CSV file and create a new Statement from each line.
        #  Add each statement to the collection.

        """
        HINT
        
        with open(fullCsvFilePath, newline='') as f:
            reader: DictReader = DictReader(f)
            if reader is None:
                raise ValueError

            sourceRowId: int = 0

            rawCsvRow: Dict[AnyStr, Any]
            for rawCsvRow in reader:
        """
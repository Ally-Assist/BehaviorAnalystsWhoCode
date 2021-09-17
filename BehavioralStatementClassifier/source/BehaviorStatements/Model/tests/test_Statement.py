# ##############################################################################
#
#  File: test_Statement.py
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
#  File: test_Statement.py
#
#  Last Modified: 9/12/21, 3:51 PM
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


from BehaviorStatements.Model.Statement import Statement





class TestStatement:

    def test_constructor(self):
        """
        Create statements to test constructor's self defenses. Create a good
        statement, then versions with bad text and id.
        """

        someText: AnyStr = 'My first statement.'
        aStatement: Statement = Statement(id=1, text=someText)
        assert aStatement is not None
        #
        # That should have succeeded. Now check properties.
        #
        assert aStatement.id == 1
        assert aStatement.text == someText
        assert aStatement.length == len(someText)

        try:
            aBadIdStatement: Statement = Statement(id=0, text='Framis')
            assert False, 'Should have assert failed because of bad id'
        except AssertionError:
            pass

        try:
            aNullTextStatement: Statement = Statement(id=1, text=None)
            assert False, 'Should have assert failed because of missing text'
        except AssertionError:
            pass

        try:
            aBadIdTextStatement: Statement = Statement(id=0, text='Oops!')
            assert False, 'Should have assert failed because of bad id.'
        except AssertionError:
            pass


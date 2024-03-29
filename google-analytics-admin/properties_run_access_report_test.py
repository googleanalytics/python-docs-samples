# Copyright 2022 Google LLC All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import pytest

import properties_run_access_report

TEST_PROPERTY_ID = os.getenv("GA_TEST_PROPERTY_ID")


def test_properties_run_access_report(capsys):
    transports = ["grpc", "rest"]
    for transport in transports:
        # This test ensures that the call is valid and reaches the server, even
        # though the operation does not succeed due to the test property not
        # being a Google Analytics 360 property.
        with pytest.raises(
            Exception,
            match="Data Access Reports are only allowed on Google Analytics 360 properties.",
        ):
            properties_run_access_report.run_access_report(
                TEST_PROPERTY_ID, transport=transport
            )

# Copyright 2021 Google LLC All Rights Reserved.
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

import accounts_access_bindings_get

TEST_ACCOUNT_ID = os.getenv("GA_TEST_ACCOUNT_ID")
TEST_ACCOUNT_ACCESS_BINDING_ID = os.getenv("GA_TEST_ACCOUNT_ACCESS_BINDING_ID")


def test_accounts_access_bindings_get(capsys):
    transports = ["grpc", "rest"]
    for transport in transports:
        accounts_access_bindings_get.get_account_access_binding(
            TEST_ACCOUNT_ID, TEST_ACCOUNT_ACCESS_BINDING_ID, transport=transport
        )
        out, _ = capsys.readouterr()
        assert "Result" in out

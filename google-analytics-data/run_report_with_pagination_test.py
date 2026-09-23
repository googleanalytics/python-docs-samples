# Copyright 2021 Google Inc. All Rights Reserved.
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
from types import SimpleNamespace
from unittest import mock

import run_report_with_pagination

TEST_PROPERTY_ID = os.getenv("GA_TEST_PROPERTY_ID")


def test_run_report_with_pagination(capsys):
    run_report_with_pagination.run_report_with_pagination(TEST_PROPERTY_ID)
    out, _ = capsys.readouterr()
    assert "Report result" in out


def test_run_report_with_pagination_requests_pages_until_row_count():
    responses = [
        SimpleNamespace(row_count=250001, rows=[]),
        SimpleNamespace(row_count=250001, rows=[]),
        SimpleNamespace(row_count=250001, rows=[]),
    ]
    client = mock.Mock()
    client.run_report.side_effect = responses

    with mock.patch.object(
        run_report_with_pagination, "BetaAnalyticsDataClient", return_value=client
    ), mock.patch.object(run_report_with_pagination, "print_run_report_response"):
        run_report_with_pagination.run_report_with_pagination("123")

    offsets = [request.offset for (request,) in client.run_report.call_args_list]
    assert offsets == [0, 100000, 200000]

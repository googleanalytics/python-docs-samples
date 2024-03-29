#!/usr/bin/env python

# Copyright 2021 Google LLC All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Analytics Admin API sample application which prints access bindings
under the specified parent account.

See https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1alpha/accounts.accessBindings/list
for more information.
"""
# [START analyticsadmin_accounts_access_bindings_list]
from google.analytics.admin import AnalyticsAdminServiceClient


def run_sample():
    """Runs the sample."""
    # TODO(developer): Replace this variable with your Google Analytics
    #  account ID (e.g. "123456") before running the sample.
    account_id = "YOUR-GA-ACCOUNT-ID"
    list_account_access_bindings(account_id)


def list_account_access_bindings(account_id: str, transport: str = None):
    """
    Lists access bindings under the specified parent account.

    Args:
        account_id(str): The id of the account.
        transport(str): The transport to use. For example, "grpc"
            or "rest". If set to None, a transport is chosen automatically.
    """
    client = AnalyticsAdminServiceClient(transport=transport)
    results = client.list_access_bindings(parent=f"accounts/{account_id}")

    print("Result:")
    for access_binding in results:
        print(access_binding)
        print()


# [END analyticsadmin_accounts_access_bindings_list]


if __name__ == "__main__":
    run_sample()

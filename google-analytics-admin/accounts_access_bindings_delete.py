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

"""Google Analytics Admin API sample application which deletes the access binding
for the account.

See https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1alpha/accounts.accessBindings/delete
for more information.
"""
# [START analyticsadmin_accounts_access_bindings_delete]
from google.analytics.admin import AnalyticsAdminServiceClient
from google.analytics.admin_v1alpha.types import DeleteAccessBindingRequest


def run_sample():
    """Runs the sample."""

    # !!! ATTENTION !!!
    #  Running this sample may change/delete your Google Analytics account
    #  configuration. Make sure to not use the Google Analytics property ID from
    #  your production environment below.

    # TODO(developer): Replace this variable with your Google Analytics
    #  account ID (e.g. "123456") before running the sample.
    account_id = "YOUR-GA-ACCOUNT-ID"

    # TODO(developer): Replace this variable with your Google Analytics
    #  account access binding ID (e.g. "123456") before running the sample.
    account_access_binding_id = "YOUR-ACCOUNT-ACCESS-BINDING-ID"

    delete_account_access_binding(account_id, account_access_binding_id)


def delete_account_access_binding(
    account_id: str, account_access_binding_id: str, transport: str = None
):
    """
    Deletes the access binding for the account.

    Args:
        account_id(str): The Google Analytics Account ID.
        account_access_binding_id(str): Google Analytics account access binding ID.
        transport(str): The transport to use. For example, "grpc"
            or "rest". If set to None, a transport is chosen automatically.
    """
    client = AnalyticsAdminServiceClient(transport=transport)
    client.delete_access_binding(
        DeleteAccessBindingRequest(
            name=f"accounts/{account_id}/accessBindings/{account_access_binding_id}"
        )
    )
    print("Access binding deleted")


# [END analyticsadmin_accounts_access_bindings_delete]


if __name__ == "__main__":
    run_sample()

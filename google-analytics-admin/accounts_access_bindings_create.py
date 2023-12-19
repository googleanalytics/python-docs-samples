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

"""Google Analytics Admin API sample application which creates a access binding
for the account.

See https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1alpha/accounts.accessBindings/create
for more information.
"""
# [START analyticsadmin_accounts_access_bindings_create]
from google.analytics.admin import AnalyticsAdminServiceClient
from google.analytics.admin_v1alpha.types import (
    AccessBinding,
    CreateAccessBindingRequest,
)


def run_sample():
    """Runs the sample."""

    # !!! ATTENTION !!!
    #  Running this sample may change/delete your Google Analytics account
    #  configuration. Make sure to not use the Google Analytics account ID from
    #  your production environment below.

    # TODO(developer): Replace this variable with your Google Analytics
    #  account ID (e.g. "123456") before running the sample.
    account_id = "YOUR-GA-ACCOUNT-ID"

    # TODO(developer): Replace this variable with an email address of the user to
    #  link. This user will be given access to your account after running the
    #  sample.
    email_address = "TEST-EMAIL-ADDRESS"

    create_account_access_binding(account_id, email_address)


def create_account_access_binding(
    account_id: str, email_address: str, transport: str = None
):
    """
    Creates a access binding for the account.

    Args:
        account_id(str): The Google Analytics Account ID.
        email_address(str): Email address of the access binding user.
        transport(str): The transport to use. For example, "grpc"
            or "rest". If set to None, a transport is chosen automatically.
    """
    client = AnalyticsAdminServiceClient(transport=transport)
    access_binding = client.create_access_binding(
        CreateAccessBindingRequest(
            parent=f"accounts/{account_id}",
            access_binding=AccessBinding(
                user=email_address, roles=["predefinedRoles/read"]
            ),
        )
    )

    print("Result:")
    print(access_binding)


# [END analyticsadmin_accounts_access_bindings_create]

if __name__ == "__main__":
    run_sample()

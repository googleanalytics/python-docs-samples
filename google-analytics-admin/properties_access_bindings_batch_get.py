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

"""Google Analytics Admin API sample application which prints details for the
Google Analytics 4 property access binding using a batch call.

See https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1alpha/properties.accessBindings/batchGet
for more information.
"""
# [START analyticsadmin_properties_access_bindings_batch_get]
from google.analytics.admin import AnalyticsAdminServiceClient
from google.analytics.admin_v1alpha.types import BatchGetAccessBindingsRequest


def run_sample():
    """Runs the sample."""
    # TODO(developer): Replace this variable with your Google Analytics 4
    #  property ID (e.g. "123456") before running the sample.
    property_id = "YOUR-GA4-PROPERTY-ID"

    # TODO(developer): Replace this variable with your Google Analytics
    #  account access binding ID (e.g. "123456") before running the sample.
    property_access_binding_id = "YOUR-ACCOUNT-ACCESS-BINDING-ID"

    batch_get_property_access_binding(property_id, property_access_binding_id)


def batch_get_property_access_binding(
    property_id: str, property_access_binding_id: str, transport: str = None
):
    """
    Retrieves details for the Google Analytics 4 property access binding using a
    batch call.

    Args:
        property_id(str): The Google Analytics Property ID.
        property_access_binding_id(str): Google Analytics account access binding ID.
        transport(str): The transport to use. For example, "grpc"
            or "rest". If set to None, a transport is chosen automatically.
    """
    client = AnalyticsAdminServiceClient(transport=transport)
    response = client.batch_get_access_bindings(
        BatchGetAccessBindingsRequest(
            parent=f"properties/{property_id}",
            names=[
                f"properties/{property_id}/accessBindings/{property_access_binding_id}"
            ],
        )
    )

    print("Result:")
    for access_binding in response.access_bindings:
        print(access_binding)
        print()


# [END analyticsadmin_properties_access_bindings_batch_get]


if __name__ == "__main__":
    run_sample()

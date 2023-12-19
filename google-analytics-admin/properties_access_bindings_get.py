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

"""Google Analytics Admin API sample application which prints the Google
Analytics 4 property access binding details.

See https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1alpha/properties.accessBindings/get
for more information.
"""
# [START analyticsadmin_properties_access_bindings_get]
from google.analytics.admin import AnalyticsAdminServiceClient


def run_sample():
    """Runs the sample."""
    # TODO(developer): Replace this variable with your Google Analytics 4
    #  property ID (e.g. "123456") before running the sample.
    property_id = "YOUR-GA4-PROPERTY-ID"

    # TODO(developer): Replace this variable with your Google Analytics
    #  account access binding ID (e.g. "123456") before running the sample.
    property_access_binding_id = "YOUR-ACCOUNT-ACCESS-BINDING-ID"

    get_property_access_binding(property_id, property_access_binding_id)


def get_property_access_binding(
    property_id: str, property_access_binding_id: str, transport: str = None
):
    """
    Retrieves the Google Analytics 4 property access binding details.

    Args:
        property_id(str): The Google Analytics Property ID.
        property_access_binding_id(str): Google Analytics account access binding ID.
        transport(str): The transport to use. For example, "grpc"
            or "rest". If set to None, a transport is chosen automatically.
    """
    client = AnalyticsAdminServiceClient(transport=transport)
    access_binding = client.get_access_binding(
        name=f"properties/{property_id}/accessBindings/{property_access_binding_id}"
    )

    print("Result:")
    print_access_binding(access_binding)


def print_access_binding(access_binding):
    """Prints the access binding details."""
    print(f"Resource name: {access_binding.name}")
    print(f"User: {access_binding.user}")
    for role in access_binding.roles:
        print(f"Role: {role}")


# [END analyticsadmin_properties_access_bindings_get]


if __name__ == "__main__":
    run_sample()

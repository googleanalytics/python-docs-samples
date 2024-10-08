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

"""Google Analytics Admin API sample application which lists key events
for the Google Analytics 4 property.

See https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1alpha/properties.keyEvents/list
for more information.
"""
# [START analyticsadmin_properties_key_events_list]
from google.analytics.admin import AnalyticsAdminServiceClient


def run_sample():
    """Runs the sample."""
    # TODO(developer): Replace this variable with your Google Analytics 4
    #  property ID (e.g. "123456") before running the sample.
    property_id = "YOUR-GA4-PROPERTY-ID"

    list_key_events(property_id)


def list_key_events(property_id: str, transport: str = None):
    """
    Lists key events for the Google Analytics 4 property.

    Args:
        property_id(str): The Google Analytics Property ID.
        transport(str): The transport to use. For example, "grpc"
            or "rest". If set to None, a transport is chosen automatically.
    """
    client = AnalyticsAdminServiceClient(transport=transport)
    results = client.list_key_events(parent=f"properties/{property_id}")

    print("Result:")
    for key_event in results:
        print(f"Resource name: {key_event.name}")
        print(f"Event name: {key_event.event_name}")
        print(f"Create time: {key_event.create_time}")
        print(f"Deletable: {key_event.deletable}")
        print(f"Custom: {key_event.custom}")
        print()


# [END analyticsadmin_properties_key_events_list]


if __name__ == "__main__":
    run_sample()

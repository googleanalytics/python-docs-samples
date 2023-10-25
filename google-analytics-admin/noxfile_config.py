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

TEST_CONFIG_OVERRIDE = {
    # An envvar key for determining the project id to use. Change it
    # to 'BUILD_SPECIFIC_GCLOUD_PROJECT' if you want to opt in using a
    # build specific Cloud project. You can also use your own string
    # to use your own Cloud project.
    "gcloud_project_env": "BUILD_SPECIFIC_GCLOUD_PROJECT",
    # 'gcloud_project_env': 'BUILD_SPECIFIC_GCLOUD_PROJECT',
    # A dictionary you want to inject into your test. Don't put any
    # secrets here. These values will override predefined values.
    "envs": {
        "GA_TEST_PROPERTY_ID": "276206997",
        "GA_TEST_ACCOUNT_ID": "199820965",
        "GA_TEST_USER_LINK_ID": "103401743041912607932",
        "GA_TEST_PROPERTY_USER_LINK_ID": "105231969274497648555",
        "GA_TEST_WEB_DATA_STREAM_ID": "2828068992",
        "GA_TEST_WEB_DATA_SECRET_ID": "2994983412",
        "GA_TEST_CONVERSION_EVENT_ID": "2719963095",
    },
}

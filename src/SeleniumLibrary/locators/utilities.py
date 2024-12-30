# Copyright 2008-2011 Nokia Networks
# Copyright 2011-2016 Ryan Tomac, Ed Manlove and contributors
# Copyright 2016-     Robot Framework Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebElement

def is_webelement(element):
    # Hook for unit tests
    return isinstance(element, (WebElement, EventFiringWebElement))

def disallow_webelement_parent(element):
    if is_webelement(element):
        raise ValueError("This method does not allow WebElement as parent")


# -*- coding: utf-8 -*-
# file name: conftest.py 
# author: hex7
# date: 19/8/2019

import json
import pytest
import os
import logging

from selenium.webdriver import Chrome, Firefox


PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = 'config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']

logger = logging.getLogger(__name__)


@pytest.fixture(scope='session')
def config(request):
    config_path = os.path.join(request.config.rootdir, CONFIG_FILE)
    # Read the JSON config file and returns it as a parsed dict
    with open(config_path) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def config_browser(config):
    # Validate and return the browser choice from the config data
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']


@pytest.fixture(scope='session')
def config_wait_time(config):
    # Validate and return the wait time from the config data
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture(scope='function')
def browser(config_browser, config_wait_time, request):
    # Initialize WebDriver
    if config_browser == 'chrome':
        driver = Chrome()
    elif config_browser == 'firefox':
        driver = Firefox()
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')

    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(config_wait_time)
    request.cls.driver = driver
    yield
    # For cleanup, quit the driver
    driver.quit()


def pytest_runtest_setup(item):
    """
    test cases setup, config logger.
    Args:
        item:

    Returns:

    """
    config = item.config
    log_dir = item.location[0].rsplit("/", 1)[0]
    logging_plugin = config.pluginmanager.get_plugin("logging-plugin")
    report_file = os.path.join(f"{log_dir}/logs",
                               f"{item._request.node.name}.log")
    logging_plugin.set_log_path(report_file)


def pytest_generate_tests(metafunc):
    """
    Data driver for test cases with test_data parameter.
    Args:
        metafunc: metatfunc

    Returns:

    """
    if "test_data" in metafunc.fixturenames:
        test_dir = os.path.dirname(metafunc.definition.location[0])
        test_case = os.path.basename(metafunc.definition.location[0])
        path_list = test_dir.split("/")
        for idx in range(len(path_list)):
            if path_list[idx] == "testcases":
                path_list[idx] = "testdata"
                break

        test_data_file = f"{test_case[:-2]}json"
        path_list.append(test_data_file)
        data_file = os.path.join(*tuple(path_list))
        data_file = os.path.join(metafunc.config.rootdir, data_file)
        with open(data_file) as f:
            data = json.load(f)
        test_data = data.get(metafunc.definition.name)
        metafunc.parametrize("test_data", test_data)

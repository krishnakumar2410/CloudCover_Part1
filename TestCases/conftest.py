import pytest

def pytest_configure(config):
    config._metadata['Project Name']= 'CloudCover'
    config._metadata['Module Name']= 'StackOverflow'
    config._metadata['QA Name'] = 'Krishna Mokadam'

import pytest
import requests
import logging
logger = logging.getLogger(__name__)


def test_one():
    res = requests.get('https://petstore.swagger.io/v2')
    logger.info(res)
    logger.info(res.headers)

    assert True

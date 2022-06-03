import requests
import logging

logger = logging.getLogger(__name__)


def log_response(response: requests):
    logger.info("Response:\n{}\n".format(response))
    logger.info("Response.url:\n{}\n".format(response.url))
    logger.info("Response.text:\n{}\n".format(response.text))
    logger.info("Response.encoding:\n{}\n".format(response.encoding))
    logger.info("Response.headers:\n{}\n".format(response.headers))

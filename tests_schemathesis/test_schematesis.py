import os

import schemathesis
from hypothesis import settings
from schemathesis import DataGenerationMethod

ROOT_DIR = os.path.abspath(os.pardir)
PATH_TO_YAML = os.path.join(ROOT_DIR, 'Task_files/petstore.yaml')

SERVICE_URL = "https://petstore.swagger.io/v2"

schema = schemathesis.from_path(
    PATH_TO_YAML,
    base_url=SERVICE_URL,
    data_generation_methods=[
        DataGenerationMethod.positive,
        DataGenerationMethod.negative
    ]
)

"""
    Interesting but complicated. Will investigate it deeper. 
    Not sure that it stable or produces repeatable testing results.
"""


@schema.parametrize()
@settings(max_examples=10)  # =10000 is good for CI. Default = 100.
def test_api(case):
    case.call_and_validate(headers={"api_key": "special-key"})

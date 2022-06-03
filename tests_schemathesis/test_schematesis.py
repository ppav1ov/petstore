import pytest
import schemathesis
from hypothesis import settings
from schemathesis import DataGenerationMethod

path_to_yaml = "C:\\Users\\ppavlov\\Downloads\\petstore.yaml"
service_url = "https://petstore.swagger.io/v2"

schema = schemathesis.from_path(
    path_to_yaml,
    base_url=service_url,
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

import os
from s3 import S3
from datetime import datetime
import pytest


@pytest.fixture
def s3(aws_region: str) -> S3:
    yield S3(aws_region)


S3_BUCKET = os.environ['S3_TEST_BUCKET']



def test_get_attributes(s3):
    # Given bucket and key
    bucket = S3_BUCKET
    key = 's3-test'

    # When get the attributes
    r = s3.get_attributes(bucket, key)

    # Then the file must be in S3 and update after time_before
    assert r.is_ok
    assert 'LastModified' in r.unwrap()

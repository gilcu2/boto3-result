import os
from s3 import S3
from datetime import datetime
import pytest


@pytest.fixture
def s3(aws_region: str) -> S3:
    yield S3(aws_region)


S3_BUCKET = os.environ['S3_TEST_BUCKET']


def test_put_get_object(s3: S3) -> None:
    # Given an object and key
    s = 'test'
    key = 'test-key'

    # When put in S3
    s3.put_object(S3_BUCKET, key, s)


def test_get_attributes(s3: S3) -> None:
    # Given bucket and key
    bucket = S3_BUCKET
    key = 's3-test'

    # When get the attributes
    r = s3.get_attributes(bucket, key)

    # Then the file must be in S3 and update after time_before
    assert r.is_ok
    assert 'LastModified' in r.unwrap()

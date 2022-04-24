import os
from s3 import S3
from datetime import datetime
import pytest
from option import Result, Option, Ok, Err

S3_BUCKET = os.environ['S3_TEST_BUCKET']


@pytest.fixture
def s3() -> S3:
    yield S3.create().unwrap()


def test_put_get_object(s3: S3) -> None:
    # Given an object data and key
    s = 's3_test'
    key = 'test-key'

    # When put and get the data in S3
    r = s3.put_object(S3_BUCKET, key, s) \
        .flatmap(lambda _: s3.get_object(S3_BUCKET, key))

    # The result must be ok
    assert r.is_ok

    # And contains the input string
    assert r.unwrap().decode('utf-8') == s



def test_get_attributes(s3: S3) -> None:
    # Given bucket, key
    key = 's3-test'
    s = 's3_test'

    # When put object and get the attributes
    r = s3.put_object(S3_BUCKET, key, s) \
        .flatmap(lambda _: s3.get_attributes(S3_BUCKET, key))

    # Then the result is ok and have attributes
    assert r.is_ok
    assert 'LastModified' in r.unwrap()

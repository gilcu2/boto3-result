# Boto3-result

Boto3 with a class for each AWS service and returning Result instead of trowing exception

## Example

## Test

Need:
- A valid boto3 configuration as explained in 
[boto3 config](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html)
- Env vars: 
  - S3_TEST_BUCKET with writing permission

```shell
pytest
```
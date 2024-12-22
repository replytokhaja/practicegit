import boto3
from botocore.exceptions import NoCredentialsError

# Initialize the S3 client
s3 = boto3.client('s3')

def list_buckets():
    """List all S3 buckets."""
    try:
        response = s3.list_buckets()
        print("Existing buckets:")
        for bucket in response['Buckets']:
            print(f"  {bucket['Name']}")
    except NoCredentialsError:
        print("Credentials not available.")

def upload_file(bucket_name, file_name, object_name=None):
    """Upload a file to an S3 bucket."""
    if object_name is None:
        object_name = file_name

    try:
        s3.upload_file(file_name, bucket_name, object_name)
        print(f"File {file_name} uploaded to {bucket_name}/{object_name}")
    except NoCredentialsError:
        print("Credentials not available.")
    except Exception as e:
        print(f"Failed to upload {file_name}: {e}")

if __name__ == "__main__":
    # List all buckets
    list_buckets()

    # Upload a file to a specific bucket
    bucket_name = "your-bucket-name"
    file_name = "path/to/your/file.txt"
    upload_file(bucket_name, file_name)

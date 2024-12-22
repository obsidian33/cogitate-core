import argparse
import boto3
import json
from botocore.exceptions import ClientError


def search_secrets(search_substring, profile=None, region='us-west-2'):
    if profile:
        session = boto3.Session(
            profile_name=profile,
            region_name=region
          )
    else:
        session = boto3.Session(region_name=region)

    client = session.client('secretsmanager')

    paginator = client.get_paginator('list_secrets')
    for page in paginator.paginate(PaginationConfig={'PageSize': 100}):
        for secret in page['SecretList']:
            secret_name = secret['Name']
            print(f"Checking secret: {secret_name}")
            if search_substring.lower() in secret_name.lower():
                try:
                    secret_value = client.get_secret_value(SecretId=secret_name)['SecretString']
                    try:
                        secret_data = json.loads(secret_value)
                        print(json.dumps(secret_data, indent=2))
                    except json.JSONDecodeError:
                        secret_data = secret_value
                        print(f"\t{secret_value}")
                except ClientError as e:
                    print(f"Error retrieving secret {secret_name}: {e}")
            else:
                try:
                    secret_value = client.get_secret_value(SecretId=secret_name)['SecretString']
                    try:
                        secret_data = json.loads(secret_value)
                    except json.JSONDecodeError:
                        secret_data = secret_value

                    if type(secret_data) is dict:
                        found = False
                        for key, value in secret_data.items():
                            if search_substring.lower() in key.lower() or search_substring.lower() in str(value).lower():
                                print(f"\nFound in {secret_name}:\n\t{key} = {value}\n")
                                found = True

                        if found:
                            print(json.dumps(secret_data, indent=2))
                    else:
                        if search_substring.lower() in str(secret_data).lower():
                            print(f"\nFound in {secret_name}: {secret_data}\n")
                        continue

                except ClientError as e:
                    print(f"Error retrieving secret {secret_name}: {e}")


def main(search_substring, profile, region):
    if profile:
        profiles = [profile]
    else:
        session = boto3.Session()
        profiles = session.available_profiles

    for profile in profiles:
        if profile == 'default':
            continue

        print(f"Searching in profile: {profile}")
        search_secrets(search_substring, profile=profile, region=region)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Search for secrets in AWS Secrets Manager')
    parser.add_argument('-p', '--profile', type=str, help='AWS profile to use for searching', default=None)
    parser.add_argument('-r', '--region', type=str, help='AWS region to search in', default='us-west-2')
    parser.add_argument('search_substring', type=str, help='Substring to search for in secret names')
    args = parser.parse_args()

    main(args.search_substring, args.profile, args.region,)

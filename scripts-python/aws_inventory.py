import boto3
import json


def list_ec2_instances():
    """Liste toutes les instances EC2"""
    ec2 = boto3.client('ec2', region_name='eu-west-3')
    response = ec2.describe_instances()

    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append({
                "id": instance['InstanceId'],
                "type": instance['InstanceType'],
                "state": instance['State']['Name'],
                "region": "eu-west-3"
            })

    return instances


def list_s3_buckets():
    """Liste tous les buckets S3"""
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    buckets = []
    for bucket in response['Buckets']:
        buckets.append({
            "name": bucket['Name'],
            "created": bucket['CreationDate'].isoformat()
        })

    return buckets


def list_iam_users():
    """Liste tous les utilisateurs IAM"""
    iam = boto3.client('iam')
    response = iam.list_users()

    users = []
    for user in response['Users']:
        users.append({
            "username": user['UserName'],
            "created": user['CreateDate'].isoformat(),
            "arn": user['Arn']
        })

    return users


def run_inventory():
    print("=== AWS Inventory ===\n")

    # EC2
    print("EC2 Instances:")
    instances = list_ec2_instances()
    if instances:
        for i in instances:
            print(f"  {i['id']} — {i['type']} — {i['state']}")
    else:
        print("  No instances found")

    # S3
    print("\nS3 Buckets:")
    buckets = list_s3_buckets()
    if buckets:
        for b in buckets:
            print(f"  {b['name']} — created {b['created']}")
    else:
        print("  No buckets found")

    # IAM
    print("\nIAM Users:")
    users = list_iam_users()
    if users:
        for u in users:
            print(f"  {u['username']} — {u['created']}")
    else:
        print("  No users found")

    # Export JSON
    report = {
        "ec2_instances": instances,
        "s3_buckets": buckets,
        "iam_users": users
    }

    with open("reports/aws_inventory.json", "w") as f:
        json.dump(report, f, indent=2)

    print("\nReport saved: reports/aws_inventory.json")


if __name__ == "__main__":
    run_inventory()

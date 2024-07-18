import boto3

import boto3

def get_all_log_groups():
    client = boto3.client('logs')
    log_groups = []
    paginator = client.get_paginator('describe_log_groups')
    
    for page in paginator.paginate():
        log_groups.extend(page['logGroups'])
    
    return [lg['logGroupName'] for lg in log_groups]

def update_log_group_retention(log_group_name, retention_days=7):
    client = boto3.client('logs')
    try:
        client.put_retention_policy(
            logGroupName=log_group_name,
            retentionInDays=retention_days
        )
        print(f"Updated retention policy for {log_group_name} to {retention_days} days.")
    except Exception as e:
        print(f"Error updating retention policy for {log_group_name}: {e}")

if __name__ == "__main__":
    log_groups = get_all_log_groups()
    print(log_groups)
    
    for log_group_name in log_groups:
        update_log_group_retention(log_group_name)
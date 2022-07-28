#!/usr/bin/env python3

# Import modules
import boto3

def main():
  """
  Main function to run the program
  """
  queue_url = 'http://localhost:4566/000000000000/login-queue'
  sqs = boto3.client('sqs', region_name='localhost', endpoint_url=queue_url, aws_access_key_id='awslocalkeyid', aws_secret_access_key='awslocalkey')
  message = sqs.receive_message(
    QueueUrl=queue_url,
  )
  print(message)

if __name__ == '__main__':
  main()

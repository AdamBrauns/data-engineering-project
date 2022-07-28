#!/usr/bin/env python3

# Import modules
import boto3
import json
from configparser import ConfigParser

def main(sqs, queue_url):
  """
  Main function to run the program
  """
  wait_sec = 10
  max_messages = 10
  while(1):
    try:
      # Receive messages in batches
      messages = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=10,
        WaitTimeSeconds=wait_sec
      )

      if (len(messages) > 1):
        for msg in messages['Messages']:
          usr_atr = json.loads(msg['Body'])
          print(msg)
      else:
        print('Error: Data is missing the following key: {0}'.format(e))
        pass
    except Exception as e:
      print('Error: {0}'.format(e))
      exit()

def sqs_connect():
  """
  Connect to sqs queue

  :return: sqs queue
  :return: queue url
  """
  try:
    sqs_params = config_parser('config.ini', 'sqs')
    return [boto3.client('sqs', region_name=sqs_params['region_name'], endpoint_url=sqs_params['queue_url'], aws_access_key_id=sqs_params['aws_access_key_id'], aws_secret_access_key=sqs_params['aws_secret_access_key']), sqs_params['queue_url']]
  except KeyError as e:
    print('SQS config missing parameter: {0}'.format(e))
    exit()

def config_parser(filename, section):
  """
  Parse config files

  :param filename: file to be parsed
  :param section: section of the file to be parsed
  :return: dictionary of config params
  """
  parser = ConfigParser()
  parser.read(filename)

  conf_file = {}
  if parser.has_section(section):
    params = parser.items(section)
    for param in params:
      conf_file[param[0]] = param[1]
  else:
    raise Exception('File {0} does not contain section {1}'.format(filename, section))
  return conf_file

if __name__ == '__main__':
  [sqs, queue_url] = sqs_connect()
  try:
    main(sqs, queue_url)
  except KeyboardInterrupt:
    print('\nExiting the program')
    exit()

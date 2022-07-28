#!/usr/bin/env python3

# Import modules
import boto3
import hashlib
import json
import psycopg2
from configparser import ConfigParser
from datetime import datetime

def main(sqs, queue_url, conn, cursor):
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
          try:
            usr_atr = json.loads(msg['Body'])
            cursor.execute("INSERT INTO user_logins (user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date) VALUES (%s, %s, %s, %s, %s, %s, %s)", (usr_atr['user_id'], usr_atr['device_type'], mask_data(usr_atr['ip']), mask_data(usr_atr['device_id']), usr_atr['locale'], usr_atr['app_version'].replace('.', ''), datetime.today().strftime('%Y-%m-%d')))
          except KeyError as e:
            print('Error: Data is missing data ({0}), removing from queue...'.format(e))
            sqs.delete_message(
              QueueUrl=queue_url,
              ReceiptHandle=msg['ReceiptHandle']
            )

          conn.commit()

      else:
        print('Info: No new messages in {0} second(s)'.format(wait_sec))
        pass
    except Exception as e:
      print('Error: {0}'.format(e))
      exit_program(conn, cursor)

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

def db_connect():
  """
  Make connection to database

  :return: connection object
  :return: database cursor
  """
  try:
    params = config_parser('config.ini', 'postgresql')
    conn = psycopg2.connect(**params)
  except Exception as e:
    print('Error: {0}'.format(e))
    exit()
  else:
    return conn, conn.cursor()

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

def mask_data(conf_data):
  """
  Mask confidential information

  :param conf_data: data to be masked
  :return: masked value
  """
  return hashlib.sha256(conf_data.encode()).hexdigest()

def exit_program(conn, cursor):
  """
  Close database connection and exit the program

  :param conn: database connection
  :param cursor: database cursor
  """
  print('\nNow exiting the program... Goodbye!')
  cursor.close()
  conn.close()
  exit()

if __name__ == '__main__':
  [sqs, queue_url] = sqs_connect()
  [conn, cursor] = db_connect()
  try:
    main(sqs, queue_url, conn, cursor)
  except KeyboardInterrupt:
    exit_program(conn, cursor)

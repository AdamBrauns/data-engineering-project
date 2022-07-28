# Data Engineer Project
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#set-up-config-file">Set up config file</a></li>
        <li><a href="#install-psycopg2">Install psycopg2</a></li>
      </ul>
    </li>
    <li><a href="#running-the-application">Running the application</a></li>
    <li><a href="#next-steps">Next Steps</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

For this data engineering exercise, I wrote a small python application that reads data from an AWS SQS Queue, transforms the data, and then writes to a Postgres database. To setup the infracture required for this application, see the README provided in the data-engineering-take-home directory located in this repository.

### Built with

* [![Python][python-shield]][python-url]
* [![Docker][docker-shield]][docker-url]
* [![AWS][aws-shield]][aws-url]
* [![PostgreSQL][postgres-shield]][postgres-url]

## Getting Started

After following the directions contained in the README inside the data-engineering-take-home directory, there is only a few additional steps required to run the application.

### Set up config file

To allign with security best practices, normally you would add the **config.ini** file to **.gitignore** to hide sensative data. However, as the instructions provide username/password, I chose to provide it in the repository for simplicity. The file should contain the following structure:
```
[sqs]
region_name=<value>
queue_url=<value>
aws_access_key_id=<value>
aws_secret_access_key=<value>

[postgresql]
host=<value>
database=<value>
user=<value>
password=<value>
```

### Install psycopg2

In order to connect and write to the postgres database, I utilized a python module called psycopg2. To install said module, simply type:

`pip3 install psycopg2-binary`

## Running the Application

To run the application, ensure that all the prerequisites in this README and the README located in the data-engineering-take-home directory have been followed. After validating all required software is installed and the infrastructure is running, simply run the program with the following command:

`python3 data_engineering_project.py`

The program will continue to run until the user exits it by executing a `ctr-c` key combination.  Note that the program will return data to the screen about the actions it is performing.

## Next Steps

- Enhance logging functionality
  - The logging in this application can be improved in a few categories:
    - Writing to syslog facility for a centralized logging location
    - More verbose logging to give enhanced details to simplify troubleshooting efforts
- Better error handling
  - The application could use an overhaul to error handling in general
    - Improve the current error handling to include additional information
    - Build in more error handlers
    - etc.
- Implement a daemonized approach
  - Implementing a daemon or cron approach will allow a more seamless experience
- The main function could be redesigned for better maintainability and readability

## Contact
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- MARKDOWN LINKS & IMAGES -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/adam-brauns/
[python-shield]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[python-url]: https://python.org
[docker-shield]: https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white
[docker-url]: https://www.docker.com/
[aws-shield]: https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white
[aws-url]: https://aws.amazon.com/
[postgres-shield]: https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white
[postgres-url]: https://www.postgresql.org/
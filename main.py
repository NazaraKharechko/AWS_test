import boto3
import socket
from time import time
import requests


def write_metric(value, metric):
    d = boto3.client('cloudwatch')
    d.put_metric_data(Namespace='Web Status',
                      MetricData=[
                          {
                              'MetricName': metric,
                              'Dimensions': [
                                  {
                                      'Name': 'Status',
                                      'Value': 'Page load time',
                                  },
                              ],
                              'Value': value,
                          },
                      ])


def check_site(url1, url2):
    load_time = 0.005
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created")
    except socket.error:
        print(f"[ERROR:] Cannot connect to site {url1} or {url2}")
        return 0.005

    if url1:
        print(f"Cheking {url1} Page load time")
        start_time1 = time()
        response = requests.get(url1)
        print(response)
        response.close()
        end_time1 = time()

        load_time1 = round(end_time1 - start_time1, 3)
        print(f'{url1} load in {load_time1} seconds')

    if url2:
        print(f" \n \n Cheking {url2} Page load time")
        start_time2 = time()
        response = requests.get(url2)
        print(response)
        response.close()
        end_time2 = time()

        load_time2 = round(end_time2 - start_time2, 3)
        print(f'{url2} load in {load_time2} seconds')


def handler(event, context):
    websiteurl1 = 'https://facebook.com'
    websiteurl2 = 'https://google.com'
    metricname = f'{websiteurl1} Page load'

    r = check_site(websiteurl1, websiteurl2)
    write_metric = (r, metricname)


if __name__ == "__main__":
    handler('', '')

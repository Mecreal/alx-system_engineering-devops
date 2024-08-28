#!/usr/bin/python3
"""Module to check if a host exists in Datadog."""
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi

# Set up the configuration
configuration = Configuration()
configuration.api_key['apiKeyAuth'] = '2904ed83417d4b1f227f1f0d2c5638b7'  # API Key
configuration.api_key['appKeyAuth'] = '17a1cddfae6ed51379bf7639a688ac471ffedf15'  # Application Key

# Create an instance of the API class
with ApiClient(configuration) as api_client:
    api_instance = HostsApi(api_client)

    try:
        # Get the list of all hosts
        response = api_instance.list_hosts()

        if response.host_list:
            print(f"Total hosts: {response.total_matching}")
            print("Hosts visible in Datadog:")
            for host in response.host_list:
                print(f"Hostname: {host.name}")
                print(f"Alias: {host.alias}")
                print(f"Tags: {host.tags}")
                print("---")
        else:
            print("No hosts are visible in Datadog. Please check your configuration.")

    except Exception as e:
        print(f"An error occurred: {e}")

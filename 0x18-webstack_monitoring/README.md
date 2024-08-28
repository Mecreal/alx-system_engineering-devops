# Webstack Monitoring Project

## Overview
This project focuses on implementing webstack monitoring using Datadog. The goal is to set up monitoring for our web servers and applications to ensure optimal performance and quick issue detection.

## Project Tasks

### 0. Sign up for Datadog and install datadog-agent
- Sign up for a free Datadog account
- Install datadog-agent on web-01
- Create an application key
- Configure the server to be visible in Datadog

### 1. Monitor some metrics
- Set up monitors for read and write requests per second
- Configure alerts within the Datadog dashboard

### 2. Create a dashboard
- Create a new dashboard with at least 4 widgets
- Monitor various metrics for visualization

## Server Information
- Web-01: IP 34.234.204.122
- Web-02: IP 52.91.121.254
- LB-01: IP 3.94.211.152

## Requirements
- All scripts should be written in Bash
- Scripts must pass Shellcheck (version 0.3.7) without errors
- The first line of all scripts should be `#!/usr/bin/env bash`
- All files should end with a new line

## Author
Abouabid Hamza

## License
This project is part of the ALX System Engineering & DevOps curriculum.
# Project: Web Infrastructure Design

## Table of Contents
1. [Simple Web Stack](#simple-web-stack)
2. [Distributed Web Infrastructure](#distributed-web-infrastructure)
3. [Secured and Monitored Web Infrastructure](#secured-and-monitored-web-infrastructure)
4. [Scale Up](#scale-up)

---

## Simple Web Stack
**File:** `0-simple_web_stack`

### Task
Design a one server web infrastructure hosting `www.foobar.com`.

### Requirements
- **Components:**
  - 1 server
  - 1 web server (Nginx)
  - 1 application server
  - 1 set of application files (code base)
  - 1 database (MySQL)
  - Domain name `foobar.com` with www record pointing to IP `8.8.8.8`
- **Explanations Needed:**
  - Role of server, domain name, DNS record, web server, application server, database
  - Communication method with user's computer
  - Infrastructure issues: SPOF, downtime for maintenance, scaling limits

### Repository
- **GitHub**: `alx-system_engineering-devops`
- **Directory**: `0x09-web_infrastructure_design`

---

## Distributed Web Infrastructure
**File:** `1-distributed_web_infrastructure`

### Task
Design a three server web infrastructure for `www.foobar.com`.

### Requirements
- **Additions:**
  - 2 servers
  - 1 load-balancer (HAproxy)
- **Explanations Needed:**
  - Reason for each added element
  - Load balancer's distribution algorithm and operation
  - Active-Active vs Active-Passive load balancing
  - Database Primary-Replica clustering
  - Primary vs Replica node differences
- **Infrastructure Issues:**
  - SPOF locations
  - Security concerns (no firewall, no HTTPS)
  - Absence of monitoring

### Repository
- **GitHub**: `alx-system_engineering-devops`
- **Directory**: `0x09-web_infrastructure_design`

---

## Secured and Monitored Web Infrastructure
**File:** `2-secured_and_monitored_web_infrastructure`

### Task
Design a secure, encrypted, and monitored three server web infrastructure for `www.foobar.com`.

### Requirements
- **Additions:**
  - 3 firewalls
  - 1 SSL certificate for HTTPS
  - 3 monitoring clients
- **Explanations Needed:**
  - Purpose of each added element
  - Role of firewalls
  - Reasons for HTTPS usage
  - Monitoring purposes and data collection
  - Monitoring web server QPS
- **Infrastructure Issues:**
  - SSL termination at load balancer
  - Single MySQL server for write operations
  - Homogenous server component distribution

### Repository
- **GitHub**: `alx-system_engineering-devops`
- **Directory**: `0x09-web_infrastructure_design`

---

## Scale Up
**File:** `3-scale_up`

### Task
Improve the infrastructure to handle increased traffic.

### Requirements
- **Additions:**
  - 1 server
  - 1 load-balancer (HAproxy) in cluster with the existing one
  - Split components (web server, application server, database) across servers
- **Explanations Needed:**
  - Reason for each added element

### Repository
- **GitHub**: `alx-system_engineering-devops`
- **Directory**: `0x09-web_infrastructure_design`

---

### Instructions for Submission
- Complete each task and take a screenshot of your diagram.
- Upload the screenshot to an image hosting service and insert the link in the answer file.
- Push your answer file to the GitHub repository and provide the file link in the submission URL box.
- Whiteboard each task in front of a mentor, staff, or student without using a computer or notes.

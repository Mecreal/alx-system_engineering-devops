# Distributed Web Infrastructure Design for www.foobar.com
![# Distributed Web Infrastructure Design for www.foobar.com
](https://raw.githubusercontent.com/Mecreal/alx-system_engineering-devops/main/0x09-web_infrastructure_design/server1.png)
## Introduction
This document details the design of a distributed web infrastructure with three servers for hosting www.foobar.com. It outlines the roles of each component and the reasoning behind their inclusion.

## Infrastructure Components and Their Detailed Roles

### 1. Servers
- **Additional Elements:** Integration of two additional servers.
- **Purpose:** Enhance redundancy, enable load balancing, and segregate different functionalities.

### 2. Web Server (Nginx)
- **Role:** Manages HTTP requests and serves static content of the website.

### 3. Application Server
- **Role:** Executes the backend application or business logic.

### 4. Load Balancer (HAproxy)
- **Purpose:** Distributes incoming traffic across servers.
- **Distribution Algorithm:** Typically, a round-robin method is used for equal load distribution.
- **Active-Active vs Active-Passive Setup:**
  - **Active-Active:** All servers handle traffic simultaneously, maximizing resource use and providing redundancy.
  - **Active-Passive:** One server is on standby and activates only if the primary server fails, leading to less efficient resource utilization.

### 5. Database (MySQL) with Primary-Replica Setup
- **Configuration:** The database operates in a Primary-Replica cluster.
- **Functionality:** The primary node handles writes and some reads, replicating data to the read-only replica nodes.
- **Primary vs Replica Nodes:** Primary node supports read-write operations, while replicas handle read operations, aiding in load distribution and redundancy.

## Identified Infrastructure Issues

### 1. Single Point of Failure (SPOF)
- **Concerns:** Potential SPOFs include the load balancer and the primary database server.

### 2. Security Issues
- **Lack of Firewall:** Absence of a firewall exposes servers to unauthorized access and attacks.
- **No HTTPS:** Data is transmitted unencrypted, risking interception and tampering.

### 3. Absence of Monitoring
- **Implications:** Difficulty in tracking performance, health, or detecting failures and anomalies.

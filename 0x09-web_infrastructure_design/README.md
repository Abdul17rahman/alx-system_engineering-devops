# Web Infrastructure Architecture

Web Applications Infrastructure/Web Infrastructure also called internet infrastructure is the physical hardware, transmission media, and software used to interconnect computers and users on the Internet

This document outlines three progressively more robust infrastructure designs for hosting a web application at `www.foobar.com`. It also explains each component's role and the limitations and potential failure points in each architecture.

---

## 📦 1. Simple WebStack - One-Server Architecture (LAMP-like)

### Overview

A single server hosts:

- NGINX web server
- Application server (e.g., Gunicorn)
- MySQL database
- Application code (PHP, Python, etc.)

### Domain:

- `www.foobar.com` points to `8.8.8.8` via a DNS `A` record

### Request Flow:

1. User enters `www.foobar.com`
2. DNS resolves to IP `8.8.8.8`
3. NGINX receives request, routes it to app server
4. App server may query MySQL and return data to NGINX
5. NGINX sends response to client

### Components:

| Component      | Role                                                            |
| -------------- | --------------------------------------------------------------- |
| Server         | Physical/virtual machine hosting everything                     |
| Domain Name    | Human-friendly access; mapped to IP                             |
| DNS `A` Record | Resolves `www.foobar.com` to IP address                         |
| NGINX          | Handles HTTP(S), serves static content, reverse proxies dynamic |
| App Server     | Runs the application logic                                      |
| MySQL          | Stores structured data                                          |

### 🔴 Issues:

- **Single Point of Failure (SPOF)**: One server going down takes the entire system down.
- **Downtime for maintenance**: Restarting services affects all components.
- **No scalability**: Cannot handle high traffic.

---

## ⚙️ 2. Distributed Architecture (High-Level Redundancy)

### Overview

- Load balancer (HAProxy) distributes requests
- Two app servers with NGINX + application logic
- Shared MySQL database

### Request Flow:

1. User hits HAProxy load balancer
2. HAProxy sends request to one of two app servers
3. Each app server:
   - Has NGINX for static/dynamic routing
   - Passes dynamic requests to app logic
   - Queries shared MySQL DB
4. Response flows back to client

### Components:

| Component       | Role                                 |
| --------------- | ------------------------------------ |
| HAProxy         | Balances traffic between app servers |
| App Servers (2) | Each runs NGINX + app logic          |
| Shared MySQL    | Centralized data store               |

### 🔴 Issues:

- **Load Balancer SPOF**: If HAProxy fails, all access is lost.
- **Database SPOF**: One MySQL instance accepting writes is a risk.
- **All-in-one servers**: App servers may be overburdened with multiple roles.
- **No CDN**: All static content is served from app servers — can increase load.

---

## 🔐 3. Production-Grade Architecture with Security and Monitoring

### Enhancements:

- 🔁 Redundant load balancers using Keepalived (floating IP)
- 🔥 3 firewalls: one before LB, one between LB and app tier, one before DB
- 🔒 SSL certificate for HTTPS (`www.foobar.com`)
- 📈 Monitoring agents (Sumologic, Prometheus, etc.) on all tiers

### Request Flow:

1. User visits `https://www.foobar.com`
2. DNS resolves to floating IP (via `A` or `CNAME` record)
3. Active HAProxy receives and terminates SSL or forwards HTTPS
4. Request routed to healthy app server (NGINX + app logic)
5. App server queries DB
6. Response is sent back through HAProxy to client

### Additional Components:

| Component          | Role                                                            |
| ------------------ | --------------------------------------------------------------- |
| SSL Certificate    | Encrypts traffic end-to-end via HTTPS                           |
| CDN (optional)     | Serves static assets faster, offloading web servers             |
| Firewalls (3)      | Control traffic at LB, app, and DB layers                       |
| Monitoring Clients | Collect metrics (CPU, RAM, QPS, errors) from app, DB, LB, NGINX |
| Floating IP        | Allows failover between two LBs                                 |
| Backup LB          | Takes over if main LB fails                                     |

### 🔴 Issues:

- **SSL Termination at LB**: App-server traffic is unencrypted unless re-encrypted internally.
- **Single writable DB**: All writes go to one DB node; failover must be manual or automated.
- **Monolithic app servers**: If app servers also run DB/web/app logic, isolating failures is hard.

---

## 🔍 Monitoring Example: Monitoring QPS (Queries Per Second)

To monitor web server QPS:

1. Install monitoring agent on app servers (e.g., Prometheus node exporter, Sumologic collector).
2. Configure NGINX to expose metrics (stub_status or custom module).
3. Send metrics to external dashboard (e.g., Grafana, Sumologic).
4. Create alert rules based on thresholds (e.g., > 1000 QPS triggers warning).

---

## 🧠 Summary of Best Practices

| Area             | Recommendation                                                   |
| ---------------- | ---------------------------------------------------------------- |
| Load Balancing   | Use **at least 2 LBs** with failover (Keepalived or cloud LB)    |
| Web Server       | Use **NGINX on each app server**, or a **CDN** for static assets |
| Application Tier | Run application logic separately from DB/web tier if possible    |
| Database         | Add **replication and failover** (MySQL Group Replication, etc.) |
| Security         | Use **firewalls between each layer**, enforce least privilege    |
| Monitoring       | Monitor each tier (LB, app, DB) and track metrics + logs         |
| SSL              | Prefer **end-to-end encryption**, not just LB termination        |

---

## 🏁 Conclusion

You can begin with a basic setup, but always plan for growth:

- Avoid SPOFs at every layer
- Use load balancing, redundancy, monitoring, and security controls
- Consider future scale (horizontal over vertical)
- Always document assumptions and failure recovery plans

This guide aims to help you evolve your infrastructure from a single-server setup to a highly available, production-grade system.

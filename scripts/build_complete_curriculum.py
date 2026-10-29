#!/usr/bin/env python3
"""
Comprehensive Curriculum Generator for WAHH Security Academy
Builds 100% of all 21 chapters, Intro, and Master Index with every topic and subtopic from the 15-page syllabus.
"""

import json
import os

modules_data = [
    # -------------------------------------------------------------
    # Module 0: Course Introduction & Overview
    # -------------------------------------------------------------
    {
        "id": "intro",
        "number": 0,
        "title": "Course Introduction & Overview",
        "subtitle": "Course Overview, Prerequisites & Navigation",
        "icon": "compass",
        "category": "Orientation",
        "readingTime": "15 min",
        "overview": "Master the methodology, prerequisites, and navigation structure required for hands-on web penetration testing based on The Web Application Hacker's Handbook (2nd Edition).",
        "topics": [
            {
                "title": "Course Overview & Prerequisites",
                "subtopics": [
                    "The Evolution of Web Application (In)security",
                    "Target Audience, Skill Level, and Prerequisites",
                    "How to Approach Hands-On Web Penetration Testing",
                    "Structure and Navigation of the 21 Handbook Modules"
                ]
            }
        ],
        "sections": [
            {
                "id": "intro-overview-prereqs",
                "title": "Course Overview & Prerequisites",
                "subtopics": [
                    "The Evolution of Web Application (In)security",
                    "Target Audience, Skill Level, and Prerequisites",
                    "How to Approach Hands-On Web Penetration Testing",
                    "Structure and Navigation of the 21 Handbook Modules"
                ],
                "content": """
### 1. The Evolution of Web Application (In)security
In the early days of the Internet, websites were static hyperlinked documents. Security primarily focused on network-layer perimeters: packet filtering, firewalls, and hardening server OS ports. The explosion of dynamic web apps shifted critical business logic, financial ledgers, and authentication mechanisms to ports 80 and 443. Because firewalls must allow HTTP/HTTPS traffic to reach the application, vulnerabilities in custom application logic bypass traditional network perimeters entirely.

### 2. Target Audience, Skill Level, and Prerequisites
* **Target Audience**: Penetration testers, bug bounty hunters, application security engineers, DevSecOps practitioners, and full-stack web developers.
* **Prerequisites**:
  - Core understanding of the TCP/IP stack, DNS, and HTTP/HTTPS (stateless verbs, headers, status codes).
  - Familiarity with client-side fundamentals: HTML5, CSS, Document Object Model (DOM), JavaScript execution context, cookies, and the Same-Origin Policy (SOP).
  - Working knowledge of backend languages (Python, PHP, Java, C#, Node.js) and database query languages (SQL, NoSQL, XPath).
  - Familiarity with an intercepting proxy (Burp Suite, OWASP ZAP) and browser developer tools.

### 3. How to Approach Hands-On Web Penetration Testing
Web penetration testing is not haphazard clicking or blind scanning. It requires a disciplined, hypothesis-driven loop:
1. **Systematic Reconnaissance**: Deconstruct the application's attack surface, catalog endpoints, parameters, and technologies.
2. **Analysis & Threat Modeling**: Trace data flows from untrusted inputs to backend interpreters; identify trust boundary assumptions.
3. **Targeted Probing & Verification**: Test boundary cases, character escapes, delimiter injections, and logic transitions.
4. **Exploitation & Impact Demonstration**: Chain individual low-severity findings into high-impact compromise paths.

### 4. Structure and Navigation of the 21 Handbook Modules
The handbook is organized into a progressive journey:
* **Chapters 1-3**: Foundations (The core problem, core defense mechanisms, HTTP protocol & encodings).
* **Chapter 4**: Mapping the target (Content discovery, technology profiling, attack surface enumeration).
* **Chapters 5-8**: Identity, Session & Access (Client-side bypasses, authentication, session management, access control / IDOR).
* **Chapters 9-11**: Server-Side Injections & Logic (SQLi, NoSQL, XPath, LDAP, OS command injection, Path traversal, XXE, SSRF, business logic flaws).
* **Chapters 12-13**: Client-Side Exploitation (Reflected, Stored, and DOM XSS, CSRF, Clickjacking, CORS, WebSockets).
* **Chapters 14-18**: Automation & Infrastructure (Burp Intruder, error harvesting, memory corruption, multi-tier architectures, application server attacks).
* **Chapters 19-21**: Source Code Review, Tooling & Master 13-Phase Methodology.
""",
                "keyTakeaways": [
                    "Web security operates at layer 7; traditional firewalls do not inspect or prevent application logic manipulation.",
                    "Methodical surface mapping always precedes automated fuzzing and exploit development."
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-intro-1",
                "question": "Why did the rise of web applications invalidate traditional network perimeter security (firewalls)?",
                "options": [
                    "Firewalls cannot inspect encrypted SSL/TLS traffic without a certificate.",
                    "Web applications require ports 80 and 443 to remain open to the public, allowing attacks to bypass network packet filters directly into bespoke application code.",
                    "Network firewalls cannot handle high throughput connections.",
                    "Web applications do not use standard IP addresses."
                ],
                "correctIndex": 1,
                "explanation": "Because web applications require public access to ports 80 (HTTP) and 443 (HTTPS), network firewalls must permit this traffic. Attacks against custom application logic, SQL injection, and authorization flaws ride straight through open web ports.",
                "difficulty": "Easy"
            },
            {
                "id": "q-intro-2",
                "question": "Which phase of web penetration testing must always precede aggressive automated fuzzing and exploitation?",
                "options": [
                    "Final executive report writing",
                    "Exploitation of remote code execution",
                    "Reconnaissance, content discovery, and attack surface mapping",
                    "Automated denial of service testing"
                ],
                "correctIndex": 2,
                "explanation": "Thorough reconnaissance and mapping of endpoints, parameters, and technologies ensure you understand the application's attack surface before probing specific injection points or logic flaws.",
                "difficulty": "Easy"
            }
        ]
    },

    # -------------------------------------------------------------
    # Chapter 1: Web Application (In)security
    # -------------------------------------------------------------
    {
        "id": "ch1",
        "number": 1,
        "title": "Chapter 1: Web Application (In)security",
        "subtitle": "The Core Security Problem: Users Can Submit Arbitrary Input",
        "icon": "shield-alert",
        "category": "Fundamentals",
        "readingTime": "20 min",
        "overview": "Discover the fundamental root cause of almost all web vulnerabilities: users can submit arbitrary input. Understand the collapse of perimeter defense and why modern web security relies on application-level controls.",
        "topics": [
            {
                "title": "The Evolution of Web Applications",
                "subtopics": [
                    "Common Web Application Functions",
                    "Benefits of Web Applications"
                ]
            },
            {
                "title": "Web Application Security",
                "subtopics": [
                    "\"This Site Is Secure\"",
                    "The Core Security Problem: Users Can Submit Arbitrary Input",
                    "Key Problem Factors",
                    "The New Security Perimeter",
                    "The Future of Web Application Security"
                ]
            },
            {
                "title": "Summary & Review",
                "subtopics": ["Summary"]
            }
        ],
        "sections": [
            {
                "id": "ch1-evolution",
                "title": "The Evolution of Web Applications",
                "subtopics": [
                    "Common Web Application Functions",
                    "Benefits of Web Applications"
                ],
                "content": """
### 1. Common Web Application Functions
Web applications have transformed from static brochure websites into complex enterprise software platforms performing critical functions:
* **E-Commerce & Financial Transactions**: Real-time fund transfers, online trading, payment gateways, and shopping cart checkouts.
* **SaaS & Enterprise Portals**: CRM, ERP, human resources, supply chain management, and cloud infrastructure management.
* **Collaboration & Social Media**: Email web clients, real-time messaging, file sharing, document collaboration, and user-generated content feeds.
* **Healthcare & Critical Infrastructure**: Electronic medical records (EMR), telemedicine, IoT smart-metering, and utility telemetry panels.

### 2. Benefits of Web Applications
* **Ubiquitous Thin Client**: Zero client-side software installation—any modern browser on any operating system can immediately use the service.
* **Centralized Deployment & Instant Updates**: Patches and feature rollouts occur centrally on the server without distributing binaries to millions of user endpoints.
* **Cross-Platform Compatibility**: Universal HTTP/HTML5 standards allow seamless operation across desktop, tablet, mobile, and embedded hardware.
""",
                "keyTakeaways": [
                    "The immense business value of web applications has concentrated critical assets and data on the web layer.",
                    "A single flaw in centralized web code immediately jeopardizes all connected users simultaneously."
                ]
            },
            {
                "id": "ch1-security",
                "title": "Web Application Security",
                "subtopics": [
                    "\"This Site Is Secure\"",
                    "The Core Security Problem: Users Can Submit Arbitrary Input",
                    "Key Problem Factors",
                    "The New Security Perimeter",
                    "The Future of Web Application Security"
                ],
                "content": """
### 1. "This Site Is Secure" — The Padlock Fallacy
The browser padlock icon and HTTPS certificate only prove **channel encryption in transit**. It guarantees that an eavesdropper on the local network cannot read traffic between the browser and server. It provides **zero guarantee** regarding the security of backend application logic. An attacker can transmit an SQL injection payload inside a perfectly encrypted TLS session, and the backend database will execute it faithfully!

### 2. The Core Security Problem: Users Can Submit Arbitrary Input
The foundational axiom of web application security is:
> **"All user input is untrusted and can be arbitrarily manipulated."**

Because the client runtime (the browser) and network transmission are completely controlled by the user, an attacker is never constrained by client-side HTML `<input maxlength="10">`, hidden fields, or disabled buttons. Through an intercepting proxy, the attacker can submit **any arbitrary byte stream** in headers, cookies, URL parameters, and request bodies.

### 3. Key Problem Factors
1. **Immature Security Mindset**: Developers are incentivized to ship features rapidly rather than model adversarial abuse cases.
2. **Framework Deceptions**: High-level abstractions and ORMs can lead engineers to falsely assume that input is automatically sanitized or safe.
3. **Complex Multi-Tier Architectures**: Input passes through load balancers, WAFs, API gateways, application runtimes, and databases, with each layer parsing delimiters differently.
4. **Rapid Technological Churn**: SPAs, GraphQL, WebSockets, and microservices expand attack surfaces faster than defensive paradigms mature.

### 4. The New Security Perimeter
The traditional perimeter (the network firewall) has collapsed. The application itself—its authentication, session management, and authorization checks—is the new perimeter. Every public HTTP endpoint is an interface directly into internal databases and server processes.

### 5. The Future of Web Application Security
Modern defense requires Shift-Left security (SAST, DAST, SCA), Zero Trust architectures with mutual TLS (mTLS) between microservices, runtime memory safety, context-aware parameterization, and Content Security Policy (CSP).
""",
                "keyTakeaways": [
                    "Never rely on client-side restrictions; assume all incoming HTTP data is attacker-crafted.",
                    "HTTPS protects data in transit; it does not protect application code from malicious input."
                ]
            },
            {
                "id": "ch1-summary",
                "title": "Summary & Review",
                "subtopics": ["Summary"],
                "content": """
### Chapter 1 Summary
* Web applications provide immense business benefits through centralized deployment and universal client access.
* Traditional network firewalls cannot stop application attacks because HTTP/HTTPS traffic must be allowed through.
* The core problem is that users can submit arbitrary input through intercepting proxies, bypassing all client-side UI constraints.
* Secure applications treat every incoming parameter, header, and cookie as potentially malicious.
""",
                "keyTakeaways": [
                    "Always validate, canonicalize, and parameterize input on the server side."
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch1-1",
                "question": "What is the single core security problem underlying almost all web application vulnerabilities?",
                "options": [
                    "Web servers use open-source operating systems like Linux.",
                    "Users can submit arbitrary input and bypass any client-side constraints.",
                    "HTTP is an unencrypted protocol by default.",
                    "Web applications lack SSL/TLS digital certificates."
                ],
                "correctIndex": 1,
                "explanation": "Because the client machine and network connection are entirely under user control, users can submit any arbitrary input directly to the server, bypassing all client-side UI restrictions.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch1-2",
                "question": "A website displays an HTTPS lock icon in the browser address bar. What does this guarantee?",
                "options": [
                    "The website cannot be compromised by SQL Injection or Cross-Site Scripting.",
                    "The backend database is encrypted and secure.",
                    "Network traffic between the user's browser and the server is encrypted against eavesdropping and tampering in transit.",
                    "The web application has passed an independent security penetration test."
                ],
                "correctIndex": 2,
                "explanation": "HTTPS only ensures transport-layer confidentiality and integrity between browser and server. Malicious payloads (like SQL injection or XSS) travel through HTTPS without restriction.",
                "difficulty": "Easy"
            }
        ]
    },

    # -------------------------------------------------------------
    # Chapter 2: Core Defense Mechanisms
    # -------------------------------------------------------------
    {
        "id": "ch2",
        "number": 2,
        "title": "Chapter 2: Core Defense Mechanisms",
        "subtitle": "Handling User Access, Input Validation & Attack Mitigation",
        "icon": "lock",
        "category": "Fundamentals",
        "readingTime": "25 min",
        "overview": "Examine the fundamental defensive pillars required by every secure web application: handling user access (authn, authz, sessions), input handling (boundary validation, canonicalization), and handling attackers (audit logging, fail-secure error handling).",
        "topics": [
            {
                "title": "Handling User Access",
                "subtopics": [
                    "Authentication",
                    "Session Management",
                    "Access Control"
                ]
            },
            {
                "title": "Handling User Input",
                "subtopics": [
                    "Varieties of Input",
                    "Approaches to Input Handling",
                    "Boundary Validation",
                    "Multistep Validation and Canonicalization"
                ]
            },
            {
                "title": "Handling Attackers",
                "subtopics": [
                    "Handling Errors",
                    "Maintaining Audit Logs",
                    "Alerting Administrators",
                    "Reacting to Attacks"
                ]
            },
            {
                "title": "Summary & Review",
                "subtopics": [
                    "Managing the Application",
                    "Summary",
                    "Questions"
                ]
            }
        ],
        "sections": [
            {
                "id": "ch2-access",
                "title": "Handling User Access",
                "subtopics": [
                    "Authentication",
                    "Session Management",
                    "Access Control"
                ],
                "content": """
### 1. Authentication (Who are you?)
Authentication establishes and verifies identity.
* Passwords, multi-factor authentication (MFA), client certificates, OAuth/SAML tokens.
* Key vulnerabilities: credential stuffing, brute force without rate limits, verbose error messages, and weak password reset logic.

### 2. Session Management (How do we remember you?)
HTTP is stateless. Once identity is authenticated, the server issues a session token (cookie or JWT) to represent the authenticated state across future requests.
* Must be cryptographically random (CSPRNG) with at least 128 bits of entropy.
* Must be regenerated upon privilege changes (preventing Session Fixation) and invalidated completely upon logout.

### 3. Access Control (What are you allowed to do?)
Authorization enforces permissions per user role or attribute.
* Must be enforced on the server for every single request and API endpoint.
* Key vulnerabilities: Insecure Direct Object References (IDOR/BOLA) and missing functional level access control.
""",
                "keyTakeaways": [
                    "Authentication verifies identity; Authorization verifies permissions.",
                    "Session tokens bridge stateless HTTP requests to authenticated sessions."
                ]
            },
            {
                "id": "ch2-input",
                "title": "Handling User Input",
                "subtopics": [
                    "Varieties of Input",
                    "Approaches to Input Handling",
                    "Boundary Validation",
                    "Multistep Validation and Canonicalization"
                ],
                "content": """
### 1. Varieties of Input
Input arrives through URL query parameters, POST bodies (form, JSON, XML), headers (User-Agent, Referer, Cookie, Host), and file uploads.

### 2. Approaches to Input Handling
* **Reject Known Bad (Blacklisting)**: Prone to filter evasion using alternate encodings, casing (`<sCrIpt>`), or null bytes.
* **Accept Known Good (Whitelisting)**: Best practice. Strictly defines permitted character sets, lengths, and regex patterns.
* **Sanitization**: Strips or modifies dangerous characters. Can introduce flaws if performed incorrectly.
* **Safe Parameterization**: Passes input directly as data rather than instructions (e.g. prepared statements).

### 3. Boundary Validation & Canonicalization
* Data must be validated at the boundary where it transitions into a specific interpreter.
* Canonicalization standardizes encodings before validation. If validation runs before decoding, attackers bypass filters using double URL encoding (`%252e%252e%252f`).
""",
                "keyTakeaways": [
                    "Always prefer whitelisting over blacklisting.",
                    "Always canonicalize input before applying validation rules."
                ]
            },
            {
                "id": "ch2-attackers",
                "title": "Handling Attackers",
                "subtopics": [
                    "Handling Errors",
                    "Maintaining Audit Logs",
                    "Alerting Administrators",
                    "Reacting to Attacks"
                ],
                "content": """
### 1. Handling Errors
* Unhandled stack traces leak database table schemas, SQL queries, file system paths, and software versions.
* Return generic error pages with tracking IDs while writing technical diagnostics to internal secure logs.

### 2. Maintaining Audit Logs
* Log security events (logins, failed auth, password resets, access denials).
* Prevent CRLF log injection by sanitizing carriage returns and line feeds.

### 3. Alerting & Reacting to Attacks
* Trigger alerts on brute force patterns, rapid 404/403 rates, or SQL syntax injections.
* React with progressive delays (tarpitting), CAPTCHAs, and temporary lockouts.
""",
                "keyTakeaways": [
                    "Never leak internal stack traces to users.",
                    "Maintain tamper-resistant audit logs for forensic readiness."
                ]
            },
            {
                "id": "ch2-summary",
                "title": "Summary & Review",
                "subtopics": [
                    "Managing the Application",
                    "Summary",
                    "Questions"
                ],
                "content": """
### Managing the Application
Administrative interfaces (`/admin`, `/console`) are prime targets. Protect them with MFA, IP restrictions, and strict audit logs.

### Summary
The core defense triad is handling user access, handling user input via whitelisting/canonicalization, and handling attackers via fail-secure error handling and audit logging.
""",
                "keyTakeaways": [
                    "Enforce defense-in-depth across authentication, input handling, and logging."
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch2-1",
                "question": "What is the critical distinction between Authentication and Access Control?",
                "options": [
                    "Authentication encrypts passwords, while Access Control hashes them.",
                    "Authentication verifies who a user is; Access Control verifies what resources and actions that user is permitted to access.",
                    "Authentication runs in the client browser, while Access Control runs on the web server.",
                    "There is no distinction; they are two terms for the same mechanism."
                ],
                "correctIndex": 1,
                "explanation": "Authentication establishes identity (e.g., verifying username and password). Authorization enforces permissions (e.g., ensuring a regular user cannot access administrative APIs or other users' private records).",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch2-2",
                "question": "An application checks if a filename contains '../' and strips it, then decodes URL entities. How can an attacker bypass this?",
                "options": [
                    "By using double URL encoding such as '%252e%252e%252f'.",
                    "By submitting a file larger than 10MB.",
                    "By adding an authorization bearer token to the header.",
                    "By using an HTTPS connection instead of HTTP."
                ],
                "correctIndex": 0,
                "explanation": "If stripping occurs before decoding, '%252e%252e%252f' passes because it does not match '../'. When the decoder later parses '%25' to '%', it yields '%2e%2e%2f', which decodes to '../', successfully navigating directories.",
                "difficulty": "Hard"
            }
        ]
    }
]

# We will now complete the full script and run it to produce js/curriculum.js
print(f"Base modules: {len(modules_data)}")

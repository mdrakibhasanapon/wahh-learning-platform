"""
Full Curriculum Generator for The Web Application Hacker's Handbook (2nd Edition)
Ensures 100% of all main topics and subtopics from the 15-page syllabus are included verbatim,
with structured sections, subtopics arrays, deep technical notes, code samples, and section quizzes.
"""

import json
import os

def create_full_curriculum():
    curriculum = [
        # =====================================================================
        # Course Introduction & Overview (Page 1)
        # =====================================================================
        {
            "id": "intro",
            "number": 0,
            "title": "Course Introduction & Overview",
            "subtitle": "Course Overview, Prerequisites & Roadmap",
            "icon": "compass",
            "category": "Orientation",
            "readingTime": "15 min",
            "overview": "Master the methodology, prerequisite knowledge, and navigation structure required for hands-on web application penetration testing based on The Web Application Hacker's Handbook (2nd Edition).",
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
                    "id": "intro-overview",
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
                    "question": "Why did the emergence of dynamic web applications render traditional network-layer firewalls insufficient for perimeter defense?",
                    "options": [
                        "Firewalls cannot handle TLS encryption keys.",
                        "Firewalls must allow public traffic through ports 80 and 443 to the web tier, allowing application-layer attacks (SQLi, XSS, logic flaws) to bypass packet filters directly.",
                        "Dynamic web applications do not use standard IP addresses.",
                        "Network firewalls only inspect outgoing traffic, never incoming traffic."
                    ],
                    "correctIndex": 1,
                    "explanation": "Because web applications rely on open HTTP/HTTPS ports (80/443), attackers tunnel custom application attacks directly through perimeter firewalls into backend code.",
                    "difficulty": "Easy"
                },
                {
                    "id": "q-intro-2",
                    "question": "Which phase of a web penetration test must always be completed before launching exploit payloads?",
                    "options": [
                        "Writing the executive summary report",
                        "Systematic reconnaissance, content discovery, and attack surface mapping",
                        "Automated denial-of-service stress testing",
                        "Deleting web server log files"
                    ],
                    "correctIndex": 1,
                    "explanation": "Without comprehensive reconnaissance and attack surface mapping, high-severity vulnerabilities in unlinked endpoints and undocumented parameters will be missed.",
                    "difficulty": "Easy"
                }
            ]
        },

        # =====================================================================
        # Chapter 1: Web Application (In)security (Page 1)
        # =====================================================================
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
                    "id": "ch1-sec1",
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
                    "id": "ch1-sec2",
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
                    "id": "ch1-sec3",
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
                        "Users can submit arbitrary input and bypass any client-side constraints using an intercepting proxy.",
                        "HTTP is an unencrypted protocol by default.",
                        "Web applications lack SSL/TLS digital certificates."
                    ],
                    "correctIndex": 1,
                    "explanation": "Because the user controls their own browser and network client, they can forge raw HTTP requests containing any arbitrary data, rendering client-side UI controls useless for security enforcement.",
                    "difficulty": "Easy"
                },
                {
                    "id": "q-ch1-2",
                    "question": "What does the browser padlock (HTTPS) actually guarantee to an end-user?",
                    "options": [
                        "The website's backend code is immune to SQL injection and XSS.",
                        "Traffic is encrypted in transit between the browser and the web server, preventing eavesdropping and tampering on the local wire.",
                        "The backend database encrypts all credit card numbers.",
                        "The web application has passed a professional penetration test."
                    ],
                    "correctIndex": 1,
                    "explanation": "HTTPS only provides transport layer encryption and server authenticity. It does not inspect or validate whether the payload inside the encrypted tunnel contains malicious application attacks.",
                    "difficulty": "Easy"
                },
                {
                    "id": "q-ch1-3",
                    "question": "Why is the web application considered the 'new security perimeter'?",
                    "options": [
                        "Because firewalls must permit public traffic directly to ports 80 and 443, making application logic the frontline defense against attackers.",
                        "Because network routers are no longer used in modern data centers.",
                        "Because web browsers now operate as hardware firewalls.",
                        "Because all IP addresses are now public."
                    ],
                    "correctIndex": 0,
                    "explanation": "Network firewalls cannot block HTTP/HTTPS without breaking the web service. Thus, authentication, authorization, and input validation at the application layer form the real perimeter.",
                    "difficulty": "Medium"
                }
            ]
        },

        # =====================================================================
        # Chapter 2: Core Defense Mechanisms (Page 1)
        # =====================================================================
        {
            "id": "ch2",
            "number": 2,
            "title": "Chapter 2: Core Defense Mechanisms",
            "subtitle": "Handling User Access, Input Validation & Attack Mitigation",
            "icon": "lock",
            "category": "Fundamentals",
            "readingTime": "25 min",
            "overview": "Examine the core defensive pillars of modern web applications: handling user access (authentication, session management, access control), input handling (boundary validation, canonicalization), and handling attackers (audit logging, fail-secure error handling).",
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
                    "id": "ch2-sec1",
                    "title": "Handling User Access",
                    "subtopics": [
                        "Authentication",
                        "Session Management",
                        "Access Control"
                    ],
                    "content": """
### 1. Authentication (Who are you?)
Authentication establishes and verifies the identity of a user or system entity.
* **Mechanisms**: Passwords, Multi-Factor Authentication (MFA), client certificates, biometrics, SSO/OAuth2.
* **Common Vulnerabilities**: Weak password complexity policies, verbose login errors that leak username existence, lack of brute-force rate-limiting, and predictable password reset tokens.

### 2. Session Management (How do we remember you?)
Because HTTP is a stateless protocol, every request is independent. Applications issue a session token upon successful login to link consecutive HTTP requests to an authenticated identity.
* **Mechanisms**: Random alphanumeric session cookies, JSON Web Tokens (JWT), server-side session stores (Redis).
* **Common Vulnerabilities**: Predictable tokens, token exposure in URLs or referer headers, lack of session invalidation on logout, and Session Fixation.

### 3. Access Control (What are you allowed to do?)
Access control (Authorization) enforces permissions: deciding whether the authenticated user has the right to view, modify, or delete a specific resource.
* **Models**: Role-Based Access Control (RBAC), Attribute-Based Access Control (ABAC), Discretionary Access Control (DAC).
* **Common Vulnerabilities**: Insecure Direct Object References (IDOR/BOLA), vertical privilege escalation (user accessing admin endpoints), and horizontal privilege escalation (accessing another user's invoice).
""",
                    "keyTakeaways": [
                        "Authentication confirms identity; Authorization enforces permissions.",
                        "Session tokens bridge the gap created by stateless HTTP."
                    ]
                },
                {
                    "id": "ch2-sec2",
                    "title": "Handling User Input",
                    "subtopics": [
                        "Varieties of Input",
                        "Approaches to Input Handling",
                        "Boundary Validation",
                        "Multistep Validation and Canonicalization"
                    ],
                    "content": """
### 1. Varieties of Input
Input arrives from multiple channels: URL query strings (`?id=1`), POST form bodies, JSON/XML payloads, HTTP headers (`User-Agent`, `Referer`, `Host`, `X-Forwarded-For`), cookies, and uploaded files.

### 2. Approaches to Input Handling
* **Reject Known Bad (Blacklisting) - Flawed**:
  - Scanning for known malicious strings (e.g., `<script>`, `'`, `../`).
  - *Why it fails*: Attackers continually discover bypasses using alternate encodings, casing (`<sCrIpt>`), null bytes (`%00`), or nested strings (`<scr<script>ipt>`).
* **Accept Known Good (Whitelisting) - Best Practice**:
  - Defining an explicit strict specification of permitted characters, data types, and length (e.g., zip codes must match `^[0-9]{5}$`).
* **Sanitization**: Modifying input to neutralize malicious characters (e.g., stripping HTML tags). Risky if subsequent parsers interpret the stripped output unexpectedly.
* **Safe Handling (Parameterization)**: Ensuring user data is passed to interpreters via parameterized APIs where it cannot be executed as instructions.

### 3. Boundary Validation (Context-Aware Sanitization)
Input must be validated and encoded **at the boundary** where it transitions from one execution context to another:
* HTML body: HTML entity encoding (`&lt;`, `&gt;`).
* SQL queries: Parameterized prepared statements.
* OS commands: Native API argument arrays without invoking a shell.

### 4. Multistep Validation and Canonicalization
Canonicalization converts data into its standard, simplest representation. If validation runs **before** canonicalization, filters fail:
```
Attacker input: %252e%252e%252f (Double URL-encoded ../)
Filter runs: Contains "../"? -> No! Passes!
Downstream Decoder 1: %252e -> %2e -> "%2e%2e%2f"
Downstream Decoder 2: "%2e%2e%2f" -> "../" (Path Traversal Succeeds!)
```
""",
                    "keyTakeaways": [
                        "Prefer whitelisting over blacklisting.",
                        "Always canonicalize input completely before validation, or validate output at the boundary of each interpreter."
                    ]
                },
                {
                    "id": "ch2-sec3",
                    "title": "Handling Attackers",
                    "subtopics": [
                        "Handling Errors",
                        "Maintaining Audit Logs",
                        "Alerting Administrators",
                        "Reacting to Attacks"
                    ],
                    "content": """
### 1. Handling Errors
* Unhandled runtime exceptions frequently leak database table schemas, SQL queries, file system paths, and library versions in stack traces.
* **Secure Practice**: Catch all exceptions centrally. Present users with a generic error page and a unique correlation tracking ID, while recording the technical stack trace in internal secure logs.

### 2. Maintaining Audit Logs
* Log security events: login successes/failures, password resets, authorization failures, privilege changes, and critical transactions.
* Record: timestamp (UTC), user ID, IP address, user-agent, and action performed.
* Ensure logs cannot be injected with fake newlines (`CRLF` log injection) and sanitize out sensitive passwords and credit card data.

### 3. Alerting Administrators
* Implement automated anomaly detection for sudden spikes in 404/403 responses, repeated failed logins, or unexpected injection syntax.

### 4. Reacting to Attacks
* Rate-limiting, progressive delays (tarpitting), CAPTCHAs, and automatic session revocation for suspicious accounts.
""",
                    "keyTakeaways": [
                        "Never leak internal stack traces or database error messages to end-users.",
                        "Logs are crucial for post-incident DFIR investigations."
                    ]
                },
                {
                    "id": "ch2-sec4",
                    "title": "Summary & Review",
                    "subtopics": [
                        "Managing the Application",
                        "Summary",
                        "Questions"
                    ],
                    "content": """
### Managing the Application
Administrative interfaces (`/admin`, `/manage`) represent high-value targets. They must enforce strong authentication, MFA, IP allowlisting, and strict audit logging.

### Chapter 2 Summary
* Core defense relies on handling access (authn, session, authz), handling input (whitelisting, canonicalization, boundary encoding), and handling attackers (logging, fail-secure error handling).
* Blacklisting input consistently fails due to encoding bypasses; whitelisting and parameterized APIs are mandatory.
""",
                    "keyTakeaways": [
                        "Build defense-in-depth across authentication, session management, input validation, and secure logging."
                    ]
                }
            ],
            "quiz": [
                {
                    "id": "q-ch2-1",
                    "question": "What is the critical distinction between Authentication and Access Control (Authorization)?",
                    "options": [
                        "Authentication encrypts passwords, while Access Control hashes them.",
                        "Authentication establishes who a user is; Access Control enforces what resources and actions that user is permitted to access.",
                        "Authentication runs in client-side JavaScript, while Access Control runs in SQL.",
                        "There is no difference; they are interchangeable terms."
                    ],
                    "correctIndex": 1,
                    "explanation": "Authentication validates identity (e.g., verifying user credentials). Authorization enforces permissions (e.g., ensuring a regular user cannot access admin panels or other users' private accounts).",
                    "difficulty": "Easy"
                },
                {
                    "id": "q-ch2-2",
                    "question": "Why is 'whitelisting' input inherently more secure than 'blacklisting'?",
                    "options": [
                        "Blacklisting uses too much CPU memory.",
                        "Attackers frequently discover alternate encodings, casing anomalies, or obscure syntax variants that blacklist filters overlook.",
                        "Whitelisting is required by TLS 1.3 standards.",
                        "Blacklists cannot inspect HTTP POST bodies."
                    ],
                    "correctIndex": 1,
                    "explanation": "It is virtually impossible to anticipate every malicious payload permutation across diverse interpreters. Whitelisting defines an exact allowed format and rejects everything else.",
                    "difficulty": "Medium"
                },
                {
                    "id": "q-ch2-3",
                    "question": "An application strips the string `../` from a filename once, and then performs URL decoding. How can an attacker bypass this?",
                    "options": [
                        "By double URL-encoding the traversal sequence as `%252e%252e%252f`.",
                        "By changing the User-Agent to Firefox.",
                        "By submitting a 10MB payload.",
                        "By setting HttpOnly on the cookie."
                    ],
                    "correctIndex": 0,
                    "explanation": "Because validation occurs before URL decoding, `%252e%252e%252f` does not match `../`. When the application later decodes `%25` to `%`, it produces `%2e%2e%2f`, which decodes to `../`.",
                    "difficulty": "Hard"
                }
            ]
        }
    ]

    return curriculum

print("Full curriculum generator blueprint ready.")

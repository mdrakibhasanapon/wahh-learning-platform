"""
Curriculum Builder for The Web Application Hacker's Handbook (2nd Edition) Learning Platform
Generates a comprehensive js/curriculum.js containing all 21 chapters, Intro, and Master Index.
Each chapter contains subsections, detailed notes, code/HTTP samples, attack scenarios, defenses,
and an interactive quiz section with multiple technical questions.
"""

import json
import os

modules = [
    {
        "id": "intro",
        "number": 0,
        "title": "Course Introduction & Overview",
        "subtitle": "Course Overview, Prerequisites & Roadmap",
        "icon": "compass",
        "category": "Orientation",
        "readingTime": "15 min",
        "overview": "Set up your mindset and methodology for web penetration testing based on The Web Application Hacker's Handbook (2nd Edition). Learn the evolution of web security and navigate the 21 handbook modules.",
        "sections": [
            {
                "id": "intro-overview",
                "title": "Course Overview & Prerequisites",
                "content": """
### Welcome to The Web Application Hacker's Handbook Interactive Platform

The Web Application Hacker's Handbook (WAHH) is the definitive bible of web application security testing. This interactive platform breaks down the entire 21-chapter methodology into structured modules, complete with technical deep-dives, cheat sheets, attack vectors, defensive controls, and interactive self-assessment quizzes for every single chapter.

#### Target Audience & Skill Level
* **Penetration Testers & Security Researchers**: Elevate your black-box and white-box web assessment skills to professional audit standards.
* **Web Developers & Software Engineers**: Understand how adversaries think, tamper with requests, and bypass superficial controls.
* **AppSec & DevSecOps Specialists**: Build robust defenses, implement architectural boundaries, and automate security checks.

#### Key Prerequisites
1. **HTTP/HTTPS Fundamentals**: Understanding stateless request/response pairs, verbs (GET, POST, PUT, DELETE, OPTIONS), status codes, and headers.
2. **Client-Side Technologies**: HTML5, DOM manipulation, JavaScript runtime, cookies, localStorage, and Same-Origin Policy (SOP).
3. **Server-Side & Databases**: Relational databases (SQL), NoSQL, backend frameworks (Node, PHP, Java, ASP.NET, Python), and API architectures.
4. **Tooling Mindset**: Working knowledge of an intercepting proxy (Burp Suite, OWASP ZAP) and browser developer tools.
""",
                "keyTakeaways": [
                    "Web apps present a unique threat model because the client is completely under the attacker's control.",
                    "Testing requires methodical mapping before jumping into automated fuzzing or exploitation.",
                    "Hands-on practice alongside structured theory is crucial to mastering input manipulation."
                ]
            },
            {
                "id": "intro-evolution",
                "title": "The Evolution of Web Application (In)security",
                "content": """
### The Changing Landscape of Web Security

In the early days of the Internet, websites were static collections of hyperlinked HTML documents. Security was primarily network-perimeter focused: firewalls, packet filters, and bastion hosts.

```
Traditional Perimeter Model:
[ Internet ] ---> [ Network Firewall ] ---> [ Hardened Web Server (Static Port 80) ]
                  (Blocks ports 21, 22, etc.)

Modern Web Application Model:
[ Internet ] ---> [ Firewall (Port 443 Open) ] ---> [ Complex App Tier ] ---> [ Internal Microservices ]
                                                     - Custom Auth             - Databases (SQL/NoSQL)
                                                     - Business Logic          - Message Queues / Cloud APIs
                                                     - Payment Gateways        - Legacy Enterprise Systems
```

#### Why Web Applications Shifted the Attack Surface
1. **The Tunneling Effect**: Firewalls must permit inbound HTTP/HTTPS (ports 80 & 443) for the business to operate. Any flaw in the application layer bypasses perimeter firewall rules entirely.
2. **Bespoke Codebases**: Unlike standardized network services (e.g., OpenSSH, BIND) maintained by dedicated security engineers, web apps are frequently custom-built by developers facing tight delivery deadlines.
3. **Proliferation of Connected Services**: Modern apps integrate third-party payment gateways, CRM APIs, single sign-on (SSO), cloud microservices, and internal databases, expanding the attack radius.
""",
                "keyTakeaways": [
                    "The perimeter is no longer the network layer; the web application itself is the new perimeter.",
                    "Every user-facing HTTP endpoint is an interface directly to backend business logic and databases."
                ]
            },
            {
                "id": "intro-approach",
                "title": "How to Approach Hands-On Web Penetration Testing",
                "content": """
### The Hacker's Mindset: Systematic Decomposition

A successful web penetration test is never random clicking. It follows a disciplined 4-stage loop:

1. **Reconnaissance & Surface Mapping**: Document all endpoints, parameters, technologies, headers, and authentication states.
2. **Analysis & Threat Modeling**: Determine where user data is parsed, how state is maintained, and which assumptions developers made.
3. **Hypothesis & Targeted Probing**: Devise specific edge-case tests (e.g., negative numbers, Unicode normalization, delimiter injection, state transitions).
4. **Exploitation & Impact Demonstration**: Chain vulnerabilities to demonstrate real business impact (e.g., IDOR to privilege escalation to data exfiltration).
""",
                "keyTakeaways": [
                    "Always map before you attack; unmapped parameters often harbor the most severe bugs.",
                    "Question every developer assumption: 'Will the client ever send negative prices? Will tokens ever be reused?'"
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-intro-1",
                "question": "Why did the rise of web applications invalidate traditional network perimeter security (like firewalls)?",
                "options": [
                    "Firewalls cannot inspect encrypted SSL/TLS traffic without a certificate.",
                    "Web applications require ports 80 and 443 to remain open to the public, allowing attacks to bypass network packet filters directly into bespoke code.",
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
            },
            {
                "id": "q-intro-3",
                "question": "What is the primary security flaw inherent in trusting client-side logic (e.g., JavaScript validation)?",
                "options": [
                    "JavaScript executes slower than compiled C code.",
                    "The client runtime is completely controlled by the user, who can modify DOM elements, bypass JS validation, or forge raw HTTP requests.",
                    "Web browsers do not support encryption.",
                    "JavaScript lacks regular expression support."
                ],
                "correctIndex": 1,
                "explanation": "Any client-side restriction can be trivialized by intercepting the HTTP request using a proxy or sending custom requests via curl or scripts.",
                "difficulty": "Easy"
            }
        ]
    },
    {
        "id": "ch1",
        "number": 1,
        "title": "Chapter 1: Web Application (In)security",
        "subtitle": "The Core Security Problem: Users Can Submit Arbitrary Input",
        "icon": "shield-alert",
        "category": "Fundamentals",
        "readingTime": "20 min",
        "overview": "Discover the fundamental root cause of almost all web vulnerabilities: users can submit arbitrary input. Understand the collapse of perimeter defense and why modern web security relies on application-level controls.",
        "sections": [
            {
                "id": "ch1-evolution",
                "title": "The Evolution & Functions of Web Applications",
                "content": """
### From Static Documents to Dynamic Web Applications

Web applications have evolved from simple brochure websites into complex distributed software running critical societal infrastructure:
* **E-Commerce & Financial Transactions**: Real-time payment processing, banking ledgers, and credit applications.
* **Corporate Portals & SaaS**: CRM, ERP, HR systems handling proprietary intellectual property and confidential personnel records.
* **Critical Infrastructure & Healthcare**: Medical records (HIPAA/GDPR), IoT control panels, and cloud resource management.

#### Benefits & Business Drivers
* **Ubiquitous Client**: Zero client-side installation—anyone with a browser on any OS can access the service.
* **Instant Deployment**: Updates are deployed centrally to the server without distributing patches to thousands of end-users.
* **Cross-Platform Compatibility**: Standardization on web protocols ensures broad reach across mobile, desktop, and embedded devices.
""",
                "keyTakeaways": [
                    "The immense business value of web apps has concentrated valuable data and functionality on the web tier.",
                    "Centralization means a single web flaw can compromise all users simultaneously."
                ]
            },
            {
                "id": "ch1-core-problem",
                "title": "The Core Security Problem: Arbitrary Input",
                "content": """
### The Fundamental Axiom of Web Security

> **"All user input is untrusted and can be arbitrarily manipulated."**

A web application cannot constrain the client environment. While developers write HTML forms with `maxlength="10"` or `<select>` dropdowns with pre-set options, the client can use an intercepting proxy to forge **any arbitrary byte stream** in any header, cookie, query string, or request body.

```http
POST /checkout HTTP/1.1
Host: shop.example.com
Content-Type: application/x-www-form-urlencoded

item_id=9812&quantity=1&price_override=-50.00&discount_code=ADMIN%27+OR+%271%27=%271
```

#### Key Problem Factors
1. **Underdeveloped Security Mindset**: Developers are trained to implement functional features under strict deadlines rather than defensive boundaries.
2. **Framework Deceptions**: Modern high-level frameworks abstract away raw HTTP, leading developers to assume request values are already sanitized or trustworthy.
3. **Complex Multi-Tier Architecture**: Input passes through reverse proxies, web application firewalls (WAFs), API gateways, application runtimes, database drivers, and template engines—each parsing data differently.
4. **Rapidly Evolving Technologies**: Single Page Applications (SPAs), GraphQL, WebSockets, and microservices introduce new attack surfaces faster than security controls mature.
""",
                "keyTakeaways": [
                    "Never rely on client-side constraints for security enforcement.",
                    "The core vulnerability is treating user-supplied data as instructions rather than inert data."
                ]
            },
            {
                "id": "ch1-perimeter",
                "title": "The New Security Perimeter & The Future",
                "content": """
### The Demise of 'This Site Is Secure'

The padlock icon in the browser address bar only indicates **channel encryption (HTTPS/TLS)**—it proves that communication between the browser and server is encrypted against eavesdroppers on the local Wi-Fi. It says **nothing** about the security of the application code itself!

```
[ TLS / SSL Encryption Layer ] = Secures Data In Transit (Prevents MITM)
         |
         v
[ Web Application Logic ]     = Vulnerable to SQLi, IDOR, Logic Flaws, Auth Bypass
```

An attacker can easily send an SQL injection payload inside a valid, TLS-encrypted HTTPS POST request. HTTPS faithfully encrypts the malicious attack string and delivers it securely to the vulnerable database parser!

#### The Future of Web Security
* Shifting security left: Static Application Security Testing (SAST), Dynamic Testing (DAST), and Software Composition Analysis (SCA).
* Zero Trust Architectures: Explicit verification at every boundary; mutual TLS (mTLS) between internal microservices.
* Robust content boundaries: Content Security Policy (CSP), subresource integrity, and type-safe parameterized query APIs.
""",
                "keyTakeaways": [
                    "HTTPS secures data in transit; it does not protect the application from malicious input.",
                    "Security must be built into application logic, session management, and data access layers."
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
            },
            {
                "id": "q-ch1-3",
                "question": "If an HTML form uses `<input type='number' min='1' max='5' name='qty'>`, how can an attacker submit `qty=-99`?",
                "options": [
                    "By executing a buffer overflow against the browser kernel.",
                    "By intercepting the outgoing HTTP request using a web proxy (like Burp Suite) and editing the parameter value before forwarding.",
                    "It is impossible because modern browsers forbid modifying HTML attributes.",
                    "By cracking the web server's TLS private key."
                ],
                "correctIndex": 1,
                "explanation": "Web proxies intercept outgoing HTTP traffic between the browser and server, allowing the penetration tester to freely change parameters, headers, and request bodies regardless of HTML validation.",
                "difficulty": "Medium"
            }
        ]
    },
    {
        "id": "ch2",
        "number": 2,
        "title": "Chapter 2: Core Defense Mechanisms",
        "subtitle": "Handling User Access, Input Validation & Attack Mitigation",
        "icon": "lock",
        "category": "Fundamentals",
        "readingTime": "25 min",
        "overview": "Examine the fundamental defensive pillars required by every secure web application: handling user access (authn, authz, sessions), input handling (boundary validation, canonicalization), and handling attackers (audit logging, fail-secure error handling).",
        "sections": [
            {
                "id": "ch2-user-access",
                "title": "Handling User Access: The Trinity of Security",
                "content": """
### The Access Control Triad

Managing user access requires three interrelated but distinct mechanisms working in lockstep:

```
[ Unauthenticated Request ]
          |
          v
1. Authentication (Who are you?)
   - Passwords, MFA tokens, Biometrics, Certificates
          |
          v
2. Session Management (How do we remember you across stateless HTTP?)
   - Cryptographically random session tokens / JWTs
          |
          v
3. Access Control / Authorization (What are you permitted to do?)
   - Role-Based (RBAC), Attribute-Based (ABAC), Resource ownership checks
```

#### Common Failures in the Access Chain
* **Authentication Flaws**: Weak password policies, vulnerable password resets, lack of brute-force throttling, verbose login errors that leak username existence.
* **Session Management Flaws**: Predictable session tokens (e.g., sequential integers, timestamps), token exposure in URLs or logs, lack of session invalidation on logout.
* **Access Control Flaws (IDOR)**: Verifying that a user is logged in, but failing to check whether user A is authorized to view or edit user B's account (`GET /invoice?id=1002`).
""",
                "keyTakeaways": [
                    "Authentication verifies identity; Authorization verifies permissions.",
                    "Stateless HTTP requires session tokens to bridge authentication to ongoing authorization."
                ]
            },
            {
                "id": "ch2-input-handling",
                "title": "Handling User Input: Validation & Canonicalization",
                "content": """
### Input Validation Paradigms

Applications receive input from numerous sources: URL query strings, POST bodies, headers (User-Agent, Referer, Cookie), and uploaded files.

#### 1. Reject Known Bad (Blacklisting) - Flawed
* Attempts to detect malicious characters (e.g., `'`, `<`, `script`, `../`).
* **Why it fails**: Attackers find endless bypasses using alternative encodings, casing (`<sCrIpt>`), nested tags (`<scr<script>ipt>`), null bytes, or alternative SQL comment syntax (`--`, `/* */`, `#`).

#### 2. Accept Known Good (Whitelisting) - Best Practice
* Defines an explicit regular expression or character set of permitted characters (e.g., an age field must match `^[0-9]{1,3}$`).
* Rejects or strictly filters anything that does not conform.

#### 3. Boundary Validation (Context-Aware Sanitization)
* Data should be validated and encoded **at the boundary** where it transitions from one interpreter to another (e.g., parameterizing SQL queries before DB execution; HTML-entity encoding before reflecting into the DOM).

#### Canonicalization & Multistep Validation Pitfall
Canonicalization is the process of converting data into a standard, canonical representation. If validation runs **before** canonicalization, attackers bypass filters:

```
Attacker input: %252e%252e%252f (Double URL-encoded ../)
Filter checks: Does input contain "../"? -> No! (Contains "%252e%252e%252f")
Application decodes: %25 -> % -> "%2e%2e%2f"
Application decodes again: "%2e%2e%2f" -> "../" (Path Traversal Executed!)
```
""",
                "keyTakeaways": [
                    "Always prefer whitelisting over blacklisting.",
                    "Always decode/canonicalize input FIRST before applying validation rules, or validate after all transforms are complete.",
                    "Use parameterized interfaces (prepared statements) rather than ad-hoc input scrubbing."
                ]
            },
            {
                "id": "ch2-attackers",
                "title": "Handling Attackers: Logging, Errors & Resilience",
                "content": """
### Managing the Adversary

A mature application anticipates attacks and reacts defensibly:

1. **Handling Errors Gracefully**:
   * Never leak technical stack traces, database schema details, or library versions in HTTP responses.
   * Return generic, user-friendly error pages while writing detailed diagnostic traces to internal server logs.
2. **Audit Logging & Forensics**:
   * Log critical security events: failed logins, password changes, privilege elevations, and access control denials.
   * Protect log integrity: ensure logs cannot be tampered with or injected with fake CRLF newlines (Log Injection).
3. **Alerting & Rate Limiting**:
   * Detect automated scanning anomalies (e.g., 50 404s per minute from a single IP or session).
   * Implement progressive delays, CAPTCHAs, or temporary IP/account lockouts to defeat brute-force automation.
""",
                "keyTakeaways": [
                    "Verbose error messages provide reconnaissance intelligence to attackers.",
                    "Logs must record who did what, when, and from what IP without logging sensitive credentials."
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch2-1",
                "question": "What is the critical distinction between Authentication and Access Control (Authorization)?",
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
                "question": "Why is 'blacklisting' (rejecting known bad input) considered inherently inferior to 'whitelisting' (accepting known good)?",
                "options": [
                    "Blacklisting requires too much server CPU power.",
                    "Attackers can frequently bypass blacklists using alternate encodings, obscure syntax variations, or null bytes that the filter author forgot to include.",
                    "Whitelisting is forbidden by modern web browser standards.",
                    "Blacklisting only works on GET requests, not POST requests."
                ],
                "correctIndex": 1,
                "explanation": "It is nearly impossible to enumerate all malicious input permutations across diverse backend interpreters. Whitelisting specifies an exact strict format, rejecting everything else.",
                "difficulty": "Medium"
            },
            {
                "id": "q-ch2-3",
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
    },
    {
        "id": "ch3",
        "number": 3,
        "title": "Chapter 3: Web Application Technologies",
        "subtitle": "HTTP Protocol, Encoding Schemes & Server Runtimes",
        "icon": "network",
        "category": "Fundamentals",
        "readingTime": "30 min",
        "overview": "Deep dive into HTTP/1.1 and HTTP/2 mechanics, request/response headers, status codes, cookies, proxy architectures, and data encodings (URL, Base64, Hex, HTML, Unicode).",
        "sections": [
            {
                "id": "ch3-http",
                "title": "The HTTP Protocol: Requests, Responses & Headers",
                "content": """
### Anatomy of an HTTP Transaction

HTTP is a plaintext, stateless, client-server protocol. Understanding raw HTTP byte streams is the foundation of penetration testing.

#### Anatomy of an HTTP Request
```http
POST /api/v1/transfer HTTP/1.1
Host: bank.example.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64)
Authorization: Bearer eyJhbGciOi...
Content-Type: application/json
Content-Length: 48
Cookie: session_id=s8df01n4kl9a023k; secure_flag=true

{"recipient": "attacker", "amount": 1000.00}
```

* **Request Line**: Verb (`POST`), Path (`/api/v1/transfer`), Protocol Version (`HTTP/1.1`).
* **Headers**: Key-value pairs providing metadata (`Host`, `User-Agent`, `Cookie`).
* **Empty Line (`\\r\\n`)**: Crucial delimiter marking the end of headers.
* **Message Body**: Arbitrary payload (JSON, form-urlencoded, XML, binary).

#### Critical HTTP Headers for Security
* `Host`: Specifies target domain; vulnerable to Host Header Injection and SSRF if used to build absolute URLs or cache keys.
* `Cookie` / `Set-Cookie`: Transmits session identifiers; flags include `HttpOnly` (blocks JS access), `Secure` (HTTPS only), and `SameSite` (`Strict`, `Lax`, `None`).
* `Content-Security-Policy (CSP)`: Restricts origins from which scripts, styles, and frames can load.
* `X-Frame-Options`: Prevents UI redressing / Clickjacking (`DENY` or `SAMEORIGIN`).
""",
                "keyTakeaways": [
                    "The Host header is attacker-controlled and cannot be trusted blindly for redirects or password reset links.",
                    "Cookies require HttpOnly, Secure, and SameSite attributes for basic protection."
                ]
            },
            {
                "id": "ch3-encoding",
                "title": "Encoding Schemes: URL, Unicode, HTML, Base64 & Hex",
                "content": """
### Navigating Multi-Layered Encodings

Web architectures use diverse encodings. Attackers exploit differences in how proxies, firewalls, and backend parsers decode these formats:

#### 1. URL Encoding (Percent-Encoding)
* Replaces non-alphanumeric bytes with `%HH` where `HH` is hexadecimal ASCII.
* Example: Space = `%20`, `'` = `%27`, `<` = `%3C`, `&` = `%26`.

#### 2. HTML Entity Encoding
* Used inside HTML documents: Named entities (`&lt;`, `&quot;`) or Decimal/Hex (`&#60;`, `&#x3C;`).
* Browsers decode HTML entities inside HTML attributes and tags, but NOT inside `<script>` blocks!

#### 3. Base64 Encoding
* Represents binary data using 64 ASCII characters (`A-Z`, `a-z`, `0-9`, `+`, `/`) with `=` padding.
* Frequently mistaken by junior developers for encryption—Base64 is strictly an encoding and provides zero confidentiality!

#### 4. Unicode & Normalization (UTF-8, UTF-16, Overlong UTF-8)
* Unicode characters with visual equivalence (e.g., `＜` U+FF1C vs `<` U+003C) can cause filter bypasses when normalized downstream.
""",
                "keyTakeaways": [
                    "Encoding is NOT encryption. Base64 can be decoded instantly without a key.",
                    "Always determine which layer of the application decodes which encoding and in what order."
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch3-1",
                "question": "What cookie attribute prevents client-side JavaScript (e.g. from an XSS vulnerability) from reading document.cookie?",
                "options": [
                    "SameSite=Strict",
                    "Secure",
                    "HttpOnly",
                    "Domain=.example.com"
                ],
                "correctIndex": 2,
                "explanation": "The HttpOnly flag directs the browser that the cookie should not be accessible via client-side scripts such as document.cookie, mitigating session hijacking via XSS.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch3-2",
                "question": "What is the URL-encoded equivalent of the single quote character (') and double quote (\") respectively?",
                "options": [
                    "%20 and %25",
                    "%27 and %22",
                    "%3C and %3E",
                    "%0A and %0D"
                ],
                "correctIndex": 1,
                "explanation": "In ASCII hexadecimal representation, the single quote (') has hex value 0x27 (%27) and the double quote (\") has hex value 0x22 (%22).",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch3-3",
                "question": "Why is Base64 representation of a sensitive token NOT considered secure storage or transmission?",
                "options": [
                    "Base64 characters cannot be sent over HTTPS.",
                    "Base64 is a reversible encoding scheme with no secret key, meaning anyone can instantly decode the original plaintext.",
                    "Base64 alters the hash checksum of the original data.",
                    "Base64 only works on Windows operating systems."
                ],
                "correctIndex": 1,
                "explanation": "Base64 is simply a public encoding algorithm designed for data transport across binary-safe mediums. It offers zero cryptographic protection or confidentiality.",
                "difficulty": "Easy"
            }
        ]
    },
    {
        "id": "ch4",
        "number": 4,
        "title": "Chapter 4: Mapping the Application",
        "subtitle": "Enumerating Content, Spidering & Attack Surface Discovery",
        "icon": "map",
        "category": "Reconnaissance",
        "readingTime": "25 min",
        "overview": "Master the art of mapping a web application's visible and hidden attack surface. Learn automated spidering, user-directed spidering, directory brute-forcing, parameter discovery, and server-side technology profiling.",
        "sections": [
            {
                "id": "ch4-spidering",
                "title": "Enumerating Content: Spidering & Hidden Discovery",
                "content": """
### Mapping Visible vs. Hidden Functionality

Mapping forms the foundation of all subsequent testing. Missing a single administrative endpoint or forgotten backup file can mean missing a critical vulnerability.

#### Automated Spidering vs. User-Directed Spidering
* **Automated Spidering**: Crawlers parse HTML tags (`<a href>`, `<form action>`, `<img src>`) and follow links recursively.
  * *Limitation*: Fails against complex JavaScript SPAs, multi-step wizards, authentication logouts, and destructive actions (e.g., automated crawlers clicking 'Delete Account').
* **User-Directed Spidering (Golden Standard)**: The penetration tester browses the entire application manually with an intercepting proxy logging all requests, ensuring all dynamic user paths and authenticated flows are captured.

#### Discovering Hidden Content & Dark Paths
1. **Directory & File Brute Forcing**: Using wordlists (`SecLists`, `dirsearch`, `gobuster`, `ffuf`) to uncover unlinked files:
   * Backup files: `config.php.bak`, `index.php~`, `database.sql`, `.env`, `.git/`
   * Admin panels: `/admin`, `/manage`, `/console`, `/actuator/health`
2. **Robots.txt & Sitemap.xml**: Frequently list sensitive directories explicitly intended to be hidden from search engines!
3. **Client-Side Source Code Inspection**: Scanning JavaScript bundles (Webpack chunks, sourcemaps) for API endpoints, internal staging URLs, and hardcoded secrets.
""",
                "keyTakeaways": [
                    "Automated spiders alone are insufficient for modern interactive applications.",
                    "Always check robots.txt, sitemap.xml, and client-side JavaScript source maps for hidden routes."
                ]
            },
            {
                "id": "ch4-surface",
                "title": "Analyzing Application & Mapping Attack Surface",
                "content": """
### Profiling Technologies & Entry Points

Once content is discovered, the penetration tester analyzes the target to construct a precise mental model:

#### 1. Identifying Server-Side Technologies
* **HTTP Response Headers**: `Server`, `X-Powered-By`, `X-AspNet-Version`.
* **Cookie Formats**: `PHPSESSID` (PHP), `JSESSIONID` (Java/Tomcat), `ASP.NET_SessionId` (Microsoft), `connect.sid` (Node/Express).
* **URL Structures & Extensions**: RESTful paths, `.jsp`, `.do` (Struts), `.aspx` (ASP.NET), `.action`.
* **Error Signatures**: Custom 404 pages or unhandled exception traces revealing underlying framework versions.

#### 2. Documenting Entry Points for Input
Every parameter that accepts user data is an entry point:
* URL parameters (Query string: `?id=10&page=2`)
* POST body parameters (Form, JSON, XML)
* HTTP request headers (`User-Agent`, `Referer`, `Origin`, `Host`, custom headers)
* REST path parameters (`/api/users/{id}/orders`)
* Cookie values
""",
                "keyTakeaways": [
                    "Map out every single parameter across all requests before testing attacks.",
                    "Fingerprint server technologies to select relevant exploit payloads."
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch4-1",
                "question": "Why is 'user-directed spidering' typically superior to purely automated crawling when mapping a modern web application?",
                "options": [
                    "Automated crawlers cannot handle HTTPS encryption.",
                    "Automated crawlers may trigger destructive operations (like deleting accounts), get trapped in recursive loops, or miss JavaScript-driven workflows that require human interaction.",
                    "User-directed spidering does not require a web proxy.",
                    "Automated crawlers are illegal in all jurisdictions."
                ],
                "correctIndex": 1,
                "explanation": "Automated crawlers lack context: they might submit forms that delete data, log the session out prematurely, or fail to render client-side JavaScript Single Page Applications (SPAs).",
                "difficulty": "Medium"
            },
            {
                "id": "q-ch4-2",
                "question": "A web application sets the cookie `JSESSIONID=A1B2C3D4...`. What backend application technology is most likely running?",
                "options": [
                    "PHP",
                    "Java (e.g., Apache Tomcat, WildFly, Spring)",
                    "Ruby on Rails",
                    "Node.js Express"
                ],
                "correctIndex": 1,
                "explanation": "JSESSIONID is the standard default session cookie name generated by Java Servlet containers such as Apache Tomcat, Jetty, and JBoss/WildFly.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch4-3",
                "question": "During directory brute-forcing, an endpoint returns HTTP 403 Forbidden. What should a penetration tester conclude?",
                "options": [
                    "The resource does not exist on the server.",
                    "The resource exists, but access is restricted; this endpoint should be cataloged and probed for authorization bypasses.",
                    "The web server has crashed.",
                    "The penetration test is over."
                ],
                "correctIndex": 1,
                "explanation": "HTTP 403 confirms the resource exists on the server. Attackers target 403 endpoints with path manipulation, header tampering (X-Forwarded-For, X-Original-URL), or alternate HTTP verbs.",
                "difficulty": "Medium"
            }
        ]
    },
    {
        "id": "ch5",
        "number": 5,
        "title": "Chapter 5: Bypassing Client-Side Controls",
        "subtitle": "Manipulating Hidden Fields, Cookies, ViewState & Form Validation",
        "icon": "unlock",
        "category": "Client-Side Controls",
        "readingTime": "25 min",
        "overview": "Learn how developers erroneously rely on client-side controls (HTML form limits, hidden fields, disabled buttons, JavaScript validation, ASP.NET ViewState) and how intercepting proxies bypass them effortlessly.",
        "sections": [
            {
                "id": "ch5-transmission",
                "title": "Transmitting Data Via the Client: The Fatal Mistake",
                "content": """
### Why Storing Critical State on the Client Fails

Many applications transmit sensitive application data to the client, expecting the browser to send it back unmodified in subsequent requests.

#### 1. Hidden Form Fields
```html
<!-- Vulnerable Checkout Form -->
<form action="/process_order" method="POST">
  <input type="hidden" name="item_id" value="1054">
  <input type="hidden" name="price" value="499.00">
  <input type="text" name="quantity" value="1">
  <button type="submit">Buy Now</button>
</form>
```
* **Attack**: The attacker uses Burp Suite or browser DevTools to change `price=499.00` to `price=0.01` before submission. If the server trusts this parameter without re-querying the database price, fraud succeeds!

#### 2. Tampering with Cookies & URL Parameters
* Storing user roles in cookies (`role=user; is_admin=false`) or query strings (`?discount=0`).
* If not cryptographically signed (HMAC) or stored in an encrypted server-side session, users can alter their permissions at will.

#### 3. ASP.NET ViewState
* ASP.NET serializes page state into a Base64-encoded string (`__VIEWSTATE`).
* If `EnableViewStateMac` is disabled or ViewState encryption is omitted, attackers can decode the state, modify values, and potentially achieve Remote Code Execution (RCE) via insecure deserialization!
""",
                "keyTakeaways": [
                    "Never rely on hidden fields for prices, privileges, or business logic states.",
                    "Store authoritative data in server-side session stores or use cryptographically signed tamper-proof tokens."
                ]
            },
            {
                "id": "ch5-form-validation",
                "title": "Bypassing Form Controls: Length, Scripts & Extensions",
                "content": """
### Evading Client-Side Validation

Web forms frequently enforce restrictions using browser-side mechanisms:

1. **HTML Length Limits (`maxlength="20"`)**:
   * Easily removed by editing the HTML attribute in browser Inspector or submitting a 1,000-character payload via curl or Burp Repeater.
2. **JavaScript Regex Validation**:
   * Forms executing `onsubmit="return validateEmail()"`: The client validation can be disabled entirely in browser settings or simply bypassed by sending the POST request directly from a proxy.
3. **Disabled Form Elements (`disabled`)**:
   * Browsers do not submit `disabled` fields. Attackers remove the `disabled` attribute or manually inject the parameter into the raw HTTP body.
4. **Thick Clients & Browser Extensions**:
   * Flash, Silverlight, Java Applets, or mobile applications communicating via HTTP/WebSocket.
   * Can be decompiled (`jadx`, `ghidra`, `dnSpy`) to extract API endpoints, algorithms, and cryptographic keys.
""",
                "keyTakeaways": [
                    "Client-side validation improves user experience, but provides ZERO security.",
                    "Every validation rule implemented on the client MUST be duplicated on the server."
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch5-1",
                "question": "An e-commerce website sends `<input type='hidden' name='price' value='199.99'>` in the checkout form. How should this application be fixed?",
                "options": [
                    "Encode the price using Base64 so the user cannot read it.",
                    "Set `readonly='true'` on the input element.",
                    "Store product prices exclusively in the backend database and look up the authoritative price using the item ID upon checkout.",
                    "Validate the price on the client side using JavaScript."
                ],
                "correctIndex": 2,
                "explanation": "Never trust financial or privilege data submitted by the client. The server must retrieve the actual product price directly from its own trusted database.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch5-2",
                "question": "What is the primary risk of an ASP.NET application having `EnableViewStateMac` set to false?",
                "options": [
                    "The application will not render on mobile devices.",
                    "Attackers can tamper with the ViewState content without detection, potentially enabling parameter tampering and deserialization attacks.",
                    "Passwords will be saved in plaintext on the user's hard drive.",
                    "The web server will reject all HTTPS connections."
                ],
                "correctIndex": 1,
                "explanation": "The Message Authentication Code (MAC) verifies that ViewState has not been tampered with. Without MAC validation, an attacker can modify state values or craft malicious serialized payloads.",
                "difficulty": "Hard"
            },
            {
                "id": "q-ch5-3",
                "question": "Why is client-side JavaScript form validation considered a usability feature rather than a security control?",
                "options": [
                    "JavaScript is an outdated programming language.",
                    "Users can bypass client-side JavaScript validation simply by modifying the script, disabling JS, or submitting raw HTTP requests via a proxy.",
                    "Browsers refuse to execute regular expressions.",
                    "JavaScript validation can only run on Windows machines."
                ],
                "correctIndex": 1,
                "explanation": "Because the browser and network requests are under complete user control, any client-side JavaScript check can be bypassed effortlessly by intercepting the HTTP request.",
                "difficulty": "Easy"
            }
        ]
    },
    {
        "id": "ch6",
        "number": 6,
        "title": "Chapter 6: Attacking Authentication",
        "subtitle": "Brute Force, Credential Stuffing & Password Reset Vulnerabilities",
        "icon": "key",
        "category": "Authentication & Sessions",
        "readingTime": "30 min",
        "overview": "Analyze design and implementation flaws in web authentication: username enumeration, brute-force vulnerabilities, verbose failure messages, insecure password reset flows, remember-me tokens, and credential storage.",
        "sections": [
            {
                "id": "ch6-design-flaws",
                "title": "Design Flaws: Enumeration, Brute Force & Verbose Errors",
                "content": """
### Common Authentication Design Weaknesses

Authentication is the front door of any web application. Minor logical oversights allow attackers to breach accounts wholesale.

#### 1. Username Enumeration
When an application behaves differently depending on whether an entered username exists:
* **Message Differences**: 'Invalid password' vs. 'User does not exist'.
* **HTTP Status Code Differences**: 200 OK vs. 404 Not Found.
* **Timing Attacks**: The application spends 300ms hashing a password with bcrypt for valid users, but returns instantly (10ms) when the username is not found!
* *Remediation*: Return uniform error messages: 'Invalid username or password' and use constant-time dummy hashing for nonexistent users.

#### 2. Brute-Force & Credential Stuffing Vulnerabilities
* Lack of rate limiting on login endpoints.
* Failure to protect secondary login endpoints (e.g., mobile API `/api/v1/login`, SSO endpoints, SOAP services).
* Bypassing rate limits using IP rotation, `X-Forwarded-For` spoofing, or submitting requests concurrently via race conditions.

#### 3. Password Reset & Recovery Flaws
* Predictable password reset tokens (e.g., MD5 of timestamp or user email).
* Token leakage via `Referer` headers when the reset page links to external third-party assets (analytics, CDNs).
* Host Header Poisoning: Modifying `Host: attacker.com` during password reset request causes the server to generate `https://attacker.com/reset?token=xyz` in the user's email!
""",
                "keyTakeaways": [
                    "Always use generic authentication failure responses with constant-time execution.",
                    "Protect all login entry points (including APIs) with robust rate-limiting and MFA."
                ]
            },
            {
                "id": "ch6-implementation",
                "title": "Implementation Flaws: Storage & Multi-Stage Logins",
                "content": """
### Storage, Fail-Open Logins & Multi-Stage Flaws

Even well-designed authentication workflows can fail due to coding bugs:

#### 1. Insecure Credential Storage
* Plaintext storage or outdated hashing algorithms (MD5, SHA-1, unsalted SHA-256).
* Fast hashes are vulnerable to offline GPU cracking (billions of hashes/sec with Hashcat).
* *Secure Standard*: Adaptive slow hashing algorithms: **Argon2id**, **bcrypt**, or **PBKDF2** with individual cryptographic salts and appropriate work factors.

#### 2. Fail-Open Authentication Bugs
```php
// Vulnerable PHP comparison
if ($user_input == $stored_password_hash) { ... }
// If $stored_password_hash is null/empty due to DB error, or type juggling triggers:
// "0e1234..." == "0e9999..." evaluates to true!
```

#### 3. Flaws in Multi-Stage Logins (2FA / MFA Bypasses)
* Step 1: User enters username and password. Server sets session cookie `logged_in=partial`.
* Step 2: User is redirected to `/verify_mfa`.
* *Vulnerability*: The user navigates directly to `/dashboard` without completing Step 2, and the server fails to verify that MFA verification was completed!
""",
                "keyTakeaways": [
                    "Always use constant-time string comparisons (`hash_equals`) and modern key derivation functions (Argon2id/bcrypt).",
                    "Multi-stage logins must enforce state machines where access is denied until all stages are validated."
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch6-1",
                "question": "Which response message from a login endpoint leaks username existence and enables account enumeration?",
                "options": [
                    "'Invalid username or password'",
                    "'Authentication failed. Please check your credentials.'",
                    "'Incorrect password for user admin@example.com'",
                    "'System temporarily unavailable'"
                ],
                "correctIndex": 2,
                "explanation": "Telling the user that the password is incorrect explicitly confirms that the username exists in the database, allowing an attacker to compile a list of valid target accounts.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch6-2",
                "question": "How does Host Header Poisoning compromise a password reset workflow?",
                "options": [
                    "It causes the web server to run a buffer overflow.",
                    "If the application uses the Host header to build the reset link, an attacker modifies the Host header to their own server, receiving the secret reset token when the victim clicks the link.",
                    "It decrypts the user's password in transit.",
                    "It disables HTTPS encryption on the reset page."
                ],
                "correctIndex": 1,
                "explanation": "If the backend constructs the reset URL like `https://` + `request.headers['Host']` + `/reset?token=...`, an attacker can trigger a reset with `Host: evil.com`, causing the victim to receive a link to the attacker's server with their token.",
                "difficulty": "Hard"
            },
            {
                "id": "q-ch6-3",
                "question": "Why is SHA-256 without a work factor considered inadequate for storing user passwords?",
                "options": [
                    "SHA-256 has been mathematically broken and has collisions.",
                    "SHA-256 is designed to be blazingly fast; modern GPUs can compute billions of SHA-256 hashes per second, making offline brute-force and rainbow table attacks extremely cheap.",
                    "SHA-256 only runs on 32-bit CPU architectures.",
                    "SHA-256 hashes cannot be stored in SQL databases."
                ],
                "correctIndex": 1,
                "explanation": "Cryptographic hash functions like SHA-256 are engineered for speed, which aids attackers cracking passwords. Password storage requires slow, memory-hard algorithms like Argon2id or bcrypt.",
                "difficulty": "Medium"
            }
        ]
    },
    {
        "id": "ch7",
        "number": 7,
        "title": "Chapter 7: Attacking Session Management",
        "subtitle": "Token Predictability, Session Fixation & Hijacking",
        "icon": "fingerprint",
        "category": "Authentication & Sessions",
        "readingTime": "25 min",
        "overview": "Explore how stateless HTTP maintains user state via tokens. Uncover vulnerabilities in token generation (predictability, PRNG flaws), transmission (logs, referer, URLs), termination, and Session Fixation.",
        "sections": [
            {
                "id": "ch7-generation",
                "title": "Weaknesses in Token Generation: Predictability & Cryptography",
                "content": """
### Anatomy of Session Tokens

Because HTTP is stateless, the server issues a session token upon successful authentication. This token is the keys to the kingdom: anyone holding the token assumes the identity of that user.

#### Requirements for Secure Tokens
1. **Cryptographic Randomness**: Generated by a Cryptographically Secure Pseudo-Random Number Generator (CSPRNG, e.g., `/dev/urandom`, `crypto.randomBytes()`).
2. **High Entropy**: At least 128 bits of entropy (e.g., 32 hexadecimal or 24 Base64 characters) to render brute force computationally infeasible.
3. **No Embedded Meaning**: Never construct tokens using predictable formulas:
   * Flawed formula: `MD5(username + timestamp)`
   * Flawed formula: `base64(user_id:role:counter)`

#### Analysis with Burp Sequencer
* Security testers collect thousands of consecutive session tokens and run statistical randomness tests:
  * FIPS 140-2 statistical tests
  * Shannon Entropy analysis
  * Bit-level character distribution checks
""",
                "keyTakeaways": [
                    "Session tokens must be opaque, cryptographically random, and have at least 128 bits of entropy.",
                    "Never embed user data or timestamps without cryptographic signing (e.g., HMAC-SHA256 in JWT)."
                ]
            },
            {
                "id": "ch7-handling",
                "title": "Weaknesses in Token Handling: Fixation & Lifecycle",
                "content": """
### Session Fixation & Lifecycle Flaws

Even cryptographically unguessable tokens can be exploited if handled insecurely:

#### 1. Session Fixation Attack
```
Attacker                      Victim                     Web Server
   |                            |                            |
   |--- 1. Get new token X ---->|                            |
   |                            |                            |
   |--- 2. Trap victim with X ->|                            |
   |    (e.g., ?session_id=X)   |                            |
   |                            |--- 3. Log in with X ------>|
   |                            |                            | (Server validates user,
   |                            |                            |  keeps SAME token X!)
   |                            |                            |
   |--- 4. Attacker uses X --------------------------------->| (Attacker logged in as Victim!)
```
* *Vulnerability*: The server fails to issue a **new session token** upon successful login, continuing to use the pre-authentication token.
* *Fix*: Always regenerate the session token immediately upon any privilege change or login (`session_regenerate_id(true)`).

#### 2. Session Termination Weaknesses
* Closing the browser tab does NOT invalidate the session on the server.
* Defective logout: Deleting the cookie in the client browser, but leaving the session active in the server database/Redis cache.
* Missing idle timeouts and absolute expiration limits.
""",
                "keyTakeaways": [
                    "Always regenerate the session identifier upon successful login to defeat Session Fixation.",
                    "Ensure logout explicitly destroys the session record in server-side storage."
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch7-1",
                "question": "What happens during a Session Fixation attack?",
                "options": [
                    "The attacker guesses the victim's password by brute force.",
                    "The attacker supplies a known session token to the victim; when the victim logs in, the server retains that same token, allowing the attacker to access the authenticated session.",
                    "The attacker floods the server with 100,000 session tokens to cause a crash.",
                    "The attacker decrypts the server's SSL certificate."
                ],
                "correctIndex": 1,
                "explanation": "Session Fixation occurs when an application accepts a session token provided before login and fails to issue a new, unique token upon authentication.",
                "difficulty": "Medium"
            },
            {
                "id": "q-ch7-2",
                "question": "What is the industry-standard minimum entropy recommended for session identifiers to prevent guessing attacks?",
                "options": [
                    "16 bits",
                    "32 bits",
                    "64 bits",
                    "128 bits"
                ],
                "correctIndex": 3,
                "explanation": "A minimum of 128 bits of cryptographic entropy (e.g. 16 raw random bytes or 32 hexadecimal characters) ensures that brute-forcing tokens across the internet is mathematically impossible.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch7-3",
                "question": "Why should session tokens never be transmitted within URL query parameters (e.g., `?sessionid=xyz`)?",
                "options": [
                    "URL parameters cannot be read by web browsers.",
                    "Tokens in URLs leak through browser history, proxy server logs, web server access logs, and HTTP Referer headers to external websites.",
                    "URL parameters are limited to 5 characters.",
                    "HTTPS cannot encrypt URL query parameters."
                ],
                "correctIndex": 1,
                "explanation": "URLs are logged in server access logs, browser history, bookmarks, and sent via Referer headers to external links, exposing session tokens to unauthorized parties.",
                "difficulty": "Easy"
            }
        ]
    },
    {
        "id": "ch8",
        "number": 8,
        "title": "Chapter 8: Attacking Access Controls",
        "subtitle": "Insecure Direct Object References (IDOR) & Privilege Escalation",
        "icon": "shield-check",
        "category": "Authorization",
        "readingTime": "25 min",
        "overview": "Investigate authorization failures: Insecure Direct Object References (IDOR), vertical vs. horizontal privilege escalation, multistep workflow bypasses, static file exposure, and HTTP verb tampering.",
        "sections": [
            {
                "id": "ch8-idor",
                "title": "IDOR: Horizontal & Vertical Privilege Escalation",
                "content": """
### Broken Object Level Authorization (BOLA / IDOR)

Access control enforces policy: ensuring users can only perform actions and access data appropriate to their authorization level.

```
Horizontal Escalation (Same Role, Different Data):
User A (ID 1001) ----> Requests /invoice?id=1002 ----> Views User B's Private Invoice!

Vertical Escalation (Lower Role to Higher Role):
Regular User    ----> Requests /admin/delete_user?id=5 ----> Deletes User Without Admin Role!
```

#### Why IDOR Vulnerabilities are Ubiquitous
1. **Developer Assumption**: Developers assume that because the UI does not show links to other users' data, users will never request those IDs.
2. **Lack of Contextual Check**:
```python
# Vulnerable Code: Checks IF user is logged in, but not WHO owns the document
@app.route('/document/<doc_id>')
@login_required
def get_doc(doc_id):
    return db.query("SELECT * FROM docs WHERE id = ?", doc_id) # VULNERABLE!

# Secure Code: Enforces tenancy and ownership check
@app.route('/document/<doc_id>')
@login_required
def get_doc_secure(doc_id):
    doc = db.query("SELECT * FROM docs WHERE id = ? AND owner_id = ?", doc_id, current_user.id)
    if not doc:
        abort(404)
    return doc
```
""",
                "keyTakeaways": [
                    "Never trust client-supplied resource identifiers without validating ownership against the active session.",
                    "Prefer random, unguessable UUIDs (v4) over sequential integers, while still maintaining strict authorization checks."
                ]
            },
            {
                "id": "ch8-methods",
                "title": "Testing Access Controls: Multi-Step & HTTP Method Tampering",
                "content": """
### Advanced Access Control Bypass Techniques

#### 1. Multistep Process Bypasses
* A wizard has 3 steps: 
  * Step 1: `/apply`
  * Step 2: `/run_credit_check` (Requires approval)
  * Step 3: `/disburse_funds`
* *Flaw*: An attacker skips Step 2 and sends an HTTP POST directly to Step 3. If Step 3 does not verify that Step 2 was completed and approved, funds are disbursed!

#### 2. HTTP Method Tampering (Verb Tampering)
* Many frameworks configure security rules based on HTTP methods:
```xml
<!-- Vulnerable web.xml configuration -->
<security-constraint>
  <web-resource-collection>
    <url-pattern>/admin/*</url-pattern>
    <http-method>GET</http-method>
    <http-method>POST</http-method>
  </web-resource-collection>
  <auth-constraint><role-name>ADMIN</role-name></auth-constraint>
</security-constraint>
```
* *Attack*: Send `HEAD`, `PUT`, `OPTIONS`, or a custom verb `TRACK /admin/users`. The security filter skips the rule, but the application container handles the request!
""",
                "keyTakeaways": [
                    "Ensure multi-step business logic validates state transitions on every request.",
                    "Apply access control rules globally by default, not by enumerating allowed HTTP methods."
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch8-1",
                "question": "What is the core flaw in an Insecure Direct Object Reference (IDOR) vulnerability?",
                "options": [
                    "The database password is leaked in the response.",
                    "The application references an internal object (e.g. database ID, file path) directly in user input without verifying whether the requesting user is authorized to access that specific object.",
                    "The web application uses HTTPS version 1.0.",
                    "The session cookie lacks the HttpOnly attribute."
                ],
                "correctIndex": 1,
                "explanation": "IDOR occurs when an application provides direct access to objects based on user-supplied input without performing contextual authorization checks to verify ownership.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch8-2",
                "question": "What is the difference between Horizontal and Vertical Privilege Escalation?",
                "options": [
                    "Horizontal affects desktop browsers; Vertical affects mobile browsers.",
                    "Horizontal escalation allows an attacker to access data belonging to other users with the same privilege level; Vertical escalation allows an attacker to gain higher privilege levels (e.g. user to admin).",
                    "Horizontal escalation is a database flaw; Vertical is a network flaw.",
                    "There is no difference."
                ],
                "correctIndex": 1,
                "explanation": "Horizontal privilege escalation involves accessing resources of peers at the same role level. Vertical privilege escalation involves gaining higher permissions, such as elevating from regular user to administrator.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch8-3",
                "question": "How can an attacker exploit HTTP Method Tampering when an access rule only restricts 'POST /admin/createUser'?",
                "options": [
                    "By sending the same request using GET, PUT, or HEAD, which might trigger the backend action while bypassing the method-specific filter.",
                    "By changing the User-Agent to Googlebot.",
                    "By adding a second Host header.",
                    "By encoding the username in Base64."
                ],
                "correctIndex": 0,
                "explanation": "If access control filters only restrict explicit methods (like POST), submitting the request with GET, PUT, or other verbs may bypass the security filter if the backend router handles alternate verbs.",
                "difficulty": "Medium"
            }
        ]
    },
    {
        "id": "ch9",
        "number": 9,
        "title": "Chapter 9: Attacking Data Stores",
        "subtitle": "SQL Injection, NoSQL, XPath & LDAP Injection",
        "icon": "database",
        "category": "Server-Side Injections",
        "readingTime": "35 min",
        "overview": "Comprehensive breakdown of data store injection attacks: classic SQL injection (Error-based, UNION-based, Blind boolean & time-based), Second-Order SQLi, NoSQL (MongoDB), XPath, and LDAP injection.",
        "sections": [
            {
                "id": "ch9-sqli",
                "title": "SQL Injection: Basic to Advanced Exploitation",
                "content": """
### SQL Injection (SQLi) Mechanics

SQL injection occurs when untrusted user data is concatenated directly into a dynamic database query string, allowing user input to break out of data context into command context.

```sql
-- Vulnerable Login Query
SELECT * FROM users WHERE username = 'USER_INPUT' AND password = 'PASSWORD_INPUT';

-- Attacker Input in Username:
admin' --

-- Resulting Executed Query:
SELECT * FROM users WHERE username = 'admin' --' AND password = '...';
-- The rest of the query is commented out! Attacker logs in as admin without a password!
```

#### The Four SQL Injection Modalities
1. **In-Band (UNION-Based)**:
   * The attacker appends a `UNION SELECT` statement to combine results from another table into the application's rendered output.
   * *Step 1*: Determine column count: `' ORDER BY 1--`, `' ORDER BY 2--` until error.
   * *Step 2*: Determine compatible data types: `' UNION SELECT 'a', NULL, 1--`.
   * *Step 3*: Extract data: `' UNION SELECT username, password, NULL FROM users--`.
2. **Error-Based**:
   * Forcing database runtime errors that dump database strings into the error output (e.g., `EXTRACTVALUE()`, `CONVERT()`).
3. **Inferential / Blind (Boolean & Time-Based)**:
   * No data or errors are displayed.
   * *Boolean*: Probing conditions (`AND SUBSTRING(password,1,1)='a'`) and observing differences in page response (e.g., 'Welcome back' vs. 'User not found').
   * *Time-Based*: Forcing delay functions (`pg_sleep(5)`, `WAITFOR DELAY '0:0:5'`, `SLEEP(5)`) to infer characters bit-by-bit.
4. **Out-of-Band (OAST)**:
   * Forcing the database to initiate DNS or HTTP requests to an attacker-controlled server (e.g., `LOAD_FILE('\\\\attacker.com\\share')`).
""",
                "keyTakeaways": [
                    "Parameterized queries (Prepared Statements) completely eliminate SQL injection regardless of user input characters.",
                    "Blind SQLi can always extract full databases; it only requires automated tooling like sqlmap or custom Python scripts."
                ]
            },
            {
                "id": "ch9-nosql-xpath-ldap",
                "title": "NoSQL, XPath & LDAP Injection",
                "content": """
### Beyond SQL: Alternative Data Store Injections

#### 1. NoSQL Injection (MongoDB)
* Many modern apps use document stores (MongoDB, CouchDB).
* If raw JSON or query parameters are parsed directly into queries without type validation:
```json
// Attacker submits JSON payload:
{"username": {"$gt": ""}, "password": {"$gt": ""}}

// MongoDB query:
db.users.find({username: {$gt: ""}, password: {$gt: ""}})
// Matches the first user in the database because any non-empty string is greater than ""!
```

#### 2. XPath Injection
* Used to query structured XML databases:
```xpath
// User query:
//users/user[username/text()='USER_INPUT' and password/text()='PASSWORD_INPUT']

// Payload:
' or '1'='1
// Subverts XML traversal logic and bypasses authentication.
```

#### 3. LDAP Injection
* Used in corporate directories (Active Directory, OpenLDAP):
* Payload: `admin*)(|(password=*))` breaks LDAP filter syntax `(&(uid=admin*)(|(password=*)))`.
""",
                "keyTakeaways": [
                    "NoSQL, XPath, and LDAP are just as vulnerable to query delimiter injection as relational SQL.",
                    "Always sanitize or use type-safe query builders."
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch9-1",
                "question": "What is the single most effective defense against all forms of SQL Injection?",
                "options": [
                    "Replacing all single quotes with double quotes.",
                    "Using parameterized queries (Prepared Statements) with bound parameters.",
                    "Installing a Web Application Firewall (WAF).",
                    "Filtering the word 'SELECT' from all input."
                ],
                "correctIndex": 1,
                "explanation": "Parameterized queries separate SQL code from data. The database treats parameters strictly as literal values, never executing them as SQL commands regardless of what characters they contain.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch9-2",
                "question": "When executing a UNION-based SQL injection, what two conditions must the attacker's injected SELECT statement satisfy?",
                "options": [
                    "It must be run by the database 'sa' or 'root' superuser.",
                    "It must return the exact same number of columns as the original query, and the data types of corresponding columns must be compatible.",
                    "It must execute within less than 50 milliseconds.",
                    "It must only query the sqlite_master table."
                ],
                "correctIndex": 1,
                "explanation": "Standard SQL requires that all queries combined via the UNION operator return identical column counts and have compatible data types in each respective column position.",
                "difficulty": "Medium"
            },
            {
                "id": "q-ch9-3",
                "question": "In a MongoDB / Express environment, what query payload bypasses authentication when input is parsed directly as JSON?",
                "options": [
                    "`' OR 1=1--`",
                    "`{\"username\": {\"$ne\": null}, \"password\": {\"$ne\": null}}`",
                    "`<script>alert(1)</script>`",
                    "`../../../../etc/passwd`"
                ],
                "correctIndex": 1,
                "explanation": "Using the MongoDB `$ne` (not equal) or `$gt` operator causes the query to match any document where username and password are not null, effectively logging in as the first user in the database.",
                "difficulty": "Hard"
            }
        ]
    },
    {
        "id": "ch10",
        "number": 10,
        "title": "Chapter 10: Attacking Back-End Components",
        "subtitle": "OS Command Injection, Path Traversal, XXE & SSRF",
        "icon": "terminal",
        "category": "Server-Side Injections",
        "readingTime": "35 min",
        "overview": "Master high-impact attacks against server-side infrastructure: OS Command Injection, Path Traversal / File Inclusion (LFI/RFI), XML External Entity (XXE) injection, Server-Side Request Forgery (SSRF), and SMTP injection.",
        "sections": [
            {
                "id": "ch10-command-injection",
                "title": "OS Command Injection & Dynamic Execution",
                "content": """
### OS Command Injection

Occurs when an application passes unsanitized user data directly to a system shell (`sh`, `bash`, `cmd.exe`) via functions like `system()`, `exec()`, `popen()`, or backticks.

```php
// Vulnerable PHP Code
$ip = $_POST['ip'];
$output = shell_exec("ping -c 3 " . $ip);
echo "<pre>$output</pre>";
```

#### Command Separators & Bypasses
* **Shell Delimiters**: `;`, `&`, `&&`, `|`, `||`, newline (`%0a`), backticks (`` `cmd` ``), `$()`
* **Payload**: `8.8.8.8; id; cat /etc/passwd` or `8.8.8.8 | whoami`
* **Space Filtering Bypasses**:
  * `${IFS}` (Linux internal field separator): `cat${IFS}/etc/passwd`
  * Brace expansion: `{cat,/etc/passwd}`
  * Input redirection: `cat</etc/passwd`
* **Keyword Filtering Bypasses**:
  * Concatenation: `c'a't /etc/pass'w'd`
  * Environment variables: `$u=cat; $u /etc/passwd`
  * Base64 decoding: `echo d2hvYW1p | base64 -d | sh`
""",
                "keyTakeaways": [
                    "Avoid calling OS shell interpreters directly.",
                    "If system execution is unavoidable, use native APIs that pass arguments as an explicit array without invoking a shell."
                ]
            },
            {
                "id": "ch10-path-traversal",
                "title": "Path Traversal & File Inclusion (LFI / RFI)",
                "content": """
### Path Traversal (Directory Traversal)

Occurs when user input is used to construct a file path without sufficient path normalization or sandboxing:

```http
GET /loadImage?filename=../../../../etc/passwd HTTP/1.1
Host: target.example.com
```

#### Traversal Evasion Techniques
* **Nested Traversal Sequences**: If the app strips `../` once non-recursively:
  * Input: `....//....//....//etc/passwd` -> When `../` is removed, leaves `../../etc/passwd`!
* **URL Encoding**: `%2e%2e%2f` (`../`), double encoding `%252e%252e%252f`.
* **Null Byte Injection (Legacy PHP < 5.3.4)**: `../../../../etc/passwd%00.png` truncates the trailing extension in C-based runtimes.

### Server-Side Request Forgery (SSRF)
When a backend server fetches a remote URL provided by the user (e.g., 'Import avatar from URL'):
* **Attack**: Point the server at internal, unauthenticated microservices or cloud metadata endpoints:
  * AWS / GCP Cloud Metadata: `http://169.254.169.254/latest/meta-data/iam/security-credentials/`
  * Internal Loopback: `http://127.0.0.1:8080/admin`
""",
                "keyTakeaways": [
                    "Validate file paths against an explicit whitelist of allowed filenames.",
                    "Use path canonicalization (`realpath()`) and verify that the target starts with the intended base directory.",
                    "Filter SSRF using strict URL whitelists and disable internal IP ranges (127.0.0.1, 10.0.0.0/8, 169.254.169.254)."
                ]
            },
            {
                "id": "ch10-xxe",
                "title": "XML External Entity (XXE) Injection",
                "content": """
### Exploiting XML Interpreters

XML documents can define custom entities. If the XML parser has external entity resolution enabled, an attacker can read arbitrary local files or trigger SSRF:

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
<stockCheck>
  <productId>&xxe;</productId>
</stockCheck>
```
* **Impact**: Local File Read (LFI), SSRF against internal services, Denial of Service (Billion Laughs entity expansion attack).
* **Prevention**: Explicitly disable Document Type Definition (DTD) processing and external entity resolution in the parser configuration:
```python
# Secure Python defusedxml
from defusedxml.ElementTree import parse
```
""",
                "keyTakeaways": [
                    "Disable external DTD parsing (`disallow-doctype-decl`) in all XML parsers.",
                    "Prefer modern data formats like JSON over XML where possible."
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch10-1",
                "question": "Which cloud metadata endpoint is commonly targeted via SSRF on AWS EC2 instances to retrieve temporary IAM credentials?",
                "options": [
                    "`http://localhost:3306`",
                    "`http://169.254.169.254/latest/meta-data/`",
                    "`http://aws.amazon.com/credentials`",
                    "`http://192.168.1.1/admin`"
                ],
                "correctIndex": 1,
                "explanation": "The link-local IPv4 address 169.254.169.254 is used by AWS (and other cloud providers) to provide instance metadata, including temporary IAM role security credentials.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch10-2",
                "question": "In a Linux OS command injection scenario where whitespace is blocked, which token can replace spaces?",
                "options": [
                    "`%20%20`",
                    "`${IFS}`",
                    "`<space>`",
                    "`\\x00`"
                ],
                "correctIndex": 1,
                "explanation": "${IFS} represents the shell's Internal Field Separator (defaulting to space, tab, and newline) and is widely used to separate command arguments when spaces are stripped.",
                "difficulty": "Medium"
            },
            {
                "id": "q-ch10-3",
                "question": "What is the primary root cause of XML External Entity (XXE) vulnerabilities?",
                "options": [
                    "The XML document is missing an SSL certificate.",
                    "The XML parser is configured to resolve external entity declarations (SYSTEM entities) defined in the document's DTD.",
                    "The server uses Linux instead of Windows.",
                    "The client submits XML instead of HTML."
                ],
                "correctIndex": 1,
                "explanation": "XXE occurs because legacy XML parsers by default parse and expand external SYSTEM entities declared in the DTD, allowing attackers to access local file paths and internal network URLs.",
                "difficulty": "Medium"
            }
        ]
    },
    {
        "id": "ch11",
        "number": 11,
        "title": "Chapter 11: Attacking Application Logic",
        "subtitle": "Flaws in Business Logic, State Transitions & Race Conditions",
        "icon": "cpu",
        "category": "Application Logic",
        "readingTime": "30 min",
        "overview": "Dive into the most elusive class of web vulnerabilities: business logic flaws. Learn how attackers violate developer assumptions, abuse state machines, manipulate currencies/limits, cheat bulk discounts, and exploit race conditions.",
        "sections": [
            {
                "id": "ch11-logic-flaws",
                "title": "The Nature of Logic Flaws: Violating Assumptions",
                "content": """
### What Are Business Logic Vulnerabilities?

Unlike SQLi or XSS, business logic flaws do not stem from syntactic parsing errors. The application behaves **exactly as coded**, but the code's design makes flawed assumptions about how users will interact with the system!

> **Automated scanners are largely blind to logic flaws** because scanners cannot understand the intended business context of an application.

#### Classic Real-World Examples
1. **Proceeding to Checkout (Step Skipping)**:
   * A 3-step checkout: `/cart` -> `/pay` -> `/confirm_order`.
   * *Flaw*: An attacker adds an expensive laptop to `/cart`, then skips `/pay` and sends a POST directly to `/confirm_order`. If the server fails to verify payment completion in its session state, the order ships for free!
2. **Negative Quantities & Values**:
   * Purchasing item A (Price: $1000, Qty: 1) and item B (Price: $10, Qty: -99).
   * Total calculated: `1000 + (-990) = $10`! The user buys a $1000 laptop for $10!
3. **Currency Rounding & Precision Abuse**:
   * Exploiting fractional cents in transactions (e.g., repeatedly transferring $0.004 which rounds down for the sender but rounds up for the recipient).
4. **Coupon & Discount Abuse**:
   * Applying the same single-use discount coupon multiple times concurrently or applying 100% discount codes to ineligible categories.
""",
                "keyTakeaways": [
                    "Logic flaws cannot be found by generic signature scanners; they require contextual human analysis.",
                    "Always test negative numbers, unexpected parameter combinations, and out-of-order workflow steps."
                ]
            },
            {
                "id": "ch11-races",
                "title": "Race Conditions & State Manipulation",
                "content": """
### Time-of-Check to Time-of-Use (TOCTOU)

When an application checks a condition in one operation and updates state in a subsequent operation, a window of vulnerability opens:

```
Thread 1 (Request A): Check Balance ($100 >= $100) -> OK!
Thread 2 (Request B): Check Balance ($100 >= $100) -> OK! (Checks BEFORE Thread 1 deducts!)
Thread 1: Deduct $100 -> Balance = $0 -> Transfer $100
Thread 2: Deduct $100 -> Balance = -$100 -> Transfer $100! ($200 transferred from $100 balance!)
```

#### Exploiting Race Conditions in Web Apps
* **Tools**: Burp Suite Repeater (Send group in parallel / HTTP/2 single-packet attack), Turbo Intruder.
* **Targets**: Redeeming gift cards, withdrawal requests, voting polls, limited-stock flash sales.
* **Defense**: Database-level transactions with row-level locks (`SELECT ... FOR UPDATE`), mutexes, or atomic database operations (`UPDATE accounts SET balance = balance - 100 WHERE id = 1 AND balance >= 100`).
""",
                "keyTakeaways": [
                    "Use HTTP/2 single-packet attacks to synchronize concurrent requests down to microsecond precision.",
                    "Enforce strict atomic database updates and mutexes for financial and state-altering workflows."
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch11-1",
                "question": "Why are automated web vulnerability scanners usually incapable of detecting business logic flaws?",
                "options": [
                    "Vulnerability scanners do not understand HTML5 syntax.",
                    "Logic flaws adhere to valid syntax and HTTP specifications; only human understanding of the business domain can detect that an operation violates intended business rules.",
                    "Automated scanners are blocked by all web servers.",
                    "Logic flaws only occur in desktop applications."
                ],
                "correctIndex": 1,
                "explanation": "Because logic flaws do not produce standard error codes or trigger signature matches (like SQL syntax errors or script reflections), scanners see normal 200 OK responses and cannot recognize business rule violations.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch11-2",
                "question": "An attacker sends two simultaneous requests to redeem a $50 gift card. Both succeed, crediting $100 total. What vulnerability was exploited?",
                "options": [
                    "Cross-Site Scripting (XSS)",
                    "A Time-of-Check to Time-of-Use (TOCTOU) Race Condition",
                    "SQL Injection",
                    "Path Traversal"
                ],
                "correctIndex": 1,
                "explanation": "This is a classic race condition where both threads check the card's validity before either thread marks the card as redeemed in the database.",
                "difficulty": "Medium"
            },
            {
                "id": "q-ch11-3",
                "question": "How should an e-commerce platform defend against negative quantity attacks (e.g. submitting `quantity=-5`)?",
                "options": [
                    "Disable the checkout page on weekends.",
                    "Enforce strict server-side validation ensuring that quantity values are positive integers strictly greater than zero.",
                    "Use HTTPS encryption.",
                    "Encode the quantity parameter using HTML entities."
                ],
                "correctIndex": 1,
                "explanation": "The server must rigorously validate all mathematical inputs, ensuring quantities are strictly positive integers (quantity >= 1) prior to calculating order totals.",
                "difficulty": "Easy"
            }
        ]
    },
    {
        "id": "ch12",
        "number": 12,
        "title": "Chapter 12: Attacking Users: Cross-Site Scripting",
        "subtitle": "Reflected, Stored & DOM-Based XSS Exploitation",
        "icon": "code",
        "category": "Client-Side Attacks",
        "readingTime": "35 min",
        "overview": "Master the primary client-side vulnerability: Cross-Site Scripting (XSS). Dissect Reflected, Stored, and DOM-based XSS, payload construction, context breakouts (HTML, attribute, JavaScript), CSP bypasses, and defenses.",
        "sections": [
            {
                "id": "ch12-varieties",
                "title": "Varieties of XSS: Reflected, Stored & DOM-Based",
                "content": """
### The Three Classes of Cross-Site Scripting

XSS occurs when an application includes untrusted user data in a web page without proper validation or contextual escaping, allowing an attacker to execute arbitrary JavaScript in the victim's browser context.

```
1. Reflected XSS (Non-Persistent):
   Attacker URL (?q=<script>...) ---> Victim Clicks ---> Server reflects script in response ---> Browser executes!

2. Stored XSS (Persistent):
   Attacker posts comment (<script>...) ---> Saved in DB ---> Every user viewing comment executes script!

3. DOM-Based XSS:
   Server response is benign! Client-side JS reads data from a Source (location.search) and passes it to an unsafe Sink (innerHTML, eval()).
```

#### Anatomy of DOM-Based XSS
* **Sources**: `location.search`, `location.hash`, `document.referrer`, `window.name`, `postMessage`.
* **Sinks**: `element.innerHTML`, `document.write()`, `eval()`, `setTimeout()`, `location.href`.

```javascript
// Vulnerable Client-Side JavaScript
const query = new URLSearchParams(window.location.search).get('name');
document.getElementById('greeting').innerHTML = "Hello " + query; // DANGEROUS SINK!
// Payload: ?name=<img src=x onerror=alert(document.domain)>
```
""",
                "keyTakeaways": [
                    "Stored XSS has the highest severity because it triggers automatically for any user viewing the page.",
                    "DOM XSS executes entirely on the client without the payload necessarily ever touching the server."
                ]
            },
            {
                "id": "ch12-exploitation",
                "title": "Context Breakouts, Filter Evasion & Defenses",
                "content": """
### Context is Everything in XSS

The required payload depends entirely on **where** the input reflects:

#### 1. HTML Body Context
* Reflection: `<div>USER_INPUT</div>`
* Payload: `<script>alert(1)</script>` or `<img src=x onerror=alert(1)>`

#### 2. HTML Attribute Context
* Reflection: `<input type="text" name="city" value="USER_INPUT">`
* Payload: `" onfocus="alert(1)" autofocus="`
* Result: `<input type="text" name="city" value="" onfocus="alert(1)" autofocus="">`

#### 3. JavaScript Variable Context
* Reflection: `<script> let search = 'USER_INPUT'; </script>`
* Payload: `'; alert(1); //`
* Result: `<script> let search = ''; alert(1); //'; </script>`

#### Modern Defenses Against XSS
1. **Context-Aware Output Encoding**:
   * HTML Entity Encoding (`&quot;`, `&amp;`, `&#x27;`) for HTML contexts.
   * JavaScript hex encoding (`\\x27`, `\\u0027`) inside script tags.
2. **Content Security Policy (CSP)**:
   * Header: `Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-r4nd0m';`
   * Blocks inline scripts lacking the secret per-request cryptographic nonce.
3. **Safe DOM APIs**:
   * Use `element.textContent = data;` instead of `element.innerHTML`.
""",
                "keyTakeaways": [
                    "Output encoding must match the exact execution context (HTML, attribute, JS variable, CSS).",
                    "CSP provides defense-in-depth, preventing unauthorized script execution even if reflection occurs."
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch12-1",
                "question": "What is the key characteristic of DOM-Based XSS that distinguishes it from Reflected and Stored XSS?",
                "options": [
                    "DOM XSS only runs on Internet Explorer.",
                    "The vulnerability exists entirely in client-side code: the payload is read from a DOM source and passed to an execution sink without needing server-side reflection.",
                    "DOM XSS requires SQL injection to function.",
                    "DOM XSS can only steal passwords, not session cookies."
                ],
                "correctIndex": 1,
                "explanation": "In DOM-based XSS, the malicious script is executed because the client's own JavaScript code takes user data from a source (like the URL hash) and writes it into an execution sink (like innerHTML), often without the payload ever reaching the backend server.",
                "difficulty": "Medium"
            },
            {
                "id": "q-ch12-2",
                "question": "If user input is reflected inside an HTML attribute: `<input value=\"USER_INPUT\">`, what payload breaks out of the attribute?",
                "options": [
                    "`' OR '1'='1`",
                    "`\" onmouseover=\"alert(1)`",
                    "`../../../../etc/passwd`",
                    "`<script>alert(1)</script>`"
                ],
                "correctIndex": 1,
                "explanation": "Because the attribute is enclosed in double quotes, injecting a double quote `\"` closes the attribute, allowing the attacker to inject event handlers like `onmouseover=\"alert(1)\"` or `autofocus onfocus=\"...\"`.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch12-3",
                "question": "Which DOM manipulation property is safe against XSS when rendering untrusted user text?",
                "options": [
                    "`element.innerHTML`",
                    "`document.write()`",
                    "`element.textContent`",
                    "`eval()`"
                ],
                "correctIndex": 2,
                "explanation": "`textContent` treats all input strictly as plain text, ensuring that HTML tags and script delimiters are rendered literally on screen without being parsed as executable markup.",
                "difficulty": "Easy"
            }
        ]
    },
    {
        "id": "ch13",
        "number": 13,
        "title": "Chapter 13: Attacking Users: Other Techniques",
        "subtitle": "CSRF, Clickjacking, SOP, CORS & Client-Side Injections",
        "icon": "user-x",
        "category": "Client-Side Attacks",
        "readingTime": "30 min",
        "overview": "Investigate attacks against the user beyond XSS: Cross-Site Request Forgery (CSRF), UI Redressing (Clickjacking), Same-Origin Policy (SOP) bypasses, Cross-Origin Resource Sharing (CORS) misconfigurations, and Open Redirects.",
        "sections": [
            {
                "id": "ch13-csrf-clickjacking",
                "title": "CSRF & UI Redressing (Clickjacking)",
                "content": """
### Cross-Site Request Forgery (CSRF)

CSRF tricks a victim's browser into submitting an unauthorized request to a vulnerable application where the victim is currently authenticated.

```
Victim Browser (Has active session cookie for bank.com)
      |
      |--- 1. Visits attacker.com ---
      |
      |<-- 2. Returns malicious auto-submitting form:
               <form action="https://bank.com/transfer" method="POST">
                 <input type="hidden" name="to" value="attacker">
                 <input type="hidden" name="amount" value="5000">
               </form>
               <script>document.forms[0].submit();</script>
      |
      |--- 3. Browser sends POST to bank.com WITH victim's session cookies automatically!
      v
Bank.com processes unauthorized transfer!
```

#### Defending Against CSRF
1. **Anti-CSRF Tokens (Synchronizer Token Pattern)**: Unpredictable, cryptographically strong token tied to user session, validated on every state-changing request.
2. **SameSite Cookie Attribute**:
   * `SameSite=Strict`: Cookies are never sent in cross-site requests.
   * `SameSite=Lax`: Cookies sent on top-level GET navigations, blocked on cross-site POSTs.

### UI Redressing (Clickjacking)
* The attacker embeds the target website inside a transparent `<iframe>` overlaid on top of a decoy game or button ('Click here to win a prize!').
* When the victim clicks, they unknowingly click a hidden button inside the framed application (e.g., 'Delete All Files' or 'Authorize App').
* **Defense**: Header `X-Frame-Options: DENY` or CSP `frame-ancestors 'none';`.
""",
                "keyTakeaways": [
                    "Browsers automatically attach cookies to cross-site requests unless SameSite attributes or anti-CSRF tokens intervene.",
                    "Prevent clickjacking using CSP frame-ancestors or X-Frame-Options: DENY."
                ]
            },
            {
                "id": "ch13-cors-sop",
                "title": "Same-Origin Policy (SOP) & CORS Misconfigurations",
                "content": """
### The Same-Origin Policy (SOP)

SOP restricts how a script loaded from one origin (`protocol + domain + port`) can interact with resources from another origin.

#### Cross-Origin Resource Sharing (CORS) Misconfigurations
CORS allows servers to relax SOP restrictions. Common developer mistakes:

```http
// Attacker sends:
GET /api/user/private-keys HTTP/1.1
Host: bank.com
Origin: https://evil-attacker.com

// Vulnerable Server Response:
HTTP/1.1 200 OK
Access-Control-Allow-Origin: https://evil-attacker.com
Access-Control-Allow-Credentials: true
```
* **The Flaw**: The server dynamically reflects whatever `Origin` header the client sends, combined with `Access-Control-Allow-Credentials: true`.
* **Exploitation**: The attacker's website can make an authenticated XMLHttpRequest/fetch and read the victim's private JSON responses!
* **Remediation**: Never dynamically mirror arbitrary origins with credentials enabled. Use a strict, immutable whitelist.
""",
                "keyTakeaways": [
                    "CORS relaxes SOP; misconfigured CORS allows external sites to steal sensitive data.",
                    "Never trust dynamically reflected Origin headers with Access-Control-Allow-Credentials: true."
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch13-1",
                "question": "What is the primary mechanism of a Cross-Site Request Forgery (CSRF) attack?",
                "options": [
                    "Stealing the victim's password from their local computer.",
                    "Inducing the victim's browser to send an unwanted HTTP request to a target website where the victim is authenticated, leveraging the browser's automatic inclusion of session cookies.",
                    "Cracking the SSL certificate of the web server.",
                    "Injecting shellcode into the web server memory."
                ],
                "correctIndex": 1,
                "explanation": "CSRF exploits the fact that browsers automatically attach credentials (cookies, HTTP basic auth) to cross-origin requests, allowing an attacker's site to forge actions on behalf of the user.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch13-2",
                "question": "Which HTTP response header effectively prevents an application from being framed in an iframe, mitigating Clickjacking?",
                "options": [
                    "`X-XSS-Protection: 1`",
                    "`X-Frame-Options: DENY`",
                    "`Content-Type: application/json`",
                    "`Server: Apache`"
                ],
                "correctIndex": 1,
                "explanation": "X-Frame-Options: DENY instructs the browser never to render the page inside any <frame>, <iframe>, or <object>, completely defeating UI redressing.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch13-3",
                "question": "Why is the CORS configuration `Access-Control-Allow-Origin: *` combined with `Access-Control-Allow-Credentials: true` rejected by modern browsers?",
                "options": [
                    "It causes infinite redirect loops.",
                    "The W3C / WHATWG specification explicitly forbids combining wildcard origins with credential sharing to prevent total privacy collapse.",
                    "Wildcards are not supported in HTTP headers.",
                    "It breaks JSON parsing."
                ],
                "correctIndex": 1,
                "explanation": "The CORS specification explicitly prohibits returning `Access-Control-Allow-Origin: *` when `Access-Control-Allow-Credentials` is set to `true` to prevent unauthorized cross-origin reading of authenticated data.",
                "difficulty": "Medium"
            }
        ]
    },
    {
        "id": "ch14",
        "number": 14,
        "title": "Chapter 14: Automating Customized Attacks",
        "subtitle": "Fuzzing, Burp Intruder & Overcoming Automation Barriers",
        "icon": "zap",
        "category": "Tooling & Methodology",
        "readingTime": "25 min",
        "overview": "Learn to write custom attack automation and harness tools like Burp Suite Intruder. Master payload positions, attack types (Sniper, Pitchfork, Cluster Bomb), response analysis, and overcoming anti-automation defenses (CAPTCHA, CSRF, rate limits).",
        "sections": [
            {
                "id": "ch14-intruder",
                "title": "Burp Intruder: Attack Types & Payload Positions",
                "content": """
### Mastering Burp Suite Intruder

Burp Intruder automates customized attacks against web applications. Knowing which attack type to select is critical:

#### The Four Intruder Attack Types
1. **Sniper**:
   * Uses a single payload set.
   * Places payloads into each defined position sequentially, one position at a time.
   * *Best for*: Fuzzing multiple parameters for SQLi/XSS individually or enumerating usernames on a single field.
2. **Battering Ram**:
   * Uses a single payload set.
   * Injects the **same** payload into all marked positions simultaneously on each request.
3. **Pitchfork**:
   * Uses multiple payload sets (one per marked position).
   * Iterates through all sets in parallel: request 1 gets payload (A1, B1), request 2 gets (A2, B2).
   * *Best for*: Testing known pairs (e.g., username list matched with corresponding password list).
4. **Cluster Bomb**:
   * Uses multiple payload sets.
   * Tests every permutation (Cartesian product): if Set A has 100 usernames and Set B has 100 passwords, Intruder sends 10,000 requests.
   * *Best for*: Comprehensive credential brute-forcing.
""",
                "keyTakeaways": [
                    "Choose Sniper for individual parameter fuzzing; Cluster Bomb for cross-parameter combinatorial attacks.",
                    "Analyze response length, status codes, and timing to detect successful hits."
                ]
            },
            {
                "id": "ch14-barriers",
                "title": "Overcoming Barriers: Rate Limits, Tokens & Sessions",
                "content": """
### Bypassing Anti-Automation Controls

Modern applications deploy defenses to obstruct automated testing:

#### 1. Per-Request Anti-CSRF Tokens
* If an endpoint requires a fresh anti-CSRF token with every POST, simple fuzzer requests fail.
* *Solution*: Configure Burp Suite **Macros** or Turbo Intruder scripts to fetch the preceding page, parse the new token, and inject it into the next fuzzer payload automatically.

#### 2. IP Rate Limiting & Throttling
* Applications block IPs after 20 attempts.
* *Techniques*:
  * Spoofing headers: `X-Forwarded-For: 127.0.0.1`, `X-Real-IP`, `Client-IP`.
  * Using rotating proxy services (AWS API Gateway IP rotators, proxies).
  * Delaying requests and introducing jitter.

#### 3. Session Invalidation During Attacks
* If fuzzing invalidates the active session token, subsequent payloads test an unauthenticated state.
* *Solution*: Configure session handling rules in Burp to check whether 'Logged In' appears in the response, and automatically re-run a login macro if logged out.
""",
                "keyTakeaways": [
                    "Use Burp Macros and Session Handling Rules to preserve valid sessions and refresh CSRF tokens during automated fuzzing.",
                    "Always monitor response lengths to identify anomalies indicating rate-limiting or authentication dropouts."
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch14-1",
                "question": "Which Burp Intruder attack type tests every combination of multiple payload lists (Cartesian product)?",
                "options": [
                    "Sniper",
                    "Battering Ram",
                    "Pitchfork",
                    "Cluster Bomb"
                ],
                "correctIndex": 3,
                "explanation": "Cluster Bomb iterates through all possible permutations of multiple payload sets (e.g. testing 100 usernames against 100 passwords = 10,000 requests).",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch14-2",
                "question": "What is the primary indicator used to identify a successful hit or unique behavior during automated fuzzing?",
                "options": [
                    "The color of the browser window.",
                    "Differences in HTTP status code, response body byte length, or response timing compared to the baseline response.",
                    "Whether the computer fan speeds up.",
                    "The font family used by the server."
                ],
                "correctIndex": 1,
                "explanation": "Security testers sort Intruder results by response status code, content length, and response time to spot anomalies, error traces, or successful logins.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch14-3",
                "question": "How can a penetration tester automate requests against an endpoint protected by single-use anti-CSRF tokens?",
                "options": [
                    "By turning off the internet connection.",
                    "By configuring a session handling Macro that issues a GET request to harvest a fresh token before each attack request is dispatched.",
                    "By deleting all cookies.",
                    "By encoding payloads in UTF-16."
                ],
                "correctIndex": 1,
                "explanation": "Burp Suite Macros can be chained with session handling rules to request the form, extract the dynamically generated anti-CSRF token, and insert it into the automated request parameter.",
                "difficulty": "Hard"
            }
        ]
    },
    {
        "id": "ch15",
        "number": 15,
        "title": "Chapter 15: Exploiting Information Disclosure",
        "subtitle": "Error Messages, Stack Traces & Public Reconnaissance",
        "icon": "info",
        "category": "Information Disclosure",
        "readingTime": "20 min",
        "overview": "Examine how subtle information leaks reveal critical backend implementation details. Uncover stack traces, SQL debug logs, framework version banners, source code repository leaks (.git), and inference timing channels.",
        "sections": [
            {
                "id": "ch15-errors",
                "title": "Exploiting Error Messages & Diagnostic Leaks",
                "content": """
### The Danger of Verbose Error Handling

Detailed error messages provide attackers with blueprints of internal application architecture:

```
HTTP/1.1 500 Internal Server Error
Content-Type: text/html

Fatal error: Uncaught PDOException: SQLSTATE[42S02]: Base table or view not found: 
1146 Table 'production_db.tbl_cust_orders' doesn't exist in /var/www/html/api/orders.php:142
Stack trace:
#0 /var/www/html/api/orders.php(142): PDO->query('SELECT * FROM t...')
#1 /var/www/html/index.php(48): include_once()
#2 {main} thrown in /var/www/html/api/orders.php on line 142
```

#### What Attackers Extract from Errors
* **Database Engine & Version**: MySQL, PostgreSQL, Oracle, SQLite.
* **Internal Server File Paths**: `/var/www/html/api/orders.php`, revealing operating system and folder structures.
* **Database Table & Column Names**: `tbl_cust_orders`, allowing precise UNION and extraction payloads.
* **Vulnerable Third-Party Library Versions**: Revealing known public CVEs ready for exploitation.
""",
                "keyTakeaways": [
                    "Disable detailed debugging and display_errors in production environments.",
                    "Present users with generic error IDs while logging technical traces securely internally."
                ]
            },
            {
                "id": "ch15-recon",
                "title": "Public Reconnaissance & Git Repository Dumps",
                "content": """
### Source Code Exposure via Misconfigured Metadata

#### 1. Exposed `.git` Folders
* When developers deploy code directly using `git clone` or fail to configure web server rules, the hidden `.git/` folder becomes web-accessible:
  * Accessing `http://target.com/.git/HEAD` returns `ref: refs/heads/main`.
* Attackers use tools like `git-dumper` to reconstruct the complete source code repository, commit history, configuration files, and past passwords!

#### 2. Server Banners & Metadata Files
* `robots.txt`, `sitemap.xml`, `crossdomain.xml`.
* HTTP response headers: `Server: Apache/2.4.41 (Ubuntu)`, `X-Powered-By: PHP/7.4.3`.
* Backup and temporary files left by text editors: `index.php.bak`, `config.inc.php~`, `.#app.js`.
""",
                "keyTakeaways": [
                    "Block public access to version control folders (.git, .svn) and environment files (.env) at the web server layer.",
                    "Strip server technology banners to deny reconnaissance intelligence to attackers."
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch15-1",
                "question": "What critical security flaw occurs when an application deploys with its `.git` folder exposed to the public web?",
                "options": [
                    "The server shuts down automatically.",
                    "Attackers can download the entire source code repository, past commit history, and hidden configuration secrets using automated git dumping tools.",
                    "The domain name expires.",
                    "Users can no longer log in."
                ],
                "correctIndex": 1,
                "explanation": "If the .git directory is accessible over HTTP, attackers can fetch objects and indexes to rebuild the full codebase, uncovering hardcoded credentials, logic flaws, and database passwords.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch15-2",
                "question": "How should production web applications handle unhandled exceptions and server errors?",
                "options": [
                    "Print the full database stack trace so users can contact support.",
                    "Display a generic error page with a unique correlation reference ID while logging the detailed technical stack trace to an internal, secure log file.",
                    "Ignore the error and keep executing instructions.",
                    "Redirect the user to google.com."
                ],
                "correctIndex": 1,
                "explanation": "Generic error pages prevent leaking sensitive internals (file paths, database versions, SQL fragments) while reference IDs allow internal engineers to look up the issue in secure logs.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch15-3",
                "question": "What is an inference attack in the context of information disclosure?",
                "options": [
                    "Deducing confidential information by observing subtle side-effects, such as variations in response times or page content size.",
                    "Using artificial intelligence to guess passwords.",
                    "Overclocking the web server CPU.",
                    "Sniffing unencrypted Wi-Fi."
                ],
                "correctIndex": 0,
                "explanation": "Inference attacks derive sensitive data indirectly by measuring side channels (such as millisecond timing differences or byte length variations) without direct error messages.",
                "difficulty": "Medium"
            }
        ]
    },
    {
        "id": "ch16",
        "number": 16,
        "title": "Chapter 16: Attacking Native Compiled Applications",
        "subtitle": "Memory Corruption, Buffer Overflows & Format Strings",
        "icon": "shield-minus",
        "category": "Native Code & Architecture",
        "readingTime": "25 min",
        "overview": "Understand how memory corruption vulnerabilities in native compiled server components (C/C++, legacy modules, custom CGI, image processing libraries) impact web applications: stack/heap overflows, off-by-one errors, integer overflows, and format strings.",
        "sections": [
            {
                "id": "ch16-overflows",
                "title": "Buffer Overflows in Web Contexts",
                "content": """
### Native Code in Modern Web Stacks

While modern web frontends run on interpreted languages, critical backend tasks rely on native compiled C/C++ code:
* High-performance web servers (Nginx, Apache modules)
* Media converters and image processing libraries (ImageMagick, FFmpeg, libpng)
* High-speed native serialization and cryptography libraries
* Legacy CGI programs and custom hardware IoT web interfaces

#### Stack Buffer Overflows
Occur when input exceeds the allocated stack buffer without bounds checking (`strcpy`, `gets`, `sprintf`):

```c
// Vulnerable C CGI script
void handle_request(char *user_input) {
    char buffer[128];
    strcpy(buffer, user_input); // DANGEROUS: No length boundary check!
}
```
* **Consequence**: Overwriting the saved Instruction Pointer (EIP/RIP) on the stack, diverting execution to shellcode or Return-Oriented Programming (ROP) chains to achieve Remote Code Execution (RCE).
""",
                "keyTakeaways": [
                    "Native components must be compiled with modern mitigations: ASLR, Stack Canaries, NX/DEP, and SafeSEH.",
                    "Replace unsafe C library calls with bounded alternatives (`strncpy`, `snprintf`) or memory-safe languages (Rust, Go)."
                ]
            },
            {
                "id": "ch16-integer-format",
                "title": "Integer Vulnerabilities & Format Strings",
                "content": """
### Integer Overflows & Format String Attacks

#### 1. Integer Overflows & Signedness Bugs
* In C/C++, integer types have fixed bit widths (e.g., 32-bit unsigned max = `4,294,967,295`).
* If an application calculates memory allocation size:
```c
unsigned short num_items = get_user_count(); // e.g. 65535
// If attacker passes 65536:
unsigned short total_bytes = num_items * sizeof(item); // Wraps around to 0!
char *buf = malloc(total_bytes); // Allocates 0 bytes!
copy_items(buf, user_data); // Massive Heap Buffer Overflow!
```

#### 2. Format String Vulnerabilities
* Passing user input directly as the format string parameter to `printf()`:
```c
printf(user_supplied_string); // VULNERABLE!
// Payload: %x %x %x %s %n
```
* **Impact**: `%x` leaks stack memory (bypassing ASLR); `%n` writes arbitrary values to memory addresses, enabling full system takeover!
""",
                "keyTakeaways": [
                    "Always validate integer arithmetic against overflow bounds.",
                    "Never pass dynamic user strings directly to printf-style formatting functions."
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch16-1",
                "question": "What is the primary danger of a stack buffer overflow vulnerability in a native web server component?",
                "options": [
                    "It changes the website CSS color scheme.",
                    "An attacker can overwrite the saved return address (EIP/RIP) on the stack to hijack control flow and achieve arbitrary remote code execution.",
                    "It causes the web browser to crash.",
                    "It invalidates the user's session cookie."
                ],
                "correctIndex": 1,
                "explanation": "By corrupting the stack frame and overwriting the saved instruction pointer, an attacker can redirect execution to injected shellcode or ROP gadgets, gaining full command execution on the host.",
                "difficulty": "Medium"
            },
            {
                "id": "q-ch16-2",
                "question": "Which format specifier in a format string vulnerability allows an attacker to write data to a memory location?",
                "options": [
                    "`%s`",
                    "`%d`",
                    "`%x`",
                    "`%n`"
                ],
                "correctIndex": 3,
                "explanation": "The `%n` format specifier writes the number of characters printed so far into the memory address pointed to by the corresponding argument, enabling arbitrary memory writes.",
                "difficulty": "Hard"
            },
            {
                "id": "q-ch16-3",
                "question": "What modern compiler mitigation detects stack buffer corruption before a function returns?",
                "options": [
                    "Stack Canaries (Stack Protectors)",
                    "Virtual Private Networks (VPN)",
                    "Base64 encoding",
                    "HTML5 DOCTYPE"
                ],
                "correctIndex": 0,
                "explanation": "Stack canaries place a secret random value on the stack before local variables. If an overflow occurs, the canary value is modified, prompting the runtime to terminate the process before execution is hijacked.",
                "difficulty": "Medium"
            }
        ]
    },
    {
        "id": "ch17",
        "number": 17,
        "title": "Chapter 17: Attacking Application Architecture",
        "subtitle": "Tiered Architectures, DMZ Bypasses & Shared Hosting",
        "icon": "layers",
        "category": "Native Code & Architecture",
        "readingTime": "20 min",
        "overview": "Analyze architectural vulnerabilities in enterprise web infrastructure: tiered DMZ boundaries, trust assumptions between front-end and back-end tiers, shared hosting tenant isolation, and cloud VPC boundary collapse.",
        "sections": [
            {
                "id": "ch17-tiered",
                "title": "Tiered Architectures & The Trust Boundary Fallacy",
                "content": """
### Multi-Tier Web Architectures

Enterprise web applications are divided into functional tiers:

```
[ Internet ] ---> [ Tier 1: Web / Reverse Proxy (DMZ) ]
                        |  (mTLS, Sanitization, Auth)
                        v
                  [ Tier 2: Application Server (Internal) ]
                        |  (Business Logic, Core Services)
                        v
                  [ Tier 3: Database & Mainframe (Protected Core) ]
```

#### The Trust Boundary Fallacy
* **Common Flaw**: Tier 2 assumes that because traffic arrives from Tier 1, all input has already been scrubbed and validated!
* **Exploitation**: If an attacker discovers an injection flaw, request smuggling vulnerability, or SSRF in Tier 1, Tier 2 treats the internal forwarded request as trusted and performs zero validation!
* **Remediation**: Adopt **Zero Trust Architecture**—every tier must authenticate and independently validate all incoming parameters.
""",
                "keyTakeaways": [
                    "Never assume that internal requests are inherently safe or pre-sanitized.",
                    "Enforce strict validation and least privilege at every tier boundary."
                ]
            },
            {
                "id": "ch17-shared",
                "title": "Shared Hosting & ASP Tenant Isolation Flaws",
                "content": """
### Risks in Shared Multi-Tenant Environments

In shared hosting or shared cloud infrastructures, multiple independent applications run on the same physical host or virtual runtime:

#### Attack Vectors Between Co-Tenants
1. **File System Permissions**: If the web server runs all virtual hosts under the same user (`www-data`) without `open_basedir` or container isolation, an attacker on `tenantA.com` can read `/var/www/tenantB/config.php`!
2. **Shared Database Instances**: Multiple tenants sharing a single database server using table prefixes (`wp_tenant1_`, `wp_tenant2_`). If one tenant experiences an SQL injection, they can read all co-tenants' tables!
3. **Internal Network Scanning**: An attacker renting a cheap account on a shared host can port-scan the internal management subnet and pivot to other tenants.
""",
                "keyTakeaways": [
                    "Isolate tenants using dedicated unprivileged system users, chroot, or isolated container boundaries.",
                    "Ensure database access controls strictly segregate tenant credentials."
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch17-1",
                "question": "What is the primary danger of the 'Trust Boundary Fallacy' in tiered web architectures?",
                "options": [
                    "It makes the web server load pages slower.",
                    "Backend tiers assume that incoming requests from the frontend DMZ proxy are already authenticated and sanitized, omitting their own security checks.",
                    "It causes SSL certificates to expire prematurely.",
                    "It prevents databases from using relational schemas."
                ],
                "correctIndex": 1,
                "explanation": "When backend services assume that frontend reverse proxies have eliminated all threats, any bypass of the frontend completely exposes unhardened backend systems.",
                "difficulty": "Medium"
            },
            {
                "id": "q-ch17-2",
                "question": "In a shared hosting environment, what configuration flaw allows one malicious tenant to read another tenant's files?",
                "options": [
                    "Using PHP 8 instead of PHP 7.",
                    "Running all virtual host web processes under the same operating system user ID (e.g. www-data) without file permission or container isolation.",
                    "Enabling gzip compression.",
                    "Using MySQL instead of PostgreSQL."
                ],
                "correctIndex": 1,
                "explanation": "If all tenants run under a shared OS user, the operating system cannot enforce file permission boundaries between tenant web directories.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch17-3",
                "question": "Which architecture model states that no actor or request should be trusted by default, regardless of whether it originates inside the corporate network?",
                "options": [
                    "Perimeter Defense Model",
                    "Zero Trust Architecture (ZTA)",
                    "Monolithic Model",
                    "Client-Server Model"
                ],
                "correctIndex": 1,
                "explanation": "Zero Trust Architecture operates on the principle of 'never trust, always verify', requiring continuous authentication and authorization at every boundary.",
                "difficulty": "Easy"
            }
        ]
    },
    {
        "id": "ch18",
        "number": 18,
        "title": "Chapter 18: Attacking the Application Server",
        "subtitle": "Server Misconfigurations, Default Portals & WAF Bypasses",
        "icon": "server",
        "category": "Native Code & Architecture",
        "readingTime": "25 min",
        "overview": "Audit web and application server infrastructure: default credentials, administrative consoles (Tomcat Manager, WebLogic), directory indexing, dangerous HTTP methods (PUT/DELETE), reverse proxy misconfigurations, and Web Application Firewall (WAF) evasions.",
        "sections": [
            {
                "id": "ch18-server-config",
                "title": "Vulnerable Server Configurations & Default Content",
                "content": """
### Auditing Server Infrastructure

Even flawless application code will fall if the underlying web server or servlet container is misconfigured:

#### 1. Default Portals & Credentials
* Apache Tomcat: `/manager/html` with `tomcat:s3cret` or `admin:admin`.
* WebLogic: `/console`
* JBoss / WildFly: `/admin-console`
* *Impact*: Attackers deploy malicious WAR files containing webshells, immediately achieving full remote code execution.

#### 2. Dangerous HTTP Methods
* Running `OPTIONS /` reveals enabled methods:
```http
OPTIONS / HTTP/1.1
Host: target.com

HTTP/1.1 200 OK
Allow: GET, HEAD, POST, PUT, DELETE, OPTIONS, TRACE
```
* **PUT**: Allows attackers to directly upload a webshell (`PUT /shell.jsp`).
* **DELETE**: Allows attackers to delete arbitrary application files.
* **TRACE**: Echoes back incoming headers, enabling Cross-Site Tracing (XST) to steal `HttpOnly` cookies.

#### 3. Directory Listings
* Web servers configured without an `index.html` file that default to showing directory indexes (`Options +Indexes` in Apache).
* Leaks sensitive configuration backups, temporary files, and hidden assets.
""",
                "keyTakeaways": [
                    "Disable dangerous HTTP methods (PUT, DELETE, TRACE) unless explicitly required and authenticated.",
                    "Remove all default admin consoles, sample applications, and disable directory listings."
                ]
            },
            {
                "id": "ch18-waf-bypasses",
                "title": "Web Application Firewalls (WAFs) & Evasions",
                "content": """
### Understanding & Bypassing WAFs

WAFs inspect incoming HTTP traffic and block known attack signatures:

#### Common WAF Evasion Techniques
1. **Case Sensitivity & Alternate Keywords**:
   * `<sCrIpT>`, `UnIoN/**/SeLeCt`
2. **Inline Comments**:
   * `SELECT/*foo*/column/*bar*/FROM/*baz*/users`
3. **HTTP Parameter Pollution (HPP)**:
   * Submitting identical parameter keys: `?id=1&id=2`. Some WAFs inspect only the first parameter while the backend uses the second!
4. **Encoding Differentials**:
   * URL encoding, double URL encoding (`%2527`), Unicode overlong sequences.
   * Chunked transfer encoding: `Transfer-Encoding: chunked` splits malicious payloads across multiple HTTP chunks, blinding naive WAF stream reassemblers.
""",
                "keyTakeaways": [
                    "A WAF is a temporary defensive shield, not a substitute for fixing root cause vulnerabilities.",
                    "WAFs can frequently be bypassed using parser differentials and alternate encodings."
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch18-1",
                "question": "What is the primary danger of leaving the HTTP PUT method enabled and unauthenticated on a web server?",
                "options": [
                    "It causes the web server to run out of memory.",
                    "An attacker can upload a web shell or arbitrary executable script directly to the web root, achieving remote code execution.",
                    "It changes the server's time zone.",
                    "It revokes all SSL certificates."
                ],
                "correctIndex": 1,
                "explanation": "If HTTP PUT is unauthenticated, an attacker can upload arbitrary files (such as a PHP or JSP webshell) directly to the web directory and execute them.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch18-2",
                "question": "What attack technique uses the HTTP TRACE method to bypass cookie HttpOnly protections?",
                "options": [
                    "Cross-Site Tracing (XST)",
                    "SQL Injection",
                    "Local File Inclusion",
                    "HTTP Request Smuggling"
                ],
                "correctIndex": 0,
                "explanation": "Cross-Site Tracing (XST) combines XSS with an HTTP TRACE request. The server echoes back the client's request headers (including HttpOnly cookies) in the response body, which JavaScript can then read.",
                "difficulty": "Medium"
            },
            {
                "id": "q-ch18-3",
                "question": "How can 'Chunked Transfer Encoding' sometimes bypass a Web Application Firewall (WAF)?",
                "options": [
                    "It encrypts the payload using AES-256.",
                    "It breaks the attack payload across multiple small chunks, preventing simple WAF pattern matchers from detecting the full signature unless the WAF fully reassembles the stream.",
                    "It changes the destination IP address.",
                    "It forces the browser to use HTTP/3."
                ],
                "correctIndex": 1,
                "explanation": "By splitting malicious keywords across chunk boundaries (e.g. 'UN' in chunk 1, 'ION' in chunk 2), naive WAFs that inspect streaming chunks independently fail to identify the complete attack payload.",
                "difficulty": "Hard"
            }
        ]
    },
    {
        "id": "ch19",
        "number": 19,
        "title": "Chapter 19: Finding Vulnerabilities in Source Code",
        "subtitle": "Static Code Review, Sources, Sinks & Language Pitfalls",
        "icon": "file-code",
        "category": "Code Review & Tooling",
        "readingTime": "30 min",
        "overview": "Master white-box source code review methodology. Understand Sources (tainted user input) and Sinks (dangerous execution points) across Java, ASP.NET, PHP, and Python. Spot common vulnerability signatures and hidden backdoors.",
        "sections": [
            {
                "id": "ch19-methodology",
                "title": "Code Review Methodology: Sources & Sinks",
                "content": """
### The Source-to-Sink Taint Tracking Model

White-box static code review is the most comprehensive audit method. Every vulnerability traces an unbroken path from an untrusted **Source** to a dangerous **Sink**:

```
[ Tainted Source ] ---> [ Sanitization / Transform? ] ---> [ Dangerous Sink ]
(e.g., req.getParameter)    (Missing or Flawed!)          (e.g., stmt.executeQuery)
```

#### Common Sources (Tainted Entry Points)
* **Java**: `request.getParameter()`, `request.getHeader()`, `request.getCookies()`.
* **PHP**: `$_GET`, `$_POST`, `$_REQUEST`, `$_COOKIE`, `$_SERVER['HTTP_*']`.
* **ASP.NET**: `Request.QueryString`, `Request.Form`, `Request.Headers`.
* **Node.js**: `req.query`, `req.body`, `req.headers`, `req.params`.

#### Common Dangerous Sinks
* **SQL Injection**: `statement.executeQuery()`, `mysql_query()`, `db.raw()`.
* **Command Injection**: `Runtime.getRuntime().exec()`, `shell_exec()`, `os.system()`, `child_process.exec()`.
* **Path Traversal**: `new File()`, `fopen()`, `file_get_contents()`.
* **XSS**: `out.println()`, `echo`, `element.innerHTML`, `response.write()`.
* **Insecure Deserialization**: `readObject()`, `unserialize()`, `pickle.loads()`.
""",
                "keyTakeaways": [
                    "Follow data flow from untrusted source to sink to verify whether proper sanitization or parameterization occurs.",
                    "Search for dangerous sink APIs first, then trace backward to find reachable input sources."
                ]
            },
            {
                "id": "ch19-language-pitfalls",
                "title": "Language-Specific Signatures & Pitfalls",
                "content": """
### Language Quirks & Common Vulnerability Patterns

#### 1. PHP Type Juggling & Loose Comparison
```php
// PHP loose comparison (==) evaluates "0e123" == "0e456" as true (both are 0)!
if ($password_hash == "0e99887766...") { ... }
// Always use strict identity comparisons (===) or hash_equals()
```

#### 2. Java Insecure Deserialization
```java
ObjectInputStream ois = new ObjectInputStream(clientSocket.getInputStream());
Object obj = ois.readObject(); // VULNERABLE!
// If Apache Commons Collections is on classpath, triggers Gadget Chain RCE!
```

#### 3. Python Insecure Deserialization & Template Injection
```python
# Insecure Pickle
data = pickle.loads(user_cookie) # RCE!

# Server-Side Template Injection (SSTI) in Jinja2
render_template_string("Hello " + user_name) # VULNERABLE!
# Payload: {{ self.__init__.__globals__.__builtins__.__import__('os').popen('id').read() }}
```
""",
                "keyTakeaways": [
                    "Never deserialize untrusted data with native object deserializers (pickle, Java readObject, PHP unserialize).",
                    "Beware of dynamic string concatenation in template engines (SSTI)."
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch19-1",
                "question": "In static code analysis, what is the definition of a 'Sink'?",
                "options": [
                    "The database connection pool.",
                    "An entry point where user data enters the application (e.g. `$_GET`).",
                    "A dangerous function or method call where tainted user data can trigger security vulnerabilities (e.g. `exec()` or `executeQuery()`).",
                    "The trash folder on the developer's workstation."
                ],
                "correctIndex": 2,
                "explanation": "In taint analysis, a Sink is the terminal function or API that executes operations (like database queries, command execution, or DOM writes). If tainted input reaches a sink unvalidated, a vulnerability exists.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch19-2",
                "question": "Why is the use of `pickle.loads()` on user-supplied cookies in Python considered a critical security vulnerability?",
                "options": [
                    "Pickle cookies take up too much memory.",
                    "Python's pickle module allows serialized objects to define `__reduce__` methods that execute arbitrary OS commands upon deserialization.",
                    "Pickle is incompatible with Python 3.",
                    "Pickle only works on local files."
                ],
                "correctIndex": 1,
                "explanation": "Python's pickle format is inherently unsafe for untrusted input. An attacker can craft a serialized payload with an arbitrary callable in `__reduce__` to achieve immediate Remote Code Execution.",
                "difficulty": "Medium"
            },
            {
                "id": "q-ch19-3",
                "question": "What is the security risk of `render_template_string(\"Hello \" + request.args.get('name'))` in Flask / Jinja2?",
                "options": [
                    "SQL Injection",
                    "Server-Side Template Injection (SSTI) leading to remote code execution",
                    "Path Traversal",
                    "Clickjacking"
                ],
                "correctIndex": 1,
                "explanation": "Concatenating user input directly into template syntax invokes the template compiler on user-controlled text, enabling SSTI where the attacker can execute arbitrary Python commands via template expressions.",
                "difficulty": "Medium"
            }
        ]
    },
    {
        "id": "ch20",
        "number": 20,
        "title": "Chapter 20: A Web Application Hacker’s Toolkit",
        "subtitle": "Proxies, Scanners, Fuzzers & Custom Automation Tools",
        "icon": "tool",
        "category": "Code Review & Tooling",
        "readingTime": "25 min",
        "overview": "Assemble the modern web penetration tester's toolkit: Burp Suite Pro, OWASP ZAP, browser developer tools, standalone fuzzers (ffuf, dirsearch, gobuster), exploitation frameworks (sqlmap, commix), and custom Python scripting.",
        "sections": [
            {
                "id": "ch20-intercepting-proxies",
                "title": "Integrated Testing Suites: Burp Suite & OWASP ZAP",
                "content": """
### The Core Testing Arsenal: Intercepting Proxies

The intercepting proxy sits between the browser and target web server, capturing every HTTP/WebSocket frame for inspection, modification, and replay.

```
[ Browser ] <--- HTTP/HTTPS ---> [ Burp Suite / ZAP Proxy ] <--- HTTP/HTTPS ---> [ Target Web Server ]
                                  - Proxy (Intercept & Edit)
                                  - Repeater (Manual Crafting)
                                  - Intruder (Fuzzing)
                                  - Scanner (Vulnerability Detection)
                                  - Extender (Custom Python/Java Plugins)
```

#### Core Components
* **Proxy**: Live interception of raw HTTP requests and responses.
* **Repeater**: Manually tweak request headers and parameters and inspect responses in real-time.
* **Intruder**: High-speed automated fuzzing and credential brute forcing.
* **Sequencer**: Statistical entropy analysis for session tokens and nonces.
* **Comparer**: Visual side-by-side diffing of HTTP responses (essential for blind SQLi and timing attacks).
""",
                "keyTakeaways": [
                    "Burp Suite Repeater is the primary tool for testing injection payloads and logic flaws.",
                    "Use Burp Sequencer to empirically test token randomness and predict predictability flaws."
                ]
            },
            {
                "id": "ch20-specialized-tools",
                "title": "Specialized Fuzzers & Custom Python Automation",
                "content": """
### Specialized CLI Tools & Scripting

While GUI proxies are indispensable, high-speed command line utilities excel at targeted phases:

1. **Content & Directory Discovery**:
   * `ffuf` (Fuzz Faster U Fool): Blazingly fast Go-based fuzzer for directory, virtual host, and parameter discovery.
   * `gobuster`, `dirsearch`: Standard file brute-forcing utilities.
2. **Specialized Injection Tools**:
   * `sqlmap`: Automated SQL injection detection and database takeover.
   * `commix`: Automated OS command injection testing.
   * `wpscan`: WordPress vulnerability scanner.
3. **Custom Python Automation with `requests`**:
   * Writing tailored scripts for race conditions, multi-step API attacks, or custom token decryption.
""",
                "keyTakeaways": [
                    "Combine fast CLI tools (ffuf) for reconnaissance with deep proxy manual testing (Burp) for exploitation.",
                    "Custom Python scripts are essential when applications use proprietary hashing, signatures, or multi-step session flows."
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch20-1",
                "question": "Which component in Burp Suite is designed for manually editing and re-sending individual HTTP requests to analyze responses?",
                "options": [
                    "Intruder",
                    "Repeater",
                    "Sequencer",
                    "Decoder"
                ],
                "correctIndex": 1,
                "explanation": "Burp Repeater is the manual workhorse for web penetration testing, allowing testers to quickly modify parameters, re-issue requests, and observe response variations.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch20-2",
                "question": "What is the primary function of Burp Sequencer?",
                "options": [
                    "To generate automated PDF pentest reports.",
                    "To perform statistical randomness and entropy tests on collected session tokens to evaluate predictability.",
                    "To brute-force WordPress passwords.",
                    "To scan network ports like Nmap."
                ],
                "correctIndex": 1,
                "explanation": "Burp Sequencer captures a large sample of tokens and performs FIPS 140-2 and Shannon entropy tests to determine whether tokens can be predicted by attackers.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch20-3",
                "question": "Why is `ffuf` generally preferred over Python-based crawlers for large-scale directory brute-forcing?",
                "options": [
                    "ffuf is written in Go and utilizes lightweight goroutines to achieve thousands of requests per second with minimal CPU overhead.",
                    "ffuf can bypass all firewalls automatically.",
                    "Python cannot make HTTP requests.",
                    "ffuf requires no wordlists."
                ],
                "correctIndex": 0,
                "explanation": "ffuf is written in Go and optimized for concurrency, enabling ultra-fast HTTP fuzzing across large wordlists compared to interpreted scripting languages.",
                "difficulty": "Medium"
            }
        ]
    },
    {
        "id": "ch21",
        "number": 21,
        "title": "Chapter 21: A Web Application Hacker’s Methodology",
        "subtitle": "The 13-Phase Penetration Testing Execution Framework",
        "icon": "clipboard-check",
        "category": "Methodology & Review",
        "readingTime": "35 min",
        "overview": "The definitive, battle-tested 13-step methodology from The Web Application Hacker's Handbook: from mapping and analyzing the application to attacking authentication, session management, access controls, input vulnerabilities, logic flaws, and reporting.",
        "sections": [
            {
                "id": "ch21-phases-1-6",
                "title": "Phases 1-6: Mapping, Analysis, Client Controls, Auth & Access",
                "content": """
### The Battle-Tested 13-Phase Methodology (Part 1)

Professional web penetration testing follows a structured methodology to guarantee full coverage:

#### 1. Map the Application's Content
* Explore visible content; consult public resources (search engines, Wayback Machine).
* Discover hidden content and default paths with wordlists; enumerate identifier-specified functions; test for debug parameters (`?debug=1`, `?test=true`).

#### 2. Analyze the Application
* Identify core functionality, data entry points, and backend technologies.
* Map the complete attack surface and identify trust boundaries.

#### 3. Test Client-Side Controls
* Test data transmission via client (hidden fields, cookies, URL parameters, ViewState).
* Test client-side controls over user input (length limits, JavaScript validation, disabled elements).

#### 4. Test the Authentication Mechanism
* Understand mechanism; test password quality, username enumeration, resilience to password guessing.
* Test account recovery, remember me, impersonation, autogenerated credentials, credential transmission/storage, and logic flaws.

#### 5. Test Session Management
* Test token randomness, predictability, and meaning.
* Check token disclosure in logs/network; test session termination, fixation, CSRF, and cookie flags.

#### 6. Test Access Controls
* Understand requirements; test with multiple user accounts (horizontal & vertical).
* Test multi-stage processes and probe for direct access to methods and static resources.
""",
                "keyTakeaways": [
                    "Methodical execution prevents blind spots. Skipping mapping leads to missed vulnerabilities.",
                    "Always create at least two accounts with different privilege levels to thoroughly test access controls."
                ]
            },
            {
                "id": "ch21-phases-7-13",
                "title": "Phases 7-13: Injections, Logic, Hosting, Server & Reporting",
                "content": """
### The Battle-Tested 13-Phase Methodology (Part 2)

#### 7. Test for Input-Based Vulnerabilities
* Fuzz all request parameters; test for SQL Injection, XSS, OS Command Injection, Path Traversal, Script Injection, and File Inclusion.

#### 8. Test for Function-Specific Input Vulnerabilities
* Test for SMTP Injection, SOAP Injection, LDAP Injection, XPath Injection, XXE, and Back-End Request Injection (SSRF).

#### 9. Test for Logic Flaws
* Identify key attack surface, test multi-stage processes, handling of incomplete input, trust boundaries, and transaction logic.

#### 10. Test for Shared Hosting Vulnerabilities
* Test segregation in shared infrastructures and multi-tenant environments.

#### 11. Test for Application Server Vulnerabilities
* Test default credentials, default content, dangerous HTTP methods, proxy functionality, virtual hosting misconfigurations, and WAF evasion.

#### 12. Miscellaneous Checks
* Check for DOM-based attacks, local privacy vulnerabilities (browser storage), SSL/TLS ciphers, and Same-Origin Policy / CORS configuration.

#### 13. Follow Up Information Leakage & Formulate Attack Chains
* Review all error messages and sensitive leaks.
* **Correlate findings to formulate post-exploitation attack paths** (e.g., IDOR leaks API key -> API key accesses internal server -> SSRF accesses cloud metadata -> Root AWS takeover!).
""",
                "keyTakeaways": [
                    "Vulnerabilities gain true impact when chained together into an end-to-end attack narrative.",
                    "Document precise reproduction steps, root cause explanations, and actionable remediations in the final report."
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch21-1",
                "question": "What is the primary objective of Phase 13 ('Follow Up Any Information Leakage') in the WAHH methodology?",
                "options": [
                    "To delete all penetration testing logs.",
                    "To correlate disparate low-severity findings and information leaks into high-impact post-exploitation attack chains.",
                    "To install commercial antivirus on the target.",
                    "To inform the police immediately."
                ],
                "correctIndex": 1,
                "explanation": "Phase 13 focuses on chaining findings together: combining an information disclosure bug with a minor logic flaw or SSRF to achieve full system compromise.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch21-2",
                "question": "Why is testing access controls with multiple accounts (e.g. Account A and Account B with the same privileges) essential in Phase 6?",
                "options": [
                    "To test whether the web server crashes under two users.",
                    "To detect Horizontal Privilege Escalation (IDOR) by attempting to access Account A's resources using Account B's session.",
                    "To see if passwords can be shared.",
                    "To test email delivery."
                ],
                "correctIndex": 1,
                "explanation": "Having two accounts at the same privilege tier allows the tester to verify whether User A can view or edit User B's private objects, proving horizontal authorization failures.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch21-3",
                "question": "In the 13-phase methodology, why is 'Analyzing the Application' (Phase 2) conducted BEFORE 'Testing for Input-Based Vulnerabilities' (Phase 7)?",
                "options": [
                    "Because automated scanners require Phase 7 to run last.",
                    "Because a tester must first understand the technologies, workflows, and data entry points to select targeted payloads rather than blindly firing irrelevant exploits.",
                    "Because Phase 2 requires root server access.",
                    "There is no specific reason; the order does not matter."
                ],
                "correctIndex": 1,
                "explanation": "Understanding which server technologies, databases, and frameworks are deployed prevents wasted effort and allows the tester to craft precise payloads for the specific environment.",
                "difficulty": "Medium"
            }
        ]
    },
    {
        "id": "master-index",
        "number": 22,
        "title": "Master Vulnerability & Reference Index",
        "subtitle": "Attack Primitives, Defensive Controls & CVE Cross-Reference",
        "icon": "book-open",
        "category": "Methodology & Review",
        "readingTime": "20 min",
        "overview": "A master reference catalog indexing attack primitives, defensive controls, CVE classifications, and tool mappings across all 21 chapters of The Web Application Hacker's Handbook.",
        "sections": [
            {
                "id": "idx-primitives",
                "title": "Alphabetical Index of Attack Primitives & Defensive Controls",
                "content": """
### Master Reference Guide

| Vulnerability Class | Attack Primitive | Root Cause | Primary Defense | WAHH Chapter |
|:---|:---|:---|:---|:---|
| **SQL Injection** | `' OR 1=1--`, `UNION SELECT` | String concatenation into SQL queries | Parameterized Queries (Prepared Statements) | Ch 9 |
| **Cross-Site Scripting (XSS)** | `<script>`, `<img onerror=...>` | Untrusted input rendered in DOM context | Context-Aware Output Encoding & CSP | Ch 12 |
| **CSRF** | Cross-domain forged POST/GET | Browser automatically attaches session cookies | Anti-CSRF Synchronizer Tokens & SameSite=Lax/Strict | Ch 13 |
| **IDOR / BOLA** | Tampering object IDs (`?id=102`) | Missing authorization check on record owner | Server-side ownership validation per session | Ch 8 |
| **Command Injection** | `; id;`, `| whoami` | Passing user data to OS shell interpreters | Avoid shell invocation; use parameterized exec array | Ch 10 |
| **Path Traversal / LFI** | `../../../../etc/passwd` | Dynamic file paths without canonicalization | Whitelisting allowed files & `realpath()` check | Ch 10 |
| **SSRF** | `http://169.254.169.254/` | Server fetches user-supplied URLs | Strict domain whitelisting; block private IP ranges | Ch 10 |
| **XXE Injection** | `<!ENTITY xxe SYSTEM ...>` | XML parser resolves external SYSTEM entities | Disable DTDs and external entity expansion | Ch 10 |
| **Session Fixation** | Forcing pre-auth token | Server retains same session token post-login | Issue fresh token on login (`session_regenerate_id`) | Ch 7 |
| **Clickjacking** | Transparent `<iframe>` overlay | Target page permits third-party framing | `X-Frame-Options: DENY` or CSP `frame-ancestors 'none'` | Ch 13 |
| **Logic Flaw** | Skipping checkout steps, negative qty | Flawed developer assumptions in state machine | Strict server-side state machine verification | Ch 11 |
| **Insecure Deserialization** | Serialized object gadget chains | Unsafe native object unpacking | Avoid native deserialization; use plain JSON | Ch 19 |
""",
                "keyTakeaways": [
                    "Keep this master reference handy as your quick cheat sheet during active web application audits.",
                    "Notice that almost all vulnerabilities share the same root cause: failing to separate instructions from data."
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-idx-1",
                "question": "Which defensive principle eliminates both SQL Injection and OS Command Injection across all modern web frameworks?",
                "options": [
                    "Doubling the length of the server's TLS key.",
                    "Strictly separating code/instructions from data using parameterized interfaces, ensuring user input can never alter execution logic.",
                    "Installing client-side browser extensions.",
                    "Using Base64 encoding on all database fields."
                ],
                "correctIndex": 1,
                "explanation": "Both SQLi and Command Injection occur when user data escapes its data container and is executed as code. Parameterized APIs pass data through dedicated channels where it can never be parsed as instructions.",
                "difficulty": "Easy"
            },
            {
                "id": "q-idx-2",
                "question": "Which combination of HTTP security headers provides defense-in-depth against XSS, Clickjacking, and credential transmission over insecure channels?",
                "options": [
                    "`Server: Apache` and `Content-Type: text/html`",
                    "`Content-Security-Policy`, `X-Frame-Options: DENY`, `Strict-Transport-Security (HSTS)`, and `Set-Cookie: ...; Secure; HttpOnly; SameSite=Strict`",
                    "`Accept: */*` and `Connection: keep-alive`",
                    "`X-Powered-By: PHP` and `Cache-Control: public`"
                ],
                "correctIndex": 1,
                "explanation": "This suite of modern security headers enforces TLS encryption (HSTS), blocks inline script execution (CSP), forbids clickjacking frames (X-Frame-Options), and safeguards cookies from XSS and CSRF.",
                "difficulty": "Medium"
            }
        ]
    }
]

output_path = "/home/rakib/.gemini/antigravity/scratch/wahh-learning-platform/js/curriculum.js"
with open(output_path, "w", encoding="utf-8") as f:
    f.write("// The Web Application Hacker's Handbook (2nd Edition) - Complete Curriculum Data\n")
    f.write("// Auto-generated comprehensive curriculum containing all 21 chapters, Intro, and Master Index\n\n")
    f.write("(typeof window !== 'undefined' ? window : global).WAHH_CURRICULUM = ")
    json.dump(modules, f, indent=2)
    f.write(";\n")
    f.write("if (typeof module !== 'undefined') module.exports = (typeof window !== 'undefined' ? window : global).WAHH_CURRICULUM;\n")

print(f"Successfully generated {output_path} with {len(modules)} modules!")

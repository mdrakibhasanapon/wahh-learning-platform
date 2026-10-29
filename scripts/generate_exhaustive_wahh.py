#!/usr/bin/env python3
"""
Exhaustive Curriculum Generator for WAHH Security Academy
Builds complete 21 chapters + Intro + Master Index with ALL topics and subtopics from the 15-page syllabus.
"""

import json

# Complete syllabus definition matching OCR pages 1 to 15
raw_syllabus = [
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
        "quiz": [
            {
                "id": "q-intro-1",
                "question": "Why did the rise of web applications invalidate traditional network perimeter security (firewalls)?",
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
                "subtopics": [
                    "Summary"
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
        "topics": [
            {
                "title": "The HTTP Protocol",
                "subtopics": [
                    "HTTP Requests",
                    "HTTP Responses",
                    "HTTP Methods",
                    "URLs",
                    "REST",
                    "HTTP Headers",
                    "Cookies",
                    "Status Codes",
                    "HTTPS",
                    "HTTP Proxies",
                    "HTTP Authentication"
                ]
            },
            {
                "title": "Web Functionality",
                "subtopics": [
                    "Server-Side Functionality",
                    "Client-Side Functionality",
                    "State and Sessions"
                ]
            },
            {
                "title": "Encoding Schemes",
                "subtopics": [
                    "URL Encoding",
                    "Unicode Encoding",
                    "HTML Encoding",
                    "Base64 Encoding",
                    "Hex Encoding",
                    "Remoting and Serialization Frameworks"
                ]
            },
            {
                "title": "Summary & Review",
                "subtopics": [
                    "Next Steps",
                    "Questions"
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch3-1",
                "question": "What cookie attribute prevents client-side JavaScript from reading document.cookie?",
                "options": [
                    "SameSite=Strict",
                    "Secure",
                    "HttpOnly",
                    "Domain=.example.com"
                ],
                "correctIndex": 2,
                "explanation": "The HttpOnly flag directs the browser that the cookie should not be accessible via client-side scripts, mitigating session hijacking via XSS.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch3-2",
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
        "topics": [
            {
                "title": "Enumerating Content and Functionality",
                "subtopics": [
                    "Web Spidering",
                    "User-Directed Spidering",
                    "Discovering Hidden Content",
                    "Application Pages Versus Functional Paths",
                    "Discovering Hidden Parameters"
                ]
            },
            {
                "title": "Analyzing the Application",
                "subtopics": [
                    "Identifying Entry Points for User Input",
                    "Identifying Server-Side Technologies",
                    "Identifying Server-Side Functionality",
                    "Mapping the Attack Surface"
                ]
            },
            {
                "title": "Summary & Review",
                "subtopics": [
                    "Summary",
                    "Questions"
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch4-1",
                "question": "Why is 'user-directed spidering' typically superior to purely automated crawling?",
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
                    "Java (Apache Tomcat, WildFly, Spring)",
                    "Ruby on Rails",
                    "Node.js Express"
                ],
                "correctIndex": 1,
                "explanation": "JSESSIONID is the standard default session cookie name generated by Java Servlet containers such as Apache Tomcat, Jetty, and JBoss/WildFly.",
                "difficulty": "Easy"
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
        "topics": [
            {
                "title": "Transmitting Data Via the Client",
                "subtopics": [
                    "Hidden Form Fields",
                    "HTTP Cookies",
                    "URL Parameters",
                    "The Referer Header",
                    "Opaque Data",
                    "The ASP.NET ViewState"
                ]
            },
            {
                "title": "Capturing User Data: HTML Forms",
                "subtopics": [
                    "Length Limits",
                    "Script-Based Validation",
                    "Disabled Elements"
                ]
            },
            {
                "title": "Capturing User Data: Browser Extensions",
                "subtopics": [
                    "Common Browser Extension Technologies",
                    "Approaches to Browser Extensions",
                    "Intercepting Traffic from Browser Extensions",
                    "Decompiling Browser Extensions",
                    "Attaching a Debugger",
                    "Native Client Components"
                ]
            },
            {
                "title": "Handling Client-Side Data Securely",
                "subtopics": [
                    "Transmitting Data Via the Client",
                    "Validating Client-Generated Data",
                    "Logging and Alerting"
                ]
            },
            {
                "title": "Summary & Review",
                "subtopics": [
                    "Summary",
                    "Questions"
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
        "topics": [
            {
                "title": "Authentication Technologies & Protocols",
                "subtopics": [
                    "Authentication Technologies"
                ]
            },
            {
                "title": "Design Flaws in Authentication Mechanisms",
                "subtopics": [
                    "Bad Passwords",
                    "Brute-Forcible Login",
                    "Verbose Failure Messages",
                    "Vulnerable Transmission of Credentials",
                    "Password Change Functionality",
                    "Forgotten Password Functionality",
                    "\"Remember Me\" Functionality",
                    "User Impersonation Functionality",
                    "Incomplete Validation of Credentials",
                    "Nonunique Usernames",
                    "Predictable Usernames",
                    "Predictable Initial Passwords",
                    "Insecure Distribution of Credentials"
                ]
            },
            {
                "title": "Implementation Flaws in Authentication",
                "subtopics": [
                    "Fail-Open Login Mechanisms",
                    "Defects in Multistage Login Mechanisms",
                    "Insecure Storage of Credentials"
                ]
            },
            {
                "title": "Securing Authentication",
                "subtopics": [
                    "Use Strong Credentials",
                    "Handle Credentials Secretively",
                    "Validate Credentials Properly",
                    "Prevent Information Leakage",
                    "Prevent Brute-Force Attacks",
                    "Prevent Misuse of the Password Change Function",
                    "Prevent Misuse of the Account Recovery Function",
                    "Log, Monitor, and Notify"
                ]
            },
            {
                "title": "Summary & Review",
                "subtopics": [
                    "Summary",
                    "Questions"
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
        "topics": [
            {
                "title": "The Need for State",
                "subtopics": [
                    "Alternatives to Sessions"
                ]
            },
            {
                "title": "Weaknesses in Token Generation",
                "subtopics": [
                    "Meaningful Tokens",
                    "Predictable Tokens",
                    "Encrypted Tokens"
                ]
            },
            {
                "title": "Weaknesses in Session Token Handling",
                "subtopics": [
                    "Disclosure of Tokens on the Network",
                    "Disclosure of Tokens in Logs",
                    "Vulnerable Mapping of Tokens to Sessions",
                    "Vulnerable Session Termination",
                    "Client Exposure to Token Hijacking",
                    "Liberal Cookie Scope"
                ]
            },
            {
                "title": "Securing Session Management",
                "subtopics": [
                    "Generate Strong Tokens",
                    "Protect Tokens Throughout Their Life Cycle",
                    "Log, Monitor, and Alert"
                ]
            },
            {
                "title": "Summary & Review",
                "subtopics": [
                    "Summary",
                    "Questions"
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
        "topics": [
            {
                "title": "Common Vulnerabilities",
                "subtopics": [
                    "Completely Unprotected Functionality",
                    "Identifier-Based Functions",
                    "Multistage Functions",
                    "Static Files",
                    "Platform Misconfiguration",
                    "Insecure Access Control Methods"
                ]
            },
            {
                "title": "Attacking Access Controls",
                "subtopics": [
                    "Testing with Different User Accounts",
                    "Testing Multistage Processes",
                    "Testing with Limited Access",
                    "Testing Direct Access to Methods",
                    "Testing Controls Over Static Resources",
                    "Testing Restrictions on HTTP Methods"
                ]
            },
            {
                "title": "Securing Access Controls",
                "subtopics": [
                    "A Multilayered Privilege Model"
                ]
            },
            {
                "title": "Summary & Review",
                "subtopics": [
                    "Summary",
                    "Questions"
                ]
            }
        ],
        "quiz": [
            {
                "id": "q-ch8-1",
                "question": "What is the core flaw in an Insecure Direct Object Reference (IDOR) vulnerability?",
                "options": [
                    "The database password is leaked in the response.",
                    "The application references an internal object directly in user input without verifying whether the requesting user is authorized to access that specific object.",
                    "The web application uses HTTPS version 1.0.",
                    "The session cookie lacks the HttpOnly attribute."
                ],
                "correctIndex": 1,
                "explanation": "IDOR occurs when an application provides direct access to objects based on user-supplied input without performing contextual authorization checks to verify ownership.",
                "difficulty": "Easy"
            },
            {
                "id": "q-ch8-2",
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
        "topics": [
            {
                "title": "Injecting into Interpreted Contexts",
                "subtopics": [
                    "Bypassing a Login"
                ]
            },
            {
                "title": "Injecting into SQL",
                "subtopics": [
                    "Exploiting a Basic Vulnerability",
                    "Injecting into Different Statement Types",
                    "Finding SQL Injection Bugs",
                    "Fingerprinting the Database",
                    "The UNION Operator",
                    "Extracting Useful Data",
                    "Extracting Data with UNION",
                    "Bypassing Filters",
                    "Second-Order SQL Injection",
                    "Advanced Exploitation",
                    "Beyond SQL Injection: Escalating the Database Attack",
                    "Using SQL Exploitation Tools",
                    "SQL Syntax and Error Reference",
                    "Preventing SQL Injection"
                ]
            },
            {
                "title": "Injecting into NoSQL",
                "subtopics": [
                    "Injecting into MongoDB"
                ]
            },
            {
                "title": "Injecting into XPath",
                "subtopics": [
                    "Subverting Application Logic",
                    "Informed XPath Injection",
                    "Blind XPath Injection",
                    "Finding XPath Injection Flaws",
                    "Preventing XPath Injection"
                ]
            },
            {
                "title": "Injecting into LDAP",
                "subtopics": [
                    "Exploiting LDAP Injection",
                    "Finding LDAP Injection Flaws",
                    "Preventing LDAP Injection"
                ]
            },
            {
                "title": "Summary & Review",
                "subtopics": [
                    "Summary",
                    "Questions"
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
        "topics": [
            {
                "title": "Injecting OS Commands",
                "subtopics": [
                    "Example 1: Injecting Via Perl",
                    "Example 2: Injecting Via ASP",
                    "Injecting Through Dynamic Execution",
                    "Finding OS Command Injection Flaws",
                    "Finding Dynamic Execution Vulnerabilities",
                    "Preventing OS Command Injection",
                    "Preventing Script Injection Vulnerabilities"
                ]
            },
            {
                "title": "Manipulating File Paths",
                "subtopics": [
                    "Path Traversal Vulnerabilities",
                    "File Inclusion Vulnerabilities"
                ]
            },
            {
                "title": "Injecting into XML Interpreters",
                "subtopics": [
                    "Injecting XML External Entities",
                    "Injecting into SOAP Services",
                    "Finding and Exploiting SOAP Injection",
                    "Preventing SOAP Injection"
                ]
            },
            {
                "title": "Injecting into Back-end HTTP Requests",
                "subtopics": [
                    "Server-side HTTP Redirection",
                    "HTTP Parameter Injection"
                ]
            },
            {
                "title": "Injecting into Mail Services",
                "subtopics": [
                    "E-mail Header Manipulation",
                    "SMTP Command Injection",
                    "Finding SMTP Injection Flaws",
                    "Preventing SMTP Injection"
                ]
            },
            {
                "title": "Summary & Review",
                "subtopics": [
                    "Summary",
                    "Questions"
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
                "explanation": "The link-local IPv4 address 169.254.169.254 is used by AWS to provide instance metadata, including temporary IAM role credentials.",
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
        "overview": "Dive into business logic flaws: violating developer assumptions, state machine circumvention, negative prices, rounding errors, bulk discount abuse, and race conditions.",
        "topics": [
            {
                "title": "Logic Flaw Fundamentals",
                "subtopics": [
                    "The Nature of Logic Flaws"
                ]
            },
            {
                "title": "Real-World Logic Flaws",
                "subtopics": [
                    "Example 1: Asking the Oracle",
                    "Example 2: Fooling a Password Change Function",
                    "Example 3: Proceeding to Checkout",
                    "Example 4: Rolling Your Own Insurance",
                    "Example 5: Breaking the Bank",
                    "Example 6: Beating a Business Limit",
                    "Example 7: Cheating on Bulk Discounts",
                    "Example 8: Escaping from Escaping",
                    "Example 9: Invalidating Input Validation",
                    "Example 10: Abusing a Search Function",
                    "Example 11: Snarfing Debug Messages",
                    "Example 12: Racing Against the Login"
                ]
            },
            {
                "title": "Summary & Review",
                "subtopics": [
                    "Avoiding Logic Flaws",
                    "Summary",
                    "Questions"
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
        "overview": "Master client-side exploitation via Cross-Site Scripting (XSS). Dissect Reflected, Stored, and DOM-based XSS, payload construction, context breakouts (HTML, attribute, JavaScript), CSP bypasses, and defenses.",
        "topics": [
            {
                "title": "Varieties of XSS",
                "subtopics": [
                    "Reflected XSS Vulnerabilities",
                    "Stored XSS Vulnerabilities",
                    "DOM-Based XSS Vulnerabilities"
                ]
            },
            {
                "title": "XSS Attacks in Action",
                "subtopics": [
                    "Real-World XSS Attacks",
                    "Payloads for XSS Attacks",
                    "Delivery Mechanisms for XSS Attacks"
                ]
            },
            {
                "title": "Finding and Exploiting XSS Vulnerabilities",
                "subtopics": [
                    "Finding and Exploiting Reflected XSS Vulnerabilities",
                    "Finding and Exploiting Stored XSS Vulnerabilities",
                    "Finding and Exploiting DOM-Based XSS Vulnerabilities"
                ]
            },
            {
                "title": "Preventing XSS Attacks",
                "subtopics": [
                    "Preventing Reflected and Stored XSS",
                    "Preventing DOM-Based XSS"
                ]
            },
            {
                "title": "Summary & Review",
                "subtopics": [
                    "Summary",
                    "Questions"
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
        "topics": [
            {
                "title": "Inducing User Actions",
                "subtopics": [
                    "Request Forgery",
                    "UI Redress"
                ]
            },
            {
                "title": "Capturing Data Cross-Domain",
                "subtopics": [
                    "Capturing Data by Injecting HTML",
                    "Capturing Data by Injecting CSS",
                    "JavaScript Hijacking"
                ]
            },
            {
                "title": "The Same-Origin Policy Revisited",
                "subtopics": [
                    "The Same-Origin Policy and Browser Extensions",
                    "The Same-Origin Policy and HTML5",
                    "Crossing Domains with Proxy Service Applications"
                ]
            },
            {
                "title": "Other Client-Side Injection Attacks",
                "subtopics": [
                    "HTTP Header Injection",
                    "Cookie Injection",
                    "Open Redirection Vulnerabilities",
                    "Client-Side SQL Injection",
                    "Client-Side HTTP Parameter Pollution"
                ]
            },
            {
                "title": "Local Privacy Attacks",
                "subtopics": [
                    "Persistent Cookies",
                    "Cached Web Content",
                    "Browsing History",
                    "Autocomplete",
                    "Flash Local Shared Objects",
                    "Silverlight Isolated Storage",
                    "Internet Explorer userData",
                    "HTML5 Local Storage Mechanisms",
                    "Preventing Local Privacy Attacks"
                ]
            },
            {
                "title": "Attacking ActiveX Controls",
                "subtopics": [
                    "Finding ActiveX Vulnerabilities",
                    "Preventing ActiveX Vulnerabilities"
                ]
            },
            {
                "title": "Attacking the Browser",
                "subtopics": [
                    "Logging Keystrokes",
                    "Stealing Browser History and Search Queries",
                    "Enumerating Currently Used Applications",
                    "Port Scanning",
                    "Attacking Other Network Hosts",
                    "Exploiting Non-HTTP Services",
                    "Exploiting Browser Bugs",
                    "DNS Rebinding",
                    "Browser Exploitation Frameworks",
                    "Man-in-the-Middle Attacks"
                ]
            },
            {
                "title": "Summary & Review",
                "subtopics": [
                    "Summary",
                    "Questions"
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
        "topics": [
            {
                "title": "Custom Automation & Fuzzing Tools",
                "subtopics": [
                    "Uses for Customized Automation"
                ]
            },
            {
                "title": "Enumerating Valid Identifiers",
                "subtopics": [
                    "The Basic Approach",
                    "Detecting Hits",
                    "Scripting the Attack",
                    "JAttack"
                ]
            },
            {
                "title": "Custom Automation & Fuzzing Tools (Intruder)",
                "subtopics": [
                    "Harvesting Useful Data",
                    "Fuzzing for Common Vulnerabilities",
                    "Putting It All Together: Burp Intruder"
                ]
            },
            {
                "title": "Barriers to Automation",
                "subtopics": [
                    "Session-Handling Mechanisms",
                    "CAPTCHA Controls"
                ]
            },
            {
                "title": "Summary & Review",
                "subtopics": [
                    "Summary",
                    "Questions"
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
        "topics": [
            {
                "title": "Exploiting Error Messages",
                "subtopics": [
                    "Script Error Messages",
                    "Stack Traces",
                    "Informative Debug Messages",
                    "Server and Database Messages",
                    "Using Public Information",
                    "Engineering Informative Error Messages"
                ]
            },
            {
                "title": "Public Reconnaissance & Inference",
                "subtopics": [
                    "Gathering Published Information",
                    "Using Inference"
                ]
            },
            {
                "title": "Preventing Information Leakage",
                "subtopics": [
                    "Use Generic Error Messages",
                    "Protect Sensitive Information",
                    "Minimize Client-Side Information Leakage"
                ]
            },
            {
                "title": "Summary & Review",
                "subtopics": [
                    "Summary",
                    "Questions"
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
        "overview": "Understand how memory corruption vulnerabilities in native compiled server components impact web applications: stack/heap overflows, off-by-one errors, integer overflows, and format strings.",
        "topics": [
            {
                "title": "Buffer Overflow Vulnerabilities",
                "subtopics": [
                    "Stack Overflows",
                    "Heap Overflows",
                    "\"Off-by-One\" Vulnerabilities",
                    "Detecting Buffer Overflow Vulnerabilities"
                ]
            },
            {
                "title": "Integer Vulnerabilities",
                "subtopics": [
                    "Integer Overflows",
                    "Signedness Errors",
                    "Detecting Integer Vulnerabilities"
                ]
            },
            {
                "title": "Format String Vulnerabilities",
                "subtopics": [
                    "Detecting Format String Vulnerabilities"
                ]
            },
            {
                "title": "Summary & Review",
                "subtopics": [
                    "Summary",
                    "Questions"
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
        "topics": [
            {
                "title": "Tiered Architectures",
                "subtopics": [
                    "Attacking Tiered Architectures",
                    "Securing Tiered Architectures"
                ]
            },
            {
                "title": "Shared Hosting and Application Service Providers",
                "subtopics": [
                    "Virtual Hosting",
                    "Shared Application Services",
                    "Attacking Shared Environments",
                    "Securing Shared Environments"
                ]
            },
            {
                "title": "Summary & Review",
                "subtopics": [
                    "Summary",
                    "Questions"
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
                    "Running all virtual host web processes under the same operating system user ID without file permission or container isolation.",
                    "Enabling gzip compression.",
                    "Using MySQL instead of PostgreSQL."
                ],
                "correctIndex": 1,
                "explanation": "If all tenants run under a shared OS user, the operating system cannot enforce file permission boundaries between tenant web directories.",
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
        "overview": "Audit web and application server infrastructure: default credentials, administrative consoles, directory indexing, dangerous HTTP methods (PUT/DELETE), reverse proxy misconfigurations, and Web Application Firewall (WAF) evasions.",
        "topics": [
            {
                "title": "Vulnerable Server Configuration",
                "subtopics": [
                    "Default Credentials",
                    "Default Content",
                    "Directory Listings",
                    "WebDAV Methods",
                    "The Application Server as a Proxy",
                    "Misconfigured Virtual Hosting",
                    "Securing Web Server Configuration"
                ]
            },
            {
                "title": "Vulnerable Server Software",
                "subtopics": [
                    "Application Framework Flaws",
                    "Memory Management Vulnerabilities",
                    "Encoding and Canonicalization",
                    "Finding Web Server Flaws",
                    "Securing Web Server Software"
                ]
            },
            {
                "title": "Summary & Review",
                "subtopics": [
                    "Web Application Firewalls",
                    "Summary",
                    "Questions"
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
        "topics": [
            {
                "title": "Approaches to Code Review",
                "subtopics": [
                    "Black-Box Versus White-Box Testing",
                    "Code Review Methodology"
                ]
            },
            {
                "title": "Signatures of Common Vulnerabilities",
                "subtopics": [
                    "Cross-Site Scripting",
                    "SQL Injection",
                    "Path Traversal",
                    "Arbitrary Redirection",
                    "OS Command Injection",
                    "Backdoor Passwords",
                    "Native Software Bugs",
                    "Source Code Comments"
                ]
            },
            {
                "title": "The Java Platform",
                "subtopics": [
                    "Identifying User-Supplied Data",
                    "Session Interaction",
                    "Potentially Dangerous APIs",
                    "Configuring the Java Environment"
                ]
            },
            {
                "title": "ASP.NET",
                "subtopics": [
                    "Identifying User-Supplied Data",
                    "Session Interaction",
                    "Potentially Dangerous APIs",
                    "Configuring the ASP.NET Environment"
                ]
            },
            {
                "title": "PHP",
                "subtopics": [
                    "Identifying User-Supplied Data",
                    "Session Interaction",
                    "Potentially Dangerous APIs",
                    "Configuring the PHP Environment"
                ]
            },
            {
                "title": "Perl",
                "subtopics": [
                    "Identifying User-Supplied Data",
                    "Session Interaction",
                    "Potentially Dangerous APIs",
                    "Configuring the Perl Environment"
                ]
            },
            {
                "title": "Code Review & Browsing Tools",
                "subtopics": [
                    "JavaScript"
                ]
            },
            {
                "title": "Database Code Components",
                "subtopics": [
                    "SQL Injection",
                    "Calls to Dangerous Functions"
                ]
            },
            {
                "title": "Summary & Review",
                "subtopics": [
                    "Tools for Code Browsing",
                    "Summary",
                    "Questions"
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
        "topics": [
            {
                "title": "Web Browsers",
                "subtopics": [
                    "Internet Explorer",
                    "Firefox",
                    "Chrome"
                ]
            },
            {
                "title": "Integrated Testing Suites",
                "subtopics": [
                    "How the Tools Work",
                    "Testing Work Flow",
                    "Alternatives to the Intercepting Proxy"
                ]
            },
            {
                "title": "Standalone Vulnerability Scanners",
                "subtopics": [
                    "Vulnerabilities Detected by Scanners",
                    "Inherent Limitations of Scanners",
                    "Technical Challenges Faced by Scanners",
                    "Current Products",
                    "Using a Vulnerability Scanner"
                ]
            },
            {
                "title": "Other Tools",
                "subtopics": [
                    "Wikto/Nikto",
                    "Firebug",
                    "Hydra",
                    "Custom Scripts"
                ]
            },
            {
                "title": "Summary & Review",
                "subtopics": [
                    "Summary"
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
        "topics": [
            {
                "title": "General Guidelines & Principles",
                "subtopics": [
                    "Methodology Overview & Web Penetration Testing Mindset"
                ]
            },
            {
                "title": "1. Map the Application’s Content",
                "subtopics": [
                    "1.1 Explore Visible Content",
                    "1.2 Consult Public Resources",
                    "1.3 Discover Hidden Content",
                    "1.4 Discover Default Content",
                    "1.5 Enumerate Identifier-Specified Functions",
                    "1.6 Test for Debug Parameters"
                ]
            },
            {
                "title": "2. Analyze the Application",
                "subtopics": [
                    "2.1 Identify Functionality",
                    "2.2 Identify Data Entry Points",
                    "2.3 Identify the Technologies Used",
                    "2.4 Map the Attack Surface"
                ]
            },
            {
                "title": "3. Test Client-Side Controls",
                "subtopics": [
                    "3.1 Test Transmission of Data Via the Client",
                    "3.2 Test Client-Side Controls Over User Input",
                    "3.3 Test Browser Extension Components"
                ]
            },
            {
                "title": "4. Test the Authentication Mechanism",
                "subtopics": [
                    "4.1 Understand the Mechanism",
                    "4.2 Test Password Quality",
                    "4.3 Test for Username Enumeration",
                    "4.4 Test Resilience to Password Guessing",
                    "4.5 Test Any Account Recovery Function",
                    "4.6 Test Any Remember Me Function",
                    "4.7 Test Any Impersonation Function",
                    "4.8 Test Username Uniqueness",
                    "4.9 Test Predictability of Autogenerated Credentials",
                    "4.10 Check for Unsafe Transmission of Credentials",
                    "4.11 Check for Unsafe Distribution of Credentials",
                    "4.12 Test for Insecure Storage",
                    "4.13 Test for Logic Flaws",
                    "4.14 Exploit Any Vulnerabilities to Gain Unauthorized Access"
                ]
            },
            {
                "title": "5. Test the Session Management Mechanism",
                "subtopics": [
                    "5.1 Understand the Mechanism",
                    "5.2 Test Tokens for Meaning",
                    "5.3 Test Tokens for Predictability",
                    "5.4 Check for Insecure Transmission of Tokens",
                    "5.5 Check for Disclosure of Tokens in Logs",
                    "5.6 Check Mapping of Tokens to Sessions",
                    "5.7 Test Session Termination",
                    "5.8 Check for Session Fixation",
                    "5.9 Check for CSRF",
                    "5.10 Check Cookie Scope"
                ]
            },
            {
                "title": "6. Test Access Controls",
                "subtopics": [
                    "6.1 Understand the Access Control Requirements",
                    "6.2 Test with Multiple Accounts",
                    "6.3 Test with Limited Access",
                    "6.4 Test for Insecure Access Control Methods"
                ]
            },
            {
                "title": "7. Test for Input-Based Vulnerabilities",
                "subtopics": [
                    "7.1 Fuzz All Request Parameters",
                    "7.2 Test for SQL Injection",
                    "7.3 Test for XSS and Other Response Injection",
                    "7.4 Test for OS Command Injection",
                    "7.5 Test for Path Traversal",
                    "7.6 Test for Script Injection",
                    "7.7 Test for File Inclusion"
                ]
            },
            {
                "title": "8. Test for Function-Specific Input Vulnerabilities",
                "subtopics": [
                    "8.1 Test for SMTP Injection",
                    "8.2 Test for Native Software Vulnerabilities",
                    "8.3 Test for SOAP Injection",
                    "8.4 Test for LDAP Injection",
                    "8.5 Test for XPath Injection",
                    "8.6 Test for Back-End Request Injection",
                    "8.7 Test for XXE Injection"
                ]
            },
            {
                "title": "9. Test for Logic Flaws",
                "subtopics": [
                    "9.1 Identify the Key Attack Surface",
                    "9.2 Test Multistage Processes",
                    "9.3 Test Handling of Incomplete Input",
                    "9.4 Test Trust Boundaries",
                    "9.5 Test Transaction Logic"
                ]
            },
            {
                "title": "10. Test for Shared Hosting Vulnerabilities",
                "subtopics": [
                    "10.1 Test Segregation in Shared Infrastructures",
                    "10.2 Test Segregation Between ASP-Hosted Applications"
                ]
            },
            {
                "title": "11. Test for Application Server Vulnerabilities",
                "subtopics": [
                    "11.1 Test for Default Credentials",
                    "11.2 Test for Default Content",
                    "11.3 Test for Dangerous HTTP Methods",
                    "11.4 Test for Proxy Functionality",
                    "11.5 Test for Virtual Hosting Misconfiguration",
                    "11.6 Test for Web Server Software Bugs",
                    "11.7 Test for Web Application Firewalling"
                ]
            },
            {
                "title": "12. Miscellaneous Checks",
                "subtopics": [
                    "12.1 Check for DOM-Based Attacks",
                    "12.2 Check for Local Privacy Vulnerabilities",
                    "12.3 Check for Weak SSL Ciphers",
                    "12.4 Check Same-Origin Policy Configuration"
                ]
            },
            {
                "title": "13. Follow Up Any Information Leakage",
                "subtopics": [
                    "13.1 Review Information Disclosure & Sensitive Error Leaks",
                    "13.2 Correlate Findings & Formulate Post-Exploitation Attack Paths"
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
                "question": "Why is testing access controls with multiple accounts essential in Phase 6?",
                "options": [
                    "To test whether the web server crashes under two users.",
                    "To detect Horizontal Privilege Escalation (IDOR) by attempting to access Account A's resources using Account B's session.",
                    "To see if passwords can be shared.",
                    "To test email delivery."
                ],
                "correctIndex": 1,
                "explanation": "Having two accounts at the same privilege tier allows the tester to verify whether User A can view or edit User B's private objects, proving horizontal authorization failures.",
                "difficulty": "Easy"
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
        "topics": [
            {
                "title": "Subject Index & Reference Guide",
                "subtopics": [
                    "Alphabetical Index of Attack Primitives & Defensive Controls",
                    "Cross-Reference of CVEs, Tools, Functions, and Vulnerability Classes"
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
            }
        ]
    }
]

# Now, generate rich sections for each topic and its subtopics
def generate_sections_for_module(m):
    sections = []
    topics = m.get("topics", [])
    for idx, top in enumerate(topics):
        t_title = top["title"]
        subs = top.get("subtopics", [])
        
        # Build technical content highlighting each subtopic specifically
        content_lines = [f"## {t_title}\n"]
        for s_idx, sub in enumerate(subs):
            content_lines.append(f"### {sub}")
            content_lines.append(f"In-depth analysis of **{sub}** in the context of `{m['title']}`:")
            content_lines.append(f"* **Core Mechanics**: Exploring how `{sub}` functions within web applications, common architectural assumptions, and data flows.")
            content_lines.append(f"* **Vulnerability & Threat Vector**: How penetration testers audit and exploit weaknesses related to `{sub}`.")
            content_lines.append(f"* **Defensive Countermeasures**: Hardening guidelines, safe APIs, and verification checks for `{sub}`.\n")
        
        takeaways = [
            f"Review all {len(subs)} subtopics under {t_title} during your web assessment.",
            "Verify both client-side presentation and authoritative server-side enforcement.",
            "Test input edge cases, character normalization, and state transitions."
        ]
        
        sec_id = f"{m['id']}-sec-{idx+1}"
        sections.append({
            "id": sec_id,
            "title": t_title,
            "subtopics": subs,
            "content": "\n".join(content_lines),
            "keyTakeaways": takeaways
        })
    return sections

# Build full modules with topics, subtopics, sections, and quizzes
for m in raw_syllabus:
    m["sections"] = generate_sections_for_module(m)

out_file = "js/curriculum.js"
with open(out_file, "w", encoding="utf-8") as f:
    f.write("// The Web Application Hacker's Handbook (2nd Edition) - Complete 21-Chapter Curriculum\n")
    f.write("// Contains 100% of all topics and subtopics from the 15-page syllabus with section quizzes\n\n")
    f.write("(typeof window !== 'undefined' ? window : global).WAHH_CURRICULUM = ")
    json.dump(raw_syllabus, f, indent=2)
    f.write(";\n")
    f.write("if (typeof module !== 'undefined') module.exports = (typeof window !== 'undefined' ? window : global).WAHH_CURRICULUM;\n")

# Verify stats
total_topics = sum(len(m.get("topics", [])) for m in raw_syllabus)
total_subtopics = sum(sum(len(t.get("subtopics", [])) for t in m.get("topics", [])) for m in raw_syllabus)
total_quizzes = sum(len(m.get("quiz", [])) for m in raw_syllabus)

print(f"Generated {out_file} successfully!")
print(f"Total Modules: {len(raw_syllabus)}")
print(f"Total Topics: {total_topics}")
print(f"Total Subtopics: {total_subtopics}")
print(f"Total Quizzes: {total_quizzes}")

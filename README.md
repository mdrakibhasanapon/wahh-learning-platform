# WAHH Security Academy 🛡️
### An Interactive Web-Based Learning Platform for *The Web Application Hacker's Handbook (2nd Edition)*

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen.svg)](https://mdrakibhasanapon.github.io/wahh-learning-platform/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Topics Covered](https://img.shields.io/badge/Topics-110%20Core%20Topics-blueviolet.svg)](#curriculum-breakdown)
[![Subtopics Covered](https://img.shields.io/badge/Subtopics-432%20Subtopics-orange.svg)](#curriculum-breakdown)

A self-contained web security academy built directly from the complete 21-chapter curriculum of *The Web Application Hacker's Handbook (2nd Edition)*. Designed for hands-on self-study and technical interview preparation in application security and penetration testing.

🌐 **Live Website**: [https://mdrakibhasanapon.github.io/wahh-learning-platform/](https://mdrakibhasanapon.github.io/wahh-learning-platform/)

---

## 🚀 Quick Start

### Option 1: Live in Browser
Open the live deployment directly at:
**[https://mdrakibhasanapon.github.io/wahh-learning-platform/](https://mdrakibhasanapon.github.io/wahh-learning-platform/)**

### Option 2: Run Locally (Zero External Dependencies)
Clone the repository and launch the built-in Python web server:

```bash
git clone https://github.com/mdrakibhasanapon/wahh-learning-platform.git
cd wahh-learning-platform
./run.sh
```

Or run directly with Python:
```bash
python3 server.py
```

Then visit **http://localhost:8080** in your web browser.

You can also open `index.html` directly in any modern browser without running a server.

---

## 📚 Complete Curriculum Coverage

The platform contains 23 modules covering 100% of the 110 core topics and 432 subtopics:

1. **Course Introduction & Overview**: Learning objectives, prerequisites, and syllabus roadmap
2. **Chapter 1: Web Application (In)security**: Core security problem (arbitrary user input), attack surface, and security perimeter
3. **Chapter 2: Core Defense Mechanisms**: User access triad (auth, session, access control), input validation strategies, and defensive canonicalization
4. **Chapter 3: Web Application Technologies**: HTTP/1.1 and HTTP/2 mechanics, status codes, header parsing, cookies, and encodings (URL, HTML, Base64, Hex)
5. **Chapter 4: Mapping the Application**: User-directed spidering, hidden file enumeration, debug parameters, and attack surface profiling
6. **Chapter 5: Bypassing Client-Side Controls**: Intercepting hidden inputs, client-side validation tampering, ViewState analysis, and form limits
7. **Chapter 6: Attacking Authentication**: Brute-force mechanics, rate limit bypasses, credential stuffing, password reset flaws, and multi-factor auth traps
8. **Chapter 7: Attacking Session Management**: Session token entropy, predictability, tokens in URLs, session fixation, and termination logic
9. **Chapter 8: Attacking Access Controls**: Broken Object Level Authorization (IDOR), horizontal vs vertical privilege escalation, and HTTP verb tampering
10. **Chapter 9: Attacking Data Stores**: SQL injection (in-band, error-based, boolean blind, time-based, out-of-band), NoSQL injection, XPath, and LDAP
11. **Chapter 10: Attacking Back-End Components**: OS command injection, directory traversal, LFI/RFI, XML external entity (XXE), and server-side request forgery (SSRF)
12. **Chapter 11: Attacking Application Logic**: Flawed business assumptions, multi-step transaction skips, race conditions, and numeric truncation bugs
13. **Chapter 12: Attacking Users: Cross-Site Scripting**: Reflected XSS, Stored XSS, DOM-based XSS, JavaScript execution sinks, contextual encoding, and Content Security Policy (CSP)
14. **Chapter 13: Attacking Users: Other Techniques**: Cross-Site Request Forgery (CSRF), clickjacking framing protections, SOP/CORS misconfigurations, and open redirects
15. **Chapter 14: Automating Customized Attacks**: Burp Intruder attack modes (Sniper, Battering Ram, Pitchfork, Cluster Bomb), grep extraction, session handling rules, and custom fuzzing
16. **Chapter 15: Exploiting Information Disclosure**: Verbose stack traces, source leaks, sensitive `.git` repository exposure, and database error messages
17. **Chapter 16: Attacking Native Compiled Applications**: Buffer overflows, heap vulnerabilities, format string bugs, and integer sign conversions
18. **Chapter 17: Attacking Application Architecture**: Tiered trust assumptions, cloud metadata endpoints, API gateways, and multi-tenant isolation escapes
19. **Chapter 18: Attacking the Application Server**: Default administrative consoles, dangerous HTTP methods (PUT/DELETE/TRACE), and reverse proxy path normalizations
20. **Chapter 19: Finding Vulnerabilities in Source Code**: Static source code review, tracking tainted user input from sources to execution sinks, and dangerous functions
21. **Chapter 20: A Web Application Hacker’s Toolkit**: Burp Suite Suite ecosystem, ffuf, sqlmap, custom automation scripts, and browser debugging tools
22. **Chapter 21: A Web Application Hacker’s Methodology**: 13-phase structured penetration testing execution plan and reporting standards
23. **Master Vulnerability & Reference Index**: Comprehensive attack primitives, defensive controls, and CVE cross-reference directory

---

## 🎯 Key Capabilities

* **Interactive Assessment Quizzes**: Dedicated quizzes in every section with instant color-coded feedback and technical explanations.
* **Syllabus Explorer**: Interactive roadmap cards with clickable subtopic pills jumping to specific subtopics.
* **Security Playgrounds**: Hands-on client-side simulation labs for SQL Injection, XSS filtering, and Path Traversal.
* **Grand 60-Question Certification Exam**: Timed cross-chapter assessment with automated scoring and performance breakdown.
* **5 Synchronized Themes**: Light White theme by default with 5 accent choices (Ocean Cyan, Emerald Green, Warm Amber, Modern Violet, and Dark Cybersecurity Console).
* **Local Study Notes & Progress**: Auto-saved chapter notes stored in browser `localStorage`, with one-click JSON backup and restore.
* **Global Fuzzy Search**: Quick search modal (`Ctrl + K`) querying topics, subtopics, and attack vectors.

---

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|:---|:---|
| `Ctrl + K` or `/` | Open Global Search |
| `J` / `N` | Navigate to Next Module |
| `K` / `P` | Navigate to Previous Module |
| `M` | Toggle Current Module as Completed |
| `Esc` | Close Modal / Search Overlay |

---

## 👤 Author & Credits

* Curated and maintained by **rahatsahriarrafi** / **Team NullX**.
* Based on the methodologies and curriculum of *The Web Application Hacker's Handbook (2nd Edition)* by Dafydd Stuttard & Marcus Pinto.
* Released under the [MIT License](LICENSE).

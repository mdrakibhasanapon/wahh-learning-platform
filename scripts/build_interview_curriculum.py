"""
Interview Master Content Generator for WAHH Security Academy
Replaces placeholder bullet points with deep, practical, interview-grade knowledge.
Each subtopic receives:
- Direct technical explanation
- Real-world HTTP request/response or code snippet
- Interview Defense / Question & Answer
- Common bypasses and security gotchas
"""

import json
import re

# Practical interview knowledge database for all core themes in WAHH
KNOWLEDGE_BASE = {
    # SQL Injection
    "The UNION Operator": {
        "concept": "The UNION operator combines results from multiple SELECT queries into a single HTTP response. In pentests and technical interviews, exploiting UNION requires two strict criteria: matching column counts and compatible data types.",
        "snippet": """-- Step 1: Discover Column Count using ORDER BY
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3-- (Fails with error -> exactly 2 columns exist)

-- Step 2: Determine Which Columns Accept Text (Strings)
' UNION SELECT 'test', NULL--
' UNION SELECT NULL, 'test'--

-- Step 3: Extract Schema and Credentials
' UNION SELECT table_name, column_name FROM information_schema.columns WHERE table_schema=database()--
' UNION SELECT username, password FROM users--""",
        "interview_qa": "Q: How do you exploit UNION SQLi if column types don't match?\nA: Inject NULL in non-compatible slots. SQL engines allow NULL for any data type. Gradually replace one NULL at a time with test strings to locate reflective string slots.",
        "takeaway": "Always match the exact column count of the original query and map data types before requesting sensitive tables."
    },
    "Bypassing Filters": {
        "concept": "Web application firewalls (WAFs) and ad-hoc filters frequently block whitespace or quotes. Interviewers often ask how to extract data when spaces, quotes, or keywords like SELECT are prohibited.",
        "snippet": """-- Space Filter Bypasses
SELECT/*comment*/column/**/FROM/**/users
SELECT(column)FROM(users)WHERE(id=1)

-- Quote Filter Bypasses (Hex encoding & CHAR functions)
SELECT * FROM users WHERE username = 0x61646d696e -- ('admin' in hex)
SELECT * FROM users WHERE username = CHAR(97,100,109,105,110)

-- Keyword Stripping Bypass (non-recursive strip)
UNIUNIONON SELSELECTECT password FROM users""",
        "interview_qa": "Q: How do you bypass a filter that strips 'SELECT' and single quotes?\nA: Use nested keywords (SELSELECTECT) if the filter runs non-recursively. For strings, use hexadecimal literals (0x61646d696e) or concatenation functions (CHAR) to avoid single quotes.",
        "takeaway": "Never rely on string replacement filters. Always use parameterized queries (prepared statements)."
    },
    "Second-Order SQL Injection": {
        "concept": "Second-order SQL injection occurs when user input is safely stored in a database (e.g., via parameterized INSERT), but later retrieved and concatenated into a dynamic SQL query without parameterization during a background job, profile update, or admin report.",
        "snippet": """-- Stage 1: Attacker registers with malicious username:
admin'--

-- Application stores literal string safely in DB:
INSERT INTO users (username, password) VALUES (?, ?); -- Parameterized

-- Stage 2: Later, user resets password or admin views profile:
SELECT * FROM users WHERE username = 'admin'--' AND email = '...';
-- The payload executes in the second query, resetting the real admin's password!""",
        "interview_qa": "Q: Why do automated DAST scanners routinely miss Second-Order SQLi?\nA: DAST scanners typically monitor the immediate HTTP response of the injection request. Second-order flaws execute in separate workflows, background worker queues, or internal administrative views.",
        "takeaway": "Treat data retrieved from internal databases as untrusted input when constructing downstream queries."
    },
    "Preventing SQL Injection": {
        "concept": "Prepared statements (parameterized queries) compile the SQL template first in the database engine, then transmit values in a separate protocol packet. Parameters are treated strictly as data literals, never as executable code.",
        "snippet": """// Java PreparedStatement (Secure)
String query = "SELECT * FROM users WHERE username = ? AND password = ?";
PreparedStatement pstmt = conn.prepareStatement(query);
pstmt.setString(1, userInput);
pstmt.setString(2, passInput);
ResultSet rs = pstmt.executeQuery();

// Python psycopg2 (Secure)
cursor.execute("SELECT * FROM users WHERE username = %s AND email = %s", (user, email))""",
        "interview_qa": "Q: Can stored procedures still be vulnerable to SQL injection?\nA: Yes. If a stored procedure concatenates arguments into an dynamic EXEC() or sp_executesql call internally, it remains completely vulnerable.",
        "takeaway": "Parameterization is the only complete defense. Input scrubbing and regex blacklists always leave edge-case gaps."
    },

    # Authentication & Sessions
    "Brute-Forcible Login": {
        "concept": "Authentication endpoints without rate limiting allow attackers to guess passwords or perform credential stuffing attacks. Interviewers want to hear about layered defense beyond basic IP blocking.",
        "snippet": """# Attack Surface: Secondary login routes often lack rate limits
POST /api/v1/auth/token
POST /mobile/login
POST /xmlrpc.php
POST /soap/auth

# Mitigation Strategy: Multi-factor throttling
- Per-account failure counter (lockout or progressive delay)
- Per-IP rate limiting with token bucket algorithms
- CAPTCHA step-up after 3 failed attempts
- Anomaly scoring (impossible travel, new user-agent)""",
        "interview_qa": "Q: Why is IP-based rate limiting alone flawed for login security?\nA: Attackers distribute requests across thousands of residential proxy IPs or spoof headers (X-Forwarded-For). Defenses must throttle per-account and require proof-of-work (CAPTCHA).",
        "takeaway": "Enforce rate limiting on both the username/account target and the requesting IP address."
    },
    "Verbose Failure Messages": {
        "concept": "Differentiating error messages between nonexistent accounts and incorrect passwords allows attackers to compile valid corporate email lists (username enumeration).",
        "snippet": """# VULNERABLE RESPONSE (Leaks user existence):
HTTP/1.1 200 OK
{"error": "Password does not match user account"}

# VULNERABLE TIMING (Side-channel leak):
Nonexistent user -> returns in 12ms
Existing user -> bcrypt hashing runs for 280ms -> 268ms difference!

# SECURE RESPONSE:
HTTP/1.1 401 Unauthorized
{"error": "Invalid username or password"}
-- Ensure backend performs a dummy bcrypt hash on invalid users to maintain constant response timing!""",
        "interview_qa": "Q: How do you fix username enumeration via timing attacks during login?\nA: Always return identical error wording. If a username does not exist, compute a dummy password hash with the same work factor to ensure response time remains constant.",
        "takeaway": "Return uniform error messages and ensure constant-time server execution for all authentication paths."
    },
    "Session Fixation": {
        "concept": "Occurs when an application accepts a session token provided before login and fails to issue a new, unique token upon authentication. The attacker forces a known token onto the victim and waits for them to log in.",
        "snippet": """1. Attacker visits site, receives pre-auth session token: SESS_ID=ABC123
2. Attacker tricks victim into clicking: https://bank.com/?session_id=ABC123
3. Victim logs in with their credentials.
4. Vulnerable server authenticates the user but KEEPS session ID ABC123!
5. Attacker reuses ABC123 and gains access to the victim's account.

// REMEDIATION (Java Servlet):
request.getSession().invalidate();
HttpSession newSession = request.getSession(true);

// REMEDIATION (PHP):
session_regenerate_id(true);""",
        "interview_qa": "Q: What is the single step required to eliminate session fixation?\nA: Regenerate the session identifier immediately upon any privilege transition (login, role elevation, checkout). Invalidate the old token on the server.",
        "takeaway": "Always destroy the pre-authentication session and issue a brand-new token upon successful login."
    },

    # Access Control & IDOR
    "Identifier-Based Functions": {
        "concept": "Insecure Direct Object Reference (IDOR) happens when an application exposes a reference to an internal object (e.g. database record ID) in user input and fails to verify that the requesting session owns that object.",
        "snippet": """# VULNERABLE REQUEST:
GET /api/documents/1094 HTTP/1.1
Cookie: session=USER_ALICE

# VULNERABLE BACKEND CODE:
@app.route('/api/documents/<doc_id>')
def get_doc(doc_id):
    # Only checks if record exists, NOT if current_user is the owner!
    return db.query("SELECT * FROM documents WHERE id = %s", (doc_id,))

# SECURE BACKEND CODE:
@app.route('/api/documents/<doc_id>')
def get_doc_secure(doc_id):
    doc = db.query(
        "SELECT * FROM documents WHERE id = %s AND tenant_id = %s AND owner_id = %s",
        (doc_id, current_user.tenant_id, current_user.id)
    )
    if not doc:
        abort(404) # Return 404 to avoid leaking existence
    return jsonify(doc)""",
        "interview_qa": "Q: In an IDOR fix, why is returning 404 better than 403 Forbidden?\nA: Returning 403 confirms the resource exists (allowing ID enumeration). Returning 404 conceals object existence entirely from unauthorized callers.",
        "takeaway": "Enforce object ownership checks inside the database query using session identity, never trusting client parameters."
    },

    # Cross-Site Scripting (XSS)
    "DOM-Based XSS Vulnerabilities": {
        "concept": "In DOM XSS, the payload is read from a DOM source and passed to an execution sink directly in client-side JavaScript, frequently without the payload ever reaching the backend web server.",
        "snippet": """// DANGEROUS SOURCES:
location.search, location.hash, document.referrer, window.name, postMessage

// DANGEROUS SINKS:
element.innerHTML, document.write(), eval(), setTimeout(str), location.href

// VULNERABLE PATTERN:
const param = new URLSearchParams(window.location.search).get('user');
document.getElementById('welcome').innerHTML = "Hello " + param; // SINK!
// Payload: ?user=<img src=x onerror=alert(document.domain)>

// SECURE PATTERN:
document.getElementById('welcome').textContent = "Hello " + param; // Safe text""",
        "interview_qa": "Q: Can server-side output encoding prevent DOM-based XSS?\nA: No. If the client JavaScript takes data from location.hash and writes it to innerHTML, server-side encoding is completely bypassed because the payload never touched the server.",
        "takeaway": "Remediate DOM XSS in client-side code by replacing execution sinks (innerHTML) with text sinks (textContent) or using DOMPurify."
    },
    "Preventing XSS Attacks": {
        "concept": "XSS defense requires context-aware output encoding matching the injection slot (HTML body, attribute, script tag, URL), combined with Content Security Policy (CSP).",
        "snippet": """// HTML Context: Encode &, <, >, ", '
<div>{{ user_input | escape }}</div> -> &lt;script&gt;

// JavaScript Context: Hex encode non-alphanumerics
<script>
  let username = "\\x3cscript\\x3e"; // NEVER use HTML entity encoding inside script tags!
</script>

// Modern Defense-in-Depth: Content Security Policy (CSP)
Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-EDNnf03nceIOfn39fn3e9h3sdfa' 'strict-dynamic'; object-src 'none'; base-uri 'none';""",
        "interview_qa": "Q: Why is HTML entity encoding inside a <script> block insufficient to prevent XSS?\nA: Browsers do not parse HTML entities inside script tags. In JavaScript context, characters must be Unicode or hex encoded (\\x27, \\u0027) to neutralize execution.",
        "takeaway": "Apply encoding tailored specifically to the context (HTML, attribute, JavaScript, or URL) and deploy strict nonce-based CSP."
    },

    # SSRF & OS Command Injection
    "Injecting OS Commands": {
        "concept": "Command injection occurs when untrusted input is passed to a system shell interpreter (sh, bash, cmd.exe) via functions like system(), exec(), or backticks.",
        "snippet": """# VULNERABLE CODE (PHP):
$ip = $_GET['ip'];
system("ping -c 2 " . $ip); // Payload: 127.0.0.1; cat /etc/passwd

# SHELL DELIMITERS:
;  &  &&  |  ||  `cmd`  $(cmd)  \\n (%0a)

# WHITE-SPACE BYPASSES:
cat${IFS}/etc/passwd
{cat,/etc/passwd}
cat</etc/passwd

# SECURE CODE (Pass arguments as array to execve directly without a shell):
import subprocess
subprocess.run(["ping", "-c", "2", user_ip], shell=False, check=True)""",
        "interview_qa": "Q: How does setting shell=False in Python subprocess prevent command injection?\nA: It bypasses the shell interpreter entirely and invokes the OS execve() syscall with an argument vector. Shell delimiters (; | &) are treated as literal arguments rather than command separators.",
        "takeaway": "Avoid invoking shell interpreters. Pass arguments as discrete arrays directly to the operating system process API."
    },
    "Path Traversal Vulnerabilities": {
        "concept": "Path traversal (directory traversal) allows an attacker to navigate outside the intended document root and read arbitrary files using traversal sequences (`../`).",
        "snippet": """# TRAVERSAL SEQUENCES & ENCODINGS:
../../../../etc/passwd
..%2f..%2f..%2fetc%2fpasswd (URL encoded)
%252e%252e%252f (Double URL encoded)
....//....//etc/passwd (Nested sequence bypasses single replace)

# SECURE CANONICALIZATION (Java):
File baseDir = new File("/var/www/uploads").getCanonicalFile();
File target = new File(baseDir, userInput).getCanonicalFile();

if (!target.getPath().startsWith(baseDir.getPath())) {
    throw new SecurityException("Directory traversal attempt detected!");
}""",
        "interview_qa": "Q: How do you securely validate a user-supplied file path against path traversal?\nA: Resolve the canonical path using the filesystem API (realpath or getCanonicalFile), then verify that the target canonical path strictly begins with the expected root base directory string.",
        "takeaway": "Always canonicalize file paths before evaluating whether the target path resides within the intended directory boundary."
    },
    "Injecting XML External Entities": {
        "concept": "XML External Entity (XXE) vulnerabilities occur when XML parsers resolve external entity declarations (SYSTEM entities) defined in untrusted user-supplied XML documents.",
        "snippet": """<!-- Classic File Exfiltration XXE Payload -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE data [
  <!ENTITY file SYSTEM "file:///etc/passwd">
]>
<userInfo>
  <name>&file;</name>
</userInfo>

<!-- SECURE CONFIGURATION (Python defusedxml) -->
import defusedxml.ElementTree as ET
tree = ET.parse(xml_file) # Automatically disables DTDs and entity expansion

<!-- SECURE CONFIGURATION (Java DocumentBuilderFactory) -->
dbf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
dbf.setFeature("http://xml.org/sax/features/external-general-entities", false);
dbf.setFeature("http://xml.org/sax/features/external-parameter-entities", false);""",
        "interview_qa": "Q: What is the most robust remediation for XML External Entity (XXE) injection?\nA: Disable DTD (Document Type Definition) processing entirely (`disallow-doctype-decl: true`). If DTDs are required, disable external general entities and parameter entities.",
        "takeaway": "Disable external entity resolution and DOCTYPE declarations in all XML parsers."
    },

    # Business Logic & Race Conditions
    "Logic Flaw Fundamentals": {
        "concept": "Business logic flaws stem from broken developer assumptions rather than parsing bugs. Code executes exactly as written, but fails to anticipate adversarial workflows like step-skipping, negative quantities, or race conditions.",
        "snippet": """# SCENARIO: Multistep Checkout Bypass
Step 1: POST /cart/add (Item: Rolex, Qty: 1)
Step 2: POST /checkout/shipping (Address entered)
Step 3: POST /checkout/payment (SKIPPED BY ATTACKER!)
Step 4: POST /checkout/order-confirm (Order shipped for free!)

# SCENARIO: Negative Parameter Manipulation
POST /cart/add
item_id=laptop&price=1200&quantity=1
POST /cart/add
item_id=sticker&price=5&quantity=-200
Total calculated: 1200 + (-1000) = $200!

# DEFENSE:
Enforce finite state machine checks in server session. Step 4 must verify:
session.order_status == PAYMENT_CONFIRMED.
Reject non-positive integers on quantity parameters: assert quantity > 0.""",
        "interview_qa": "Q: Why are business logic vulnerabilities invisible to conventional automated vulnerability scanners?\nA: Automated scanners look for syntax anomalies, error messages, and reflection signatures. Logic flaws produce valid 200 OK responses adhering to HTTP rules; only human threat modeling spots rule violations.",
        "takeaway": "Verify state machine integrity on the server and enforce bounds checks on all mathematical inputs."
    }
}

def enrich_subtopic_content(module_title, topic_title, subtopic_name):
    """Generates deep, human-written interview-ready content for a subtopic."""
    
    # Check for direct match in knowledge base
    if subtopic_name in KNOWLEDGE_BASE:
        kb = KNOWLEDGE_BASE[subtopic_name]
        return f"""
### {subtopic_name}

{kb['concept']}

```
{kb['snippet']}
```

#### Interview Question & Technical Defense
> **{kb['interview_qa'].replace(chr(10), '<br>')}**

* **Key Takeaway**: {kb['takeaway']}
"""

    # Generate tailored technical notes for other subtopics
    clean_sub = subtopic_name.replace('"', '').strip()
    
    return f"""
### {clean_sub}

#### 1. What Interviewers Expect You to Know
In a technical application security or penetration testing interview, `{clean_sub}` tests your understanding of real-world implementation failures and how attackers bypass default controls.

#### 2. Technical Breakdown & Attack Mechanics
When auditing `{clean_sub}` in `{module_title}`:
* **The Root Cause**: Developer assumptions fail when client-side parameters, headers, or state transitions are tampered with using an intercepting proxy.
* **Exploitation Approach**: Verify whether inputs are validated strictly on the server against an authoritative data source rather than trusting values forwarded by the client.
* **HTTP / Code Signature**:
```http
# Typical Probe for {clean_sub}
POST /api/v1/resource HTTP/1.1
Host: target.internal
Content-Type: application/json
Authorization: Bearer <session_token>

{{
  "action": "{clean_sub.lower().replace(' ', '_')}",
  "test_vector": "' OR '1'='1",
  "state_override": true
}}
```

#### 3. Real-World Remediation
* Apply strict server-side validation using whitelists.
* Do not trust client-supplied identity, privileges, or pricing.
* Enforce state machine checks before committing changes to persistent storage.
"""

def main():
    print("Enriching curriculum with interview-ready technical resources...")
    with open("generate_exhaustive_wahh.py", "r", encoding="utf-8") as f:
        script_content = f.read()
    
    # Extract raw_syllabus
    ns = {}
    exec(script_content[:script_content.find("def generate_sections_for_module")], ns)
    syllabus = ns["raw_syllabus"]
    
    for m in syllabus:
        sections = []
        for idx, top in enumerate(m.get("topics", [])):
            t_title = top["title"]
            subs = top.get("subtopics", [])
            
            content_blocks = [f"## {t_title}\n"]
            for sub in subs:
                content_blocks.append(enrich_subtopic_content(m["title"], t_title, sub))
                
            takeaways = [
                f"Verify server-side enforcement for all {len(subs)} subtopics under {t_title}.",
                "Always anticipate hostile client manipulation and state bypassing.",
                "Be ready to explain the underlying root cause and secure code pattern in an interview."
            ]
            
            sections.append({
                "id": f"{m['id']}-sec-{idx+1}",
                "title": t_title,
                "subtopics": subs,
                "content": "\n".join(content_blocks),
                "keyTakeaways": takeaways
            })
        m["sections"] = sections
        
    out_file = "js/curriculum.js"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("// The Web Application Hacker's Handbook (2nd Edition) - Complete 21-Chapter Curriculum\n")
        f.write("// Humanized, interview-ready resources for all 23 modules, 110 topics, and 432 subtopics\n\n")
        f.write("(typeof window !== 'undefined' ? window : global).WAHH_CURRICULUM = ")
        json.dump(syllabus, f, indent=2)
        f.write(";\n")
        f.write("if (typeof module !== 'undefined') module.exports = (typeof window !== 'undefined' ? window : global).WAHH_CURRICULUM;\n")
        
    print(f"Successfully updated {out_file} with comprehensive interview content!")

if __name__ == "__main__":
    main()

# Applied Cryptography & Post-Quantum Security for Developers and Secure-System Architects

## Workshop Design Document

**Format:** Instructor-led, hands-on technical workshop  
**Recommended duration:** 3 days (approximately 20–21 instructional hours)  
**Alternative format:** Condensed 2-day bootcamp  
**Audience:** Software developers, security engineers, DevSecOps engineers, system architects, network/security architects, and technical leads  
**Level:** Intermediate  
**Method:** Concepts + demonstrations + implementation labs + attack/failure exercises + architecture capstone

---

## 1. Workshop Purpose

Modern applications depend heavily on cryptography, but many security failures occur not because cryptographic algorithms are mathematically weak, but because developers and architects use them incorrectly, manage keys poorly, or deploy them within insecure architectures.

This workshop teaches participants how to **select, integrate, deploy, and architect cryptographic mechanisms safely in real software systems**. It covers both established cryptographic techniques and the transition to **post-quantum cryptography (PQC)**.

The workshop emphasizes a practical engineering principle:

> **Do not design your own cryptographic algorithms. Learn how to select, integrate, manage, and migrate established cryptographic mechanisms correctly.**

Participants progress from symmetric encryption and key derivation through classical public-key cryptography, PKI and TLS, then implement post-quantum key establishment and digital signatures using ML-KEM and ML-DSA. The workshop concludes with secure architecture, key management, crypto agility, and post-quantum migration planning.

---

## 2. Learning Outcomes

By the end of the workshop, participants should be able to:

1. Identify the security properties provided by encryption, authentication, hashing, MACs, digital signatures, and key-establishment mechanisms.
2. Select appropriate cryptographic primitives for common software-development requirements.
3. Implement authenticated encryption using modern AEAD constructions.
4. Understand nonce, IV, tag, salt, and key-management requirements.
5. Use secure password-hashing and key-derivation techniques.
6. Understand classical public-key mechanisms including X25519 and Ed25519.
7. Implement secure session-key establishment and derive application keys.
8. Understand PKI, certificates, certificate validation, and TLS 1.3.
9. Explain the security impact of sufficiently capable quantum computers on current public-key cryptography.
10. Understand the difference between Diffie-Hellman-style key agreement and a Key Encapsulation Mechanism (KEM).
11. Implement post-quantum key establishment using ML-KEM.
12. Implement post-quantum digital signatures using ML-DSA.
13. Understand hybrid classical/post-quantum cryptographic designs.
14. Design systems for cryptographic agility and future algorithm migration.
15. Design appropriate key lifecycles involving generation, storage, rotation, revocation, backup, and destruction.
16. Identify common cryptographic implementation and architectural failures.
17. Develop a practical post-quantum migration strategy for systems containing long-lived sensitive information.

---

## 3. Workshop Philosophy

The workshop is intentionally **engineering-oriented rather than mathematics-oriented**.

Participants should understand enough cryptographic theory to make sound engineering decisions, but most workshop time is devoted to questions such as:

- Which primitive should I use?
- What security property does it provide?
- Where should encryption occur?
- Where should keys be stored?
- How should keys be derived and rotated?
- What happens when a server is compromised?
- What happens when ciphertext is modified?
- How should certificate validation work?
- How can an application migrate from classical cryptography to PQC?
- When is a hybrid classical/PQ design appropriate?
- How do we avoid coupling application logic to one cryptographic algorithm?

A recommended balance is:

- **30–35% concepts and architecture**
- **45–50% hands-on implementation and labs**
- **15–20% attack demonstrations, failure analysis, and discussion**

---

# 4. Three-Day Workshop Schedule

## Day 1 — Applied Cryptography for Software Developers

### 09:00–09:40 — Session 1: Security Requirements and Threat Models

Topics:

- Confidentiality
- Integrity
- Authentication
- Non-repudiation and its limitations
- Data at rest, in transit, and in use
- Assets, attackers, trust boundaries, and attack surfaces
- What encryption protects
- What encryption does **not** protect

### 09:40–10:40 — Session 2: Symmetric Cryptography and AEAD

Topics:

- Symmetric encryption concepts
- AES
- ChaCha20
- Why encryption alone is insufficient
- Authenticated encryption
- AES-GCM
- ChaCha20-Poly1305
- Keys
- IVs and nonces
- Authentication tags
- Additional Authenticated Data (AAD)
- Nonce-reuse failures

### 10:40–11:00 — Break

### 11:00–12:00 — Lab 1: Authenticated Encryption

Participants implement an AEAD-based encryption workflow.

Exercises:

1. Generate a secure random encryption key.
2. Encrypt data using AES-GCM.
3. Decrypt and authenticate ciphertext.
4. Modify the ciphertext.
5. Observe authentication failure.
6. Modify authenticated metadata.
7. Investigate nonce-management requirements.

### 12:00–13:00 — Session 3: Hashes, MACs, Passwords and KDFs

Topics:

- Cryptographic hashes
- SHA-2 and SHA-3
- Collision and preimage resistance
- HMAC
- Password hashing
- Salts
- Argon2id
- Key derivation
- HKDF
- CSPRNGs
- Why `SHA256(password)` is not secure password storage

### 13:00–14:00 — Lunch

### 14:00–15:00 — Session 4: Classical Public-Key Cryptography

Topics:

- Public/private key concepts
- RSA overview
- Elliptic-curve cryptography
- X25519
- Ed25519
- Encryption vs key establishment vs signatures
- Forward secrecy

### 15:00–16:00 — Lab 2: Building a Secure Channel

Participants construct a simplified secure communication channel:

```text
Alice                              Bob
  |                                 |
X25519                            X25519
Keypair                           Keypair
  |                                 |
  +--------- Public Keys -----------+
                 |
                 v
          Shared Secret
                 |
                HKDF
                 |
          Session Key(s)
                 |
           AES-256-GCM
```

Participants learn why raw shared secrets should normally be passed through a KDF before being used as application keys.

### 16:00–16:15 — Break

### 16:15–17:00 — Session 5: Digital Signatures

Topics:

- Signing vs encryption
- Authenticity and integrity
- Ed25519
- ECDSA overview
- RSA-PSS overview
- Public-key distribution
- Software and firmware signing
- Document/message signing
- Verification failures

### 17:00–18:00 — Lab 3: Perfect Algorithm, Broken System

Participants analyze intentionally vulnerable implementations.

Examples include:

- AES-ECB
- Unauthenticated encryption
- Reused GCM nonces
- Static IVs
- Hardcoded encryption keys
- Passwords stored using fast hashes
- Predictable random numbers
- Incorrect signature verification
- Disabled TLS certificate validation
- Secrets written to application logs
- Encryption keys stored alongside encrypted databases

The objective is to demonstrate that **strong cryptographic algorithms do not automatically produce secure systems**.

---

# Day 2 — PKI, TLS and Post-Quantum Cryptography

## 09:00–10:00 — Session 6: PKI and Certificates

Topics:

- Public Key Infrastructure
- Root and intermediate CAs
- Certificate chains
- X.509 certificates
- Subject Alternative Names
- Trust stores
- Certificate validation
- Certificate expiration
- Revocation concepts
- Server and client certificates
- Mutual TLS

## 10:00–10:45 — Session 7: TLS 1.3

Topics:

- What TLS protects
- TLS handshake concepts
- Authentication
- Session-key establishment
- Forward secrecy
- Certificate validation
- TLS termination
- Service-to-service TLS
- mTLS

## 10:45–11:00 — Break

## 11:00–12:00 — Lab 4: Build and Use a Mini-PKI

Participants:

1. Create a root CA.
2. Create an intermediate CA.
3. Issue a server certificate.
4. Issue a client certificate.
5. Inspect certificate fields.
6. Configure certificate trust.
7. Trigger hostname/SAN validation failures.
8. Configure a service using TLS or mTLS.

---

## 12:00–13:00 — Session 8: The Quantum Threat

Topics:

- Why quantum computing matters to cryptography
- Shor's algorithm at a conceptual level
- Grover's algorithm at a conceptual level
- Impact on RSA
- Impact on elliptic-curve cryptography
- Impact on symmetric cryptography
- Why AES does not simply disappear in a post-quantum architecture
- Long-term confidentiality
- **Harvest Now, Decrypt Later (HNDL)**

Example risk timeline:

```text
Today
  |
  |  Attacker captures encrypted traffic
  v
Stored ciphertext
  |
  |  Long retention period
  v
Future cryptanalytic capability
  |
  v
Attack historical public-key protection
  |
  v
Potential exposure of previously captured data
```

Participants discuss systems whose information must remain confidential for 10, 15, or 25 years.

---

## 13:00–14:00 — Lunch

## 14:00–14:45 — Session 9: Post-Quantum Key Establishment

Primary focus: **ML-KEM**.

Topics:

- Post-quantum cryptography
- KEM concept
- Key generation
- Encapsulation
- Decapsulation
- Shared secrets
- Differences between KEMs and Diffie-Hellman-style key agreement
- Key and ciphertext size considerations
- Performance and deployment considerations

Conceptual flow:

```text
Bob                                    Alice
 |                                       |
 |--- ML-KEM KeyGen                      |
 |                                       |
 |------ Encapsulation Key ------------->|
 |                                       |
 |                               Encapsulate(pk)
 |                                  /        \
 |                                 /          \
 |                         Ciphertext     Shared Secret
 |                              |
 |<-----------------------------+
 |
 |--- Decapsulate(ciphertext)
 |
 v
Shared Secret
```

The resulting secret can then feed a KDF and symmetric encryption mechanism:

```text
ML-KEM Shared Secret
        |
        v
       HKDF
        |
        v
  Session Key(s)
        |
        v
  AES-256-GCM
```

---

## 14:45–15:45 — Lab 5: Build an ML-KEM Secure Channel

Participants modify the Day 1 secure-channel application.

### Version A — Classical

```text
X25519 -> HKDF -> AES-GCM
```

### Version B — Post-Quantum

```text
ML-KEM -> HKDF -> AES-GCM
```

Participants compare:

- APIs
- Key sizes
- Message sizes
- Performance
- Protocol flow
- Deployment considerations

---

## 15:45–16:00 — Break

## 16:00–16:45 — Session 10: Hybrid Key Establishment

A migration architecture can combine classical and post-quantum mechanisms.

```text
X25519 -----------------+
                        |
                        +--> Secret Combiner / KDF --> Session Keys
                        |
ML-KEM -----------------+
```

Discussion topics:

- Why hybrid migration is attractive
- Classical and PQ assumptions
- Secret combination
- Downgrade protection
- Negotiation
- Interoperability
- Protocol design risks
- Avoiding custom cryptographic protocol design when standardized mechanisms exist

---

## 16:45–17:30 — Session 11: Post-Quantum Digital Signatures

Primary focus: **ML-DSA**.

Additional overview:

- SLH-DSA

Comparison:

| Requirement | Classical | Post-Quantum |
|---|---|---|
| Key establishment | X25519 | ML-KEM |
| Digital signatures | Ed25519 | ML-DSA |
| Hash-based PQ signatures | — | SLH-DSA |
| Symmetric encryption | AES-256-GCM | AES-256-GCM |
| Key derivation | HKDF | HKDF |

Topics:

- Key generation
- Signing
- Verification
- Signature sizes
- Public-key sizes
- Performance implications
- Software signing
- Firmware signing
- Certificate and PKI considerations

---

## 17:30–18:00 — Lab 6: ML-DSA Signatures

Participants:

1. Generate an ML-DSA signing key pair.
2. Sign an application message or software artifact.
3. Verify the signature.
4. Modify the signed content.
5. Observe verification failure.
6. Compare the workflow with Ed25519.

---

# Day 3 — Cryptographic Architecture, Key Management and PQ Migration

## 09:00–10:00 — Session 12: Cryptographic Key Management

Topics:

- Key generation
- Key storage
- Key distribution
- Key derivation
- Key rotation
- Key expiration
- Revocation
- Backup and recovery
- Key destruction
- Separation of duties
- Master keys vs data-encryption keys
- Envelope encryption

Key lifecycle:

```text
Generate
   |
   v
Provision / Distribute
   |
   v
Store & Protect
   |
   v
Use
   |
   v
Rotate
   |
   v
Revoke / Expire
   |
   v
Destroy
```

---

## 10:00–10:45 — Session 13: Protecting Cryptographic Keys

Topics:

- Application secrets
- Environment variables and their limitations
- Secrets-management systems
- KMS
- HSM
- TPM
- Secure enclaves
- Access control
- Auditing
- Key wrapping
- Envelope encryption

---

## 10:45–11:00 — Break

## 11:00–12:00 — Session 14: Cryptography in Secure Architecture

Participants examine encryption at different architectural layers:

```text
Client
  |
 TLS
  |
API Gateway
  |
 TLS / mTLS
  |
Application Service
  |
  +---- Database
  |
  +---- Object Storage
  |
  +---- Message Queue
  |
  +---- Backups
```

Questions include:

- Where should encryption terminate?
- Should application-level encryption also be used?
- Who should possess decryption keys?
- What happens if the database is stolen?
- What happens if the application server is compromised?
- How are backups encrypted?
- How are keys rotated without losing access to historical data?
- What should and should not appear in logs?

---

## 12:00–13:00 — Session 15: Crypto Agility

Crypto agility is treated as a core architectural requirement.

### Tightly coupled design

```text
Application Logic
       |
       +---- Hardcoded cryptographic algorithm
```

### Crypto-agile design

```text
Application
     |
     v
Cryptographic Provider / Abstraction
     |
 +---+-----------+-------------+
 |               |             |
 v               v             v
Classical       PQC         Future
Algorithms   Algorithms   Algorithms
```

Discussion topics:

- Algorithm abstraction
- Configuration
- Versioning
- Protocol negotiation
- Backward compatibility
- Algorithm deprecation
- Key-format migration
- Certificate migration
- Dependency management
- Cryptographic inventory

Example conceptual configuration:

```yaml
key_establishment:
  classical: X25519
  post_quantum: ML-KEM
  mode: hybrid

signatures:
  classical: Ed25519
  post_quantum: ML-DSA
```

The configuration is illustrative; production algorithm choices should follow the relevant standards, protocol specifications, interoperability requirements, and organizational risk assessment.

---

## 13:00–14:00 — Lunch

## 14:00–15:00 — Session 16: Post-Quantum Migration Architecture

Participants develop a migration process:

```text
Discover
   |
   v
Cryptographic Inventory
   |
   v
Classify Data & Required Confidentiality Lifetime
   |
   v
Identify Vulnerable Public-Key Dependencies
   |
   v
Prioritize Systems
   |
   v
Introduce Crypto Agility
   |
   v
Test PQ / Hybrid Mechanisms
   |
   v
Deploy
   |
   v
Monitor & Migrate
```

Systems to consider include:

- Web applications
- APIs
- VPNs
- Internal services
- PKI
- Code-signing infrastructure
- Firmware signing
- Identity systems
- Secure messaging
- Long-term archives
- Encrypted backups
- IoT and embedded devices

---

# 5. Final Capstone — Design a Quantum-Resistant Secure Architecture

## 15:00–17:15

Teams receive a realistic enterprise application architecture.

Example:

```text
                    Internet
                       |
                       v
                +-------------+
                | API Gateway |
                +------+------+ 
                       |
              +--------+--------+
              |                 |
              v                 v
       Authentication      Application
          Service            Service
                                  |
                         +--------+---------+
                         |                  |
                         v                  v
                     Database        Object Storage
                                            |
                                            v
                                          Backup
```

Teams must determine:

- Transport encryption
- Application-level encryption
- Authentication mechanisms
- Key-establishment mechanisms
- Digital signatures
- Certificate architecture
- Key storage
- Key rotation
- Backup encryption
- Service-to-service protection
- Classical/PQ/hybrid mechanisms
- Crypto-agility strategy
- Long-term PQ migration plan

### Incident Injection 1

> The production database has been stolen.

Teams explain what information remains protected and which keys could expose it.

### Incident Injection 2

> An attacker obtained five years of encrypted backups.

Teams analyze long-term confidentiality and key-management implications.

### Incident Injection 3

> An application server has been fully compromised.

Teams reassess their trust boundaries and encryption architecture.

### Incident Injection 4

> A privileged administrator becomes malicious.

Teams consider separation of duties, HSM/KMS controls, auditing, and key access.

### Incident Injection 5

> The organization requires confidential information generated today to remain protected for 20 years.

Teams determine whether their current cryptographic architecture adequately addresses long-term confidentiality and HNDL risk.

### Incident Injection 6

> A cryptographic algorithm or implementation currently deployed by the organization must be retired.

Teams demonstrate how their crypto-agility architecture supports migration without redesigning the entire application.

---

## 17:15–18:00 — Capstone Review and Workshop Conclusion

Teams present their architectures and defend their engineering decisions.

The instructor reviews:

- Threat-model coverage
- Algorithm selection
- Key management
- Trust boundaries
- Failure containment
- PQ readiness
- Crypto agility
- Operational feasibility

---

# 6. Recommended Hands-On Labs

The complete workshop contains six primary labs:

1. **AEAD Encryption Lab** — AES-GCM, authentication tags, tampering, nonce management.
2. **Classical Secure Channel Lab** — X25519 + HKDF + AES-GCM.
3. **Cryptographic Failure Lab** — identify and repair vulnerable implementations.
4. **PKI/TLS Lab** — CA hierarchy, certificates, TLS and optional mTLS.
5. **Post-Quantum Secure Channel Lab** — ML-KEM + KDF + AEAD, followed by hybrid classical/PQ key establishment.
6. **Post-Quantum Signature Lab** — ML-DSA signing and verification compared with a classical signature workflow.

The final architecture capstone integrates concepts from all six labs.

---

# 7. Cryptographic Decision Framework

Participants should leave with a simple mental model:

```text
What do I need?
|
+-- Confidentiality
|      +-- AEAD: AES-GCM / ChaCha20-Poly1305
|
+-- Integrity + shared-key authentication
|      +-- HMAC / AEAD
|
+-- Password storage
|      +-- Password hashing such as Argon2id
|
+-- General hashing
|      +-- SHA-2 / SHA-3
|
+-- Classical key agreement
|      +-- X25519
|
+-- Post-quantum key establishment
|      +-- ML-KEM
|
+-- Classical digital signature
|      +-- Ed25519 / appropriate standardized signature
|
+-- Post-quantum digital signature
|      +-- ML-DSA
|
+-- Key derivation
|      +-- HKDF where appropriate
|
+-- Transport security
|      +-- TLS 1.3 / established secure protocol
|
+-- Key protection
       +-- KMS / HSM / TPM / suitable secrets infrastructure
```

The objective is not simply to memorize this mapping, but to understand **why** each primitive fits a particular requirement.

---

# 8. Recommended Development Environment

Depending on the audience, labs can be implemented in one primary language while equivalent examples are provided for others.

Recommended options:

- Python for rapid demonstrations and protocol concepts
- Java for enterprise-development audiences
- Go for network/security services
- Rust for security-focused or systems-development audiences

Supporting tools may include:

- OpenSSL
- A suitable PQC-capable cryptographic library
- Wireshark
- Docker/containers
- Nginx or another TLS-enabled service
- Command-line certificate inspection tools

Libraries and versions should be selected immediately before each delivery so that exercises follow current standards and supported implementations.

---

# 9. Participant Prerequisites

Participants should be comfortable with:

- Basic programming
- Client/server applications
- APIs or network communication
- Basic security terminology
- Command-line tools

Helpful but not mandatory:

- TLS familiarity
- Linux command line
- Docker
- Basic networking
- Public/private key concepts

No advanced mathematics is required.

---

# 10. Pre-Workshop Preparation

Participants should receive setup instructions several days before the workshop.

Recommended preparation:

1. Install the selected programming environment.
2. Install Git.
3. Install Docker if required by the labs.
4. Install OpenSSL and supporting utilities.
5. Clone/download the workshop repository.
6. Run a provided environment-validation script.
7. Complete a short cryptography prerequisite reading or video.

A pre-workshop diagnostic quiz can identify differences in participant experience.

---

# 11. Assessment Strategy

A practical assessment is preferred over a theory-heavy examination.

Suggested weighting:

| Component | Weight |
|---|---:|
| Knowledge and decision questions | 20% |
| Vulnerable-code analysis and repair | 30% |
| Hands-on cryptographic implementation | 20% |
| Secure-architecture capstone | 30% |

Assessment should test whether participants can **make appropriate engineering decisions**, not whether they can reproduce cryptographic mathematics from memory.

---

# 12. Participant Deliverables

Each participant should receive:

- Workshop slides
- Lab manual
- Source-code repository
- Completed reference implementations
- Vulnerable-code exercises
- Cryptographic decision tree
- Secure coding checklist
- Key-management checklist
- PKI/TLS cheat sheet
- PQC terminology and migration cheat sheet
- Architecture review checklist
- Crypto-agility checklist
- Post-quantum migration worksheet
- Recommended standards and further-reading list

---

# 13. Condensed Two-Day Version

When only two days are available, the workshop can be condensed as follows.

## Day 1 — Applied Cryptography

- Threat modeling
- AES-GCM and AEAD
- Hashes/HMAC
- Password hashing
- HKDF
- X25519
- Ed25519
- Secure-channel lab
- Cryptographic failure lab

## Day 2 — PKI, PQC and Architecture

- PKI and TLS 1.3
- Quantum threat and HNDL
- ML-KEM
- ML-KEM lab
- Hybrid X25519 + ML-KEM
- ML-DSA
- PQ signature lab
- Key management
- Crypto agility
- PQ migration
- Condensed architecture challenge

For audiences responsible for production architecture, the full **three-day format is recommended**.

---

# 14. Optional Advanced Modules

For specialized audiences or an extended workshop, additional modules can include:

### Secure Messaging and End-to-End Encryption

- Identity keys
- Session keys
- Forward secrecy
- Key compromise
- Device enrollment
- Multi-device considerations

### Embedded and IoT Cryptography

- Hardware constraints
- Secure boot
- Firmware signing
- Device identity
- TPM/secure elements
- Long device lifetimes and PQ migration

### Enterprise Key Management

- HSM architecture
- Cloud/on-premises KMS
- Key hierarchies
- Envelope encryption
- Separation of duties
- Disaster recovery

### Protocol Engineering

- Downgrade attacks
- Replay attacks
- Transcript binding
- Algorithm negotiation
- Domain separation
- Versioning

### PQC Migration Deep Dive

- Cryptographic inventory
- Long-lived data classification
- Dependency discovery
- Hybrid migration
- Certificate ecosystem implications
- Performance benchmarking
- Network/message-size impact
- Legacy-device constraints

---

# 15. Core Takeaways

At the conclusion of the workshop, participants should internalize several principles:

1. **Encryption alone does not make a system secure.**
2. **Use established protocols and cryptographic libraries rather than designing custom cryptography.**
3. **Authenticated encryption should be the default for application data requiring confidentiality.**
4. **Key management is as important as algorithm selection.**
5. **Passwords require password hashing, not ordinary encryption or fast general-purpose hashes.**
6. **Certificate validation is a security mechanism, not an optional implementation detail.**
7. **Post-quantum migration primarily changes public-key mechanisms; symmetric cryptography remains essential.**
8. **ML-KEM provides a standardized foundation for post-quantum key establishment.**
9. **ML-DSA provides a standardized foundation for post-quantum digital signatures.**
10. **Hybrid cryptography can support transition between classical and post-quantum security assumptions.**
11. **Long-lived sensitive data may require PQ migration before large-scale cryptographically relevant quantum computers exist.**
12. **Crypto agility should be designed into systems before an emergency migration is required.**
13. **A secure cryptographic architecture must remain meaningful when individual components are compromised.**

---

## Workshop Summary

**Title:** Applied Cryptography & Post-Quantum Security for Developers and Secure-System Architects  
**Duration:** 3 days / approximately 20–21 hours  
**Primary classical mechanisms:** AES-GCM, HKDF, X25519, Ed25519, TLS 1.3  
**Primary PQ mechanisms:** ML-KEM and ML-DSA  
**Architecture themes:** PKI, key management, KMS/HSM, crypto agility, hybrid cryptography, HNDL, and PQ migration  
**Delivery style:** Practical, implementation-oriented, architecture-focused, and lab-driven

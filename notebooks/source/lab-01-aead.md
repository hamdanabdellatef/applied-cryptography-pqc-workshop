# Lab 1 — Authenticated Encryption

**Self-study notebook · Python · synthetic data only.** Core guided lab: 60 minutes. Independent study with extensions: 90–120 minutes.

You are protecting an invoice in storage that an attacker can read and modify. You will encrypt it, change one input at a time, implement a decryption boundary, bind it to context, and test the limits of those protections.

Start with the workshop website's **Session 2 self-study lesson** for the full explanation. This notebook is self-contained: no repository checkout, cloud credentials, GPU, or external data is required.

## How to use this notebook

Run cells in order, predict each outcome first, and write your observations. **Stop at the learner exercise before reading the reference solution.** Run all is supported for checking the supplied material, but reports an untouched exercise as NOT ATTEMPTED; it does not award a learner pass.

The core path is Sections 1–8. Section 9 contains extensions. All keys are disposable and generated in memory. Clearing variables is not a guarantee of secure memory erasure; restart/delete the runtime after the lab.

## 1. Setup

The cell installs exact course versions only if needed. A fresh Colab CPU runtime has internet access for this step. If it changes a package that you had already imported, restart the runtime and run from the top. The website and requirements file use these same pins.

```python
import importlib.metadata
import subprocess
import sys

PINS = {"cryptography": "50.0.1", "ipywidgets": "8.1.7", "matplotlib": "3.10.6"}
needed = []
for package, version in PINS.items():
    try:
        installed = importlib.metadata.version(package)
    except importlib.metadata.PackageNotFoundError:
        installed = None
    if installed != version:
        needed.append(f"{package}=={version}")
if needed:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", *needed])
print("Python:", sys.version.split()[0])
print("Course packages:", {name: importlib.metadata.version(name) for name in PINS})
```

```python
import math
import secrets
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, ChaCha20Poly1305

# Enable widget support when this notebook is running in Google Colab.
try:
    from google.colab import output as colab_output
except ImportError:
    pass
else:
    colab_output.enable_custom_widget_manager()

print("Setup ready. Do not print keys or use real confidential data.")
```

## 2. Encrypt and decrypt an invoice

The **key** is a random secret. A **nonce** is public but must never repeat for a new encryption under that key. **AAD** is public context whose exact bytes are authenticated. The encrypted result includes a 16-byte tag.

Predict the length of the returned bytes before running the cell. For this API, expect `len(plaintext) + 16`; storing the separate 12-byte nonce adds another 12 bytes.

```python
key = AESGCM.generate_key(bit_length=256)
nonce = secrets.token_bytes(12)
plaintext = b"invoice=7;amount=125;currency=USD"
aad = b"workshop-invoice:v1:tenant=acme:record=invoice-7"
aead = AESGCM(key)
encrypted = aead.encrypt(nonce, plaintext, aad)
assert aead.decrypt(nonce, encrypted, aad) == plaintext
assert len(encrypted) == len(plaintext) + 16
print("Plaintext bytes:", len(plaintext))
print("Ciphertext plus tag bytes:", len(encrypted))
print("Nonce bytes:", len(nonce))
print("Synthetic invoice recovered:", aead.decrypt(nonce, encrypted, aad).decode())
```

**Explain:** why can the nonce be stored with the ciphertext, but not the key? The receiver needs the original nonce; its disclosure is allowed by the construction. Disclosure of the key lets an attacker decrypt and create valid records.

## 3. Tamper with one input

Predict the outcome for each option: original, ciphertext, tag, nonce, key, AAD. Each mutation flips one bit or changes context. The expected result is acceptance only for the original record.

The two ciphertext terms can be confusing: `encrypted` is the API's combined ciphertext-plus-tag result. The first-byte mutation below changes the encrypted content; the last-byte mutation changes the tag. We do not remove the tag before decryption.

```python
def flip_first(data):
    return bytes([data[0] ^ 1]) + data[1:]


def run_trial(change="original"):
    trial_key, trial_nonce, trial_body, trial_aad = key, nonce, encrypted, aad
    if change == "ciphertext":
        trial_body = flip_first(encrypted)
    elif change == "tag":
        trial_body = encrypted[:-1] + bytes([encrypted[-1] ^ 1])
    elif change == "nonce":
        trial_nonce = flip_first(nonce)
    elif change == "key":
        trial_key = flip_first(key)
    elif change == "aad":
        trial_aad = b"workshop-invoice:v1:tenant=other:record=invoice-7"
    elif change != "original":
        raise ValueError("Unknown experiment")
    try:
        AESGCM(trial_key).decrypt(trial_nonce, trial_body, trial_aad)
    except InvalidTag:
        print(f"{change}: REJECTED (InvalidTag); no plaintext returned")
        return False
    print(f"{change}: ACCEPTED")
    return True


for change in ("original", "ciphertext", "tag", "nonce", "key", "aad"):
    assert run_trial(change) == (change == "original")
```

Use the dropdown to repeat individual experiments after stating a prediction. If your notebook viewer does not display widgets, call `run_trial("tag")` or any of the other choices directly; the checks above exercise the same function.

```python
selector = widgets.Dropdown(options=["original", "ciphertext", "tag", "nonce", "key", "aad"], description="Change:")
button = widgets.Button(description="Run experiment", button_style="info")
trial_output = widgets.Output()


def on_trial_clicked(_):
    with trial_output:
        trial_output.clear_output(wait=True)
        run_trial(selector.value)


button.on_click(on_trial_clicked)
display(widgets.VBox([selector, button, trial_output]))
```

**Your notes:** record which inputs you changed and what the exception tells you. It tells you authentication failed; it does not identify which field was changed. In this experiment we know the cause because we controlled it.

## 4. Your implementation: enforce the verification boundary

Implement `learner_decrypt_verified` below. It must:

1. Reject a nonce whose length is not 12 bytes with `ValueError` (our lab format).
2. Use `AESGCM` to verify and decrypt the combined ciphertext/tag with the expected AAD.
3. Return the authenticated plaintext, including `b""` when the authenticated message is empty.
4. Allow `InvalidTag` to propagate. Do not return default data or retry unauthenticated decryption.

Only this exercise cell is intentionally incomplete. Keep its name so the checker can call it. The equivalent local task lives in `labs/lab-01-aead/starter.py`.

```python
def learner_decrypt_verified(key, nonce, ciphertext, expected_aad):
    # Replace this line with your implementation.
    raise NotImplementedError("Your implementation goes here")
```

<details><summary>Hint 1</summary><p>Check <code>len(nonce)</code> before calling the library. The lab requires exactly 12 bytes.</p></details>
<details><summary>Hint 2</summary><p>Create an <code>AESGCM</code> object with the key, then call its <code>decrypt</code> method with nonce, combined ciphertext/tag, and expected AAD.</p></details>
<details><summary>Hint 3</summary><p>You do not need an exception handler inside this helper. Returning the library call preserves both authenticated plaintext and its failure behavior.</p></details>

## 5. Check your implementation

The checker covers success, each changed authentication input, truncation, an empty message, and an invalid nonce length. Each test fixture uses a new key. A fixed nonce inside this fixture is used for only one encryption with that fixture's key.

```python
def check_decrypt(candidate):
    fixture_key = AESGCM.generate_key(bit_length=256)
    fixture_nonce = bytes(range(12))
    fixture_aad = b"test-context"
    fixture_body = AESGCM(fixture_key).encrypt(fixture_nonce, b"test-message", fixture_aad)
    assert candidate(fixture_key, fixture_nonce, fixture_body, fixture_aad) == b"test-message"
    cases = [
        (flip_first(fixture_key), fixture_nonce, fixture_body, fixture_aad),
        (fixture_key, flip_first(fixture_nonce), fixture_body, fixture_aad),
        (fixture_key, fixture_nonce, flip_first(fixture_body), fixture_aad),
        (fixture_key, fixture_nonce, fixture_body[:-1] + bytes([fixture_body[-1] ^ 1]), fixture_aad),
        (fixture_key, fixture_nonce, fixture_body, b"other-context"),
        (fixture_key, fixture_nonce, fixture_body[:8], fixture_aad),
    ]
    for changed_key, changed_nonce, changed_body, changed_aad in cases:
        try:
            candidate(changed_key, changed_nonce, changed_body, changed_aad)
        except InvalidTag:
            pass
        else:
            raise AssertionError("Modified or truncated record was not rejected")
    empty_key = AESGCM.generate_key(bit_length=256)
    empty_body = AESGCM(empty_key).encrypt(fixture_nonce, b"", fixture_aad)
    assert candidate(empty_key, fixture_nonce, empty_body, fixture_aad) == b""
    try:
        candidate(fixture_key, b"short", fixture_body, fixture_aad)
    except ValueError:
        pass
    else:
        raise AssertionError("Wrong-length nonce was not rejected")


try:
    check_decrypt(learner_decrypt_verified)
except NotImplementedError:
    learner_status = "NOT ATTEMPTED: implement Section 4 and rerun this cell."
else:
    learner_status = "PASS: learner implementation passed the acceptance checks."
print(learner_status)
```

## 6. Reference solution and record helpers

**Pause before continuing:** attempt the exercise and read the hints first. The following supplied code does not overwrite `learner_decrypt_verified`; it defines a separate reference function called `decrypt_verified`.

The code comes from the course's `src/crypto_workshop/aead.py`. It also provides `build_aad`, `seal_record`, and `open_record` so we can bind the encrypted invoice to an expected tenant and record. The restricted JSON encoding fixes field order, whitespace, purpose, and version for this exercise. It is not a general wire-protocol design.

<!-- workshop:reference-aead -->

```python
check_decrypt(decrypt_verified)
print("PASS: supplied reference solution passed acceptance checks.")
print("Learner result remains:", learner_status)
```

## 7. Bind the invoice to the expected context

The application must obtain `tenant_id` and `record_id` from an authorized request or other trusted context. Copying a label from the untrusted blob is not authorization.

Predict what happens if the attacker puts this blob in another tenant's row or another invoice's row.

```python
record_key = generate_key()
record = seal_record(record_key, plaintext, "acme", "invoice-7")
assert open_record(record_key, record, "acme", "invoice-7") == plaintext
for tenant, record_id in [("other", "invoice-7"), ("acme", "invoice-8")]:
    try:
        open_record(record_key, record, tenant, record_id)
    except InvalidTag:
        print(f"REJECTED: record does not authenticate for {tenant}/{record_id}")
    else:
        raise AssertionError("Context substitution was accepted")
print("Public AAD:", build_aad("acme", "invoice-7").decode())
```

**Explain:** the metadata is visible; its binding is authenticated. Putting a secret in AAD would disclose it. If both encryption and decryption omit a field, changing that field cannot be detected through that binding.

## 8. Replay: a valid tag is not a clock

Predict what happens when the unchanged record is opened again. This is repeated decryption, not nonce reuse for encryption.

```python
first_read = open_record(record_key, record, "acme", "invoice-7")
replayed_read = open_record(record_key, record, "acme", "invoice-7")
assert first_read == replayed_read == plaintext
print("Both reads authenticate. AEAD alone does not detect replay or rollback.")
```

**Your design answer:** to reject an old version, what state would the application need? One approach is a version bound in AAD and compared with a trusted latest-version record. Storing a version beside the ciphertext without trusted comparison does not solve rollback.

## 9. Extensions

### 9A. Explore the birthday effect

This is a probability model, not a real cipher experiment. The slider selects **tiny toy nonce spaces** to make the curve visible. It never changes the 12-byte nonce used by AES-GCM above.

The approximation is `1 - exp(-q(q-1)/(2 * 2**n))`. Probability means “at least one repeated value among all draws,” not “probability that this one draw repeats.” Production GCM limits involve additional constraints, so this graph is not a key-lifetime calculator.

```python
def collision_probability(draws, bits):
    return -math.expm1(-draws * (draws - 1) / (2 * 2**bits))


def plot_collision(bits=8):
    max_draws = math.ceil(3 * math.sqrt(2**bits))
    draws = list(range(1, max_draws + 1))
    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.plot(draws, [100 * collision_probability(q, bits) for q in draws], color="#196a83")
    ax.set(xlabel="Random draws under one key", ylabel="Approximate collision probability (%)",
           title=f"Toy {bits}-bit nonce space — NOT an AES-GCM parameter", ylim=(0, 100))
    ax.grid(alpha=0.25)
    fig.tight_layout()
    plt.show()
    plt.close(fig)


plot_collision(8)
widgets.interact(plot_collision, bits=widgets.IntSlider(value=8, min=4, max=16, step=2, description="Toy bits"))
```

Check the same approximation on a 96-bit space without trying to generate billions of samples:

```python
q = 2**32
p = collision_probability(q, 96)
print(f"At 2^32 random 96-bit draws: approximate probability = {p:.3e}")
print("This birthday calculation alone is NOT a safe production usage budget.")
assert 0 < p < 1e-9
```

### 9B. Intentionally break nonce uniqueness

The following isolated experiment violates the rule on purpose with a disposable key. Never copy this pattern into the normal encryption helper. Both synthetic plaintexts have equal length. We strip only the tags when demonstrating the XOR relationship; we never use this stripping pattern for ordinary decryption.

The attacker in this scenario knows the first message and both encrypted contents. They do not know the key. Since the stream repeats, they recover the second message as `C1 XOR C2 XOR P1`.

```python
def xor_bytes(left, right):
    if len(left) != len(right):
        raise ValueError("This demonstration requires equal lengths")
    return bytes(a ^ b for a, b in zip(left, right))


broken_demo_key = AESGCM.generate_key(bit_length=256)
reused_nonce = secrets.token_bytes(12)
known_message = b"amount=00000125"
hidden_message = b"amount=00000999"
broken_aead = AESGCM(broken_demo_key)
c1 = broken_aead.encrypt(reused_nonce, known_message, b"demo-only")[:-16]
c2 = broken_aead.encrypt(reused_nonce, hidden_message, b"demo-only")[:-16]
attacker_recovery = xor_bytes(xor_bytes(c1, c2), known_message)
assert attacker_recovery == hidden_message
print("Recovered without supplying the key to the XOR calculation:", attacker_recovery.decode())
del broken_demo_key, broken_aead
```

**Explain:** successful decryption of the original records would not make reuse safe. The confidentiality damage occurs across records. GCM authentication can also be weakened; this exercise does not implement a forgery.

### 9C. Compare another AEAD interface

ChaCha20-Poly1305 uses a different construction but still requires a secret key, unique nonce per key, matching AAD, and tag verification. Do not share the same key material between the two algorithms in this exercise.

```python
chacha_key = ChaCha20Poly1305.generate_key()
chacha_nonce = secrets.token_bytes(12)
chacha = ChaCha20Poly1305(chacha_key)
chacha_body = chacha.encrypt(chacha_nonce, plaintext, aad)
assert chacha.decrypt(chacha_nonce, chacha_body, aad) == plaintext
assert len(chacha_body) == len(plaintext) + 16
try:
    chacha.decrypt(chacha_nonce, flip_first(chacha_body), aad)
except InvalidTag:
    print("ChaCha20-Poly1305 also rejects the changed ciphertext.")
else:
    raise AssertionError("Changed ciphertext unexpectedly accepted")
```

## 10. Exit ticket

Write a short answer to each question in your own notebook copy:

1. Which inputs can be public, and which must be secret?
2. What does `InvalidTag` establish, and what does it not tell you?
3. How does expected AAD prevent moving an invoice into another tenant's context?
4. Why does valid replay still succeed?
5. What must change when you re-encrypt the same invoice under the same key?

<details><summary>Answer guide</summary><p>The key is secret; nonce, ciphertext, tag and AAD can be public. InvalidTag establishes a verification failure without locating its cause. Expected AAD binds the record to context that the application independently trusts. AEAD has no freshness state, so unchanged replay can verify. A new encryption needs a new nonce under that key, even when the plaintext is unchanged.</p></details>

Your deliverables are the completed learner function, its passing checks, a tampering observation table, and the five explanations. Passing the supplied reference solution is not a substitute for your implementation.

## References and cleanup

- [cryptography 50.0.1 AEAD API](https://cryptography.io/en/50.0.1/hazmat/primitives/aead/)
- [RFC 5116: AEAD interface and nonce reuse](https://www.rfc-editor.org/rfc/rfc5116)
- [NIST SP 800-38D: GCM](https://csrc.nist.gov/pubs/sp/800/38/d/final)

Save your explanations. Clear outputs before sharing, and disconnect/delete the runtime. These in-memory demo keys are not designed for persistence or recovery. Last content review: 19 September 2026.

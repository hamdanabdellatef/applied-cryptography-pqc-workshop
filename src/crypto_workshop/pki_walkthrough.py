"""Session 6 visual teaching tools for the fixed make_pki hierarchy.

Real certificate/CRL signatures; deliberately not a general RFC 5280 validator.
The shared Day 2 helpers must be loaded before this module is used.
"""
from html import escape
from cryptography.exceptions import InvalidSignature


def certificate_fields(cert):
    """Readable values without revealing the private key."""
    rows = [
        ('Version', cert.version.name, 'X.509 structure version'),
        ('Serial (hex)', hex(cert.serial_number), 'Issuer-scoped certificate identifier; used by CRLs'),
        ('Subject', cert.subject.rfc4514_string(), 'Claim about the key owner; not a trust decision'),
        ('Issuer', cert.issuer.rfc4514_string(), 'Claim about the signer; verify the signature'),
        ('Not before (UTC)', str(cert.not_valid_before_utc), 'Start of validity'),
        ('Not after (UTC)', str(cert.not_valid_after_utc), 'End of validity'),
        ('Public key', cert.public_key().curve.name, 'EC public key inside SubjectPublicKeyInfo'),
        ('Signature algorithm', cert.signature_algorithm_oid.dotted_string, 'Issuer used ECDSA with SHA-256'),
        ('SHA-256 fingerprint', cert.fingerprint(hashes.SHA256()).hex(), 'Digest of this certificate, not proof of trust'),
        ('Signed body', f'{len(cert.tbs_certificate_bytes)} DER bytes', 'TBSCertificate: fields protected by the issuer signature'),
        ('Signature', cert.signature.hex(), 'Signature is outside the signed body'),
    ]
    for ext in cert.extensions:
        rows.append((f'{ext.oid.dotted_string} ({ext.oid._name})', str(ext.value),
                     'Critical: validator must understand and process' if ext.critical else 'Noncritical extension'))
    return rows


def show_table(headers, rows):
    from IPython.display import HTML, display
    style = 'border:1px solid #879aa8;padding:8px;white-space:normal;overflow-wrap:anywhere;text-align:left;vertical-align:top'
    head = ''.join(f'<th style="{style}">{escape(str(h))}</th>' for h in headers)
    body = ''.join('<tr>' + ''.join(f'<td style="{style}">{escape(str(v))}</td>' for v in row) + '</tr>' for row in rows)
    display(HTML(f'<table style="border-collapse:collapse;width:100%;table-layout:fixed"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'))


def print_material(keys, certs, role='server', show_private=False):
    """Print only fresh disposable workshop material, never user-supplied keys."""
    cert = certs[role]
    print(f'=== {role.upper()} CERTIFICATE: public claims and public key ===')
    print(cert.public_bytes(serialization.Encoding.PEM).decode())
    print('=== PUBLIC KEY: SubjectPublicKeyInfo, no identity or issuer signature ===')
    print(cert.public_key().public_bytes(serialization.Encoding.PEM,
          serialization.PublicFormat.SubjectPublicKeyInfo).decode())
    if show_private:
        print('=== DISPOSABLE TEACHING PRIVATE KEY: PKCS#8, unencrypted; never reuse ===')
        print(keys[role].private_bytes(serialization.Encoding.PEM,
              serialization.PrivateFormat.PKCS8, serialization.NoEncryption()).decode())
    else:
        print('Private key hidden. Set show_private=True to explain this disposable key.')
    for field, value, meaning in certificate_fields(cert):
        print(f'{field}: {value}\n  Why: {meaning}')


def inspection_panel(keys, certs):
    import ipywidgets as widgets
    from IPython.display import display
    role = widgets.Dropdown(options=list(certs), value='server', description='Inspect:')
    private = widgets.Checkbox(value=False, description='Print disposable private key', indent=False)
    button = widgets.Button(description='Print PEM and fields', button_style='info')
    output = widgets.Output()

    def render(_):
        output.clear_output(wait=True)
        with output:
            print_material(keys, certs, role.value, private.value)
            show_table(('Field / extension', 'Decoded value', 'Interpretation'), certificate_fields(certs[role.value]))
    button.on_click(render)
    display(widgets.VBox([widgets.HBox([role, private]), button, output]))
    render(None)
    return {'role': role, 'private': private, 'button': button, 'output': output}


def make_teaching_crl(keys, certs, serial=None, state='fresh'):
    """Direct, full CRL for leaf certificates issued by our intermediate only."""
    now = datetime.now(timezone.utc)
    last, next_time = now - timedelta(minutes=5), now + timedelta(hours=1)
    if state == 'stale':
        last, next_time = now - timedelta(days=2), now - timedelta(days=1)
    if state == 'future':
        last, next_time = now + timedelta(hours=1), now + timedelta(hours=2)
    builder = (x509.CertificateRevocationListBuilder().issuer_name(certs['intermediate'].subject)
               .last_update(last).next_update(next_time)
               .add_extension(x509.CRLNumber(1), critical=False))
    if serial is not None:
        revoked = (x509.RevokedCertificateBuilder().serial_number(serial)
                   .revocation_date(now - timedelta(minutes=10))
                   .add_extension(x509.CRLReason(x509.ReasonFlags.key_compromise), critical=False).build())
        builder = builder.add_revoked_certificate(revoked)
    signer = keys['server'] if state == 'bad-signature' else keys['intermediate']
    return builder.sign(signer, hashes.SHA256())


def crl_decision(crl, leaf, issuer, at=None):
    """Validate direct CRL evidence for this fixed hierarchy; fail closed."""
    at = at or datetime.now(timezone.utc)
    if crl is None:
        return False, 'UNKNOWN: CRL unavailable; classroom hard-fail policy denies'
    if crl.issuer != issuer.subject or leaf.issuer != issuer.subject:
        return False, 'REJECT: CRL/leaf issuer does not match this issuing CA'
    if not issuer.extensions.get_extension_for_class(x509.KeyUsage).value.crl_sign:
        return False, 'REJECT: issuer lacks cRLSign usage'
    try:
        issuer.public_key().verify(crl.signature, crl.tbs_certlist_bytes,
                                   ec.ECDSA(crl.signature_hash_algorithm))
    except InvalidSignature:
        return False, 'REJECT: CRL signature invalid'
    if not (crl.last_update_utc <= at < crl.next_update_utc):
        return False, 'UNKNOWN: CRL stale or not yet current; classroom hard-fail policy denies'
    if crl.get_revoked_certificate_by_serial_number(leaf.serial_number):
        return False, f'REVOKED: serial {hex(leaf.serial_number)} appears in this signed CRL'
    return True, 'GOOD within this model: valid fresh direct CRL does not list this leaf serial'


SCENARIOS = ('valid', 'unknown-root', 'missing-intermediate', 'expired', 'wrong-purpose',
             'wrong-identity', 'missing-client', 'altered-signed-body', 'revoked',
             'stale-crl', 'missing-crl', 'forged-crl', 'authorization-denied')


def validation_trace(keys, certs, role='server', scenario='valid'):
    """Return a deterministic teaching sequence with PASS, FAIL and SKIP rows.

    Checks are real operations on one fixed P-256 chain. No general path building,
    wildcard matching, name constraints, policies, indirect CRLs or online status.
    """
    if role not in ('server', 'client') or scenario not in SCENARIOS:
        raise ValueError('Unknown role or scenario')
    selected = ('client' if role == 'server' else 'server') if scenario == 'wrong-purpose' else role
    leaf, intermediate, root = certs[selected], certs['intermediate'], certs['root']
    at = datetime.now(timezone.utc)
    if scenario == 'expired':
        at = leaf.not_valid_after_utc + timedelta(seconds=1)
    state = {'stale-crl': 'stale', 'forged-crl': 'bad-signature'}.get(scenario, 'fresh')
    crl = None if scenario == 'missing-crl' else make_teaching_crl(
        keys, certs, leaf.serial_number if scenario == 'revoked' else None, state)
    rows, stopped = [], False

    def check(label, explanation, operation):
        nonlocal stopped
        if stopped:
            rows.append((label, 'SKIP', 'Not reached after a required check failed'))
            return
        try:
            ok, evidence = operation()
        except InvalidSignature:
            ok, evidence = False, 'Cryptographic signature verification failed'
        rows.append((label, 'PASS' if ok else 'FAIL', explanation + ' — ' + evidence))
        stopped = not ok

    check('Certificate supplied', 'Peer must present a leaf', lambda: (
        not (role == 'client' and scenario == 'missing-client'), selected + ' certificate'))
    check('Local trust anchor', 'Trust is local configuration, not the peer-supplied root', lambda: (
        scenario != 'unknown-root', 'configured root SHA-256: ' + root.fingerprint(hashes.SHA256()).hex()))
    check('Path available', 'Only root → intermediate → leaf is supported here', lambda: (
        scenario != 'missing-intermediate', 'issuing intermediate supplied'))

    def signatures():
        intermediate.verify_directly_issued_by(root)
        leaf.verify_directly_issued_by(intermediate)
        if scenario == 'altered-signed-body':
            intermediate.public_key().verify(leaf.signature, leaf.tbs_certificate_bytes + b'!',
                                             ec.ECDSA(leaf.signature_hash_algorithm))
        return True, 'root public key verifies intermediate; intermediate public key verifies leaf'
    check('Issuer signatures', 'Names alone are insufficient', signatures)

    def constraints():
        rb = root.extensions.get_extension_for_class(x509.BasicConstraints).value
        ib = intermediate.extensions.get_extension_for_class(x509.BasicConstraints).value
        lb = leaf.extensions.get_extension_for_class(x509.BasicConstraints).value
        ok = rb.ca and ib.ca and not lb.ca and (rb.path_length is None or rb.path_length >= 1)
        ok = ok and (ib.path_length is None or ib.path_length >= 0)
        ok = ok and all(c.extensions.get_extension_for_class(x509.KeyUsage).value.key_cert_sign for c in (root, intermediate))
        return bool(ok), 'CA flags, keyCertSign and path lengths for this one-intermediate chain'
    check('CA constraints', 'Issuers need authority to issue', constraints)
    check('Validity time', 'At ' + str(at), lambda: (
        all(c.not_valid_before_utc <= at <= c.not_valid_after_utc for c in (intermediate, leaf)),
        'leaf and intermediate must both be in date'))
    purpose = ExtendedKeyUsageOID.SERVER_AUTH if role == 'server' else ExtendedKeyUsageOID.CLIENT_AUTH
    check('Key use and EKU', 'Expected ' + ('serverAuth' if role == 'server' else 'clientAuth'), lambda: (
        leaf.extensions.get_extension_for_class(x509.KeyUsage).value.digital_signature
        and purpose in leaf.extensions.get_extension_for_class(x509.ExtendedKeyUsage).value,
        str(leaf.extensions.get_extension_for_class(x509.ExtendedKeyUsage).value)))
    expected = 'invoice.test' if role == 'server' else 'client.test'
    if scenario == 'wrong-identity':
        expected = 'other.test'
    check('Expected identity', 'DNS service match' if role == 'server' else 'Application mapping of client SAN, not TLS hostname checking', lambda: (
        expected in leaf.extensions.get_extension_for_class(x509.SubjectAlternativeName).value.get_values_for_type(x509.DNSName),
        'independently configured exact identity: ' + expected))
    check('Leaf revocation', 'Verify issuer, signature, freshness and serial', lambda: crl_decision(crl, leaf, intermediate))
    check('Application permission', 'Separate from certificate validation', lambda: (
        scenario != 'authorization-denied', 'synthetic allow-list for read:invoice; not a real authorization service'))
    return rows, crl


def show_crl(crl):
    if crl is None:
        print('No CRL received. Missing evidence is not GOOD status.')
        return
    print(crl.public_bytes(serialization.Encoding.PEM).decode())
    print('Issuer:', crl.issuer.rfc4514_string())
    print('This update:', crl.last_update_utc, '| Next update:', crl.next_update_utc)
    print('CRL number:', crl.extensions.get_extension_for_class(x509.CRLNumber).value.crl_number)
    print('Listed serials:', [hex(entry.serial_number) for entry in crl])
    for entry in crl:
        print('Serial:', hex(entry.serial_number), 'Revocation date:', entry.revocation_date_utc,
              'Reason:', entry.extensions.get_extension_for_class(x509.CRLReason).value.reason)


def walkthrough_panel(keys, certs):
    import ipywidgets as widgets
    from IPython.display import display
    role = widgets.Dropdown(options=['server', 'client'], description='Validate:')
    scenario = widgets.Dropdown(options=SCENARIOS, description='Case:')
    start = widgets.Button(description='Start / reset', button_style='info')
    next_step = widgets.Button(description='Next check')
    reveal = widgets.Button(description='Show all checks')
    crl_button = widgets.Button(description='Print current CRL')
    output, crl_output = widgets.Output(), widgets.Output()
    state = {'rows': [], 'visible': 0, 'crl': None}

    def render():
        output.clear_output(wait=True)
        with output:
            print('Predict the next decision, then click Next check. Results show a fixed-chain teaching model.')
            show_table(('Check', 'Result', 'Evidence'), state['rows'][:state['visible']])
            if state['visible'] == len(state['rows']):
                print('REJECT' if any(row[1] == 'FAIL' for row in state['rows']) else 'ACCEPT within this teaching model')
        next_step.disabled = state['visible'] >= len(state['rows'])

    def reset(_=None):
        state['rows'], state['crl'] = validation_trace(keys, certs, role.value, scenario.value)
        state['visible'] = 0
        crl_output.clear_output()
        render()

    def advance(_):
        state['visible'] = min(len(state['rows']), state['visible'] + 1)
        render()

    def all_checks(_):
        state['visible'] = len(state['rows'])
        render()

    def print_crl(_):
        crl_output.clear_output(wait=True)
        with crl_output:
            show_crl(state['crl'])
    start.on_click(reset)
    next_step.on_click(advance)
    reveal.on_click(all_checks)
    crl_button.on_click(print_crl)
    role.observe(reset, names='value')
    scenario.observe(reset, names='value')
    display(widgets.VBox([widgets.HBox([role, scenario]), widgets.HBox([start, next_step, reveal, crl_button]), output, crl_output]))
    reset()
    return {'role': role, 'scenario': scenario, 'next': next_step, 'reset': start,
            'all': reveal, 'crl_button': crl_button, 'state': state}

# Design decisions and review comments

## Current scaffold

The supplied document is a curriculum reference. The initial request established the structure. The subsequent request authorized the AEAD lesson and Lab 1 end to end, with separate public self-study and instructor pages and Mermaid diagrams.

The curriculum keeps all 16 sessions, six labs, the capstone, resource handouts, optional slides, and advanced-module placeholders. Python is the only planned implementation language.

Use Markdown under `docs/` as the teaching-content source, Python under `labs/` and `src/`, and standard `.ipynb` notebooks under `notebooks/`. Notebook Markdown should explain experiments without duplicating whole lessons. `course.json` inventories lessons and labs; update it and MkDocs navigation together when restructuring.

MkDocs is a deliberately small Python-based website scaffold with search, navigation, and static HTML output. Its default theme is temporary. The reference site's chapter hierarchy, sequential reading, and interactive explanations are useful design patterns; this scaffold does not reproduce its design or copy its prose. Rich browser interactions may require small JavaScript components while executable cryptography stays in Python/Colab.

## Curriculum comments

- The detailed schedule is 22 h 45 min of instruction, not the stated 20–21 hours. Preserve the outline, then pilot the labs and trim scope or extend delivery time.
- Lab 2 and Lab 5 need explicit peer-authentication and protocol-boundary explanations. Key establishment plus encryption alone is an incomplete secure-channel design. Teach against established protocol references when developing these lessons.
- The hybrid extension depends on Session 10, which currently follows Lab 5. Make it a post-session extension or move time between those slots.
- Thirty minutes for Lab 6 is tight. Provide prepared setup and keep benchmarking optional, or rebalance Day 2.
- Password hashing/KDFs and classical signatures currently receive lessons but no dedicated labs. Add short guided exercises within their lessons before adding more full labs.
- Plan Colab-compatible PKI experiments inside the runtime, with local network tooling as an optional extension. Validate service lifecycle and cleanup before delivery.
- Choose and test the PQC library early. Do not commit to an unverified installation path or API. Record standards, parameters, versions, and runtime compatibility during implementation.
- Use one evolving sample application across the channel labs to make comparisons concrete.
- Prioritize diagrams of trust boundaries, nonce allocation, certificate chains, KEM message flow, and key lifecycles. Keep lattice mathematics optional for this audience.

## Publication decisions still open

Repository owner/name and release ref; domain and host; content/code licensing; solution visibility; final visual theme; tested Python and cryptographic dependency versions.

Keep instructor notes outside `docs/`. This prevents inclusion in the generated website, but does not make them private in a public repository.

Direct Colab links should target a tested release ref. Colab stores personal notebook copies separately; never require participants to edit the course repository.

## Sources consulted for structure

- User-supplied design: `source/workshop-design.md`.
- Reference website: https://www.lattices.io/ — chapter navigation, sequential lessons, and embedded interactions.
- MkDocs authoring: https://www.mkdocs.org/user-guide/writing-your-docs/
- MkDocs configuration: https://www.mkdocs.org/user-guide/configuration/
- Colab FAQ: https://research.google.com/colaboratory/faq.html

These are structural references. The completed AEAD lesson now has a reviewed primary-source bibliography; other modules still need technical references.

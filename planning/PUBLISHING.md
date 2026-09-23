# Publishing the workshop

Target repository: https://github.com/hamdanabdellatef/applied-cryptography-pqc-workshop

Target website: https://hamdanabdellatef.github.io/applied-cryptography-pqc-workshop/

The repository contains Markdown sources, Python examples, clean notebooks and the course build configuration. Virtual environments, local verification outputs, generated site files and local secrets are excluded by `.gitignore`.

## GitHub Pages

In repository Settings → Pages, select GitHub Actions as the build source. The workflow in `.github/workflows/pages.yml` validates the inventory, builds MkDocs strictly, uploads only `site/`, and deploys that artifact to Pages. A push to `main` publishes an update; the workflow can also be run manually.

This follows [GitHub's custom Pages workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages). Do not select the Markdown `docs/` folder as a branch-published HTML site; MkDocs must build it first.

## Updating content

Edit the authoritative Markdown and regenerate affected notebook companions with the matching script in `scripts/`. Run appropriate checks, then commit and push to `main`. Check the Actions run and deployed page before announcing an update.

`scripts/site_hooks.py` adds Colab launch links next to implemented notebook downloads at build time, using `repo_url`. Source notebooks remain clean. Learners should save their own Colab copy. Labs 2–3 remain clearly identified as scaffolds.

If the repository owner or name changes, update `site_url` and `repo_url` in `mkdocs.yml`. No custom domain is configured.

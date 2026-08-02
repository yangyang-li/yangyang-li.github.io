# Yangyang Li — Academic Homepage

Source code for [yangyang-li.github.io](https://yangyang-li.github.io), an English-first static academic website with an independent Chinese résumé.

The site was rebuilt from a legacy WordPress installation during an August 2026 Codex collaboration. It uses the thin-starter release of [al-folio](https://github.com/alshedivat/al-folio) and publishes through GitHub Actions.

## Site structure

- **Home** — profile, research overview, education, research interests, and selected publications
- **中文履历** — academic appointments, projects, awards, patents, and software copyrights
- **Publications** — year-sorted BibTeX catalogue with external DOI and publisher links
- **Academic Service** — teaching, conference service, reviewing, supervision, and memberships
- **Contact** — public email and scholarly identity links

The first release intentionally has no blog, news feed, comments, analytics, backend service, or locally hosted publication PDFs.

## Content maintenance

| Content                       | Source                         |
| ----------------------------- | ------------------------------ |
| Site identity and features    | `_config.yml`                  |
| Homepage and navigation pages | `_pages/`                      |
| Publications                  | `_bibliography/papers.bib`     |
| Publication verification list | `_data/publication_review.csv` |
| Academic identity links       | `_data/socials.yml`            |
| Images                        | `assets/img/`                  |

The archived WordPress directory `liyangyang.com/` is reference material only. It is outside this Git repository and is also explicitly ignored. WordPress code, configuration, logs, databases, GeoIP data, and uploaded paper PDFs must never be committed.

## Publications

The initial bibliography was extracted conservatively from the archived WordPress publication files:

```powershell
python bin/migrate_publications.py
```

The script reads the archive but does not copy PDFs into this repository. Review `_data/publication_review.csv` before treating automatically extracted metadata as authoritative.

## Local checks

Install JavaScript dependencies and check formatting:

```powershell
npm ci
npm run lint:prettier
```

For a complete local production build, install Ruby and Bundler versions compatible with `Gemfile.lock`, then run:

```powershell
bundle install
bundle exec jekyll build
```

The generated `_site/` directory is ignored.

## Deployment

Every push to `master` runs `.github/workflows/deploy.yml`. The workflow installs the pinned al-folio gems, builds the Jekyll site, and deploys the generated `_site` artifact with GitHub's official Pages Actions. In repository **Settings → Pages**, set **Source** to **GitHub Actions**; do not use GitHub's legacy branch-based Jekyll builder, because it cannot load the `al_folio_core` theme gem.

The old Dinky-based homepage is preserved in the remote `legacy-site` branch.

## Visual direction

The design uses warm white, charcoal text, one restrained green accent, Roboto for English, and an open-source Song-style Chinese font with system fallbacks. An original low-contrast ink landscape and small boat provide a quiet visual motif without reducing readability. A matching Open Graph image is included for social sharing.

## License

The site customization and personal content are maintained by Yangyang Li. The underlying al-folio theme and its dependencies retain their respective licenses; see `LICENSE` and upstream project metadata.

---
layout: about
title: Home
permalink: /
subtitle: Senior Engineer (Professor-level) · Academy of Cyber · Beijing, China

selected_papers: false
social: true

announcements:
  enabled: false

latest_posts:
  enabled: false

profile:
  align: right
  image: yangyang-li.jpg
  image_circular: false
---

<style>
  :root { --yangyang-accent: #2f6b5f; --yangyang-paper: #fbfaf6; }
  html[data-theme="light"] {
    --global-theme-color: #2f6b5f;
    --global-hover-color: #244f47;
    --global-hover-text-color: #ffffff;
  }
  html[data-theme="dark"] {
    --global-theme-color: #78b6a7;
    --global-hover-color: #9bc9bd;
    --global-hover-text-color: #171b1a;
  }
  a,
  .navbar-nav .nav-item.active > .nav-link { color: #2f6b5f !important; }
  a:hover,
  .navbar-nav .nav-link:hover { color: #244f47 !important; }
  html[data-theme="dark"] a,
  html[data-theme="dark"] .navbar-nav .nav-item.active > .nav-link { color: #78b6a7 !important; }
  html[data-theme="dark"] a:hover,
  html[data-theme="dark"] .navbar-nav .nav-link:hover { color: #9bc9bd !important; }
  .navbar-nav .nav-item:not(.active) > .nav-link { color: var(--global-text-color) !important; }
  body {
    font-family: Roboto, "Noto Serif SC", "Songti SC", "STSong", SimSun, sans-serif;
    background-color: var(--yangyang-paper);
    background-image:
      linear-gradient(rgba(251, 250, 246, 0.78), rgba(251, 250, 246, 0.86)),
      url("{{ '/assets/img/shanshui-hero.png' | relative_url }}");
    background-position: center top;
    background-size: cover;
    background-attachment: fixed;
  }
  .home-hero {
    margin: 1.5rem 0 2.75rem;
    padding: 1.5rem 0 1.75rem;
    border-bottom: 1px solid rgba(47, 107, 95, 0.22);
  }
  .profile img {
    aspect-ratio: 1 / 1;
    object-fit: cover;
    object-position: 13% center;
  }
  .profile .more-info {
    margin-top: 0.85rem;
    font-family: inherit;
    font-size: 0.9rem;
    font-style: normal;
    line-height: 1.45;
    overflow-wrap: anywhere;
    text-align: center;
  }
  .profile .more-info p { margin-bottom: 0.2rem; }
  article > h2 > a { text-transform: capitalize; }
  .post article > h2:not(.bibliography) {
    margin: 2.65rem 0 1rem;
    padding-bottom: 0.45rem;
    border-bottom: 1px solid rgba(47, 107, 95, 0.24);
    color: #2f6b5f;
    font-size: clamp(1.4rem, 3vw, 1.75rem);
    font-weight: 400;
  }
  .post article > h2:not(.bibliography) > a {
    color: inherit !important;
  }
  .post article > h3 {
    margin: 1.65rem 0 0.75rem;
    font-size: 1.08rem;
    font-weight: 600;
    letter-spacing: 0.01em;
  }
  html[data-theme="dark"] .post article > h2:not(.bibliography) {
    color: #78b6a7;
  }
  .publications .author > em {
    border-bottom: 0;
    color: var(--global-text-color);
    font-style: normal;
    font-weight: 700;
  }
  .home-selected-publications > h2 {
    margin: 2.65rem 0 1rem;
    padding-bottom: 0.45rem;
    border-bottom: 1px solid rgba(47, 107, 95, 0.25);
    color: #2f6b5f !important;
    font-weight: 400;
  }
  html[data-theme="dark"] .home-selected-publications > h2 {
    border-bottom-color: rgba(120, 182, 167, 0.25);
    color: #78b6a7 !important;
  }
  .home-selected-publications .links { display: none !important; }
  .home-selected-publications h2.bibliography { display: none !important; }
  .home-selected-publications ol.bibliography {
    margin: 0;
    padding-left: 0;
    list-style: none;
  }
  .home-selected-publications ol.bibliography > li { margin-bottom: 1.35rem; }
  @media (min-width: 576px) {
    .profile {
      width: 24.25%;
      margin-top: 2rem;
    }
  }
  .home-hero p { max-width: 47rem; font-size: clamp(1rem, 1.6vw, 1.13rem); line-height: 1.8; }
  html[data-theme="dark"] body {
    background-color: #171b1a;
    background-image:
      linear-gradient(rgba(23, 27, 26, 0.74), rgba(23, 27, 26, 0.86)),
      url("{{ '/assets/img/shanshui-hero.png' | relative_url }}");
  }
  html[data-theme="dark"] .home-hero {
    border-color: rgba(120, 182, 167, 0.25);
  }
  @media (prefers-color-scheme: dark) {
    html:not([data-theme]) body {
      background-color: #171b1a;
      background-image:
        linear-gradient(rgba(23, 27, 26, 0.74), rgba(23, 27, 26, 0.86)),
        url("{{ '/assets/img/shanshui-hero.png' | relative_url }}");
    }
  }
  @media (max-width: 720px) {
    body { background-position: 62% top; background-attachment: scroll; }
    .home-hero { margin-top: 1rem; padding-top: 1rem; }
  }
</style>

<div class="home-hero" aria-label="Introduction">
  <p>I am a Senior Engineer (Professor-level) at the <strong>Academy of Cyber</strong> in Beijing. My work focuses on understanding and safeguarding networked social systems, with particular interests in social computing, content security, trustworthy artificial intelligence, and intelligent network systems.</p>
  <p>I collaborate with researchers across computer science, artificial intelligence, multimedia, and cybersecurity. My recent research investigates social bot and anomalous-user detection, misinformation and stance analysis, graph learning, and large-language-model applications in social computing.</p>
</div>

## Research Interests

- Social computing and content security
- Social networks, misinformation, and social bot detection
- Trustworthy AI, graph learning, and large language models
- Mobile Internet, edge computing, cloud computing, and data-center networks

## Education

- **Ph.D. in Computer Science**, Beijing University of Posts and Telecommunications, July 2015
- **Visiting Ph.D. in Computer Engineering**, University of Toronto, March 2013–September 2014
- **B.Eng. in Information Engineering**, Nanjing University of Information Science and Technology, July 2009

## Current Focus

My current work brings together graph-based reasoning, multimodal learning, and foundation models to study trustworthy information diffusion and intelligent agents in open social environments.

<section class="home-selected-publications" markdown="1">

## Selected Publications

### Social Computing & Content Security

{% bibliography --query @*[homepage_group=social] %}

### Graph Learning & Trustworthy AI

{% bibliography --query @*[homepage_group=graph] %}

### Multimodal & Intelligent Systems

{% bibliography --query @*[homepage_group=systems] %}

</section>

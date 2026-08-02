---
layout: page
permalink: /publications/
title: Publications
description: Peer-reviewed journal and conference publications, listed in reverse chronological order.
nav: true
nav_order: 2
---

<style>
  body {
    font-family: Roboto, "Noto Serif SC", "Songti SC", "STSong", SimSun, sans-serif;
    background-color: #fbfaf6;
    background-image: linear-gradient(rgba(251, 250, 246, 0.78), rgba(251, 250, 246, 0.86)), url("{{ '/assets/img/shanshui-hero.png' | relative_url }}");
    background-position: center top;
    background-size: cover;
    background-attachment: fixed;
  }
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
  a, .navbar-nav .nav-item.active > .nav-link { color: #2f6b5f !important; }
  a:hover, .navbar-nav .nav-link:hover { color: #244f47 !important; }
  html[data-theme="dark"] a, html[data-theme="dark"] .navbar-nav .nav-item.active > .nav-link { color: #78b6a7 !important; }
  html[data-theme="dark"] a:hover, html[data-theme="dark"] .navbar-nav .nav-link:hover { color: #9bc9bd !important; }
  .navbar-nav .nav-item:not(.active) > .nav-link { color: var(--global-text-color) !important; }
  html[data-theme="dark"] body { background-color: #171b1a; background-image: linear-gradient(rgba(23, 27, 26, 0.74), rgba(23, 27, 26, 0.86)), url("{{ '/assets/img/shanshui-hero.png' | relative_url }}"); }
  @media (max-width: 576px) { body { background-position: 62% top; background-attachment: scroll; } }
  .publications .author > em {
    border-bottom: 0;
    color: var(--global-text-color);
    font-style: normal;
    font-weight: 700;
  }
  .publications .links a.btn {
    display: inline-block;
    margin: 0.35rem 0.35rem 0 0;
    padding: 0.28rem 0.72rem;
    border: 1px solid var(--global-theme-color);
    border-radius: 0.2rem;
    color: var(--global-theme-color);
    font-size: 0.78rem;
    line-height: 1.2;
  }
  .publications .links a.btn:hover {
    background: var(--global-theme-color);
    color: var(--global-hover-text-color);
    text-decoration: none;
  }
  .publications ol.bibliography {
    list-style: decimal;
    padding-left: 2.25rem;
  }
  .publications ol.bibliography > li {
    padding-left: 0.35rem;
  }
  .publications ol.bibliography > li::marker {
    color: var(--global-theme-color);
    font-weight: 600;
  }
</style>

The bibliography below is generated from a single BibTeX catalogue. Records were migrated from the archived publication collection; DOI links are shown only where they could be verified from the source document.

{% include bib_search.liquid %}

<div class="publications">

{% bibliography %}

</div>

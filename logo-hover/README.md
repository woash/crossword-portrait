# Portfolio logo hover section

Live: https://woash.github.io/crossword-portrait/logo-hover/

## Embed in Webflow

Paste the contents of `webflow-embed.html` into a Webflow Code Embed element. Make the element full width and publish your page. The section background is transparent; change the iframe height in the snippet if needed.

## Editing

Edit `build.py` and run `python3 build.py` to regenerate `index.html` and `section-source.html`. Hosted project images are listed in `images`; the first three are displayed. The SVG is in `assets/logo.svg`.

The original SVG words separate periodically to reveal three images. Each opening features the next image with two thinner previews. Hovering any image enlarges it to the same size and pauses the cycle. Reduced-motion preferences keep the images revealed without the opening cycle. Clicking navigates to https://www.aashitaverma.com/work in the full page.

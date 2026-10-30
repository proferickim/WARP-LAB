# Research image sources

The images below are extracted from the author's supplied papers. They show the
systems and experiments described in those publications; they are not photographs of the
current WARP Lab rooms. Original source PDFs are not included in this repository.
The images retain the rights of their respective authors and publishers.

| Website asset | Source and location | Treatment |
| --- | --- | --- |
| `images/research/full-duplex-network-overview.webp` | *A State-of-the-Art Survey on Full-Duplex Network Design*, Proceedings of the IEEE, 2024, Fig. 1, PDF page 3. [Paper](https://ieeexplore.ieee.org/document/10449676) | Complete embedded figure extracted and resized; original colors and labels retained. |
| `images/research/isac-testbed.webp` | *Pilot Allocation for OFDM Uplink ISAC Under RF Imperfections: Analysis, Prototyping, and Tradeoffs*, IEEE WCL, 2026, Fig. 3, PDF page 4. [Paper](https://ieeexplore.ieee.org/document/11611185) | Embedded photograph extracted; empty wall cropped; resized for the web. |
| `images/research/isac-experiment.webp` | Same paper, Fig. 3, PDF page 4. | Complete figure extracted and resized. |
| `images/research/semantic-testbed.webp` | *Bridging Neural Networks And Wireless Systems with MIMO-OFDM Semantic Communications*, IEEE Wireless Communications, 2025, Fig. 2, PDF page 3. [Paper](https://ieeexplore.ieee.org/document/11175613) | Testbed area captured from the figure; original annotations retained. |
| `images/research/semantic-architecture.webp` | Same paper, Fig. 2, PDF page 3. | Complete system figure captured. |
| `images/research/flexible-duplex-testbed.webp` | *Low Complexity Frequency Domain Nonlinear Self-Interference Cancellation for Flexible Duplex*, IEEE TWC, 2025, Fig. 8(a), PDF page 13. [Paper](https://ieeexplore.ieee.org/document/10948162) | Panel (a) cropped from the embedded figure. |
| `images/research/zero-if-testbed.webp` | *Frequency-Domain Nonlinear Self-Interference Cancellation in Full-Duplex Zero-IF Transceivers: From Algorithm to Prototype*, IEEE Internet of Things Journal, Fig. 12, PDF page 13. | Complete experimental figure captured. |

Photographs have not been generated, recolored, or reconstructed. WebP compression
and cropping are the only image changes. Each image on the site links to the
relevant research area or publication, and the Research page provides larger figures.

## Updating the homepage

- Replace the main figure: `images/research/full-duplex-network-overview.webp`; update its dimensions and caption in `_pages/home.html` if needed.
- Research photographs and captions: `_data/research.yml`.
- Short homepage news: `short` in `_data/news.yml`; full news text remains in `text`.
- Colors and layout: `css/main.scss`. Night is the initial theme; the header Light/Dark button remembers the visitor's choice.
- Theme behavior: `js/site.js`, with the initial preference restored in `_includes/head.html`.

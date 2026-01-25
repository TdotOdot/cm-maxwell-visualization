# CM-Maxwell Electromagnetic Wave Visualization

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18364711.svg)](https://doi.org/10.5281/zenodo.18364711)

Visualization code for electromagnetic wave structure derived from the Cognitional Mechanics (CM) unified Maxwell equation.

## Overview

This repository provides a Python implementation for visualizing the electromagnetic wave solution of the CM-Maxwell unified equation:
```
(1/c ∂/∂t + ∇·) F = J
```

The visualization demonstrates:
- Orthogonal relationship between **E** (electric field), **B** (magnetic field), and **S** (Poynting vector)
- Phase synchronization across field components
- Energy flux direction and wave propagation

![EM Wave Visualization](figures/em_wave_preview.png)

## Repository Structure
```
.
├── code/
│   ├── em_wave_analysis.py    # Main visualization script
│   ├── requirements.txt        # Python dependencies
│   └── README.md              # Usage instructions
├── paper/
│   ├── cm_maxwell_wave_visualization.tex
│   ├── cm_maxwell_wave_visualization.pdf
│   └── fig1.png
├── figures/
│   └── .gitkeep
└── LICENSE
```

## Quick Start
```bash
cd code
pip install -r requirements.txt
python em_wave_analysis.py
```

Open `em_wave_analysis.html` in your browser for interactive 3D visualization.

## Related Publications

- **Main Paper**: T.O., "A Unified Maxwell Equation Derived from Cognitional Mechanics: A Practical Foundation for Engineering Electromagnetics," Zenodo, 2026. DOI: [10.5281/zenodo.18312668](https://doi.org/10.5281/zenodo.18312668)
- **This Supplement**: T.O., "Visualization of Electromagnetic Wave Structure from CM-Maxwell Unified Equation," Zenodo, 2026. DOI: [10.5281/zenodo.18364711](https://doi.org/10.5281/zenodo.18364711)

## Citation

If you use this code in your research, please cite:
```bibtex
@article{to2026cmviz,
  author = {T.O.},
  title = {Visualization of Electromagnetic Wave Structure from the CM-Maxwell Unified Equation},
  year = {2026},
  publisher = {Zenodo},
  doi = {10.5281/zenodo.18364711},
  url = {https://doi.org/10.5281/zenodo.18364711}
}
```

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contact

For questions related to Cognitional Mechanics theory, see the [CM-GUT series](https://zenodo.org/communities/cm-gut).
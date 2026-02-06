# Electromagnetic Wave Visualization Code

Python implementation for visualizing electromagnetic wave structure from the CM-Maxwell unified equation.

## Requirements

- Python 3.8+
- numpy >= 1.24.0
- plotly >= 5.14.0

## Installation
```bash
pip install -r requirements.txt
```

## Usage

### Basic Execution
```bash
python em_wave_analysis.py
```

This generates `em_wave_analysis.html` in the current directory. Open it in any modern web browser for interactive 3D visualization.

### Output Description

The visualization shows:

- **Red arrows**: Electric field **E** at discrete z positions
- **Blue arrows**: Magnetic field **B** at discrete z positions  
- **Green arrows**: Poynting vector **S** = (1/μ₀)**E**×**B**
- **Red helix**: Continuous trajectory of **E** field
- **Blue helix**: Continuous trajectory of **B** field

All three vectors (**E**, **B**, **S**) originate from the same point on the z-axis, demonstrating their orthogonal relationship and phase synchronization.

## Customization

### Key Parameters

Edit `em_wave_analysis.py` to adjust:
```python
# Line 6-7: Wave parameters
wavelength = 1.0          # Wavelength in meters
num_positions = 12        # Number of sample points along z

# Line 12-15: Arrow display
arrow_length = 0.5        # Base arrow length
head_length = 0.1         # Arrow head length
head_width = 0.05         # Arrow head radius
shaft_width = 6           # Arrow shaft line width
```

### Camera View

Modify line 121 to change viewing angle:
```python
camera=dict(eye=dict(x=-1.8, y=-1.8, z=1.5))
```

- Positive x/y: View from positive quadrant
- Negative x/y: View from negative quadrant (current: ensures +z points away from viewer)
- z: Elevation angle

### Field Strength Ratio

Line 98-99 controls E/B visual length relative to S:
```python
u_E = arrow_length * 0.55 * np.cos(phase[idx])  # 0.55 = scaling factor
```

Adjust `0.55` to balance visual appearance (physical lengths are equal in the equations).

## Physical Interpretation

The code implements the plane wave solution in vacuum:
```
E(z,t) = E₀ cos(kz - ωt) x̂
B(z,t) = B₀ cos(kz - ωt) ŷ  
S(z,t) = (1/μ₀) E × B = const ẑ
```

Where:
- k = 2π/λ (wave number)
- c = 1/√(ε₀μ₀) (speed of light)
- **E** ⊥ **B** ⊥ **S** (mutual orthogonality)

## Troubleshooting

**Issue**: Arrows appear too small/large  
**Solution**: Adjust `arrow_length` parameter

**Issue**: Colors hard to distinguish  
**Solution**: Modify color strings in `add_arrow()` calls (lines 96-107)

**Issue**: Browser performance issues  
**Solution**: Reduce `num_positions` or helix resolution (line 110: `z_fine` divisions)

## Technical Notes

- Arrow construction uses manual mesh geometry (not Plotly Cone) for consistent visual sizing
- Camera position set to ensure +z propagation direction points away from viewer
- Annotations positioned in 3D space; may require adjustment if parameters change significantly

## License

MIT License - see repository root LICENSE file.
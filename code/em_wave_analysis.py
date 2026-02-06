# em_wave_analysis.py
import numpy as np
import plotly.graph_objects as go

wavelength = 1.0
k = 2 * np.pi / wavelength
num_positions = 12

z_positions = np.linspace(0, 6.0, num_positions)
phase = k * z_positions

arrow_length = 0.5
head_length = 0.1
head_width = 0.05
shaft_width = 6

def add_arrow(fig, x0, y0, z0, u, v, w, color):
    norm = np.sqrt(u**2 + v**2 + w**2)
    if norm < 1e-10:
        return
    
    u_norm, v_norm, w_norm = u/norm, v/norm, w/norm
    
    shaft_end_x = x0 + u_norm * (arrow_length - head_length)
    shaft_end_y = y0 + v_norm * (arrow_length - head_length)
    shaft_end_z = z0 + w_norm * (arrow_length - head_length)
    
    fig.add_trace(go.Scatter3d(
        x=[x0, shaft_end_x], y=[y0, shaft_end_y], z=[z0, shaft_end_z],
        mode='lines', line=dict(color=color, width=shaft_width),
        showlegend=False, hoverinfo='skip'
    ))
    
    apex_x = x0 + u_norm * arrow_length
    apex_y = y0 + v_norm * arrow_length
    apex_z = z0 + w_norm * arrow_length
    
    perp1 = np.array([-v_norm, u_norm, 0]) if abs(w_norm) > 0.9 else np.array([0, -w_norm, v_norm])
    perp1_norm = np.linalg.norm(perp1)
    perp1 = perp1 / perp1_norm if perp1_norm > 1e-10 else np.array([1, 0, 0])
    perp2 = np.cross([u_norm, v_norm, w_norm], perp1)
    
    theta = np.linspace(0, 2*np.pi, 8, endpoint=False)
    base_x = shaft_end_x + head_width * (perp1[0]*np.cos(theta) + perp2[0]*np.sin(theta))
    base_y = shaft_end_y + head_width * (perp1[1]*np.cos(theta) + perp2[1]*np.sin(theta))
    base_z = shaft_end_z + head_width * (perp1[2]*np.cos(theta) + perp2[2]*np.sin(theta))
    
    for i in range(8):
        fig.add_trace(go.Mesh3d(
            x=[apex_x, base_x[i], base_x[(i+1)%8]],
            y=[apex_y, base_y[i], base_y[(i+1)%8]],
            z=[apex_z, base_z[i], base_z[(i+1)%8]],
            i=[0], j=[1], k=[2], color=color, opacity=1.0,
            showlegend=False, hoverinfo='skip'
        ))

fig = go.Figure()

for idx in range(len(z_positions)):
    x0, y0, z0 = 0, 0, z_positions[idx]
    
    u_E = arrow_length * 0.55 * np.cos(phase[idx])
    v_E = arrow_length * 0.55 * np.sin(phase[idx])
    add_arrow(fig, x0, y0, z0, u_E, v_E, 0, 'red')
    
    u_B = -arrow_length * 0.55 * np.sin(phase[idx])
    v_B = arrow_length * 0.55 * np.cos(phase[idx])
    add_arrow(fig, x0, y0, z0, u_B, v_B, 0, 'blue')
    
    add_arrow(fig, x0, y0, z0, 0, 0, arrow_length, 'green')

z_fine = np.linspace(0, 6.0, 480)
phase_fine = k * z_fine
fig.add_trace(go.Scatter3d(x=np.cos(phase_fine), y=np.sin(phase_fine), z=z_fine, mode='lines', line=dict(color='red', width=1), showlegend=False))
fig.add_trace(go.Scatter3d(x=-np.sin(phase_fine), y=np.cos(phase_fine), z=z_fine, mode='lines', line=dict(color='blue', width=1), showlegend=False))

annotations = [
    dict(x=1.2, y=0, z=3, text="E: Electric field<br>E(z,t) = E₀ cos(kz-ωt)", showarrow=False, font=dict(size=10, color='red')),
    dict(x=0, y=1.2, z=3, text="B: Magnetic field<br>B(z,t) = B₀ cos(kz-ωt)", showarrow=False, font=dict(size=10, color='blue')),
    dict(x=0, y=0, z=4, text="S: Poynting vector<br>S = (1/μ₀)E×B<br>Energy flux +z direction", showarrow=False, font=dict(size=10, color='green')),
    dict(x=1.3, y=0, z=0.5, text="Red helix: E field trajectory", showarrow=False, font=dict(size=9, color='darkred')),
    dict(x=0, y=1.3, z=1, text="Blue helix: B field trajectory", showarrow=False, font=dict(size=9, color='darkblue'))
]

fig.update_layout(
    title="Electromagnetic Wave Structure (CM-Maxwell unified equation)<br>Wave propagates in +z direction",
    scene=dict(
        xaxis_title="X", yaxis_title="Y", zaxis_title="Z (propagation direction)",
        aspectmode='manual',
        aspectratio=dict(x=0.7, y=0.7, z=1.0),
        camera=dict(eye=dict(x=-1.8, y=-1.8, z=1.5)),
        annotations=annotations
    )
)

fig.write_html("em_wave_analysis.html")
print("✅ saved: em_wave_analysis.html")
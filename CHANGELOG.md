# Changelog

## [0.2.0] - 2026-05-16
### Added
- ✨ **Complete Lighting System** with 5 professional presets (Studio, Outdoor, Dramatic, Soft, Neon)
- 💡 **Three-Point Lighting Generator** with automatic light positioning and energy configuration
- ⏱️ **Dynamic Animation Support** with keyframe automation for intensity and color changes
- 🌍 **Ambient Lighting Control** for world background configuration
- 🖱️ **Lighting UI Panel** with one-click preset buttons in Blender interface
- 📚 **Comprehensive Documentation** with guides, API reference, and workflow examples
- 🎬 **Professional Light Types**: Sun, Spot, Area, and Point lights optimized for each preset
- ✅ **Simulation-Safe Code**: Works both inside Blender and standalone Python

### Generators
- `src/anim3d/generators/lighting.py` — Complete lighting module (13KB, 400+ lines)
- `src/anim3d/ui/panels_lighting.py` — UI with operator integration (6KB, 200+ lines)

### Documentation
- `LIGHTING_GUIDE.md` — 5000+ words comprehensive guide with examples
- `LIGHTING_FIX.md` — Feature summary and quick reference

### Enhanced
- `src/anim3d/__init__.py` — Updated to v0.2.0, improved registration
- `src/anim3d/ui/panels_main.py` — Integrated with lighting system
- `src/anim3d/operators.py` — Professional operator classes
- `src/anim3d/generators/__init__.py` — Module initialization

## [0.1.0] - 2026-05-15
### Added
- Initial release of Anim3D Blender addon
- Project structure and base modules
- Addon metadata and installation instructions

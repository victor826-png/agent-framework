# Third-party source snapshots

These are ordinary folders tracked by this repository, so their files can be browsed and edited
without initializing Git submodules. Each folder is a source snapshot of the linked upstream
repository and its original Git history is not included. PyTorch's pinned nested dependencies and
EBGeometry's example mesh data are included as source folders too.

Microsoft Agent Framework itself is the current repository and is not duplicated here.

| Directory | Upstream | Purpose |
| --- | --- | --- |
| `TorchSharp` | [dotnet/TorchSharp](https://github.com/dotnet/TorchSharp) | PyTorch bindings for .NET |
| `pytorch` | [pytorch/pytorch](https://github.com/pytorch/pytorch) | PyTorch, including its pinned nested dependencies |
| `PicoGK` | [leap71/PicoGK](https://github.com/leap71/PicoGK) | Geometry kernel |
| `ShapeKernel` | [leap71/LEAP71_ShapeKernel](https://github.com/leap71/LEAP71_ShapeKernel) | Higher-level geometry operations |
| `HelixHeatX` | [leap71/LEAP71_HelixHeatX](https://github.com/leap71/LEAP71_HelixHeatX) | Geometry and thermal-design example |
| `cgal` | [CGAL/cgal](https://github.com/CGAL/cgal) | Computational geometry |
| `EBGeometry` | [rmrsk/EBGeometry](https://github.com/rmrsk/EBGeometry) | Header-only implicit geometry and spatial queries |
| `AMGX` | [NVIDIA/AMGX](https://github.com/NVIDIA/AMGX) | GPU-accelerated linear solvers |
| `amrex` | [AMReX-Codes/amrex](https://github.com/AMReX-Codes/amrex) | Adaptive-mesh scientific computing |
| `NanoVDB` | [AcademySoftwareFoundation/openvdb/nanovdb](https://github.com/AcademySoftwareFoundation/openvdb/tree/master/nanovdb) | Optimized sparse-volume representation for GPUs |
| `fvdb-core` | [openvdb/fvdb-core](https://github.com/openvdb/fvdb-core) | Sparse volumetric operations integrated with PyTorch |
| `OpenUSD` | [PixarAnimationStudios/OpenUSD](https://github.com/PixarAnimationStudios/OpenUSD) | Scene description, hierarchies, transforms, and geometry |
| `Assimp` | [assimp/assimp](https://github.com/assimp/assimp) | 3D asset import and export |
| `Imath` | [AcademySoftwareFoundation/Imath](https://github.com/AcademySoftwareFoundation/Imath) | Vector, matrix, and transformation math |
| `LEAP71_LatticeLibrary` | [leap71/LEAP71_LatticeLibrary](https://github.com/leap71/LEAP71_LatticeLibrary) | Lattice generation with PicoGK and ShapeKernel |
| `LEAP71_RoverWheel` | [leap71/LEAP71_RoverWheel](https://github.com/leap71/LEAP71_RoverWheel) | Multi-layer rover wheel geometry |
| `LEAP71_QuasiCrystals` | [leap71/LEAP71_QuasiCrystals](https://github.com/leap71/LEAP71_QuasiCrystals) | Quasi-crystal geometry examples |
| `PicoGKRuntime` | [leap71/PicoGKRuntime](https://github.com/leap71/PicoGKRuntime) | C++ runtime for the PicoGK geometry kernel |
| `PicoGKInstaller` | [leap71/PicoGKInstaller](https://github.com/leap71/PicoGKInstaller) | Installer for the PicoGK Runtime |

Each project retains its own upstream license and notices. Review the applicable terms before
redistributing or combining these projects in a product. These snapshots do not guarantee that
each project builds with the same toolchain or configuration.

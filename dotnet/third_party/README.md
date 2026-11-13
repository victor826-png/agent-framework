# Third-party source snapshots

This directory contains source snapshots as ordinary tracked folders. Their original upstream Git history is not presumed to be included. The inventory below covers the 18 directories currently represented here; **priority is a sequencing aid, not a claim that a dependency is integrated or buildable**.

The machine-readable inventory is [THIRD_PARTY_MANIFEST.json](THIRD_PARTY_MANIFEST.json). It records upstream URLs, priority, locally evidenced license metadata, and explicit unknowns. Upstream commit IDs remain `unknown` unless independently verified. Build status is `not_verified`: this inventory does not claim that these projects compile or pass tests.

Microsoft Agent Framework itself is the current repository and is not duplicated here.

| Directory | Upstream | Purpose | Priority |
| --- | --- | --- | --- |
| `TorchSharp` | [dotnet/TorchSharp](https://github.com/dotnet/TorchSharp) | PyTorch bindings for .NET | P0 |
| `PicoGK` | [leap71/PicoGK](https://github.com/leap71/PicoGK) | Geometry kernel | P0 |
| `ShapeKernel` | [leap71/LEAP71_ShapeKernel](https://github.com/leap71/LEAP71_ShapeKernel) | Higher-level geometry operations | P0 |
| `HelixHeatX` | [leap71/LEAP71_HelixHeatX](https://github.com/leap71/LEAP71_HelixHeatX) | Geometry and thermal-design example | P1 |
| `cgal` | [CGAL/cgal](https://github.com/CGAL/cgal) | Computational geometry | P0 |
| `EBGeometry` | [rmrsk/EBGeometry](https://github.com/rmrsk/EBGeometry) | Header-only implicit geometry and spatial queries | P0 |
| `AMGX` | [NVIDIA/AMGX](https://github.com/NVIDIA/AMGX) | GPU-accelerated linear solvers | P0 |
| `amrex` | [AMReX-Codes/amrex](https://github.com/AMReX-Codes/amrex) | Adaptive-mesh scientific computing | P0 |
| `NanoVDB` | [AcademySoftwareFoundation/openvdb/nanovdb](https://github.com/AcademySoftwareFoundation/openvdb/tree/master/nanovdb) | Optimized sparse-volume representation for GPUs | P0 |
| `fvdb-core` | [openvdb/fvdb-core](https://github.com/openvdb/fvdb-core) | Sparse volumetric operations integrated with PyTorch | P0 |
| `OpenUSD` | [PixarAnimationStudios/OpenUSD](https://github.com/PixarAnimationStudios/OpenUSD) | Scene description, hierarchies, transforms, and geometry | P0 |
| `Assimp` | [assimp/assimp](https://github.com/assimp/assimp) | 3D asset import and export | P1 |
| `Imath` | [AcademySoftwareFoundation/Imath](https://github.com/AcademySoftwareFoundation/Imath) | Vector, matrix, and transformation math | P1 |
| `LEAP71_LatticeLibrary` | [leap71/LEAP71_LatticeLibrary](https://github.com/leap71/LEAP71_LatticeLibrary) | Lattice generation with PicoGK and ShapeKernel | P1 |
| `LEAP71_RoverWheel` | [leap71/LEAP71_RoverWheel](https://github.com/leap71/LEAP71_RoverWheel) | Multi-layer rover wheel geometry | P1 |
| `LEAP71_QuasiCrystals` | [leap71/LEAP71_QuasiCrystals](https://github.com/leap71/LEAP71_QuasiCrystals) | Quasi-crystal geometry examples | P1 |
| `PicoGKRuntime` | [leap71/PicoGKRuntime](https://github.com/leap71/PicoGKRuntime) | C++ runtime for the PicoGK geometry kernel | P1 |
| `PicoGKInstaller` | [leap71/PicoGKInstaller](https://github.com/leap71/PicoGKInstaller) | Installer for the PicoGK Runtime | P1 |

The PicoGKInstaller snapshot also contains a `.gitmodules` file declaring five nested submodule paths. Those declarations are recorded in the manifest; their presence does not mean the nested folders have been initialized or verified as materialized.

## License and integration notes

- A license is identified only where a license file or project metadata was observed in this snapshot. An `unknown_or_requires_review` entry is not permission to redistribute.
- CGAL and other projects may have component-specific terms. Review the exact components and dependencies before combining or distributing them.
- A source folder is not evidence of a successful build, a supported runtime, or an agent-facing integration.
- `pytorch` is intentionally absent from this inventory: its third-party snapshot was removed from the current repository state. TorchSharp remains a separate .NET binding project; this does not vendor the PyTorch source tree.

## Verification

From the repository root, run:

```sh
python3 eng/verify-third-party.py
```

The script uses only the Python standard library. It checks that manifest paths exist, directory names are unique, priorities and upstream URLs are well-formed, README rows match the manifest, and the removed PyTorch directory is not reintroduced. It does not build dependencies or certify license compatibility.

# Third-party repositories

The repositories below are tracked as Git submodules so the Agent Framework repository stores
their pinned revisions rather than copying their source and history into this repository.
Microsoft Agent Framework itself is the current repository and is not duplicated here.

Initialize the top-level source repositories from the repository root:

```sh
git submodule update --init
git -C dotnet/third_party/pytorch submodule update --init --recursive --depth 1
git -C dotnet/third_party/EBGeometry submodule update --init --depth 1
```

PyTorch's nested submodules are required by its build. EBGeometry is header-only; its nested
`common-3d-test-models` submodule supplies example meshes. TorchSharp currently has an upstream
`vision` gitlink without a corresponding `.gitmodules` entry, so avoid recursive initialization
of TorchSharp until upstream provides its mapping.

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

Each project retains its own upstream license and notices. Review the applicable terms before
redistributing or combining these projects in a product. The submodules pin source revisions;
they do not guarantee that each project builds with the same toolchain or configuration.

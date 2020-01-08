# HiPS : Hierarchical Petri net Simulator

## Overview

HiPS tool is developed at the Department of Computer Science and Engineering,
Shinshu University, which is a tool design and analysis of Petri nets, 
developed using Microsoft Visual C # and C++. HiPS tool has a way of intuitive
GUI which enable hierarchical and/or timed-net design. HiPS tool has also 
functioned of static/dynamic analysis: T-invariant detection, Reachability 
path analysis, deadlock state detection, and k-boundedness analysis. Also, 
it is possible to perform a random walk simulation with each firing steps.

- SourceForge http://sourceforge.net/projects/hips-tools/
- introduction video https://youtu.be/usF1JrQegOE

## Features

- Design Entry based on Hierarchical Petri nets
- Incidence Matrix and Invariant Checking for P/T-net (T-invariant and 
  S-invariant)
- Structural Properties Checking for P/T-net (Structurally Bounded, 
  (Partially) Conservative, (Partially) Repetitive, and (Partially) Consistent)
- Behavioral Analysis for P/T-net (Reachability, Deadlock, Reversibility and 
  Synchronic Distances)
- Liveness and Safeness Properties Checking for Free-Choice (Subclass) net
- Process Trace Graph Generator using High Speed and Memory Efficiency Algorithm
- Multi-Threaded Implementations (Partially Support)
- Step-by-Step Random-Walk Simulation for P/T and High-level net
- Timeline Step-Magnitude Continuous Simulation for P/T-net

## Documentation / samples

- users manual : http://hips-tools.sourceforge.net/wiki/index.php/Users_Manual_(en)_for_1.x
- model examples : https://sourceforge.net/projects/hips-tools/files/version%201.x/examples/

## Installation instructions

Unzip this archive file, then copy your own directory which has read/write 
privilege of your system.

We require the Microsoft Visual Studio 2017 redistributable package.
https://go.microsoft.com/fwlink/?LinkId=746572

If this is not already installed on your system, it is included as vc_redist.x64.exe 
in the zip file.

## References

If you use HiPS Tool for your research, we would appreciate it if you would refer to 
the following papers:

Yojiro HARIE, Yuta MITSUI, Kohei FUJIMORI, Amit BATAJOO, Katsumi WASAKI :
HiPS: Hierarchical Petri Net Design, Simulation, Verification and Model Checking Tool ; 
Proceedings of the 6th IEEE Global Conference on Consumer Electronics (GCCE 2017), 
pp.686-690, October, 2017.

## License

Creative Commons Attribution Non-Commercial Share Alike

## Contact

email: wasaki@cs.shinshu-u.ac.jp
website: https://sourceforge.net/projects/hips-tools/

Copyright: 2008-2019, Shinshu University, Nagano, Japan.


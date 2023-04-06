# Pipeline Simulator for Computer Architecture I Course

This repository contains a pipeline simulator for the Computer Architecture I course at Unisinos College of Computer Engineering. The simulator reads an input file containing assembly code and simulates its execution in a 5-stage pipeline. 
The pipeline stages are: instruction fetch, decode, execute, memory access, and write back.

The simulator also detects hazards that may occur during the execution of the instructions, helping students understand how hazards affect the performance and efficiency of a pipelined processor.

## Authors

- Felipe Drumm (FDrumm@edu.unisinos.br)
- Klaus Becker (BeckerKlaus@edu.unisinos.br)
- Mauro Moura  (MauroMoura@edu.unisinos.br)

## Course

- Computer Architecture I - UNISINOS College of Computer Engineering

## Professor

- Lucio Rene Prade

## Getting Started

This section will be updated with information about prerequisites, dependencies, and installation or setup processes once the project has been developed.

## Usage

To use this pipeline simulator, run the main script with the path to the assembly file as an argument:

```bash
python3 pipeline_simulator.py path/to/your/assembly/file.s

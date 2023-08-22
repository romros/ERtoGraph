# utils.py

import pygraphviz as pgv
import os


def dot_to_svg(dot_string, output_directory, output_filename="graph"):
    """
    Convert a DOT string to an SVG file.

    Parameters:
    - dot_string: str - The input DOT string.
    - output_directory: str - The directory where the SVG will be saved.

    Returns:
    - str: Path to the generated SVG file.
    """

    # Guarda el fitxer DOT
    dot_file = os.path.join(output_directory, output_filename + ".dot")
    with open(dot_file, 'w') as file:
        file.write(dot_string)

    # Create a graph from the DOT string
    graph = pgv.AGraph(string=dot_string)

    # Define the output file name (could use a timestamp or UUID for uniqueness)
    output_file = os.path.join(output_directory, output_filename + ".svg")

    # Save the graph as an SVG
    graph.draw(output_file, prog="dot", format="svg")

    return dot_file, output_file  # Retorna ambdós camins

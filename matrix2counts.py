#!/usr/bin/env python

""" This script creates a network plot with the main players in the given research field
    (adapted from Olivia Tanuwidjaja's post on
    https://towardsdatascience.com/discovering-entity-connections-insights-using-network-analytics-part-2-d445751413b3 )

    
    Requirements
    ------------

    Excel file with two sheets: one with papers and respective papers and another with the authors and respective affiliations
    (check provided file authors.xlsm for an example)

    
    Parameters
    ----------

    filepath : string
               Path to the Excel file.

    use_affiliations : boolean
                       Whether to use the authors' affiliation to color the respective nodes.
                       Defauts to True.

    remove_single : boolean
                    Whether to remove edges (and, consequently, some nodes) between authors that only share a single paper.
                    Defaults to True.

    colormap : string
               Name of matplotlib colormap to use to color nodes.
               Defaults to 'viridis'.     
"""

# local
from utils_authors_affil import get_node_size_by_papers, get_affiliations
from utils_network import get_network_body, plot_network

__author__ = "Ana Sofia Carmo (anascacais@gmail.com)"
__credits__ = ["Ana Sofia Carmo", "Olivia Tanuwidjaja"]


def main(filepath, use_affiliations=True, remove_single=True, colormap='viridis'):

    G = get_network_body(filepath, remove_single)

    node_size = get_node_size_by_papers(G, filepath)
    legend, node_color = get_affiliations(G, filepath, use_affiliations, colormap)

    plot_network(G, node_size, node_color, legend, remove_single, colormap)


if __name__ == '__main__':
    main(filepath='authors.xlsm')
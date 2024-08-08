# Network Analytics

## _A visualization tool to help uncover the main players within a research field_

## Why network plots?

Network plots (aka network graphs) provide a visualization of relationships or connections (and their magnitude) between entities. Uses of network plots include:

- Identification of the players within a field, and how they are positioned in comparison to the others
- Visualization of the individual relationships between the players and the magnitude of that relationship

## What we are trying to understand?

In this case, I used network plots to understand who were the main players in the research field of seizure forecast. The main objectives were to answer the following questions:

**Q1:** Who are the most "prolific" authors in the field of seizure forecast?  
**Q2:** Are there specific research entities that have particularly large contributions to the field?  
**Q3:** How do authors / research entities collaborate?

## Exploring data

Data collection followed a review of the state-of-the-art on seizure forecast, and required the report of 1) name of the authors for each entry (i.e. paper) and 2) main affiliation of each author. Unfortunately, since bibliography management software programs don't (yet) support affiliation report, I ended up doing this step manually.

Then, for the visualization, I started on a post by Olivia Tanuwidjaja on [Discovering entity connections insights using Network Analytics][credit], and adapted so that:

- Nodes represent authors;
- Edges represent co-authorship of a paper between two authors (and closeness alludes to frequency of authorship);
- The color of a node corresponds to one of the affiliations of the corresponding author;
- The size of a node is proportional to the number of papers the corresponding author has authorship;
- The resulting network can help identify not only research entities, as well as groups that often work together!

![Research Network - Seizure Forecasting](research_network.png)

#### Q1. Most prolific authors

Since the size of the nodes represents the number of papers co-authored by that author, we can easily identify the most prolific authors, by looking for the largest nodes. In my case, M. Cook (Prof Mark Cook), P. Karoly (Philippa J Karoly, PhD), and B. Brinkmann (Benjamin Brinkmann, PhD) particularly stood out.

#### Q2. Most influential research entities

Again, since the color of the nodes corresponds to the affiliation of the author, we can combine this information with the size of the nodes to identify which research entities publish more in the field. Firstly, the frequency of names with the color yellow (University of Melbourne, Australia) is apparent; and more specifically, two of the most prolific authors belong to this research entity (of course, being commonly co-authors, as seen by the closeness of their nodes).

Other relevant entities include Mayo Clinic and University of Freiburg.

#### Q3. A look int collaborations

Interestingly, we can immediately identify a large conglomerate of nodes pertaining to authors from the University of Melbourne, Mayo Clinic, SeizureTracker, Epilepsy Foundation (with Sonya Dumanis, PhD, in particular), and King's College London.

## License

MIT

[credit]: https://towardsdatascience.com/discovering-entity-connections-insights-using-network-analytics-part-2-d445751413b3

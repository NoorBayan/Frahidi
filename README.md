# Frahidi: Advancing Classical Arabic Poetry Analysis with Modern AI Techniques

 <p align="center"> 
 <img src = "https://raw.githubusercontent.com/NoorBayan/Frahidi/main/images/FarahidiLogo1.png" width = "300px"/>
 </p>
 
Welcome to Frahidi, a comprehensive system designed to perform prosodic tasks for classical Arabic poetry. Frahidi generates high-quality datasets that can be used for fine-tuning AI models, offering robust support for Arabic poetry's complex prosodic structure. This system follows the traditional principles of Arabic prosody while leveraging modern AI technologies.

## Table of Contents
1. [Introduction](#introduction)
2. [System Overview](#system-overview)
3. [Data Preparation](#data-preparation)
4. [Model Construction](#model-construction)
   - [Prosodic Writing](#prosodic-writing)
   - [Meter and Taf’ilat Detection](#meter-and-tafilat-detection)
   - [Fine-grained Prosodic Analysis](#fine-grained-prosodic-analysis)
5. [Visualization of Results](#visualization-of-results)
6. [Usage Instructions](#usage-instructions)
7. [Sample Outputs](#sample-outputs)
8. [Future Enhancements](#future-enhancements)
9. [Contributing](#contributing)

## Introduction
The Frahidi system is named after Al-Khalil ibn Ahmad Al-Farahidi, the founder of Arabic prosody. Its primary goal is to automate the tasks related to Arabic prosody, such as detecting poetic meters, identifying taf’ilat (prosodic units), and analyzing rhyme patterns. It generates a well-organized dataset designed for fine-tuning machine learning models to handle all prosodic tasks efficiently.

---

## System Overview
Frahidi’s architecture is divided into three main phases:
1. **Data Preparation** – Gathering, classifying, and cleansing poetry data for model training.
2. **Model Construction** – Building key components that analyze prosodic structure.
3. **Result Visualization** – Offering a clear and comprehensive view of prosodic outcomes.

---

## Data Preparation
In this phase, Frahidi aggregates, cleans, and verifies data from a vast corpus of Arabic poetry:
- **Data Sources**: Over 16 websites and 60 poetry blogs, including articles and books, are used to collect around 500,000 poems, amounting to over 15 million poetic verses.
- **Data Classification**: Poems are categorized based on language, meter, style, and subject matter. Frahidi employs custom algorithms for classification, filling gaps where pre-existing tags are missing.
- **Data Refinement**: After classification, a custom polishing model ensures the quality of each poetic verse for optimal processing.

---

## Model Construction

### Prosodic Writing
The core of Frahidi’s system is **Prosodic Writing**. This step converts written Arabic into its corresponding prosodic form:
- **Tashkeel (Diacritization)**: This crucial step assigns the correct vowel marks, handling the specific challenges of classical Arabic poetry.
- **Prosodic Rules Library**: Frahidi’s library contains a robust set of functions that apply traditional Arabic prosody rules to each poetic line.
- **Output**: The final result is a prosodically annotated verse, where only the spoken sounds are written.

 <p align="center"> 
 <img src = "https://raw.githubusercontent.com/NoorBayan/Frahidi/main/images/ProsodyWriting.png" width = "600px"/>
 </p>
 
### Meter and Taf’ilat Detection
Once a poem is converted into prosodic writing, Frahidi uses a custom encoding system (e.g., 0 for silent, 1 for vowelized, and 2 for unvowelized) to identify:
- **Poetic Meters**: Frahidi detects which of the 16 classical Arabic poetic meters (bahrs) the poem follows.
- **Taf’ilat Patterns**: Prosodic units (taf’ilat) are discovered by referencing six traditional prosody texts.

The Taf’ilat detection model consists of four main components:

1. **Encoding Model**: This component receives the output from the prosodic writing system and encodes the letters (0 for silent, 1 for vowelized, and 2 for unvowelized). Unfortunately, the provided vowelization model does not achieve full vowelization.

2. **Taf’ilat Patterns Database**: This component represents the solution space for all possible patterns.

3. **Pattern Detection Model**: Based on a search algorithm, this component explores the solution space. Due to the incomplete binary encoding caused by unvowelized letters, the search algorithm returns a set of near-optimal solutions rather than a single correct solution.

4. **Dynamic Oracle Model**: Trained in parallel with the poetic meter detection model, this oracle model refines the results by receiving the detected meter. Based on the meter, it eliminates irrelevant taf’ilat patterns and categorizes the remaining solutions into two groups based on proximity to the correct pattern using a threshold function. During training, the selection is diversified between the two groups, adjusting error margins and tuning parameters, similar to processes in linguistic analysis systems, to minimize error margins.


 <p align="center"> 
 <img src = "https://raw.githubusercontent.com/NoorBayan/Frahidi/main/images/Feet_Detection.png" width = "600px"/>
 </p>
 
### Fine-grained Prosodic Analysis
Frahidi further analyzes the poem for:
- **Modifications**: Handling exceptional cases such as metrical shifts (zihafat and ‘ilal).
- **Rhyme Rules**: It checks and analyzes rhyme patterns and resolves any structural issues.

 <p align="center"> 
 <img src = "https://raw.githubusercontent.com/NoorBayan/Frahidi/main/images/FineGrainedProsodicAnalysis.png" width = "700px"/>
 </p>
---

## Visualization of Results
Frahidi includes a visual component that presents all prosodic data in an intuitive, easily interpretable interface. Users can view:
- **Meter and Taf’ilat**: Visual representation of the poem’s prosodic structure.
- **Rhyme and Rhythm**: Detailed insights into rhyme patterns and rhythmic anomalies.


---

## Usage Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/Frahidi.git

### Explore Frahidi on Google Colab
To explore the full details of the Frahidi system and interact with its extensive features, access our interactive Google Colab notebook. This notebook provides an easy-to-use interface for searching, analyzing, and learning more about the Frahidi system.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1c2AsPfdwj4ELEypTEmsSTewtVQ8MVXP3?usp=drive_link)

 <p align="center">
   <img src = "https://raw.githubusercontent.com/NoorBayan/Frahidi/main/images/FarahidiColab.png" width = "800px"/>
 </p>

### Steps to Use Frahidi on Google Colab:
1. **Run the first cell** by clicking the "Run" button to load the necessary files and libraries.
2. **Execute the notebook**, and dropdown menus will appear with various poetry categories. You can experiment by selecting different options, and the corresponding poetic data will be displayed based on your choices.

## Sample Outputs
Here is an example of Frahidi's output:
 <p align="center"> 
 <img src = "https://raw.githubusercontent.com/NoorBayan/Frahidi/main/images/PoemVisualization.png" width = "700px"/>
 </p>

## Future Enhancements
- **Support for Dialects**: Expansion of the system to handle non-Classical Arabic.
- **Enhanced Visualization**: Additional features for real-time editing and correction of poetic verses.
- **Integration with Other AI Models**: Collaborating with other NLP models for more refined text generation and analysis.

## Contributing
We welcome contributions! Please refer to the [Contributing Guidelines](CONTRIBUTING.md) for more details.

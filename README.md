# File Manager Using B-Tree

![Python Badge](https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python&logoColor=FFFFFF)

![Status](https://img.shields.io/badge/Status-Completed-green)  ![License](https://img.shields.io/badge/License-MIT-yellow.svg) 

## About the Project
This project is a Python-based file manager and image retrieval system built using a custom B-Tree data structure and a graphical user interface. The application allows users to manage image files stored in the **Banco_Imagens** folder by performing operations such as insertion, deletion, search, and in-order display of the stored image entries.

Developed by **Abner Augusto Pereira Diniz** (RA: 168476) at the Universidade Federal de São Paulo, the project demonstrates how B-Trees can be used to efficiently organize and retrieve files. It leverages a modern GUI built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) and image processing through [Pillow (PIL)](https://python-pillow.org/).

## :hammer: Features

- **B-Tree Implementation**:  
  - **Insertion**: Supports both individual (Insertion Type 1) and bulk insertion (Insertion Type 2) while maintaining lexicographical order.
  - **Search**: Retrieves images based on partial filename matches (category-based search).
  - **Deletion**: Deletes all images associated with a specified category.
  - **In-Order Traversal**: Displays the B-Tree in sorted order, listing all inserted image entries.

- **Graphical User Interface (GUI)**:  
  - Built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for a modern and user-friendly experience.
  - Uses [Pillow (PIL)](https://python-pillow.org/) for loading and displaying images.
  - Provides interactive elements such as buttons, checkboxes, and entry fields.
  - Displays real-time feedback including error messages for failed operations (e.g., no results found, all images already inserted).

- **Experimental Analysis**:  
  - The project includes performance tests using a dataset of up to 50,000 entries.
  - Experimental results indicate efficient operations with average execution times:
    - **Search**: ~0.0059 seconds
    - **Insertion**: ~0.0759 seconds
    - **Deletion**: ~0.0359 seconds
    - **Printing (In-Order Traversal)**: ~0.0085 seconds

## ✅ Technologies used

- [Python](https://www.python.org/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [Pillow (PIL)](https://python-pillow.org/)

## Methodology

The project employs a custom B-Tree with a minimum degree (*t = 3*), ensuring each node (except the root) contains at least `t - 1` keys and at most `2t - 1` keys. The B-Tree remains balanced to guarantee O(log n) performance for its operations. Image files are organized in the **Banco_Imagens** folder, and filenames are sorted using Python’s `re` module for proper lexicographical ordering.

## Experimental Analysis

The project was tested on a system with the following configuration:
- **Hardware**: Intel i5-13600K, 32GB DDR4, 3.50 GHz
- **Software**: Windows 11 Home 64-bit, Python 3.11.9

**Average Execution Times:**

| Operation   | Time (seconds) |
|-------------|----------------|
| Search      | 0.0059         |
| Insertion   | 0.0759         |
| Deletion    | 0.0359         |
| Printing    | 0.0085         |

## Usage

1. **Install Dependencies**  
   Ensure you have [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) and [Pillow (PIL)](https://python-pillow.org/) installed.

2. **Prepare Your Data**  
   Place your image files in the **Banco_Imagens** folder. Filenames should follow a naming convention that includes the category (e.g., `asteroide1.jpg`).

3. **Run the Application**  
   Execute the main Python script:

   ```bash
   python GUI.py
   
4. **Interact with the GUI**
    - Insertion: Choose between inserting a single image or all images at once.
    - Search: Input a category or partial filename to display matching images.
    - Deletion: Enter a category name to delete all images associated with that category.
    - Print: Display the B-Tree content in sorted order.

## References
  - RODEH, O.; BACIK, J.; MASON, C. "BTRFS", ACM Transactions on Storage, 2013.
  - WU, C.-H.; KUO, T.-W.; LAN-YANG CH’ANG, "An efficient B-tree layer implementation for flash-memory storage systems", ACM Transactions in Embedded Computing Systems, 2007.
  - NIVIO ZIVIANI. Projeto De Algoritmos Com Implementações Em Pascal E C, 3rd Ed.
  - PAULO FEOFILLOF. Algoritmos, Elsevier Brasil, 2013.

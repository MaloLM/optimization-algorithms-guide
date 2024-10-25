# Optimization Algorithms Guide

This project is an open-source collection of various optimization algorithms, each presented in a Jupyter notebook (Python). Its purpose is to provide a comprehensive resource for understanding and implementing these algorithms. It is a valuable asset for both educational and practical applications in optimization tasks.

!["A quick overview of some visualizations."](./assets/images/demo/demo.gif "A quick overview of some visualizations")

## Table of Contents

1. [Installation](#installation)
2. [Dependencies](#dependencies)
3. [Each Algorithm's Notebook](#each-algorithms-notebook)
   - [Biomimicry Based Algorithms](#biomimicry-based-algorithms)
   - [Decomposition Methods](#decomposition-methods)
   - [Deterministic Mathematical Optimization](#deterministic-mathematical-optimization)
   - [Stochastic Optimization](#stochastic-optimization)
4. [Further Exploration](#further-exploration)
5. [Licensing](#licensing)
6. [Contributing](#contributing)
7. [Disclaimer of Liability and Usage Terms](#disclaimer-of-liability-and-usage-terms)
8. [Contact Information](#contact-information)

## Installation

Follow these steps to set up the project:

1. **Clone the Repository**: 
   - Open your terminal.
   - Navigate to the directory where you want to clone the project.
   - Run the command: `git clone https://github.com/MaloLM/optimization-algorithms-guide.git`.

2. **Install Dependencies**: 
   - Make sure you have Python installed on your system.
   - Navigate to the root directory of the cloned project in the terminal.
   - Run the command: `pip install -r requirements.txt`.
   - This will install all the Python dependencies listed in the `requirements.txt` file.

3. **Launch JupyterLab**:
   - After installing dependencies, stay in the project's root directory.
   - Run the command: `jupyter lab`.
   - This will start the JupyterLab server and may open a browser window automatically.
   - If a browser window doesn't open, you can manually navigate to the URL provided in the terminal (usually something like `http://localhost:8888/lab`).

After completing these steps, you should be ready to use the project.
## Dependencies
- Detailed list of dependencies included in `requirements.txt`.

## Each Algorithm's Notebook
For each algorithm, the corresponding Jupyter notebook will include:
- General Introduction
- Usage Examples
- Strengths
- Weaknesses
- Python Demonstration
- Recommended Open Source Tools
- Research Sources

## Algorithms Overview
### Biomimicry based algorithms (even if part of the stochastic optimization)
- [Ant colony optimization](./algorithms/biomimicry%20based/Ant%20colony.ipynb)
- [Differential evolution](./algorithms/biomimicry%20based/Differential%20evolution.ipynb)
- [Genetic algorithms](./algorithms/biomimicry%20based/Genetic%20algorithm.ipynb)
- [Particle swarm optimization](./algorithms/biomimicry%20based/Particle%20swarm%20optimization.ipynb)

### Decomposition methods
- [Branch and bound](./algorithms/decompsition%20methods/branch%20and%20bound.ipynb)

### Deterministic mathematical optimization
- [Conjugate gradient](./algorithms/deterministic%20mathematical%20optimization/Conjugate%20gradient.ipynb)
- [Gradient descents](./algorithms/deterministic%20mathematical%20optimization/Gradient%20descents.ipynb)
- [Interior point method](./algorithms/deterministic%20mathematical%20optimization/Interior%20point%20method.ipynb)
- [Newton and quasi-Newton methods](./algorithms/deterministic%20mathematical%20optimization/Newton%20methods.ipynb)
- [Simplex method](./algorithms/deterministic%20mathematical%20optimization/Simplex%20algorithm.ipynb)

### Stochastic optimization
- [Bayesian optimization](./algorithms/stochastic%20optimization/Bayesian%20optimization.ipynb)
- [Hill climbing](./algorithms/stochastic%20optimization/Hill%20climbing.ipynb)
- [Tabu search](./algorithms/stochastic%20optimization/Tabu%20search.ipynb)

## Further Exploration

-  [Mathematical optimization (Wikipedia)](https://en.wikipedia.org/wiki/Mathematical_optimization)

This page on Mathematical Optimization provides a comprehensive overview of optimization in mathematics. It defines optimization as the process of selecting the best element from a set of alternatives based on some criteria.

-  [Optimization algorithms and methods (Wikipedia)](https://en.wikipedia.org/wiki/Category:Optimization_algorithms_and_methods)

The page features a comprehensive list of 164 pages dedicated to various optimization algorithms and methods. This category is a detailed resource, encompassing a wide array of optimization techniques and strategies used in different computational and mathematical contexts.

-  [Test Functions for Optimization (Wikipedia)](https://en.wikipedia.org/wiki/Test_functions_for_optimization)

This page provides a comprehensive resource on test functions used in applied mathematics to evaluate optimization algorithms. These functions, also known as artificial landscapes, are instrumental in assessing various characteristics of optimization algorithms, including their convergence rate, precision, robustness, and general performance.

## Licensing

This project is licensed under the Apache 2.0 License. It allows you to freely use, modify, and distribute the project, subject to certain conditions. For complete details, see [LICENSE](./LICENSE).

## Contributing

### Reporting Issues or Suggesting Improvements

If you encounter any problems or have suggestions for improvements, please feel free to report them in the **Issues** section of the GitHub repository. To ensure efficient and effective communication, please follow these guidelines when submitting an issue:

1. **Use a Clear Title**: Write a concise and informative title for the issue that briefly summarizes the problem or suggestion.

2. **Provide Detailed Information**: In the description, include as much relevant information as possible. This might include:
   - The steps to reproduce the issue (if applicable).
   - The expected outcome versus the actual outcome.
   - Any error messages or screenshots that illustrate the problem.
   - Your environment details, like the operating system and version of the software you are using.

3. **Label Your Issue**: If possible, categorize your issue using labels. Common labels include `bug`, `feature request`, `enhancement`, `documentation`, etc.

4. **Be Respectful and Constructive**: Remember to be respectful and constructive in your communication. We appreciate your contribution to improving this project.

### Creating a Pull Request

1. **Update Your Fork**:
   ```bash
   git fetch upstream
   git merge upstream/main main
   ```
2. **Create a New Branch**:
   ```bash
   git checkout -b branch-name
   ```
3. **Make Your Changes**.
4. **Commit and Push Your Changes**:
   ```bash
   git add .
   git commit -m "Descriptive commit message"
   git push origin branch-name
   ```
5. Navigate to the GitHub page of your fork, and click on "New Pull Request".
6. Ensure the base branch is the main branch of the main repository, and the compare branch is your branch with changes.


Thank you for helping us make this project better!

## Disclaimer of Liability and Usage Terms

This project python code is only provided for demonstration and educational purposes. It is not intended for, nor should it be used directly, as it is, in production environments or for direct integration into operational systems.

Users are advised that employing the code directly in such manners may result in unforeseen issues or incidents. The creators, contributors, or distributors of this code expressly disclaim any liability for any adverse outcomes resulting from the direct reuse or misapplication of the code. It is the responsibility of the user to evaluate and bear all risks associated with the use and adaptation of this code.

As an alternative to demonstrations codes, practical, open-source tools that have proven effective are suggested for each algorithm and in multiple languages.

## Contact Information

<div> 
   <a href="https://portfolio.dopee.io/#/contact" target="_blank">
      <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=maildotru&logoColor=white" alt="E-mail" height=40>
   </a>
   
   <a href="https://portfolio.dopee.io" target="_blank">
      <img src="https://img.shields.io/badge/Portefolio-green?style=for-the-badge&logo=vuedotjs&logoColor=white" alt="Portefolio" height=40>
   </a>
   
   <a href="https://www.linkedin.com/in/malo-le-mestre/" target="_blank">
      <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Linkedin" height=40>
   </a>
</div>

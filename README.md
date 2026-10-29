# Python Lab Repository

Welcome to the **Python Lab** repository! This repository contains a comprehensive collection of Python programs, exercises, and projects spanning fundamental programming concepts, data structures, object-oriented programming (OOP), data manipulation, file handling, and introductory data science and natural language processing.

---

## 📂 Repository Structure & Overview

### 1. 🔰 Fundamentals & Core Python
- **`basicPyPrograms/`**
  - Basic Python exercises: data types, operators, number printing (1 to 10), and factorial computation (`fact.py`).
- **`ConditionalStatements/`**
  - Decision making with `if`, `elif`, and `else` divided into `BasicQuestions`, `MediumQuestions`, and `HardQuestions`.
- **`Loops/`**
  - Iteration and loop constructs:
    - `For_Loops/`: For loop syntax, number sequences, and iterations.
    - `While_Loop/`: While loops and condition-based iteration.

---

### 2. 📦 Data Structures
- **`Array/`**
  - Array initialization, traversal, and operations (`array.py`, `array2.py`).
- **`List/`**
  - Extensive list operations, indexing, slicing, search, list manipulation programs (`program1.py` to `program10.py`, `Student.py`).
- **`Tuples/`**
  - Immutable sequences, tuple operations (`tuple.py`), `pointManagement.py`, and `webServerConfig.py`.
- **`Sets/`**
  - Unique collections, set operations, mathematical sets (`set.py`), plus real-world scenarios:
    - `projectEmployeeAnalysis.py`: Analyzing employee skill/project allocations using set theory.
    - `weeklyAttendanceSystem.py`: Managing attendance records with set intersections and unions.
- **`Frozenset/`**
  - Working with immutable sets (`frozen.py`).
- **`Dictionary/`**
  - Key-value mapping, lookups, dictionary comprehension, and record storage (`Dictionary.py`).
- **`String/`**
  - `BasicStringsConcept/`: String declaration, formatting, and built-in methods.
  - `StringQuestions/`: String reversal, anagrams, palindrome checks, and text processing challenges.

---

### 3. 🧩 Functions, Modules & Packages
- **`Functions/`**
  - `NormalFunctions/`: Function definitions, parameters, return values, and scopes.
  - `LambdaFunctions/`: Anonymous functions, filtering, and mapping.
- **`Module/`**
  - Defining and importing custom Python modules (`module.py`, `main.py`).
- **`package/`**
  - Modular arithmetic package: `add.py`, `evenOdd.py`, `multiplication.py`, `square.py`.
  - `student_package/`: A complete structured package containing `student_info.py`, `exam_info.py`, and package initialization (`__init__.py`).

---

### 4. 🏛️ Object-Oriented Programming (OOP)
Located in `oops/`:
- **`class&Object/`**: Class blueprints, attributes, methods, and instances (`BankAccount.py`).
- **`Inheritance/`**:
  - Single inheritance (`singleInheritance.py`)
  - Multilevel inheritance (`MultilevelInheritance.py`)
  - Multiple inheritance (`MultipleInheritance.py`)
  - Hierarchical inheritance (`HirarchicalInheritance.py`)
  - Hybrid inheritance (`HybridInheritance.py`)
  - Access specifiers (`PublicPrivateAccessModifiers.py`)
  - Name mangling (`nameMangling.py`)
- **`polymorphism/`**: Method overriding, dynamic dispatch, and duck typing (`duckTyping.py`).
- **`operatorOverloading/`**: Dunder methods and custom operator behaviors (`operatorOverloading.py`).
- **`destructor/`**: Object cleanup and garbage collection using `__del__` (`destructor.py`).
- **`abstract/`**: Abstract classes and abstract methods using `abc` module (`abstractClass&Methods.py`).

---

### 5. ⚠️ Exception Handling
- **`exceptionHandling/`**
  - Try, except, else, and finally blocks (`first.py`).
  - Handling multiple built-in exceptions (`multipleExceptions.py`).
  - Defining and raising custom user-defined exceptions (`customException.py`).

---

### 6. 📁 File Handling
- **`FileHandling/`**
  - `BasicFiles.py/`: Reading, writing, and appending files (`file1.py`, `file2.py`).
  - `Directory/`: Directory listing and file system navigation (`dir.py`).
  - `AdvancedFiles/`: Advanced file input/output manipulation (`fileOperations.py`).
  - `HardQuestions/`: 23 comprehensive practical questions (`question1.py` to `question23.py`) operating over sample datasets:
    - `attendance.txt`
    - `books.txt`
    - `employees.txt`
    - `students.txt`
    - `transactions.txt`

---

### 7. 🔣 Regular Expressions
- **`regularExpression/`**
  - Pattern matching, `search`, `match`, `findall`, and substitutions (`function.py`, `function2.py`).
  - Advanced regex patterns for validating emails, phone numbers, and log extraction (`advancedRegex.py`).

---

### 8. ⚡ Algorithms
- **`Algorithms/`**
  - Implementation of classic algorithms such as Run Length Encoding (`run_length_encoding.py`).

---

### 9. 📊 Data Science, Analysis & NLP
- **`numpy/`**
  - `arrayCreation&Printing/`: Initializing and reshaping arrays (`arr.py`).
  - `2dArrayOperations/`: Indexing, slicing, and matrix operations (`2dArrayOps.py`).
  - `matrixOperations/`: Linear algebra and dot products (`dotProduct.py`).
  - `statistics/`: Mean, median, variance, and standard deviation calculations (`stats.py`).
  - `labels/`: Working with array tags and structured arrays.
- **`pandas/`**
  - Series creation and manipulation (`series.py`).
  - DataFrame loading, cleaning, indexing, and aggregations (`dataframe.py`, `dataframeOperations.py`).
  - Sample datasets: `data.csv`, `data2.csv`, `data3.csv`.
- **`matplotlib/`**
  - Plotting line graphs, bar charts, and data extraction from CSVs (`graphdemo.py`, `extract.py`, `ds.csv`).
- **`NLP/`**
  - Text tokenization, stop-word removal, and text processing (`text_processing.py`).
  - NLTK-based Natural Language Processing workflows (`nltk_nlp.py`).

---

### 10. 🖥️ Desktop GUI with Tkinter
- **`TKINTER_WIDGET/`**
  - 20 standalone Python Tkinter GUI scripts demonstrating key widgets:
    - **Controls & Input**: `Button.py`, `label.py`, `Entry.py`, `Checkbutton.py`, `Radiobutton.py`
    - **Pickers & Sliders**: `Spinbox.py`, `Scale.py`, `Listbox.py`, `Combobox.py`
    - **Layout & Windows**: `Frame.py`, `LabelFrame.py`, `PanedWindow.py`, `Toplevel.py`
    - **Text & Graphics**: `Text.py`, `Message.py`, `Canvas.py`
    - **Menus & Dialogs**: `Menu.py`, `Menubutton.py`, `MessageBox.py`, `Scrollbar.py`

---

### 11. 🌐 Web Development with Django
- **`Django/`**
  - `Django_Web_Experiment/mydemoproject/`:
    - Full Django 5.x project with `demoapp`.
    - Implements user authentication flow (login view with POST validation and flash messages).
    - Custom templates (`login.html`) and SQLite database (`db.sqlite3`).

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher installed on your system.
- Recommended libraries:
  ```bash
  pip install numpy pandas matplotlib nltk django
  ```

### Running a Program
Navigate to the desired folder and run the script with Python:
```bash
python List/program1.py
```

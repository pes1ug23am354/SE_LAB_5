# SE_LAB_5 — Static Code Analysis

**Author:** Vivan Jeevan Naik  
**SRN:** PES1UG23AM354  
**Repository Link:** [https://github.com/pes1ug23am354/SE_LAB_5](https://github.com/pes1ug23am354/SE_LAB_5)

---

## Objective
The goal of this lab is to perform static code analysis on a given Python program using three tools:
- **Pylint** for code quality and structure
- **Flake8** for style and PEP8 compliance
- **Bandit** for security analysis

The provided file `inventory_system.py` was analyzed and improved to create a cleaner, more secure, and maintainable version named `clean_inventory_system.py`.

---

## Files in the Repository
1. `inventory_system.py` – Original file provided for analysis  
2. `clean_inventory_system.py` – Updated and cleaned version of the original file  
3. `pylint_report.txt` – Pylint report for the cleaned file  
4. `flake8_report.txt` – Flake8 style report for the cleaned file  
5. `bandit_report.txt` – Bandit security analysis report for the cleaned file  
6. `README.md` – Documentation and summary of the lab  

---

## Steps Performed
1. **Setup Environment**  
   - Installed required tools using `pip install pylint flake8 bandit`.  
   - Initialized a Git repository to track changes.

2. **Static Analysis**  
   - Ran Pylint, Flake8, and Bandit on the original file.  
   - Collected and reviewed issues related to style, logic, and security.

3. **Code Improvement**  
   - Added input validation and proper error handling.  
   - Replaced print statements with Python’s logging module.  
   - Added descriptive docstrings and comments.  
   - Followed PEP8 style conventions.

4. **Reanalysis**  
   - Re-ran Pylint, Flake8, and Bandit on the cleaned file.  
   - Generated final reports for submission.

---

## Tools and Commands Used
- **Run Pylint**
  ```bash
  pylint clean_inventory_system.py > pylint_report.txt 2>&1

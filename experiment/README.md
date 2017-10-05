```
Command to run the script:
    python parseNB.py notebook.md
```

# Sample output 1

```
Output when sample-000/notebook.md is provided as input argument:

Yaml representation of data:
Inactive: [12/23/17 - 12/24/17 No work due to Christmas - this is just ana example
    so do not out it in your notebook]
Logistic: [08/21/17 Read the entire class overview section]
Meetings: [08/21/17 Residential Meeting attended, 09/21/17 Online Meeting attended]
Practice: [08/24/17 Bought Raspberry PI, 08/25/17 Enabled Python 2 and 3 via pyenv
    on OSX]
Theory: [08/22/17 - 08/23/17 Read and watched all videso in the Theory Introduction
    section]
Writing: [08/26/17 Installed and Learned aquamacs, 00/01/17 Installed and Learned
    jabref]

Below section(s) not present in notebook.md:
None

Student attended the below classes:
2017-08-21 00:00:00
2017-09-21 00:00:00
```

# Sample output 2

```
Output when hid203/notebook.md, which has missing sections, is provided as input argument:

Yaml representation of data:
Logistic: [08/21/17 Read the entire class overview section]
Practice: [08/24/17 Bought Raspberry PI, 08/25/17 Enabled Python 2 and 3 via pyenv
    on OSX]
Theory: [08/22/17 - 08/23/17 Read and watched all videso in the Theory Introduction
    section]
Writing: [08/26/17 Installed and Learned aquamacs, 00/01/17 Installed and Learned
    jabref]

Below section(s) not present in notebook.md:
['Meetings', 'Inactive']

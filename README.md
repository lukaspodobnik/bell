# BELL

**BELL** is a small, minimal bookkeeping tool for teachers, designed to manage students, grades, and classroom activities directly from the command line.

---

## Features

- Add, remove, and list students
- Record grades and exam results
- Organize notes and a schedule
- Show syllabi (only works with the bavarian "Lehrplanplus" for maths and computer science)
- Lightweight, CLI-first workflow with human-readable storage

_Note that currently this tool only works for the subjects maths and computer science._

---

## Installation

todo

---

## How to get started

- Start with 'bell init', where ever you want your root directory to be
- cd into classroom/ and use 'bell init year'
- cd into the year and use 'bell init class 10A maths' (for example)
- Use the very wise --help option to see usage of the commands in the terminal

---

## Classroom Structure

BELL will create a predefined directory structure. Here is an example:

```
classroom/
    .bell/
        classroom_structure/
    2025-26/
        cs/
            10A/
                notes/
                .exams.csv
                .grades.csv
                .students.csv
            12C/
                notes/
                .exams.csv
                .grades.csv
                .students.csv
        maths/
            9B/
                notes/
                .exams.csv
                .grades.csv
                .students.csv
        .schedule.csv
    2026-27/
        .schedule.csv
```

Note that you **can** add other directories and files (these are going to be ignored by BELL), but you **cannot** remove any of the generated direcotries or files by hand - this will break the tool.

---

## Documentation

### `bell init`

Initialize a new classroom workspace.

Sets up the main classroom directory in the current directory. This is the first
step for using BELL and must be run before initializing years or classes.

**Usage**

```console
$ bell init
```

---

### `bell init year`

Initialize the academic year.

Creates a directory for the current (or specified) academic year inside the
classroom workspace. This is the second step after using &#x27;bell init&#x27;. Use this command
within the classroom directory.

**Usage**:

```console
$ bell init year [OPTIONS]
```

**Options**:

* `-y, --year YYYY-YY`: Specify a different academic year.  [default: 2025-26]
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

---

### `bell init class_`

Initialize a class.

Creates a directory for the specified class in the given subject within the
current academic year. This is the third step after using &#x27;bell init year&#x27;. Use this command
within a year directory.

**Usage**:

```console
$ bell init class_ [OPTIONS] [CLASS] SUBJECT:{maths|cs}
```

**Arguments**:

* `[CLASS]`: Name of the class, e.g., 10A or 9B  [required]
* `SUBJECT:{maths|cs}`: Subject name (e.g., maths).  [required]

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

---

### `bell add lesson`

Add a lesson to the schedule.

Assigns the current class and subject to the specified slot and weekday in
the schedule.

**Usage**:

```console
$ bell add lesson [OPTIONS] SLOT WEEKDAY:{monday|tuesday|wednesday|thursday|friday}
```

**Arguments**:

* `SLOT`: Time slot of the lesson.  [required]
* `WEEKDAY:{monday|tuesday|wednesday|thursday|friday}`: Weekday of the lesson.  [required]

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

---

### `bell add exam`

Add a planned exam.

Registers a new exam for the current class with the given type and optional
date.

**Usage**:

```console
$ bell add exam [OPTIONS] EXAM_TYPE:{mündlich|stegreifaufgabe|schulaufgabe|kurzarbeit}
```

**Arguments**:

* `EXAM_TYPE:{mündlich|stegreifaufgabe|schulaufgabe|kurzarbeit}`: Type of exam.  [required]

**Options**:

* `-d, --date DD-MM-YYYY`: Optional date of the exam.  
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

---

### `bell add note`

Add a note for the current class.

Prompts for the content of the note in the terminal and saves it as a markdown
file under the class&#x27;s notes folder for later reference.

**Usage**:

```console
$ bell add note [OPTIONS]
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

---


### `bell add student`

Add a student (or multiple students) to the current class.

Adds a single student or --multiple students to the class roster,
making them available for other commands.

**Usage**:

```console
$ bell add student [OPTIONS] [STUDENT]
```

**Arguments**:

* `[STUDENT]`: The Student to add.

**Options**:

* `-m, --multiple`: Set this to add multiple students.
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

---


### `bell add grade`

Add a grade for a student or all students of the class.

Records a grade for the given student and exam type on the current or specified date,
optionally including a --comment. Note, that --number usually should not be specified;
it is used differentiate between exams of the same type (e.g., 1. Kurzarbeit and 2. Kurzarbeit).
The --all option can be used to grade a whole class.
If --all is set, all other parameters besides --exam-type are ignored

**Usage**:

```console
$ bell add grade [OPTIONS] [STUDENT] [GRADE]
```

**Arguments**:

* `[STUDENT]`: The student to assign the grade to.
* `[GRADE]`: The grade value (1-6).

**Options**:

* `-c, --comment TEXT`: Optional comment for the grade.  [default:  ]
* `-n, --number INTEGER`: Number of the exam, (e.g., 1 for the first exam of given type).  [default: 0]
* `-t, --exam-type [mündlich|stegreifaufgabe|schulaufgabe|kurzarbeit]`: Type of the exam.  [default: mündlich]
* `-d, --date DD-MM-YYYY`: Date of the grading.  
* `-a, --all`: Set to grade all students of this class.
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

---


### `bell remove class_`

Remove a class from the current academic year.

Deletes the class folder and all associated files for the specified subject.
This command is irreversible, so use it with caution.

**Usage**:

```console
$ bell remove class_ [OPTIONS] [CLASS] SUBJECT:{maths|cs}
```

**Arguments**:

* `[CLASS]`: Name of the class, e.g., 10A or 9B  [required]
* `SUBJECT:{maths|cs}`: Subject name.  [required]

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

---


### `bell remove lesson`

Remove a lesson from the schedule for this year.

**Usage**:

```console
$ bell remove lesson [OPTIONS] SLOT WEEKDAY:{monday|tuesday|wednesday|thursday|friday}
```

**Arguments**:

* `SLOT`: Time slot of the lesson.  [required]
* `WEEKDAY:{monday|tuesday|wednesday|thursday|friday}`: Weekday of the lesson.  [required]

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

---


### `bell remove exam`

Remove a planned exam for this class.

**Usage**:

```console
$ bell remove exam [OPTIONS] NUMBER EXAM_TYPE:{mündlich|stegreifaufgabe|schulaufgabe|kurzarbeit}
```

**Arguments**:

* `NUMBER`: Number of the exam, (e.g., 1 for the first exam of given type).  [required]
* `EXAM_TYPE:{mündlich|stegreifaufgabe|schulaufgabe|kurzarbeit}`: Type of the exam.  [required]

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

---


### `bell remove grade`

Remove a grade for a student in this class.

**Usage**:

```console
$ bell remove grade [OPTIONS] STUDENT NUMBER EXAM_TYPE:{mündlich|stegreifaufgabe|schulaufgabe|kurzarbeit}
```

**Arguments**:

* `STUDENT`: Student name.  [required]
* `NUMBER`: Number of the exam, (e.g., 1 for the first exam of given type).  [required]
* `EXAM_TYPE:{mündlich|stegreifaufgabe|schulaufgabe|kurzarbeit}`: Type of exam.  [required]

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

---


### `bell remove student`

Remove a student from this class.

**Usage**:

```console
$ bell remove student [OPTIONS] STUDENT
```

**Arguments**:

* `STUDENT`: The student to remove.  [required]

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

---


### `bell show syllabus`

Show the syllabus for this class.

Use --subject and --level to specify which syllabus to show.

**Usage**:

```console
$ bell show syllabus [OPTIONS]
```

**Options**:

* `-s, --subject [maths|cs]`: The subject of the syllabus.
* `-l, --level INTEGER`: The grade-level of the syllabus.
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

---


### `bell show grades`

Show grades for this class.

Use --student to only show grades for a specific student.
Use --exam-type to only show grades for a specific exam type.
Use --last to only show the grads for the last exam.

**Usage**:

```console
$ bell show grades [OPTIONS]
```

**Options**:

* `-s, --student "first_name(s) last_name"`: The student to show grades for.
* `-t, --exam-type [mündlich|stegreifaufgabe|schulaufgabe|kurzarbeit]`: Type of the exam.
* `-l, --last`: Set this to only show the grades for the last exam.
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

---


### `bell show note`

Show notes for this class.

**Usage**:

```console
$ bell show note [OPTIONS]
```

**Options**:

* `-a, --all`: Show all notes
* `-n, --last-n INTEGER RANGE`: Show last N notes  [default: 1; x&gt;=1]
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

---


### `bell show exams`

Show all planned (and already completed) exams for this class.

**Usage**:

```console
$ bell show exams [OPTIONS]
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

---


### `bell show schedule`

Show the schedule for this year.

**Usage**:

```console
$ bell show schedule [OPTIONS]
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

---


### `bell show students`

Show all students in this class.

**Usage**:

```console
$ bell show students [OPTIONS]
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

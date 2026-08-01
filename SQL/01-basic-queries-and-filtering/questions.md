# Basic Queries & Data Filtering

## Exercise 1

**Task**

Retrieve each employee's first name, middle initial, last name, and salary.

<img width="282" height="196" alt="image" src="https://github.com/user-attachments/assets/e8a25bbc-589f-467a-93fc-c13f959e1aec" />


---

## Exercise 2

**Task**

List all unique salary amounts paid to employees.

```sql
SELECT DISTINCT Salary
FROM EMPLOYEE;
```

---

## Exercise 3

**Task**

Show all employees who work in department 5.

```sql
SELECT *
FROM EMPLOYEE
WHERE Dno = 5;
```

---

## Exercise 4

**Task**

Find employees who earn more than 30,000.

```sql
SELECT *
FROM EMPLOYEE
WHERE Salary > 30000;
```

---

## Exercise 5

**Task**

List all unique locations where the company has projects.

```sql
SELECT DISTINCT Plocation
FROM PROJECT;
```

---

## Exercise 6

**Task**

Show the first name, last name, and salary of female employees earning at least 25,000, sorted by salary from highest to lowest.

```sql
SELECT Fname, Lname, Salary
FROM EMPLOYEE
WHERE Sex = 'F'
  AND Salary >= 25000
ORDER BY Salary DESC;
```

---

## Exercise 7

**Task**

Find employees whose last name starts with 'S' or whose first name starts with 'J'.

```sql
SELECT Fname, Lname
FROM EMPLOYEE
WHERE Lname LIKE 'S%'
   OR Fname LIKE 'J%';
```

---

## Exercise 8

**Task**

Show the three highest-paid employees.

```sql
SELECT Fname, Lname, Salary
FROM EMPLOYEE
ORDER BY Salary DESC
LIMIT 3;
```

---

## Exercise 9

**Task**

List dependents born before January 1, 1980, ordered by birth date from oldest to newest.

```sql
SELECT *
FROM DEPENDENT
WHERE Bdate < '1980-01-01'
ORDER BY Bdate ASC;
```

---

## Exercise 10

**Task**

Show work assignments where employees worked more than 15 hours, sorted by employee SSN and then by hours worked in descending order.

```sql
SELECT *
FROM WORKS_ON
WHERE Hours > 15
ORDER BY Essn ASC, Hours DESC;
```

---

## Exercise 11

**Task**

Find male employees who do not have a supervisor.

```sql
SELECT *
FROM EMPLOYEE
WHERE Sex = 'M'
  AND Super_ssn IS NULL;
```

---

## Exercise 12

**Task**

Show the two lowest-paid employees in departments 4 and 5.

```sql
SELECT Fname, Lname, Salary, Dno
FROM EMPLOYEE
WHERE Dno IN (4, 5)
ORDER BY Salary ASC
LIMIT 2;
```

---

## Exercise 13

**Task**

List all unique relationship types recorded for dependents.

```sql
SELECT DISTINCT Relationship
FROM DEPENDENT;
```

---

## Exercise 14

**Task**

Show all projects located in Houston or Stafford, sorted alphabetically by project name.

```sql
SELECT *
FROM PROJECT
WHERE Plocation IN ('Houston', 'Stafford')
ORDER BY Pname ASC;
```

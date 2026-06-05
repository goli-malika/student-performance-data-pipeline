-- Average Marks

SELECT AVG(Average)
FROM students;

-- Top Students

SELECT Name, Average
FROM students
ORDER BY Average DESC
LIMIT 5;

-- Attendance Report

SELECT Name, Attendance
FROM students
ORDER BY Attendance DESC;
# GenTimeTable
A Python-based system that allows school administrators to input data into an SQLite database and automatically generates optimized timetables for classes and teachers based on predefined school criteria. The program ensures efficient scheduling while considering constraints like teacher availability, subject requirements, and classroom capacity.

## 💾 Database Tables
### Teachers
| Column Name | Data Type    | Description                               |
| ----------- | ------------ | ----------------------------------------- |
| id          |	TEXT         | Unique identifier for the teacher         |
| name        |	TEXT         | Full name of the teacher                  |
| weekMax     |	INTEGER      | Max periods the teacher can take per week |
| weekMin     |	INTEGER      | Mix periods the teacher can take per week |
| dayMax      | INTEGER      | Max periods the teacher can take per day  |
| dayMin      | INTEGER      | Min periods the teacher can take per day  |

### Subjects
| Column Name | Data Type    | Description                               |
| id          | INTEGER      | Unique subject identifier                 |
| subjectName | TEXT         | Name of the subject                       |

### Classes
| Column Name | Data Type    | Description                               |
| id          | INTEGER      | Unique identifier for the class           |
| grade       | INTEGER      | Grade level (e.g. "5", "10")              |
| section     | TEXT         | Section label (e.g. "A", "B")             |

### TeacherSubjects
| Column Name | Data Type    | Description                               |
| teacherId   | INTEGER      | References `Teachers(id)`                 |
| subjectId   | INTEGER      | References `Subjects(id)`                 |

### SubjectClasses
| Column Name | Data Type    | Description                               |
| classId     | INTEGER      | References `Classes(id)`                  |
| subjectId   | INTEGER      | References `Subjects(id)`                 |
| teacherId   | INTEGER      | References `Teachers(id)`                 |
| weekPeriods | INTEGER      | Periods for this subject in a week        |
| dayPeriods  | INTEGER      | Maximum periods for this subject in a day |
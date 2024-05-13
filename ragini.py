import statistics

def generate_byline(class_name,teacher_name,exam_scores,has_extra_credit):
# calculate statistics
    mean_score=statistics.mean(exam_scores)
    rounded_mean_score=round(mean_score)
    median_score=statistics.median(exam_scores)
    std_dev_score=statistics.stdev(exam_scores)

# create teh byline string
    byline= f"""
    Class: {class_name}
    Teacher: {teacher_name}
    Number of Students: {len(exam_scores)}
    Extra Credit Available: {has_extra_credit}
    Exam Score Statistics:
    Mean Score: {mean_score:.2f}
    Rounded Mean Score: {rounded_mean_score}
    Median Score: {median_score}
    Standard Deviation Score: {std_dev_score:.2f}
    """
    return byline

# sample exam scores
exam_scores=[85,90,78,93,88,80,82,87,92,95]
# sample student information
class_name="Mathematics"
teacher_name="Mr. Smith"
has_extra_credit=True

# generate byline
byline=generate_byline(class_name, teacher_name, exam_scores, has_extra_credit )

#print byline
print(byline)


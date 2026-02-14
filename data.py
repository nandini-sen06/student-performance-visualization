import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student" :  ["Raj", "Ajay", "Vijay", "Meena", "Priya"],
    "Math" : [76,54,87,43,98],
    "Science" : [87,42,73,32,85],
    "English" : [69,75,72,43,76]
}

df = pd.DataFrame(data)
print(df)

# Average Per Student
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

plt.bar(df["Student"],df["Average"])
plt.xlabel("Students")
plt.ylabel("Average")
plt.title("Average Per Student")
plt.savefig("average_per_student.png", dpi=300)
plt.show()

# Average Per Subject
subjects = ["Math", "Science", "English"]
avg = df[subjects].mean()

plt.bar(subjects, avg, color = "orange")
plt.title("Average Per Subject")
plt.xlabel("Subjects")
plt.ylabel("Average")
plt.savefig("average_per_subject.png", dpi=300)
plt.show()

# Distribution of Math Score
plt.hist(df["Math"], bins=5, edgecolor = "black", color="violet")
plt.title("Distribution of Math Scores")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.savefig("math_distribution.png", dpi=300) 
plt.show()
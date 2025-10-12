import random

# members and task
members = ["Sean", "Nico", "Mark", "Jace", "Cy"]
tasks = [
   "Advanced CSS selectors and combinators",

   "CSS specificity and inheritance",

   "Flexbox layout and its applications",

   "CSS Grid for responsive design",

   "Creating reusable styles with CSS variables",

   "Using media queries for responsive design",

   "CSS frameworks and their benefits",
]

# randomize list of members and tasks
#random.shuffle(tasks)
#random.shuffle(members)

# format for task
#task_random = {Member: [] for Member in members}

# distribute
#for i, task in enumerate(tasks):
 #   member = members[i % len(members)]
  #  task_random[member].append(task)

#print(task_random)
member = random.choice(members)
task = random.choice(tasks)

distribu = member.append(task)
print(distribu)

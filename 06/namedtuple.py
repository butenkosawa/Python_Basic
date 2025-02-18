import collections

Worker = collections.namedtuple("Worker", 'Last_name Name Birthday Salary')
workers = []
workers.append(Worker('Butenko', 'Oleksandr', '05.04.1986', 145678.67))
workers.append(Worker('Zinchenko', 'Serhii', '15.04.1986', 85226.24))
# teammate = Worker('Butenko', 'Oleksandr', '05.04.1986', 45678.67)
# print(teammate.Name)
print(workers)
del workers[0]
print(workers)

# full_name = ''
# for worker in workers:
#     full_name = worker.Last_name + ' ' +  worker.Name
#     print(full_name)
from tkinter import *
root = Tk()
root.geometry("600x800")
root.title('Project Metric & Capacity Calculator')
root.configure(background="#E3E4FA")
root.resizable(width=False, height=False)
employee_work_hours = 6.5


def project(value):
    global annotators_for_each_task
    global mergers_for_each_task
    global metricperhour
    if c.get() == 'ABGC':
        annotator_count.set(2)
        merger_count.set(1)
        metric_per_hour.set(3)
        annotators_for_each_task = float(annotator_count.get())
        mergers_for_each_task = float(merger_count.get())
        metricperhour = float(metric_per_hour.get())
    elif c.get() == 'Venus':
        annotator_count.set(2)
        merger_count.set(1)
        metric_per_hour.set(2)
        annotators_for_each_task = float(annotator_count.get())
        mergers_for_each_task = float(merger_count.get())
        metricperhour = float(metric_per_hour.get())
    elif c.get() == 'Standardization':
        annotator_count.set(2)
        merger_count.set(1)
        metric_per_hour.set(2.75)
        annotators_for_each_task = float(annotator_count.get())
        mergers_for_each_task = float(merger_count.get())
        metricperhour = float(metric_per_hour.get())
    elif c.get() == 'TQS':
        annotator_count.set(1)
        merger_count.set(0)
        metric_per_hour.set(8)
        annotators_for_each_task = float(annotator_count.get())
        mergers_for_each_task = float(merger_count.get())
        metricperhour = float(metric_per_hour.get())
    elif c.get() == 'DVSLI':
        annotator_count.set(1)
        merger_count.set(0)
        metric_per_hour.set(16)
        annotators_for_each_task = float(annotator_count.get())
        mergers_for_each_task = float(merger_count.get())
        metricperhour = float(metric_per_hour.get())
    elif c.get() == 'CQS':
        annotator_count.set(3)
        merger_count.set(0)
        metric_per_hour.set(11)
        annotators_for_each_task = float(annotator_count.get())
        mergers_for_each_task = float(merger_count.get())
        metricperhour = float(metric_per_hour.get())
    elif c.get() == 'Fallout':
        annotator_count.set(1)
        merger_count.set(0)
        metric_per_hour.set(15)
        annotators_for_each_task = float(annotator_count.get())
        mergers_for_each_task = float(merger_count.get())
        metricperhour = float(metric_per_hour.get())


def calculate(value):
    global metricperhour
    global tasks_entry
    global resc_entry
    global days_entry
    global daysavailable
    global res_req
    global tasks
    if d.get() == 'No. of days required':
        total_tasks = Label(root, text="Total tasks", width=20, font=("bold", 15), bg="#E3E4FA")
        total_tasks.place(x=68, y=230)
        tasks = DoubleVar()
        tasks_entry = Entry(root, textvariable=tasks, width=15)
        tasks_entry.place(x=280, y=230)


        label_4 = Label(root, text="Available Resources", width=20, font=("bold", 15), bg="#E3E4FA")
        label_4.place(x=48, y=280)
        available_resources = DoubleVar()
        resc_entry = Entry(root, textvariable=available_resources, width=15)
        resc_entry.place(x=280, y=280)


        label_4 = Label(root, text="Days Required", width=20, font=("bold", 15), bg="#E3E4FA")
        label_4.place(x=200, y=680)
        daysavailable = DoubleVar()
        days_entry = Entry(root, textvariable=daysavailable, width=15)
        days_entry.place(x=430, y=680)


    if d.get() == 'No. of resources required':
        total_tasks = Label(root, text="Total tasks", width=20, font=("bold", 15), bg="#E3E4FA")
        total_tasks.place(x=68, y=230)
        tasks = DoubleVar()
        tasks_entry = Entry(root, textvariable=tasks, width=15)
        tasks_entry.place(x=280, y=230)


        label_3 = Label(root, text="Days Available", width=20, font=("bold", 15), bg="#E3E4FA")
        label_3.place(x=68, y=280)
        daysavailable = DoubleVar()
        days_entry = Entry(root, textvariable=daysavailable, width=15)
        days_entry.place(x=280, y=280)


        label_4 = Label(root, text="Resources required", width=20, font=("bold", 15), bg="#E3E4FA")
        label_4.place(x=200, y=680)
        res_req = DoubleVar()
        resc_entry = Entry(root, textvariable=res_req, width=15)
        resc_entry.place(x=430, y=680)
        # if c.get() == 'TQS':
        #     metric_per_hour.set(9)
        #     metricperhour = float(metric_per_hour.get())


    if d.get() == 'No. of tasks to be done':


        label_4 = Label(root, text="Available Resources", width=20, font=("bold", 15), bg="#E3E4FA")
        label_4.place(x=68, y=230)
        available_resources = DoubleVar()
        resc_entry = Entry(root, textvariable=available_resources, width=15)
        resc_entry.place(x=280, y=230)


        label_3 = Label(root, text="Days Available", width=20, font=("bold", 15), bg="#E3E4FA")
        label_3.place(x=68, y=280)
        daysavailable = DoubleVar()
        days_entry = Entry(root, textvariable=daysavailable, width=15)
        days_entry.place(x=280, y=280)


        tasks_label = Label(root, text="Tasks to be done", width=20, font=("bold", 15),bg="#E3E4FA")
        tasks_label.place(x=200, y=680)
        tasks = DoubleVar()
        tasks_entry = Entry(root, textvariable=tasks, width=15)
        tasks_entry.place(x=430, y=680)


        # if c.get() == 'TQS':
        #     metric_per_hour.set(10)
        #     metricperhour = float(metric_per_hour.get())


def reset():
    c.set('Select project name')
    d.set('To calculate')
    entry_8.delete(0, 'end')
    tasks_entry.delete(0, 'end')
    resc_entry.delete(0, 'end')
    days_entry.delete(0, 'end')
    entry_9.delete(0, 'end')
    entry_10.delete(0, 'end')
    entry_11.delete(0, 'end')
    entry_12.delete(0, 'end')


def output():
    if d.get() == 'No. of days required':
        no_of_tasks = float(tasks_entry.get())
        no_of_employee = float(resc_entry.get())
        Total_prod_tasks = (annotators_for_each_task + mergers_for_each_task) * no_of_tasks
        days_required = Total_prod_tasks / (metricperhour * no_of_employee * employee_work_hours)
        daysavailable.set("{:.2f}".format(days_required))
        total_prod.set(Total_prod_tasks)
        planned_efforts_in_hrs.set("{:.2f}".format(Total_prod_tasks / metricperhour))
    if d.get() == 'No. of resources required':
        no_of_tasks = float(tasks_entry.get())
        days_required = float(days_entry.get())
        Total_prod_tasks = (annotators_for_each_task + mergers_for_each_task) * no_of_tasks
        no_of_employee = Total_prod_tasks / (metricperhour * days_required * employee_work_hours)
        res_req.set("{:.2f}".format(no_of_employee))
        total_prod.set("{:.2f}".format(Total_prod_tasks))
        planned_efforts_in_hrs.set("{:.2f}".format(Total_prod_tasks / metricperhour))
    if d.get() == 'No. of tasks to be done':
        no_of_employee = float(resc_entry.get())
        days_required = float(days_entry.get())
        no_of_tasks = (days_required * metricperhour * no_of_employee * employee_work_hours)/(annotators_for_each_task + mergers_for_each_task)
        Total_prod_tasks = (annotators_for_each_task + mergers_for_each_task) * no_of_tasks
        tasks.set("{:.2f}".format(no_of_tasks))
        total_prod.set("{:.2f}".format(Total_prod_tasks))
        planned_efforts_in_hrs.set("{:.2f}".format(Total_prod_tasks / metricperhour))


label_0 = Label(root, text="Calculator Form", width=20, font=("bold", 20), bg="#E3E4FA",fg="blue")
label_0.place(x=120, y=60)


label_1 = Label(root, text="Project :", width=20, font=("bold", 15),bg="#E3E4FA")
label_1.place(x=80, y=130)
list_of_projects = ['ABGC', 'Venus', 'Standardization', 'TQS', 'DVSLI', 'CQS', 'Fallout']
c = StringVar()
droplist = OptionMenu(root, c, *list_of_projects, command=project)
droplist.config(width=20,bg="white")
c.set('Select project name')
droplist.place(x=280, y=130)


label_2 = Label(root, text="To Calculate :", width=20, font=("bold", 15), bg="#E3E4FA")
label_2.place(x=70, y=180)
to_calculate = ['No. of days required', 'No. of resources required', 'No. of tasks to be done']
d = StringVar()
droplist = OptionMenu(root, d, *to_calculate, command=calculate)
droplist.config(width=20,bg="white")
d.set('To calculate')
droplist.place(x=280, y=180)


label_5 = Label(root, text="Role: ", width=20, font=("bold", 15), bg="#E3E4FA")
label_5.place(x=68, y=330)
label_6 = Label(root, text="Annotator", width=20, font=("bold", 13),bg="#E3E4FA")
label_6.place(x=220, y=330)
label_7 = Label(root, text="Merger", width=20, font=("bold", 13), bg="#E3E4FA")
label_7.place(x=350, y=330)


label_8 = Label(root, text="Count/task(fixed value):", width=20, font=("bold", 15), bg="#E3E4FA")
label_8.place(x=28, y=380)
annotator_count = DoubleVar()
entry_8 = Entry(root, textvariable=annotator_count, width=10)
entry_8.place(x=280, y=380)
merger_count = DoubleVar()
entry_9 = Entry(root, textvariable=merger_count, width=10)
entry_9.place(x=420, y=380)


label_9 = Label(root, text="Metric/Hour(fixed value):", width=20, font=("bold", 15), bg="#E3E4FA")
label_9.place(x=28, y=430)
metric_per_hour = DoubleVar()
entry_10 = Entry(root, textvariable=metric_per_hour, width=10)
entry_10.place(x=280, y=430)


output_label = Label(root, text="Output:", width=15,font=("bold", 15), bg="#E3E4FA" )
output_label.place(x=18, y=580)
label_10 = Label(root, text="Total Productivity(tasks) :", width=20, font=("bold", 15), bg="#E3E4FA")
label_10.place(x=200, y=580)
total_prod = DoubleVar()
entry_11 = Entry(root, textvariable=total_prod, width=15)
entry_11.place(x=430, y=580)


label_11 = Label(root, text="Planned Efforts(hrs) :", width=20, font=("bold", 15), bg="#E3E4FA")
label_11.place(x=200, y=630)
planned_efforts_in_hrs = DoubleVar()
entry_12 = Entry(root, textvariable=planned_efforts_in_hrs, width=15)
entry_12.place(x=430, y=630)


b1 = Button(root, text='Calculate', font='arial 15', width=15, bg="white", fg='black' , bd=5, command=output).place(x=68, y=500)
b2 = Button(root, text='Reset', font='arial 15',width=15, bg="white", fg='black', bd=5, command=reset).place(x=320,y=500)


root.mainloop()
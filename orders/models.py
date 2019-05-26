from django.db import models


class Order(models.Model):
    STATUS_OPEN = 'open'
    STATUS_DONE = 'done'
    STATUS_IN_WORK = 'in_work'
    STATUS_REJECTED = 'rejected'
    STATUS_CHOICES = (
        (STATUS_OPEN, 'Open'),
        (STATUS_DONE, 'Done'),
        (STATUS_IN_WORK, 'In progress'),
        (STATUS_REJECTED, 'Rejected'),
    )
    owner = models.ForeignKey('customers.CustomUser', related_name='owner',
                              on_delete=models.PROTECT)
    master = models.ForeignKey('customers.CustomUser', related_name='master',
                               on_delete=models.SET_NULL,
                               null=True, blank=True, )

    PROBLEM_REPAIR = 'repair'
    PROBLEM_CREATE = 'create'
    PROBLEM_ORDER = (
        (PROBLEM_REPAIR, 'Repair Instrument'),
        (PROBLEM_CREATE, 'Create New Instrument')
    )
    problem = models.CharField(choices=PROBLEM_ORDER, max_length=254,
                               default=PROBLEM_REPAIR)

    description = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=254,
                              default=STATUS_OPEN)
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    warranty = models.DateField(null=True, blank=True)
    def __str__(self):
        return '{}'.format(self.status)
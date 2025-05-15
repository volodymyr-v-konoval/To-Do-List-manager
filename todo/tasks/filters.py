import django_filters

from .models import Task


class TaskFilter(django_filters.FilterSet):
    due_date = django_filters.DateFilter(field_name='due_date', lookup_expr='exact')
    status = django_filters.ChoiceFilter(
        choices=Task.Status.choices,
        field_name='status',
        lookup_expr='exact'
    )

    class Meta:
        model = Task
        fields = ['status', 'due_date']

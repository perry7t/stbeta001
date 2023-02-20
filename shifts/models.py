from django.db import models
from datetime import datetime, date



class Customer(models.Model):
    owner = models.IntegerField(default=1)
    customer_name = models.CharField('Customer name', max_length=255)
    customer_short = models.CharField('Short name', max_length=12)

    def __str__(self):
        return self.customer_name


class SiteAddress(models.Model):
    site_address_name = models.CharField('Site name', max_length=255)
    address = models.CharField('address', max_length=255)
    postcode = models.CharField('Postcode', max_length=20)
    city = models.CharField('City', max_length=120)

    def __str__(self):
        return self.site_address_name


class Site(models.Model):
    customer = models.ForeignKey('Customer', blank=True, null=True, on_delete=models.CASCADE)
    site_name = models.CharField('Site name', max_length=255)
    address = models.ForeignKey('SiteAddress', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.site_name

    @property
    def Customer_value(self):
        return self.customer.customer_name

    @property
    def Short_value(self):
        return self.customer.customer_short


class Function(models.Model):
    function_name = models.CharField('Function name', max_length=255)
    function_short = models.CharField('Function short', max_length=12, default="")

    def __str__(self):
        return self.function_short


class Shiftuser(models.Model):
    owner = models.IntegerField(default=1)
    first_name = models.CharField('First name', max_length=50)
    last_name = models.CharField('Last name', max_length=50)
    function = models.ForeignKey('Function', blank=True, null=True, on_delete=models.CASCADE)
    email = models.EmailField('User email')

    def __str__(self):
        return self.first_name + " " + self.last_name + ", " + self.function.function_name

    @property
    def Function_value(self):
        return self.function.function_name

    @property
    def Function_short(self):
        return self.function.function_short


class Status(models.Model):
    status_name = models.CharField('Status', max_length=255)
    color = models.CharField('background color', blank=True, max_length=100)
    template_name = models.CharField('Template', blank=True, max_length=50, default="")

    def __str__(self):
        return self.status_name


class Shift(models.Model):
    status = models.ForeignKey('Status', default=1, on_delete=models.CASCADE)
    shift_title = models.CharField('Shift title', max_length=255)
    function = models.ForeignKey('Function', on_delete=models.CASCADE)
    start_date = models.DateField('Start date')
    start_time = models.TimeField('Start time')
    end_date = models.DateField('End date')
    end_time = models.TimeField('End time')
    site = models.ForeignKey('Site', blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey('Shiftuser', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('start_date', 'start_time')

    def __str__(self):
        return self.shift_title


class Shift_view(models.Model):
    status = models.ForeignKey('Status', default=1, on_delete=models.CASCADE)
    shift_title = models.CharField('Shift title', max_length=255)
    function = models.ForeignKey('Function', on_delete=models.CASCADE)
    start_date = models.DateField('Start date')
    start_time = models.TimeField('Start time')
    end_date = models.DateField('End date')
    end_time = models.TimeField('End time')
    site = models.ForeignKey('Site', blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey('Shiftuser', blank=True, null=True, on_delete=models.CASCADE)
    weeknr = models.DateField('weeknr')
    daynr = models.DateField('daynr')

    class Meta:
        managed = False
        db_table = "shift_view"




# .isocalendar() \(year, wk num, wk day)
# .isocalendar()[0] returns the year
# .isocalendar()[1] returns the week number
# .isocalendar()[2] returns the week day
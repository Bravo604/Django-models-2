from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Адрес электронной почты')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        db_table = 'customers'

    def __str__(self):
        return f'{self.name} - {self.phone} - {self.email}'


class Work(models.Model):
    address = models.CharField(max_length=100, verbose_name='Домашний адрес')
    city = models.CharField(max_length=20, verbose_name='Город')
    company = models.CharField(max_length=100, verbose_name='Организация')
    postalZip = models.CharField(max_length=100, verbose_name='Почтовый индекс')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Клиент')

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        db_table = 'company'

    def __str__(self):
        return f'{self.address} - {self.city} - {self.company} - {self.postalZip}'


class Account(models.Model):
    pin = models.IntegerField(verbose_name='ПИН')
    acc_num = models.CharField(max_length=100, verbose_name='Номер счета')
    pan = models.CharField(max_length=100)
    cvv = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Клиент')

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'
        db_table = 'accounts'

    def __str__(self):
        return f'{self.pin} - {self.acc_num} - {self.pan} - {self.cvv}'



from django.db import models
from django.contrib.auth.models import User

class Pao(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Carne(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Opcionais(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Pedido(models.Model):
    STATUS_CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Concluído', 'Concluído'),
        ('Cancelado', 'Cancelado'),
    )

    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    pao = models.ForeignKey(Pao, on_delete=models.CASCADE)
    carne = models.ForeignKey(Carne, on_delete=models.CASCADE)
    opcionais = models.ManyToManyField(Opcionais)
    dataPedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Em andamento')
    notas = models.TextField(blank=True)

    def __str__(self):
        return f"Pedido de {self.cliente.username} - {self.dataPedido}"

    def save(self, *args, **kwargs):
        if self.pk is not None:
            original_order = Pedido.objects.get(pk=self.pk)
            if original_order.status != self.status:
                self.notas += f"Status mudou de {original_order.status} para {self.status}\n"
        super(Pedido, self).save(*args, **kwargs)

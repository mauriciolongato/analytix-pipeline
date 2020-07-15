from django.db import models
from django.contrib.postgres.fields import ArrayField


class Simulation(models.Model):
    """
    Guarda os dados de quem criou qual simulaçao e quando
    """
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    id_user = models.CharField(max_length=5000)
    id_role = models.CharField(max_length=5000)
    description = models.CharField(max_length=5000)
    validation_source_hash = models.CharField(max_length=50)

    def __str__(self):
        return str(self.created_at) + ' - ' + str(self.id_user) + ' - ' + str(self.name)


class SimulationData(models.Model):
    """
    Guarda a informação das simulações
    """
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE)
    metric_name = models.CharField(max_length=100) # sellout
    metric_format = models.CharField(max_length=100) # R$
    key_set = ArrayField(models.CharField(max_length=100, blank=True))
    value = models.CharField(max_length=100)

    def __str__(self):
        return str(self.simulation) + ' - ' + str(self.metric_name) + ' - ' + str(self.key_set)


# ARQUIVOS
class Arquivo(models.Model):
    tag_arquivo = models.CharField(max_length=50, blank=True)
    arquivo = models.FileField()

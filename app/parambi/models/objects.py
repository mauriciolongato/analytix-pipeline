from django.db import models


class RegistroHeader(models.Model):
    """
    cod_registro = 1
    """
    cod_registro = models.IntegerField()
    num_relatorio = models.BigIntegerField()
    dt_emissao = models.IntegerField()
    cod_ean_comprado = models.BigIntegerField()
    cod_ean_fornecedor = models.BigIntegerField()
    cod_ean_local_venda = models.BigIntegerField()
    des_local_venda = models.CharField(max_length=50, blank=True)
    bandeira_loja = models.CharField(max_length=5, blank=True)
    filler = models.CharField(max_length=100, blank=True)

    def __str__(self):
       return self.num_relatorio + ' - ' + self.bandeira_loja + ' - ' + self.des_local_venda


class RegistroDetalhe(models.Model):
    """
    cod_registro = 2
    """
    cod_registro = models.IntegerField()
    num_relatorio = models.BigIntegerField()
    cod_produto = models.BigIntegerField()
    des_produto = models.CharField(max_length=100, blank=True)
    tip_cod_produto = models.CharField(max_length=5, blank=True)
    qt_vendida = models.FloatField()
    un_medida = models.CharField(max_length=5, blank=True)
    dt_hora_inicio_periodo_venda = models.IntegerField()
    dt_hora_fim_periodo_venda = models.IntegerField()
    qt_entrada = models.IntegerField()
    filler = models.CharField(max_length=5, blank=True)

    def __str__(self):
       return self.num_relatorio + ' - ' + self.des_produto


# ARQUIVOS
class Arquivo(models.Model):
    tag_arquivo = models.CharField(max_length=50, blank=True)
    arquivo = models.FileField()

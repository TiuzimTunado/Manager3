from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Nota(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT, related_name= 'nota_disciplina')
    aluno = models.CharField(max_length=100)
    nota = models.FloatField()

    def __str__(self):
        return f"{self.aluno} - {self.disciplina} - {self.nota}"

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()

from django.db import models

class Project(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class ActivityLog(models.Model):
    projeto = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='logs')
    texto_do_log =models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log em {self.data_criacao.strftime('%d/%m/%Y')} - {self.projeto.titulo}"


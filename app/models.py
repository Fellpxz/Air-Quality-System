from django.db import models

# Create your models here.

class Samples(models.Model):
    mp10 = models.DecimalField(max_digits=10, decimal_places=2)
    mp25 = models.DecimalField(max_digits=10, decimal_places=2)
    o3 = models.DecimalField(max_digits=10, decimal_places=2)
    co = models.DecimalField(max_digits=10, decimal_places=2)
    no2 = models.DecimalField(max_digits=10, decimal_places=2)
    so2 = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Amostra {self.id}"
    
    def clean(self):
        # Verifica se já existem 6 ou mais instâncias do modelo
        if Samples.objects.count() >= 6:
            raise ValueError("O limite máximo de amostras é 6.")
    
    # Certo que explicar esse código que acabei de fazer, bom criei uma def. apenas nome! fiz um IF que pega a conta das amostras, e verifica sé é maior que 6.

'''
Primeiramente explicando os códigos acima, bom primeiramente foi criado uma classe "Samples",
depois criamos vários campos: mp10 e outros...

Esses campos tem consigo a models, que é algo que é de lei, sempre tem que ter e logo a frente
um dos seus métodos DecimalField que serve para campos decimais.

Max_Digits = Este argumento define o número máximo de dígitos que podem ser armazenados no 
campo Decimal. Isso inclui dígitos antes e depois do ponto decimal. Por exemplo, se você
definir max_digits como 10, seu campo Decimal poderá armazenar até 10 dígitos no total.

Decimal_Places =  Este argumento define o número de dígitos que podem ser armazenados após
o ponto decimal. Por exemplo, se você definir decimal_places como 2, seu campo Decimal poderá
armazenar até 2 dígitos após o ponto decimal.

Por ultimo temos a

    def __str__(self):
        return f"Amostra {self.id}"

O método __str__() é usado para retornar uma representação legível em texto de um objeto em 
Python. Ele é geralmente implementado em classes de modelos do Django (ou qualquer outra 
classe) para definir como o objeto deve ser exibido quando convertido em uma string.
'''
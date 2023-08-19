from django.db import models


class OrderCV(models.Model):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]

    EMPLOYMENT_CHOICES = [
        ('full_time', 'Полная занятость'),
        ('part_time', 'Частичная занятость'),
        ('freelance', 'Фриланс'),
        ('internship', 'Стажировка'),
    ]

    EXPERIENCE_CHOICES = [
        ('no_experience', 'Нет опыта'),
        ('junior', 'Junior'),
        ('mid', 'Middle'),
        ('senior', 'Senior'),
    ]

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    position_sought = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_CHOICES)
    schedule = models.CharField(max_length=100)
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    last_job = models.CharField(max_length=255)
    last_position = models.CharField(max_length=100)
    tasks_at_previous_jobs = models.TextField()
    about_me = models.TextField()
    key_skills = models.TextField()
    education_university = models.CharField(max_length=255)

    def __str__(self):
        return self.position_sought  # Возвращаем название должности при выводе объекта

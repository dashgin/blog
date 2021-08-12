from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# import faker
# import django
#
# f = faker.Faker()
# u = django.contrib.auth.get_user_model()
# for i in range(500):
#     p = Post(id=(i+20), author=u.objects.first(), subtitle=f.text(max_nb_chars=80), title=f.text(max_nb_chars=50),
#              content=f.paragraph(nb_sentences=5), is_published=True, category=Category.objects.first(), created_at=t)
#     p.save()
#     p.tags.add(Tag.objects.first())
#     p.save()

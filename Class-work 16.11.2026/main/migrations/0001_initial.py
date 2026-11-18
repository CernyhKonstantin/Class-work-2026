from django.db import migrations, models
class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name="Tag", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("name", models.CharField(max_length=50, unique=True)), ("slug", models.SlugField(blank=True, max_length=60, unique=True))], options={"ordering":["name"]}),
        migrations.CreateModel(name="Card", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("title", models.CharField(max_length=150)), ("description", models.TextField(blank=True)), ("created_at", models.DateTimeField(auto_now_add=True)), ("updated_at", models.DateTimeField(auto_now=True))], options={"ordering":["-created_at"]}),
        migrations.AddField(model_name="card", name="tags", field=models.ManyToManyField(blank=True, related_name="cards", to="main.tag")),
    ]

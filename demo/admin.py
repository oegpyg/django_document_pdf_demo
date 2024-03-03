from django.contrib import admin
from django.apps import apps

# Gets all the models registered in the specified application
models = apps.get_app_config('demo').get_models()

# Register all the models in the admin provided they do not have the 'no_admin' attribute.
# If it has the Admin class inside the model, it is considered as the custom model admin.
for model in models:
    admin.site.register(model)

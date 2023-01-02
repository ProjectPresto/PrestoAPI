from django.template.defaultfilters import slugify


def create_unique_slug(model, validated_data):
    if 'slug' not in validated_data:
        i = 0
        identifier = validated_data['name'] if 'name' in validated_data else validated_data['title']
        while True:
            newSlug = slugify(identifier) if i == 0 else f"{slugify(identifier)}-{i}"
            if not model.objects.filter(slug=newSlug).exists():
                validated_data['slug'] = newSlug
                break
            i += 1
    return validated_data


def update_unique_slug(model, instance, validated_data):
    if 'slug' not in validated_data and ('name' in validated_data or 'title' in validated_data):
        identifier = validated_data['name'] if 'name' in validated_data else validated_data['title']
        old_identifier = instance.name if hasattr(instance, 'name') else instance.title

        print(identifier, old_identifier)

        if identifier == old_identifier:
            return validated_data

        i = 0
        while True:
            newSlug = slugify(identifier) if i == 0 else f"{slugify(identifier)}-{i}"
            if not model.objects.filter(slug=newSlug).exists():
                validated_data['slug'] = newSlug
                break
            i += 1
    return validated_data
